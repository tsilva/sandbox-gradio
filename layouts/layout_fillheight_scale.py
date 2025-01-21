import gradio as gr

with gr.Blocks(fill_height=True) as demo:
    gr.Chatbot(scale=1)
    gr.Textbox(scale=0)

demo.launch()
