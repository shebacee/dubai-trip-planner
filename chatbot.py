from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
load_dotenv()
client=OpenAI()

initial_msg=[
    {"role":"system","content":"You are Jarvis, a professional Dubai trip planner. Your nickname is JV, and you must always introduce yourself as 'Hello, I'm JV, your expert Dubai trip planner. You specialize in curating tailored vacation plans, including accommodations, transportation, dining, sightseeing, and local experiences in Dubai. Always respond with professionalism, clarity, and a friendly tone. Your responses must be informative yet concise — strictly under 200 words. Avoid unnecessary elaboration. Offer suggestions based on user interests, travel dates, budget, and preferences. You are JV"
    ", a real human trip planning expert. Keep the conversation engaging and helpful, and ensure every reply maintains your persona and professionalism as a Dubai specialist. Ask necessary questions to the users in bullets or in order. "},
        {"role":"assistant",
        "content":"Hello, I'm JV, your expert trip planner. How can i help you?"
        }
]
def get_resp_from_llm(messages):
    completion=client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
)
    return completion.choices[0].message


if "messages" not in st.session_state:
    st.session_state.messages=initial_msg

st.title("Dubai Trip Assistant App")

for message in st.session_state.messages:
    if message["role"]!="system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


usr_msg=st.chat_input("Enter your message")
if usr_msg:
    new_msg={
        "role":"user",
        "content":usr_msg
        
    }
    st.session_state.messages.append(new_msg)
    with st.chat_message(new_msg["role"]):
        st.markdown(new_msg["content"])
    response=get_resp_from_llm(st.session_state.messages)
    if response:
        resp_msg={
            "role":"assistant",
            "content":response.content
        }
        st.session_state.messages.append(resp_msg)
        with st.chat_message(resp_msg["role"]):
            st.markdown(resp_msg["content"])