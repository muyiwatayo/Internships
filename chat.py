import re

def simple_chatbot():
    """A simple rule-based chatbot function."""
    
    # Define a dictionary of patterns and responses
    # The keys are regular expressions (patterns) to match in the user's input,
    # and the values are the corresponding responses.
    rules = {
        r'hi|hello|hey': 'Hello! How can I help you today?',
        r'how are you': 'I am an AI, so I don\'t have feelings, but I\'m ready to chat!',
        r'what is your name': 'I am a simple rule-based chatbot, a creation of Python code.',
        r'weather|temperature': 'I cannot check the current weather, but I can talk about other things.',
        r'bye|goodbye|exit': 'Goodbye! It was nice chatting with you.',
        r'thank you|thanks': 'You\'re welcome!',
        r'.*': 'I\'m not sure how to respond to that. Can you try asking something else?', # Default response
    }

    print("--- Simple Chatbot Initialized ---")
    print("Type 'bye' or 'exit' to quit.")
    
    while True:
        user_input = input("You: ").lower().strip()

        # Check for the exit command first
        if user_input in ['bye', 'goodbye', 'exit']:
            print("Chatbot: Goodbye! It was nice chatting with you.")
            break
        
        # Iterate through the rules to find a match
        matched = False
        for pattern, response in rules.items():
            # Use re.search for flexible pattern matching anywhere in the input
            if re.search(pattern, user_input):
                print(f"Chatbot: {response}")
                matched = True
                break
        
        # The default response is already handled by the '.*' pattern at the end of the rules.
        # This check is technically redundant but helps illustrate the matching process.
        # if not matched:
        #     print("Chatbot: I'm not sure how to respond to that. Can you try asking something else?")

# To run the chatbot:
if __name__ == "__main__":
    simple_chatbot()