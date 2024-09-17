import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class GenAIException(Exception):
    pass

class ChatBot:
    CHATBOT_NAME = "myAI"

    def __init__(self, api_key):
        self.genai = genai
        self.genai.configure(api_key=os.getenv("GENAI_API_KEY"))
        self.model = self.genai.GenerativeModel("gemini-pro")
        self.conversation = None
        self._conversation_history = []

        self.preload_conversation()



    def clear_conversation(self):
        self.conversation = self.model.start_chat(history=[])

    def start_conversation(self):
        self.conversation = self.model.start_chat(history=self._conversation_history)

    def send_prompt(self, prompt, temperature=0.1):
        if temperature < 0 or temperature > 1:
            raise GenAIException("Temperature must be between 0 and 1")
        if not prompt:
            raise GenAIException("Prompt cannot be empty. Type something!")
        
        try:
            response = self.conversation.send_message(
                content=prompt,
                generation_config=self._generation_config(temperature),
            )
            response.resolve()
            return f"{response.text}\n" + "---" * 10
        except Exception as e:
            raise GenAIException(f"An error occurred: {e}")
        
    @property
    def history(self):
        conversation_history = [
            {"role": message["role"], "text": message.parts[0]} for message in self.conversation.history
        ]
        return conversation_history

    def _generation_config(self, temperature):
        return genai.types.GenerationConfig(
            temperature=temperature
        )

    def _construct_message(self, text, role="user"):
        return {
            "role": role,
            "parts": [text]
        }


    def preload_conversation(self, conversation_history= None):
        if isinstance(conversation_history, list):
            self._conversation_history = conversation_history
        else:
            self._conversation_history = [
                self._construct_message( "Hello, what can I do for you today?"),
                self._construct_message("Be more detailed", 'model')
            ]
