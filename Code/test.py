
import os
import openai
import gradio as gr
openai.api_key = "API Key"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: ",
def gpt_output(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    return response.choices[0].text

# gpt_output("who is the founder of python programming language")

# while True:
#     query = input("Ask a Question To AI:\n")
#     gpt_output(query)
def chatgpt_clone(input,history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ''.join(s)
    output = gpt_output(inp)
    history.append((input,output))
    return history,history


block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>AGI AI Assistant</center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone,inputs=[message, state],outputs=[chatbot,state])

block.launch(debug=True)
