import gradio as gr

with gr.Blocks() as demo:
  num1 = gr.Number()
  num2 = gr.Number()
  product = gr.Number(lambda a, b: a * b, inputs=[num1, num2])

demo.launch()