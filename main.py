import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

with gr.Interface(
    fn=greet,
    inputs=[
        gr.Textbox(label="Name"),
        gr.Slider(minimum=1, maximum=10, step=1, label="Intensity")
    ],
    outputs=gr.Textbox(label="Greeting"),
    title="Greeting Demo",
    description="A simple demo using Gradio 5"
) as demo:
    demo.launch(share=True)
