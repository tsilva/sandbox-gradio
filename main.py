import gradio as gr

gr.ChatInterface(
    fn=lambda message, history: "You typed: " + message,
    type="messages"
).launch()