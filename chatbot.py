import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st


load_dotenv()

#Groq API Key
os.environ["GROQ_API_KEY"]      =   os.getenv("GROQ_API_KEY")

#Create a LLM Object
llm  = ChatGroq(
                model           =   "llama3-70b-8192",
                temperature     =   0
                )

st.title("AI Chatbot")
# If the Global variable is not created, create it once.
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Parse through the Global and print the Chat History
for chats in st.session_state.chat_history:
    with st.chat_message(chats["role"]):
        st.markdown(chats['content'])



if user_input := st.chat_input("........"):
    # Print User Input
    with st.chat_message("User"):
        st.markdown(user_input)
        # Store the User input in Streamlit Global
        st.session_state.chat_history.append({"role":"User", "content": user_input})

    ############################## Instruction to LLM, Constant msg most of the time ###############################
    system_msg = {
                    "role"      : "system", 
                    "content"   : "'''You are helpful assistant who helps to answer User queries'''" 
                }
    
    ###################################### Variable Input Query to LLM ################################################
    Human_msg   = {
                    "role"      : "user", 
                    "content"   : f"'''User Query:'{user_input}''''"
                }

    ######################################## Prompt ##########################################
    prompt      = [system_msg, Human_msg]

    #################################### AI invoking ########################################################
    llm_response = llm.invoke(prompt)
    
    # Print AI Response
    with st.chat_message("Assistant"):
        st.markdown(llm_response.content)
        # Store the AI Response in Streamlit Global
        st.session_state.chat_history.append({"role":"Assistant", "content": llm_response.content})