import gradio as gr

with gr.Blocks() as demo:
    textbox = gr.Textbox("The quick brown fox jumped.")
    selection = gr.Textbox()
    
    def get_selection(select_evt: gr.SelectData):
        return select_evt.value

    textbox.select(get_selection, None, selection)

demo.launch()
