import streamlit as st
import os
from dotenv import load_dotenv
import asyncio
from openai import AsyncOpenAI
from agents import Agent, Runner, ModelSettings, OpenAIChatCompletionsModel

load_dotenv()

# System prompt in Lithuanian
SYSTEM_PROMPT = "Atsakyk tik lietuvių kalba, nepriklausomai nuo klausimo kalbos. Jei klausimas užduotas kita kalba, vis tiek atsakyk lietuviškai."

api_key = os.getenv("OPENAI_API_KEY")
endpoint = "https://api.openai.com/v1"
model = "gpt-4.1-nano"

client = AsyncOpenAI(
    base_url=endpoint,
    api_key=api_key
)

model_instance = OpenAIChatCompletionsModel(
    model=model,
    openai_client=client
)

agent = Agent(
    name="WarmyBot",
    instructions=SYSTEM_PROMPT,
    model=model_instance,
    model_settings=ModelSettings(temperature=0.7),
)

async def get_agent_response(messages):
    # Compose the conversation for the agent
    conversation = ""
    for msg in messages:
        if msg["role"] == "user":
            conversation += f"User: {msg['content']}\n"
        elif msg["role"] == "assistant":
            conversation += f"Assistant: {msg['content']}\n"
    # Run the agent and get the response
    result = await Runner.run(agent, conversation)
    return result.final_output

async def main():
    st.title("Warmy Bot (Agent Version)")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("What is up?")
    if prompt:
        # Show user message
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Get agent response
        with st.chat_message("assistant"):
            response_text = await get_agent_response(st.session_state.messages)
            st.markdown(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})

if __name__ == "__main__":
    asyncio.run(main()) 