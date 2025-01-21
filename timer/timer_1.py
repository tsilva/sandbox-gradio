import gradio as gr

def set_textbox_fn(count):
    return count + 1, f"timer1: {count}", f"timer2: {count * 2}"

with gr.Blocks() as demo:
    counter = gr.State(0)
    timer = gr.Timer(3)
    textbox1 = gr.Textbox(label="Timer 1")
    textbox2 = gr.Textbox(label="Timer 2")
    timer.tick(set_textbox_fn, inputs=[counter], outputs=[counter, textbox1, textbox2])

demo.launch(show_api=False)
