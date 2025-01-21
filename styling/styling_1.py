import gradio as gr

with gr.Blocks(theme=gr.themes.Glass(), css=".gradio-container {background-color: red}") as demo:
  num1 = gr.Number()
  num2 = gr.Number()
  product = gr.Number(lambda a, b: a * b, inputs=[num1, num2])

demo.launch()