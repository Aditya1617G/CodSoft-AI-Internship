# Task 2 – Rule-Based Chatbot
# Created by Aditya for CodSoft AI Internship – 2025

print("Chatbot: Hello! I'm your AI assistant. Type 'bye' to end the chat.")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("Chatbot: Hello there! How can I help you?")
    elif "how are you" in user_input:
        print("Chatbot: I'm doing great! Thanks for asking. What about you?")
    elif "your name" in user_input:
        print("Chatbot: I'm a rule-based chatbot created by Aditya during the CodSoft Internship.")
    elif "what is codsoft" in user_input:
        print("Chatbot: CodSoft is an amazing internship platform for beginners in AI and tech!")
    elif "what can you do" in user_input:
        print("Chatbot: I can chat, respond to greetings, and answer basic questions. Try asking me something!")
    elif "who made you" in user_input:
        print("Chatbot: I was developed by Aditya as part of his CodSoft AI internship project.")
    elif "bye" in user_input or "exit" in user_input:
        print("Chatbot: Goodbye! Have a great day!")
        break
    else:
        print("Chatbot: Sorry, I didn't understand that. Try asking something else!")
