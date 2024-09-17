# MyAI Chatbot

Welcome to *MyAI*, a Python-based chatbot powered by Google's Generative AI API. This chatbot is designed to simulate human-like conversations, providing responses to prompts through both text and voice recognition. The project allows users to interact via text input or voice commands and offers text-to-speech responses for a more interactive experience.

## Features

- AI-Powered Conversations: Uses Google's Gemini model to generate responses based on user prompts.
- Text and Voice Input: Users can either type commands or speak to the chatbot using voice recognition.
- Text-to-Speech: The chatbot can respond by converting text output into speech.
- Conversation History: Tracks the conversation context to maintain a coherent dialogue.
- Customizable Response Temperature: Adjusts the creativity of the responses by tweaking the temperature setting.

## Project Structure

The project contains the following main files:

1. `chatbot.py`: Contains the `ChatBot` class which handles conversation management, prompt processing, and API interactions with Google Generative AI.
2. `app.py`: The main entry point of the chatbot application that handles user input, text-to-speech (TTS), and speech-to-text (STT) operations.

## Prerequisites

Before running the project, ensure you have the following dependencies installed:

- Python 3.x
- Required Python packages:
  - `google-generativeai`
  - `pyttsx3`
  - `speech_recognition`
  - `python-dotenv`

To install these dependencies, you can run:

```bash
pip install google-generativeai pyttsx3 speech_recognition python-dotenv
```

## Setup Instructions

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone <repository-url>
   cd myai-chatbot
   ```

2. API Key Configuration:
   - Obtain your API key from [Google Studio](https://aistudio.google.com/)
   - Create a `.env` file in the project directory and add the following line:
     ```
     GENAI_API_KEY=your_api_key_here
     ```

3. Install Packages:
   Install all the app dependencies with the following command:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Application:
   Start the chatbot by running the following command:
   - Terminal
   ```bash
   python app.py
   ```

   - With User Interface
   ```bash
   python flask_app.py
   ```
   

5. Usage:
   - Type your questions or prompts directly.
   - Use the command `clear` to clear the conversation history.
   - Type `exit` to quit the chatbot.
   - Type `voice` to use speech recognition for input instead of typing.
   - The chatbot will respond in both text and speech.

## Key Functions

### Text-to-Speech (TTS)
The chatbot can convert text responses into speech using `pyttsx3`. This enhances user experience by enabling spoken interaction.

### Speech-to-Text (STT)
Users can speak their inputs into the microphone, which is then recognized and transcribed into text using the `speech_recognition` library.

### Google Generative AI API
The chatbot uses the GenerativeModel from Google Generative AI to generate responses to user inputs based on the context of the conversation.

## How It Works

1. Conversation Initialization:
   When you start the chatbot, it loads a pre-defined conversation history or starts fresh if no history is provided.
   
2. Prompt Submission:
   You submit prompts to the chatbot either by typing or using voice input. The chatbot sends the prompt to the Generative AI model and receives a response.
   
3. Response Generation:
   Based on the prompt, the AI generates a response, which is then displayed to the user and spoken out loud using TTS.

## Future Improvements

- Add more customizable conversational features.
- Implement advanced NLP-based functionalities to make conversations even more intuitive.
- Enhance the GUI for a better user interface.

## Troubleshooting

- API Key Error: Ensure that your API key is correctly placed in the `.env` file.
- Microphone Issues: If speech recognition fails, ensure your microphone is working and configured properly.
- TTS Issues: Check if `pyttsx3` is properly installed and configured to use the correct voice settings for your OS.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Google Generative AI for the robust language model.
- `pyttsx3` for text-to-speech capabilities.
- `speech_recognition` for enabling voice input.

## Credit
- [Ifihan](https://github.com/ifihan)

---

Feel free to contribute or suggest improvements!