import gradio as gr

with gr.Blocks() as demo:
    im = gr.ImageEditor(width="25vw")

demo.launch()