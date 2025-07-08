TaskBot - Intelligent Automation Agent

🌐 TaskBot is an AI-powered web application designed to automate browser-based tasks, leveraging the power of Groq's language models and browser automation tools.

Features

Web Automation: Perform browser-based tasks such as form filling, data extraction, and navigation.
Voice Input: Use voice commands to interact with TaskBot for seamless task execution.
Chat Interface: Communicate with the AI assistant to get help with automation tasks or general queries.



Quick Start
Prerequisites

Python >= 3.11

Playwright for browser automation
Groq API key (set in .env file)

Installation

Clone the repository:

git clone https://github.com/rithwikthirumalaraju14/Automation_Agent.git
cd filename


Install dependencies:

pip install -r requirements.txt


Install Playwright browser:

playwright install chromium --with-deps --no-shell
pip install "browser-use[cli]"




Set up environment variables:

Create a .env file in the root directory and add your Groq API key:
GROQ_API_KEY=your_groq_api_key_here


Run the application:

python app.py

The app will be available at http://localhost:5000.
Usage

Chat Interface: Use the message input field to ask general questions or seek help with automation tasks.
Task Execution: Enter automation tasks in the task input field (e.g., "Navigate to http://localhost:8529/_db/_system/_admin/aardvark/index.html#collections, login with username 'root' and password 'testtest', then create a new collection named 'UserData'").
Voice Input: Click the microphone button to dictate messages or tasks.
Clear Chat: Use the "Clear Chat" button to reset the conversation history.

Example Tasks
Here are some example tasks you can try with TaskBot:

Database Management:
Navigate to http://localhost:8529/_db/_system/_admin/aardvark/index.html#collections, login with username 'root' and password 'testtest', then create a new collection named 'UserData'


Data Entry:
Go to https://example-form.com, fill out the contact form with name 'John Doe', email 'john@example.com', and message 'Hello from TaskBot', then submit


Content Extraction:
Visit https://news-website.com, extract the top 5 article headlines and save them to a text file



Project Structure
taskbot/
├── static/                 # Static assets (CSS, images, etc.)
├── templates/              # HTML templates
│   └── index.html         # Main UI template
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
└── .env                   # Environment variables

Contributing
We welcome contributions! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m 'Add your feature').
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.

For bug reports or feature requests, please open an issue on GitHub.
Roadmap

Enhanced Voice Recognition: Improve voice input accuracy and support for multiple languages.
Advanced Automation Workflows: Support complex multi-step automation tasks.
UI Improvements: Add support for real-time task progress visualization.
Parallel Task Execution: Enable parallel processing of multiple automation tasks.
Documentation Expansion: Provide detailed guides for advanced use cases.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

Built with Flask and Playwright.
Powered by Groq for AI capabilities.
Inspired by the browser-use project.


Made with ❤️ by the TaskBot team
