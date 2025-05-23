# chatbot_logic.py

def simple_chatbot(user_query):
    responses = {
        "What is the total revenue?": "The total revenue is $394.33 billion (Apple, 2022).",
        "How has net income changed over the last year?": "Net income has decreased by 5.2% from 2022 to 2023.",
        "What is the cash flow for Apple in 2024?": "Apple's cash flow in 2024 was $118.25 billion.",
        "How much did Tesla’s cash flow grow in 2024?": "Tesla's cash flow grew by 12.57% in 2024.",
        "What was Microsoft’s cash flow in 2023?": "Microsoft's cash flow in 2023 was $87.58 billion."
    }

    # Normalize query
    user_query = user_query.strip().lower()

    for key in responses:
        if user_query == key.lower():
            return responses[key]
    return "Sorry, I can only respond to predefined financial queries."


# For quick terminal testing
if __name__ == "__main__":
    print("\n📊 Financial Chatbot Ready!\n")
    print("💬 You can ask me the following predefined queries:")
    print("--------------------------------------------------")
    print("1. What is the total revenue?")
    print("2. How has net income changed over the last year?")
    print("3. What is the cash flow for Apple in 2024?")
    print("4. How much did Tesla’s cash flow grow in 2024?")
    print("5. What was Microsoft’s cash flow in 2023?")
    print("--------------------------------------------------")
    print("Type your query below (or type 'exit' to quit):\n")

    while True:
        query = input("You: ")
        if query.lower() == "exit":
            print("👋 Exiting chatbot. Goodbye!")
            break
        print("Bot:", simple_chatbot(query))
