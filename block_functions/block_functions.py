"""import gradio as gr

from transformers import pipeline

pipe = pipeline("translation", model="t5-base")

def translate(text):
    return pipe(text)[0]["translation_text"]  

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            english = gr.Textbox(label="English text")
            translate_btn = gr.Button(value="Translate")
        with gr.Column():
            german = gr.Textbox(label="German Text")

    translate_btn.click(translate, inputs=english, outputs=german, api_name="translate-to-german")
    examples = gr.Examples(examples=["I went to the supermarket yesterday.", "Helen is a good swimmer."],
                           inputs=[english])

demo.launch()
"""

# NOTE: The code below calls a space that has the code above as a function

import gradio as gr

from transformers import pipeline

english_translator = gr.load(name="spaces/gradio/english_translator")
english_generator = pipeline("text-generation", model="distilgpt2")

def generate_text(text):
    english_text = english_generator(text)[0]["generated_text"]  
    german_text = english_translator(english_text)
    return english_text, german_text

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            seed = gr.Text(label="Input Phrase")
        with gr.Column():
            english = gr.Text(label="Generated English Text")
            german = gr.Text(label="Generated German Text")
    btn = gr.Button("Generate")
    btn.click(generate_text, inputs=[seed], outputs=[english, german])
    gr.Examples(["My name is Clara and I am"], inputs=[seed])

demo.launch()
