# Web Search Chatbot

A Streamlit-based chatbot that uses OpenAI's GPT-3.5-turbo model to respond in Lithuanian.

## Features

- Interactive chat interface using Streamlit
- OpenAI GPT-3.5-turbo integration
- Automatic Lithuanian language responses
- Session state management for conversation history

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   Create a `.env` file in the project root with your OpenAI API key:
   ```
   SECRET=your_openai_api_key_here
   ```

3. **Get an OpenAI API key:**
   - Visit [OpenAI Platform](https://platform.openai.com/api-keys)
   - Create a new API key
   - Add it to your `.env` file

## Usage

Run the application:
```bash
streamlit run main.py
```

The chatbot will:
- Respond in Lithuanian regardless of the input language
- Maintain conversation history during the session
- Use GPT-3.5-turbo model for responses

## Requirements

- Python 3.8 or higher
- OpenAI API key
- Internet connection for API calls