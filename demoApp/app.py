import gradio as gr
from transformers import pipeline

# Set up the sentiment analysis pipeline
classifier = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

def predict_sentiment(text):
    result = classifier(text)
    return f"{result[0]['label']} (confidence: {result[0]['score']:.2f})"

demo = gr.Interface(fn=predict_sentiment, inputs="text", outputs="text")
demo.launch(share=True)
