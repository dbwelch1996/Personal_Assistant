import gradio as gr
import openai
import config

openai.api_key = config.API_KEY


conversations =  [{"role": "system", "content": "You are a helpful assistant who speaks like donald trump."},

]


def transcribe(audio):
    
    global conversations
    print(audio)
    audio_file = open (audio, "rb")
    
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    conversations.append({"role": "user", "content": transcript["text"]})
    
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversations)
    
    system_message = response["choices"][0]["content"] 
    conversations.append({"role": "assistant", "content": system_message})  
    
    #19:01
     
    print(response)
    return transcript["text"]
    

ui = gr.Interface(fn =transcribe, inputs = gr.Audio(source = "microphone", type = "filepath"), outputs = "text")

ui.launch()