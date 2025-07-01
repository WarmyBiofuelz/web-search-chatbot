# Web Search Chatbot

A Streamlit-based chatbot project with three different implementations:

- **main.py**: Simple Streamlit chatbot using the OpenAI API.
- **main-agento.py**: Streamlit chatbot using the modern OpenAI Agents SDK (function-calling, agent abstraction).
- **main-ddg.py**: Streamlit chatbot using the GitHub Models platform and a DuckDuckGo web search tool for real-time information.

## Features

- Interactive chat interface using Streamlit
- OpenAI GPT-3.5-turbo, GPT-4, or GitHub Models integration
- Session state management for conversation history
- Tool support (web search) in `main-ddg.py`

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   # or, if you use uv:
   uv pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   Create a `.env` file in the project root with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   SECRET2=your_github_models_api_key_here
   ```
   You can include both lines if you want to test all scripts.

3. **Get API keys:**
   - [OpenAI Platform](https://platform.openai.com/api-keys) for OpenAI API key
   - [GitHub Models Platform](https://models.github.ai/) for GitHub Models API key

## Script Usage

### 1. `main.py` — OpenAI Streamlit Chatbot
A simple chatbot using the OpenAI API (GPT-3.5-turbo or GPT-4).

```bash
streamlit run main.py
```

### 2. `main-agento.py` — OpenAI Agent SDK Chatbot
A chatbot using the modern OpenAI Agents SDK (function-calling, agent abstraction).

```bash
streamlit run main-agento.py
```

### 3. `main-ddg.py` — GitHub Models Agent with DuckDuckGo Search
A chatbot using the GitHub Models platform and a DuckDuckGo web search tool for real-time information. The agent will use the web_search tool for current events, recent data, or real-time updates.

```bash
streamlit run main-ddg.py
```

## Setting API Keys for Testing

To test the chatbots, you need to provide valid API keys in a `.env` file in the project root:

- For OpenAI API (used by main.py and main-agento.py):
  ```
  OPENAI_API_KEY=your_openai_api_key_here
  ```
- For GitHub Models API (used by main-ddg.py):
  ```
  SECRET2=your_github_models_api_key_here
  ```

If you want to use both, you can include both lines in the same `.env` file. The scripts will automatically load the correct key for each use case.

**Note:** Never commit your actual API keys to GitHub or share them publicly.

## Requirements

- Python 3.8 or higher (Python 3.12 recommended for best compatibility)
- OpenAI API key and/or GitHub Models API key
- Internet connection for API calls

## License

MIT