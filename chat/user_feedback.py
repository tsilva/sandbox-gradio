import gradio as gr

def chatbot(message, history):
    return "You typed: " + message

demo = gr.ChatInterface(
    chatbot,
    type="messages",
    flagging_mode="manual",
    flagging_options=["Like", "Spam", "Inappropriate", "Other"]
)

demo.launch()
