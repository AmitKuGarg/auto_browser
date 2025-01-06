# Auto Browser Agent 🌐

An intelligent tool that uses natural language processing to understand user queries, find relevant information in a vector database, and automatically launch appropriate web pages.

## 🚀 Features

- Natural language query processing
- Vector database search using OpenAI's text-embedding-3-large model
- Intelligent response generation with GPT-4-mini
- Automated browser action execution
- User-friendly Gradio interface

## 📋 Prerequisites

- Python 3.12 or higher
- Chrome/Firefox browser installed
- OpenAI API key

## 🛠️ Installation

1. Clone the repository:
```bash
cd auto-browser-agent
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
# Create a .env file and add your OpenAI API key
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

## 💻 Usage

1. Start the Gradio interface:
```bash
python main.py C:\\learn\\vector_store
```

2. Open your browser and navigate to `http://localhost:7860`

3. Enter your query in natural language

![image](https://github.com/user-attachments/assets/05baffb8-3060-415b-91dd-33cad549a28f)
