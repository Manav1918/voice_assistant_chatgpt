#Say thanks if you like this program
import openai
import speech_recognition as sr
import os
api_key = os.environ.get("OPENAI_API_KEY") # save your open ai api key in environment variables where "OPENAI_API_KEY" will be name and value is your "API KEY"
# Set the OpenAI API key
openai.api_key = api_key


import pyttsx3
engine = pyttsx3.init()
# Set voice
voices = engine.getProperty('voices')
for voice in voices:
    print(voice.name)
engine.setProperty('voice', voices[1].id) # 1 is the index of the voice to be used

# Set rate and volume
engine.setProperty('rate', 200) # 200 words per minute
engine.setProperty('volume', 0.8) # 80% volume

##---------------------- convert your voice to text and get response using chatGPT-------------------------------------

# Set up SpeechRecognition
r = sr.Recognizer()

# Define function to transcribe speech to text
def transcribe_speech():
    with sr.Microphone() as source:
        print("Speak now!")
        audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        return text
    except:
        print("Sorry, I could not recognize your voice.")
        return None

# Define function to generate response from OpenAI API
def generate_response(query):
    # Call the OpenAI API
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{"role": "user",
                                                       "content": query}])


    # Print the Output
    output = response.choices[0].message.content
    return output
def say_text(say_it):
    engine.say(say_it)
    engine.runAndWait()

# Main loop
while True:
    prompt = transcribe_speech()
    if prompt:
        if prompt =='stop' or prompt =='exit':
            print('I hope you enjoyed using this app. Bye! Wish to see you again.')
            break
        else:
            print(f"You said: {prompt}")
            response = generate_response(prompt)
            print(f"Response: {response}")
            say_text(response)

