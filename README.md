# TaskBot - Intelligent Automation Agent

🌐 **TaskBot** is an AI-powered web application designed to automate browser-based tasks, leveraging the power of Groq's language models and browser automation tools.

---

## ✨ Features

- **Web Automation**: Perform browser-based tasks such as form filling, data extraction, and navigation.
- **Voice Input**: Use voice commands to interact with TaskBot for seamless task execution.
- **Chat Interface**: Communicate with the AI assistant to get help with automation tasks or general queries.

---

## 🚀 Quick Start

### ✅ Prerequisites

- Python >= 3.11
- [Playwright](https://playwright.dev/python/) for browser automation
- Groq API key (set in `.env` file)

### 🛠 Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/rithwikthirumalaraju14/Automation_Agent.git
    cd Automation_Agent
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Install Playwright browser:**

    ```bash
    playwright install chromium --with-deps --no-shell
    pip install "browser-use[cli]"
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add your Groq API key:

    ```env
    GROQ_API_KEY=your_groq_api_key_here
    ```

5. **Run the application:**

    ```bash
    python app.py
    ```

    The app will be available at: [http://localhost:5000](http://localhost:5000)

---

## 💡 Usage

- **Chat Interface**: Use the message input field to ask general questions or seek help with automation tasks.
- **Task Execution**: Enter automation tasks in the task input field.  
  _Example_:  
  `"Navigate to http://localhost:8529/_db/_system/_admin/aardvark/index.html#collections, login with username 'root' and password 'testtest', then create a new collection named 'UserData'"`
- **Voice Input**: Click the microphone button to dictate messages or tasks.
- **Clear Chat**: Use the "Clear Chat" button to reset the conversation history.

---

## 🧪 Example Tasks

### 🗃️ Database Management
> Navigate to `http://localhost:8529/_db/_system/_admin/aardvark/index.html#collections`, login with username `root` and password `testtest`, then create a new collection named `UserData`.

### 📝 Data Entry
> Go to `https://example-form.com`, fill out the contact form with name `John Doe`, email `john@example.com`, and message `Hello from TaskBot`, then submit.

### 📰 Content Extraction
> Visit `https://news-website.com`, extract the top 5 article headlines and save them to a text file.

---

## Thankyou

