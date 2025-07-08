from flask import Flask, render_template, request, jsonify, Response
from phi.agent import Agent as PhiAgent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

from browser_use import Agent as BrowserAgent
from browser_use.llm import ChatGroq

from dotenv import load_dotenv
import os
import json
from datetime import datetime
import asyncio

# Load environment variables
load_dotenv()

# Set your Groq API key securely (optional if already in .env)
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

app = Flask(__name__)

# Global LLM object
llm = ChatGroq(
    model='meta-llama/llama-4-maverick-17b-128e-instruct'
)

# Initialize the Web Agent (for ArangoDB trainer)
web_agent = PhiAgent(
    name="ArangoDB Trainer",
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    tools=[DuckDuckGo()],
    instructions=[
        "You are an experienced ArangoDB Trainer with attention to detail. "
        "Train customers on how to use ArangoDB or similar graph database products.",
        "If the user wants to use `arangosh`, explain the appropriate shell commands.",
        "If the user prefers manual instructions (GUI or UI walkthrough), provide detailed step-by-step guidance for that as well.",
        "Be interactive, ask follow-up questions if the user's goal is unclear.",
        "Use markdown formatting to structure explanations, code blocks, and steps."
    ],
    show_tool_calls=True,
    markdown=True,
)

# Chat history (in-memory)
chat_history = []

# Helper to run async tasks from sync Flask routes
def run_async_task(coro):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()

        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400

        # Append user input to chat history
        chat_history.append({
            'type': 'user',
            'message': user_message,
            'timestamp': datetime.now().isoformat()
        })

        # Agent response
        response = web_agent.run(user_message)

        chat_history.append({
            'type': 'agent',
            'message': response.content,
            'timestamp': datetime.now().isoformat()
        })

        return jsonify({
            'response': response.content,
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/api/chat/stream', methods=['POST'])
def chat_stream():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()

        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400

        chat_history.append({
            'type': 'user',
            'message': user_message,
            'timestamp': datetime.now().isoformat()
        })

        def generate():
            try:
                response_content = ""
                for chunk in web_agent.run(user_message, stream=True):
                    if chunk:
                        response_content += str(chunk)
                        yield f"data: {json.dumps({'chunk': str(chunk)})}\n\n"

                chat_history.append({
                    'type': 'agent',
                    'message': response_content,
                    'timestamp': datetime.now().isoformat()
                })

                yield f"data: {json.dumps({'done': True})}\n\n"

            except Exception as e:
                yield f"data: {json.dumps({'error': str(e)})}\n\n"

        return Response(generate(), mimetype='text/plain')

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    return jsonify(chat_history)

@app.route('/api/clear', methods=['POST'])
def clear_history():
    global chat_history
    chat_history = []
    return jsonify({'message': 'Chat history cleared'})

@app.route('/api/create-collection', methods=['POST'])
def create_collection():
    try:
        data = request.get_json()
        task = data.get('task', '').strip()

        if not task:
            return jsonify({'error': 'Task cannot be empty'}), 400

        async def run_browser_task():
            try:
                agent = BrowserAgent(task=task, llm=llm)
                await agent.run()
                return f"Task executed successfully: {task}"
            except Exception as e:
                return f"Error executing task: {str(e)}"

        result = run_async_task(run_browser_task())

        chat_history.append({
            'type': 'agent',
            'message': result,
            'timestamp': datetime.now().isoformat()
        })

        return jsonify({
            'response': result,
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
