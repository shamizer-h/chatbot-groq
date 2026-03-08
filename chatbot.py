import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY", ""))

conversation_history = []

system_message = {
    "role": "system",
    "content": "You are a helpful and friendly AI assistant. Answer clearly and concisely."
}

print("=" * 50)
print("        Welcome to AI Chatbot using Groq")
print("=" * 50)
print("Type your message and press Enter to chat.")
print("Type 'quit' to exit the chatbot.")
print("=" * 50)

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() in ["quit", "exit", "bye"]:
        print("\nChatbot: Goodbye! Have a great day!")
        break

    if not user_input:
        print("Please type something!")
        continue

    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[system_message] + conversation_history,
        max_tokens=1024,
        temperature=0.7
    )

    bot_reply = response.choices[0].message.content

    conversation_history.append({
        "role": "assistant",
        "content": bot_reply
    })

    print(f"\nChatbot: {bot_reply}")
