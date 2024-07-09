import streamlit as st
from src import functions


# Streamlit App
st.title("Zero-Shot Sentiment and Intention Analysis")

conversation_file = "data/conversation.json"
conversation_example = functions.load_conversation(conversation_file)

# Show conversation example
st.write("### Conversation Example")
for turn in conversation_example:
    st.write(f"**{turn['role'].capitalize()}:** {turn['text']}")

# Analyze conversation button
if st.button("Analyze Conversation"):
    analyzer = functions.SentimentIntentionAnalyzer("facebook/bart-large-mnli")
    analysis = analyzer.analyze_conversation(conversation_example)

    st.write("### Analysis Results")
    for result in analysis:
        st.write(f"**{result['role'].capitalize()}:** {result['text']}")
        st.write(f"**Sentiment:** {result['sentiment']}")
        st.write(f"**Intention:** {result['intention']}")
        st.write("---")

# Input for custom text
st.write("### Custom Text Analysis")
custom_text = st.text_area("Enter text here:", "")
if custom_text:
    analyzer = functions.SentimentIntentionAnalyzer("facebook/bart-large-mnli")
    sentiment = analyzer.analyze_sentiment(custom_text)
    intention = analyzer.analyze_intention(custom_text)

    st.write("### Custom Text Analysis Results\n")
    st.write(f"**Text:** \n{custom_text}\n")
    st.write(f"**Sentiment:** label:\n {sentiment['labels'][0]}\n\n  score:\n{sentiment['scores'][0]}\n ")
    st.write(f"**Intention:** \n{intention}\n")


# Input for custom dialogue
st.write("### Enter Dialogue")

conversation = []
role = st.radio("Role", ("agent", "customer"))
text = st.text_input("Text")
if st.button("Add Message"):
    if text:
        conversation.append({"role": role, "text": text})
        st.write(f"**{role.capitalize()}:** {text}")
        st.text_input("Text", value="", key=len(conversation))

# Show conversation and analyze button
if st.button("Analyze Conversation - Dialog"):
    if conversation:
        analyzer = functions.SentimentIntentionAnalyzer("facebook/bart-large-mnli")
        analysis = analyzer.analyze_conversation(conversation)

        st.write("### Analysis Results")
        for result in analysis:
            st.write(f"**{result['role'].capitalize()}:** {result['text']}")
            st.write(f"**Sentiment:** {result['sentiment']}")
            st.write(f"**Intention:** {result['intention']}")
            st.write("---")
    else:
        st.write("Please enter at least one message in the dialogue.")

# Display the current conversation for reference
if conversation:
    st.write("### Current Conversation")
    for turn in conversation:
        st.write(f"**{turn['role'].capitalize()}:** {turn['text']}")