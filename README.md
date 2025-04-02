# AI Chatbot - ReadMe

## Overview
This is a simple AI chatbot using Streamlit and Groq's LLM (Llama3-70b-8192). It maintains a chat history and generates responses to user queries using AI.

## Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Required Python libraries: `os`, `dotenv`, `langchain_groq`, `streamlit`

## Installation & Setup
1. **Clone the repository (if applicable)**
   ```sh
   git clone <repo_url>
   cd <repo_folder>
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Create a `.env` file in the project root.
   - Add the following line and replace `your_groq_api_key` with your actual key:
     ```sh
     GROQ_API_KEY=your_groq_api_key
     ```

## Running the Application
1. Open a terminal and navigate to the project directory.
2. Run the Streamlit app:
   ```sh
   streamlit run <filename>.py
   ```
   *(Replace `<filename>.py` with the actual script name)*

## Key Features
- Loads Groq API Key from `.env` file.
- Uses Llama3-70b-8192 model with temperature `0`.
- Displays user input and chatbot responses in a chat interface.
- Maintains chat history throughout the session.

## Basic Flow
1. **Load API Key**: The `.env` file is read to set the Groq API key.
2. **Initialize LLM**: Creates a chatbot object using `ChatGroq`.
3. **Display UI**: Uses Streamlit to create an interactive chat interface.
4. **Chat Processing**:
   - Stores user input in session history.
   - Prepares a prompt with a system instruction.
   - Sends the query to the AI model.
   - Displays and stores the AI response.

## Notes
- Ensure a valid API key is provided.
- This chatbot is a basic implementation and can be further enhanced.

