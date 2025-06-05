import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.Chatcompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if__name__ == "__main__":
while True:
    user_input = input("you: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        break

    response = chat_with_gpt(user_input)
    print("chatbot:", response)
