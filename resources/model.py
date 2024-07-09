from transformers import pipeline


class Models():
    def __init__(self, model_name):
        self.model1 = pipeline("zero-shot-classification", model=model_name)
