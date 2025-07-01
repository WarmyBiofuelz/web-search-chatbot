# Web Search Chatbot (Final Version)

This repository contains the final version of the Streamlit chatbot: **main-ddg.py**.

## Description

- **main-ddg.py**: A Streamlit chatbot using the GitHub Models platform and a DuckDuckGo web search tool for real-time, up-to-date information. The agent will use the web_search tool for current events, recent data, or real-time updates.

## Features

- Interactive chat interface using Streamlit
- Uses the GitHub Models platform (openai/gpt-4.1-nano)
- Session state management for conversation history
- Tool support: web search via DuckDuckGo
- Strong prompt to ensure the agent uses the web_search tool for current information

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   # or, if you use uv:
   uv pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   Create a `.env` file in the project root with your GitHub Models API key:
   ```
   SECRET2=your_github_models_api_key_here
   ```

3. **Get a GitHub Models API key:**
   - [GitHub Models Platform](https://models.github.ai/) for your API key

## Usage

Run the final chatbot:
```bash
streamlit run main-ddg.py
```

## Setting API Key for Testing

To test the chatbot, you need to provide a valid API key in a `.env` file in the project root:

- For GitHub Models API (used by main-ddg.py):
  ```
  SECRET2=your_github_models_api_key_here
  ```

**Note:** Never commit your actual API keys to GitHub or share them publicly.

## Requirements

- Python 3.8 or higher (Python 3.12 recommended for best compatibility)
- GitHub Models API key
- Internet connection for API calls

## License

MIT