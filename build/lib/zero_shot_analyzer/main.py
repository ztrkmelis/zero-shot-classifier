from src import functions


config_file = "../config/config.ini"
conversation_file = "../data/conversation.json"

first_model = functions.load_config(config_file)
conversation = functions.load_conversation(conversation_file)

analyzer = functions.SentimentIntentionAnalyzer(first_model)
analysis = analyzer.analyze_conversation(conversation)

for turn in analysis:
    print(turn)
