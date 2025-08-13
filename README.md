# LangChain Memory Management Guide
This repository provides a practical introduction to LangChain and LangGraph, focusing on conversation memory management in AI applications. It includes examples of both Jupyter notebook-based exploration and a Chainlit-powered chatbot implementation.

## Prerequisites
- Python 3.13
- UV Package Manager ([Install Guide](https://docs.astral.sh/uv/getting-started/installation/))


## Setup Instructions
1. Clone & setup:
```
git clone https://github.com/byahmedali/Hands-on-Intro-to-LangChain-and-LangGraph.git

cd Hands-on-Intro-to-LangChain-and-LangGraph

uv sync
```

2. Create a `.env` file with your GROQ API key:
```
GROQ_API_KEY="your_groq_api_key"
```

## Usage

### Jupyter Notebook
The `notebook.ipynb` demonstrates:
- Setting up a basic Chat Model
- Managing conversation history
- Using LangGraph for message persistence (in-memory)

### Chainlit Chatbot
The `chatbot.py` implements same concepts in a Chainlit UI with streaming responses.

To run the chatbot:
```
chainlit run chatbot.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.