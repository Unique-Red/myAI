# this is to test from terminal

import sys
from chatbot import ChatBot
import pyttsx3
import speech_recognition as sr
import os
from dotenv import load_dotenv

load_dotenv()

def text_to_speech(text):
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 138)
    voices = speaker.getProperty('voices')
    speaker.setProperty("voice", voices[1].id)
    speaker.say(text)
    speaker.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio)
        print("You:", user_input)
        return user_input
    
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

def main():
    api_key = os.getenv("GENAI_API_KEY")
    
    chatbot = ChatBot(api_key=api_key)
    chatbot.start_conversation()
    print("Welcome to myAI! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            sys.exit("Exiting...")
        elif user_input == "clear":
            chatbot.clear_conversation()
            print("Conversation cleared!")
            continue
                    
        # Add voice recognition
        elif user_input.lower() == "voice":
            user_input = speech_to_text()
            if not user_input:
                continue

        try:
            response = chatbot.send_prompt(user_input)
            print(f"{chatbot.CHATBOT_NAME}: {response}")
            
            # Add text-to-speech
            text_to_speech(response)
        except Exception as e:
            print(f"An Error occurred: {e}")

if __name__ == "__main__":
    main()
