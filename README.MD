# 🤖 ORIN - AI Chatbot

An advanced conversational AI application powered by the **Groq API** and **LLaMA 3.3 70B** model. This project provides two interfaces for interacting with the AI chatbot: a modern web-based UI built with Streamlit and a lightweight command-line interface.

![alt text](<Screenshot (246).png>)

## Link
https://ai-chatbot-llama.streamlit.app/

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Running the Web Interface](#running-the-web-interface)
  - [Running the CLI Interface](#running-the-cli-interface)
- [Architecture & Components](#architecture--components)
- [Dependencies](#dependencies)
- [Configuration Details](#configuration-details)
- [API Details](#api-details)
- [Features in Detail](#features-in-detail)
- [Troubleshooting](#troubleshooting)

---

## 📖 Project Overview

This chatbot application leverages the power of **Groq's high-performance inference engine** to deliver fast and intelligent conversational responses. The project demonstrates a production-ready implementation with:

- **Dual Interface Architecture**: Both web and CLI interfaces for flexibility
- **LLaMA 3 Model**: Utilizes the powerful 70B parameter variant for superior reasoning
- **Conversational Memory**: Maintains conversation history within a session
- **Fast Response Times**: Groq's optimized inference engine ensures quick responses
- **User-Friendly Design**: Modern Streamlit UI with intuitive interactions

---

## ✨ Features

### Web Interface (Streamlit)
- 🎨 **Modern UI Design**: Dark-themed interface with cyan accent colors
- 💬 **Chat History**: Persistent conversation history within the session
- ⚡ **Real-time Response**: Displays "Thinking..." indicator while processing
- 🎯 **One-Click Clear**: Clear all chat history with a single button
- 📱 **Responsive Layout**: Centered layout optimized for different screen sizes
- 📊 **Sidebar Information**: Quick access to project details and model information
- 🔄 **Session Management**: Automatic session state management

### CLI Interface (Command Line)
- 🖥️ **Terminal-Based Chat**: Simple and straightforward command-line interaction
- 📝 **Interactive Loop**: Continuous conversation until user exits
- ✅ **Multiple Exit Options**: Supports 'quit', 'exit', or 'bye' commands
- 🛡️ **Input Validation**: Prevents empty messages from being sent
- 📊 **Clean Formatting**: Well-structured output with clear separators
- 💾 **Conversation Tracking**: Maintains full conversation history

---

## 📁 Project Structure

```
chatbot_project/
├── app.py                 # Streamlit web interface
├── chatbot.py            # CLI interface
├── requirements.txt      # Python dependencies
└── README.MD            # Project documentation
```

### File Descriptions

| File | Purpose | Type |
|------|---------|------|
| **app.py** | Streamlit web application with interactive chat UI | Web Interface |
| **chatbot.py** | Command-line chatbot interface for terminal usage | CLI Interface |
| **requirements.txt** | Python package dependencies | Configuration |
| **README.MD** | Project documentation and setup guide | Documentation |

---

## 📦 Prerequisites

Before running this project, ensure you have:

- **Python 3.8 or higher** installed on your system
- **pip** (Python package manager)
- A **Groq API Key** (sign up at [console.groq.com](https://console.groq.com))
- Internet connection to communicate with the Groq API

### System Requirements
- **RAM**: Minimum 2GB (for smooth operation)
- **Storage**: ~500MB (for dependencies)
- **OS**: Windows, macOS, or Linux

---

## 🚀 Installation

### Step 1: Clone or Download the Project
Download the project files to your local machine.

### Step 2: Navigate to Project Directory
```bash
cd path/to/chatbot_project
```

### Step 3: Create a Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- `groq` - Groq API Python client
- `streamlit` - Web framework for the UI

---

## 🔑 Configuration

### API Key Setup

#### Option 1: Using Environment Variables (Recommended for CLI)
```bash
# Windows (Command Prompt)
set GROQ_API_KEY=your_api_key_here

# Windows (PowerShell)
$env:GROQ_API_KEY = "your_api_key_here"

# macOS/Linux
export GROQ_API_KEY=your_api_key_here
```

#### Option 2: Using Streamlit Secrets (Recommended for Web)
1. Create a `.streamlit` directory in your project folder:
   ```bash
   mkdir .streamlit
   ```

2. Create a `secrets.toml` file inside `.streamlit`:
   ```toml
   GROQ_API_KEY = "your_api_key_here"
   ```

3. Add `.streamlit` to `.gitignore` to prevent committing sensitive data

#### Obtaining Your Groq API Key
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Generate an API key from the dashboard
4. Copy and store it securely

---

## 💻 Usage

### Running the Web Interface

#### Command:
```bash
streamlit run app.py
```

#### What Happens:
1. Streamlit server starts (typically on `http://localhost:8501`)
2. Your default browser opens automatically with the chatbot UI
3. Start typing messages in the input box to interact with the AI

#### Features Available:
- Type messages in the input field: "Type your message here..."
- View chat history in the main area
- Clear conversation with the "Clear Chat" button in the sidebar
- View model and project information in the sidebar

#### Browser Interface:
- **Input Field**: Located at the bottom with placeholder text
- **Chat Area**: Shows all messages from both user and assistant
- **Sidebar**: Contains about section, clear button, and project details

---

### Running the CLI Interface

#### Command:
```bash
python chatbot.py
```

#### What Happens:
1. A welcome message displays with instructions
2. You'll see the prompt: `You: `
3. Type your message and press Enter
4. The bot responds with: `Chatbot: [response]`
5. Continue the conversation or exit anytime

#### Example Interaction:
```
==================================================
        Welcome to AI Chatbot using Groq
==================================================
Type your message and press Enter to chat.
Type 'quit' to exit the chatbot.
==================================================

You: Hello, how are you?

Chatbot: Hello! I'm doing great, thank you for asking. How can I help you today?

You: quit

Chatbot: Goodbye! Have a great day!
```

#### Exit Options:
- Type `quit` and press Enter
- Type `exit` and press Enter
- Type `bye` and press Enter

---

## 🏗️ Architecture & Components

### Component Diagram

```
┌─────────────────────────────────────────────────┐
│         Groq API (llama-3.3-70b-versatile)      │
└──────────────────┬──────────────────────────────┘
                   │
          ┌────────┴────────┐
          │                 │
    ┌─────▼──────┐    ┌────▼──────────┐
    │  app.py    │    │  chatbot.py    │
    │ (Streamlit)│    │  (CLI)         │
    └────────────┘    └────────────────┘
```

### Data Flow

#### Web Interface Flow:
1. User enters message in Streamlit UI
2. Message appended to session state
3. Request sent to Groq API with conversation history
4. Response received and displayed
5. Response added to conversation history
6. UI updates automatically

#### CLI Interface Flow:
1. User enters message in terminal
2. Input validation (checks for empty input)
3. Message appended to conversation history
4. Request sent to Groq API with system message + history
5. Response received and printed
6. Response appended to conversation history

---

## 📚 Dependencies

### Core Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| **groq** | Latest | Official Groq API Python client for LLM communication |
| **streamlit** | Latest | Web framework for creating the interactive UI |

### Installation Command
```bash
pip install groq streamlit
```

### Dependency Details

#### Groq Client
- Handles API communication with Groq servers
- Manages authentication using API keys
- Supports streaming and non-streaming responses
- Includes error handling and retry logic

#### Streamlit
- Builds the web interface without complex frontend code
- Manages session state automatically
- Provides chat UI components
- Handles routing and page updates

---

## ⚙️ Configuration Details

### Model Configuration

#### Model Used: LLaMA 3.3 70B
- **Parameters**: 70 billion parameters
- **Training Data**: Extensive corpus of high-quality data
- **Capabilities**: General conversation, reasoning, coding, creative writing
- **Max Tokens**: 1024 (configurable in code)
- **Temperature**: 0.7 (balanced between deterministic and creative)

### System Prompts

#### Current System Message:
```
"You are a helpful and friendly AI assistant. Answer clearly and concisely."
```

#### To Customize:
- **In app.py** (Line 54-55): Modify the system content in `client.chat.completions.create()`
- **In chatbot.py** (Line 10-11): Modify the `system_message` dictionary

### Configurable Parameters

| Parameter | Current Value | Purpose |
|-----------|---------------|---------|
| `max_tokens` | 1024 | Maximum response length |
| `temperature` | 0.7 | Creativity level (0=deterministic, 1=random) |
| `model` | llama-3.3-70b-versatile | Model selection |

### Modifying Parameters

Edit these values in either file:
```python
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # Change model
    messages=[...],
    max_tokens=1024,                   # Increase for longer responses
    temperature=0.7                    # Increase for more creative responses
)
```

---

## 🔌 API Details

### Groq API Specifications

#### Authentication
- **Method**: API Key in header
- **Header**: `Authorization: Bearer [YOUR_API_KEY]`
- **Environment Variable**: `GROQ_API_KEY`

#### Request Format
```python
client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "..."},
        {"role": "user", "content": "..."},
        {"role": "assistant", "content": "..."}
    ],
    max_tokens=1024,
    temperature=0.7
)
```

#### Response Format
```python
{
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "The AI response text..."
            }
        }
    ]
}
```

#### Rate Limits
- Check your Groq dashboard for current rate limits
- Default: Usually generous for free tier
- Implement retry logic for production use

#### Cost
- Groq offers a free tier with generous limits
- Check pricing at [groq.com/pricing](https://groq.com/pricing)

---

## 🎯 Features in Detail

### Session Management (Streamlit)

#### How It Works:
```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

- Automatically initializes message history on first visit
- Persists messages during the session
- Clears when user clicks "Clear Chat" button
- Resets when page is refreshed

#### Message Structure:
```python
{
    "role": "user" | "assistant",
    "content": "message text"
}
```

### Conversation History Management

#### Web Interface:
- Automatic session state handling
- Maximum history limited only by browser memory
- All messages visible in the chat interface

#### CLI Interface:
- Manual list management
- Full conversation history maintained in memory
- Session ends when user exits the program

### Error Handling

#### Current Error Handling:
- Empty input validation (CLI only)
- API connection errors handled by Groq client
- Missing API key raises an error with clear message

#### Best Practices:
```python
try:
    response = client.chat.completions.create(...)
except Exception as e:
    print(f"Error: {e}")
    # Handle error appropriately
```

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue 1: `ModuleNotFoundError: No module named 'groq'`
**Cause**: Dependencies not installed
**Solution**:
```bash
pip install -r requirements.txt
```

#### Issue 2: `ModuleNotFoundError: No module named 'streamlit'`
**Cause**: Streamlit not installed
**Solution**:
```bash
pip install streamlit
```

#### Issue 3: `GROQ_API_KEY not found` or Authentication Error
**Cause**: API key not configured
**Solution**:
- For CLI: Set environment variable `GROQ_API_KEY`
- For Web: Create `.streamlit/secrets.toml` with your key
- Verify the key is valid at console.groq.com

#### Issue 4: Streamlit App Won't Open in Browser
**Cause**: Port 8501 might be in use
**Solution**:
```bash
streamlit run app.py --server.port 8502
```

#### Issue 5: Slow Responses
**Cause**: API overload or network issue
**Solution**:
- Check your internet connection
- Check Groq API status
- Reduce `max_tokens` for faster responses

#### Issue 6: Empty Responses from API
**Cause**: Model may have issues with your input
**Solution**:
- Try simpler, more specific prompts
- Increase `max_tokens`
- Check if API is responsive with curl test

### Debugging Tips

#### Enable Verbose Logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

#### Test API Connection:
```python
from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "test"}],
    max_tokens=10
)
print(response)
```

#### Check Environment Variable:
```bash
# Windows
echo %GROQ_API_KEY%

# macOS/Linux
echo $GROQ_API_KEY
```

---

## 📝 Example Use Cases

### 1. General Q&A
```
You: What is the capital of France?
Chatbot: The capital of France is Paris.
```

### 2. Code Assistance
```
You: Write a Python function to calculate factorial
Chatbot: [Provides complete function with explanation]
```

### 3. Creative Writing
```
You: Write a short poem about winter
Chatbot: [Generates original poem]
```

### 4. Information Retrieval
```
You: Explain machine learning
Chatbot: [Provides comprehensive explanation]
```

---

## 🔒 Security Considerations

### API Key Protection
- ✅ **Do**: Store API key in environment variables or secrets files
- ✅ **Do**: Add `.streamlit/secrets.toml` to `.gitignore`
- ❌ **Don't**: Hardcode API keys in source files
- ❌ **Don't**: Commit secrets to version control

### Input Validation
- Always validate user input
- Consider rate limiting for production
- Implement content filtering if needed

---

## 🚢 Deployment

### Local Deployment
```bash
# Web
streamlit run app.py

# CLI
python chatbot.py
```

### Cloud Deployment (Streamlit Cloud)
1. Push project to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Deploy directly from repository
4. Set secrets in Streamlit Cloud dashboard

### Docker Deployment
Create a `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

---

## 📄 License

This project is open source. Feel free to use and modify for your needs.

---

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Add conversation persistence (database storage)
- Implement user authentication
- Add support for additional models
- Create web-based settings panel
- Add conversation export features

---

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review API documentation at [groq.com/docs](https://groq.com/docs)
3. Check Streamlit documentation at [docs.streamlit.io](https://docs.streamlit.io)

---

## 🎓 Learning Resources

- **Groq API**: https://console.groq.com/docs
- **Streamlit**: https://docs.streamlit.io
- **LLaMA Model**: https://www.meta.com/research/llama/
- **Python Chat Applications**: https://python.langchain.com

---

## ⭐ Acknowledgments

- Built with [Groq API](https://groq.com)
- UI powered by [Streamlit](https://streamlit.io)
- Model: [LLaMA 3.3](https://www.meta.com/research/llama/) by Meta
- Thanks to the open-source community

---

**Last Updated**: April 2026 | **Status**: Active Development | **Version**: 1.0
