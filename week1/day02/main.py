"""
Day 02:
Topics: 
    - System role,
    - Temperature       # in groq, 3 temperature are {0, 1, 2}.

"""

import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found!")

client = Groq(api_key=my_api_key)
model = "llama-3.1-8b-instant"

messages = [
    {
        "role": "system",
        "content": "Act as a highly creative and adaptive thinker."
    },
    {
        "role": "user", 
        "content": "Provide only a single Romanized Hindi word for my coffee shop, with no additional text."
     }
]

response = client.chat.completions.create(model=model, temperature=2, messages=messages)
print(response.choices[0].message.content)
