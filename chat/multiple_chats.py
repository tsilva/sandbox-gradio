import gradio as gr

def chatbot(message, history):
    return "You typed: " + message

demo = gr.ChatInterface(
    chatbot,
    type="messages",
    save_history=True
)

demo.launch()
