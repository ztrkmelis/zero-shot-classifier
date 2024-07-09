# Zero Shot Dialog Classifier #

This project is designed to demonstrate the ability to build a sentiment and intention classifier using a zero-shot classification model from Hugging Face's transformers library. The project involves creating a simulated chat transcript, analyzing it for sentiment and intention, and packaging the solution as a Python package.

##  Directory Structure
```
project/
│
├── src/
│   ├── __init__.py
│   ├── functions.py
│
├── config/
│   ├── config.ini
│
├── data/
│   ├── conversation.json
│
├── resources/
│   ├── model.py
│
├── setup.py
└── README.md
```

## Installation

1.  Clone the repository:

```
git clone https://github.com/ztrkmelis/zero-shot-classifier
``` 

2. Install required packages:
Install the package:
```
pip install requirements.txt
```

3. Install the package:
```
python setup.py install
```

## Configuration

The configuration file is located at config/config.ini. It specifies the model name to be used for zero-shot classification.

config/config.yaml:
```
ModelName1 = facebook/bart-large-mnli
```

## Data
The simulated chat data is stored in data/conversations.json.

data/chat_data.json:
```
{
  "conversation": [
    {"role": "agent", "text": "Hello! How can I assist you today?"},
    {"role": "customer", "text": "Hi, I am interested in buying the new iPhone 14."},
    {"role": "agent", "text": "Great choice! The iPhone 14 is a fantastic phone. Are you looking for any specific color or storage capacity?"},
    ...
  ]
}
```

## Usage
To run the sentiment and intention classification:

Navigate to the project directory.
Call the sentiment and intention classification script form main.py
```
python zero_shot_analyzer/main.py
```

## Sample Output
```
Message: agent
Sentiment: {'positive': 0.569855809211731}
Intention: {'assistance': 0.8100928664207458, 'help': 0.7849386930465698, 'compare': 0.7784042358398438, 'offers': 0.6487736701965332, 'features inquiry': 0.6237306594848633, 'evaluate': 0.621386706829071, 'comparison': 0.5866707563400269, 'support': 0.5098862051963806}
-----
Message: customer
Sentiment: {'positive': 0.6837472915649414}
Intention: {'order': 0.944553792476654, 'compare': 0.917231559753418, 'purchase': 0.873462975025177, 'help': 0.8684824705123901, 'thanks': 0.7722960710525513, 'buy': 0.7704021334648132, 'offers': 0.7506646513938904, 'greeting': 0.7314315438270569, 'features inquiry': 0.7022606134414673, 'evaluate': 0.6893923282623291, 'feedback': 0.6095067858695984, 'availability': 0.6017317175865173, 'change package': 0.5485347509384155, 'ask about product': 0.5394827127456665, 'assistance': 0.5387248992919922}
-----
```

## Streamlit demo
It is possible see a demo and play with the model results thanks to a streamlit demo. To run the streamlit app, use the following command:

To run the Streamlit app, use the following command:
```
streamlit run streamlit_app.py
```

### Streamlit App Usage
1. Enter Dialogue: 
Add messages to the dialogue by selecting the role (agent or customer) and typing the message text. Click "Add Message" to add each message to the conversation.

2. Analyze Conversation: Once you have entered the dialogue, click the "Analyze Conversation" button to analyze the sentiment and intention of each message.

3. View Results: The analysis results will be displayed below the conversation input section, showing the sentiment and intention for each message.

### Streamlit App Example
Here's an example of how you might use the app:

1. Add a message from the agent: "Hello! How can I assist you today?"
2. Add a message from the customer: "Hi, I am interested in buying the new iPhone 14."
3. Continue adding messages to build the conversation.
4. Click "Analyze Conversation" to see the sentiment and intention for each message.

## Discussion Questions

### 1. Advantages and Disadvantages of Zero-Shot Learning
##### Advantages:

1. Flexibility: Zero-shot learning can classify text into categories without needing any task-specific training data.

2. Efficiency: Saves time and resources as it doesn’t require a labeled dataset for every new task.

3. Scalability: Easily adaptable to various tasks and domains with the same pre-trained model.

##### Disadvantages:

1. Accuracy: May not be as accurate as models fine-tuned on specific datasets.
2. Context Understanding: Might struggle with nuanced or context-specific language understanding.
3. Resource Intensive: Requires powerful computational resources for inference with large models.

##### Use Turkish Model:

1. Model Availability: Use models specifically trained on Turkish datasets.
2. Data Augmentation: Create a Turkish-specific dataset for fine-tuning.
3. Language Adaptation: Ensure the model understands Turkish syntax and context by leveraging models pre-trained on Turkish text.

### 2. Dialog or Independent Parts

Considering the case study above, the system can be thought of either as analyzing independent messages (independent particles) or as understanding the flow of a conversation (dialog). Here's a detailed comparison and suggestion.

#### Independent Parts
##### Advantages:

1. Simplicity: Each message is processed independently, which simplifies the implementation.
2. Scalability: It is easy to scale as each message is treated as a standalone entity, requiring no context management.

##### Disadvantages:

1. Context Ignorance: The model may fail to capture the context of the conversation, leading to potential misinterpretation of intentions or sentiments that depend on previous interactions.

#### Dialog Context
##### Advantages:

1. Context Awareness: Understanding the flow and context of a conversation improves the accuracy of sentiment and intention predictions.
2. Coherent Analysis: Keeping a dialog history may allow for more coherent and contextually relevant responses.

##### Disadvantages:

1. Complexity: Managing and maintaining the state of the conversation increases the complexity of the implementation.
2. Resource Intensive: Tracking and processing the entire conversation history can be resource intensive.

##### Code Enhancements for a Dialog Based System
To evaluate the system as a dialog, the following enhancements can be made to the existing code:

1. Implement a mechanism to track the history of conversations between the agent and the customer.

2. Fine tune models for conversational understanding, BERT or GPT based contextual architectures may handle context across multiple turns.

3. Advanced Pipelines: Use conversational AI techniques, such as Hugging Face's transformers conversational pipelines.


Thank you for reading!