import gradio as gr

input_textbox = gr.Textbox() # inputs outside blocks dont get rendered

with gr.Blocks() as demo:
    # input_textbox = gr.Textbox(render=False) # this is how to control render when not in blocks
    gr.Examples(["hello", "bonjour", "merhaba"], input_textbox)
    input_textbox.render()

demo.launch()
