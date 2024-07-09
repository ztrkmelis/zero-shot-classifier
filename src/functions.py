import json
import configparser
from resources import model


class SentimentIntentionAnalyzer:
    def __init__(self, model_name):
        self.classifier = model.Models(model_name).model1
        self.threshold = 0.5

    def analyze_sentiment(self, text):
        result = self.classifier(text, candidate_labels=["positive", "negative", "neutral"])
        return {label: score for label, score in zip(result['labels'], result['scores']) if score >= self.threshold}

    def analyze_intention(self, text):
        candidate_labels = [
            "buy", "purchase", "order",
            "inquiry", "ask about product", "product details", "features inquiry", "availability",
            "change package",
            "support", "assistance", "help",
            "compare", "comparison", "evaluate",
            "shipping", "delivery", "track order",
            "accessories", "add-ons", "phone case", "screen protector",
            "pricing", "discount", "offers",
            "greeting", "farewell", "thanks", "complaint", "feedback",
        ]
        result = self.classifier(text, candidate_labels=candidate_labels, multi_label=True)
        return {label: score for label, score in zip(result['labels'], result['scores']) if score >= self.threshold}

    def analyze_conversation(self, conversation):
        # analysis = []
        # for step in conversation:
        #     sentiment = self.analyze_sentiment(step["text"])
        #     intention = self.analyze_intention(step["text"])
        #     analysis.append({
        #         "role": step["role"],
        #         "text": step["text"],
        #         "sentiment": sentiment["labels"][0],
        #         "sentiment_score": sentiment["scores"][0],
        #         "intention": intention["labels"][0],
        #         "intention_score": intention["scores"][0]
        #     })
        # return analysisü
        for message in conversation:
            text = list(message.values())[0]  # Extract the message text
            sentiment = self.analyze_sentiment(text)
            intention = self.analyze_intention(text)
            print(f"Message: {text}")
            print(f"Sentiment: {sentiment}")
            print(f"Intention: {intention}")
            print("-----")


class LoadFiles:
    def __init__(self, config_file, conversation_file):
        self.config_file = config_file
        self.conversation_file = conversation_file

    def load_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        return config["DEFAULT"]["ModelName1"]

    def load_conversation(self):
        with open(self.conversation_file, "r") as file:
            conversation = json.load(file)
        return conversation["conversation"]
