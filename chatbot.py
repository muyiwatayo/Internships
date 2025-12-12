import os
from dotenv import load_dotenv
load_dotenv()

from gemini import Gemini

client = Gemini(api_key=os.environ["API_KEY"])

system_prompt = "You are a friendly and supporting teaching assistant for for XD "

user_prompt = input("What's your question? ")

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    model="gemini-2o"
)

response_text = chat_completion.choices[0].message.content

print(response_text)