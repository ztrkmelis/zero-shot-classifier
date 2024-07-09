from src import functions


def main():
    config_file = "../config/config.ini"
    conversation_file = "../data/conversation.json"

    loader = functions.LoadFiles(config_file, conversation_file)
    first_model = loader.load_config()
    conversation = loader.load_conversation()

    analyzer = functions.SentimentIntentionAnalyzer(first_model)
    analyzer.analyze_conversation(conversation)


if __name__ == '__main__':
    main()
