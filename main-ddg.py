import streamlit as st
import os
from dotenv import load_dotenv
import asyncio
from openai import AsyncOpenAI
from agents import Agent, Runner, ModelSettings, OpenAIChatCompletionsModel, function_tool
from duckduckgo_search import DDGS

load_dotenv()

SYSTEM_PROMPT = (
    "Your knowledge is mostly limited to the end of 2023, and now it is 2025. "
    "When answering questions involving current events, recent data, or real-time updates, ALWAYS use the web_search tool (DuckDuckGo) to find accurate and up-to-date information. "
    "If you are unsure or do not have the information, use the web_search tool to look it up online. "
    "Do not guess or answer from your own knowledge for current or factual questions—always use the web_search tool. "
    "Example:\n"
    "User: What is the date today?\n"
    "Assistant: [uses web_search tool to find the current date]\n"
    "Whenever needed, use the web_search tool to find the latest information."
)

api_key = os.getenv("SECRET2")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

client = AsyncOpenAI(
    base_url=endpoint,
    api_key=api_key
)

model_instance = OpenAIChatCompletionsModel(
    model=model,
    openai_client=client
)

@function_tool
def web_search(query: str) -> str:
    """Ieškok informacijos internete naudodamas DuckDuckGo."""
    with DDGS() as ddgs:
        results = ddgs.text(query, region="wt-wt", safesearch="off", max_results=3)
        snippets = [r["body"] for r in results if "body" in r]
        return "\n".join(snippets) if snippets else "Nerasta rezultatų."

tools = [web_search]

agent = Agent(
    name="Assistant",
    instructions=SYSTEM_PROMPT,
    model=model_instance,
    model_settings=ModelSettings(temperature=0.1),
    tools=tools
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
    st.title("Warmy Bot (DDG Web Search Agent, GitHub Models)")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Kuo galiu padėti?")
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