"""Module api openAi"""

import openai

openai.api_key = "your api key"

while True:
    try:
        prompt = input("\nEnter your question: ")

        if prompt == "exit":
            break

        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2048)
        print(completion.choices[0].text)

    except ValueError:
        print("something unexpected happened")
