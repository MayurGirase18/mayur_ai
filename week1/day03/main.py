"""
Day 03:
Topics: 
    - Tokens,
    - Usage,
    - max_tokens,
    - finish_reason

"""

import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path = env_path)

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Key not found!")

client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

messages = [
    {
        "role": "system",
        "content": "Act as Jatin Sapru. Use poetic Hinglish energy, rhyming catchphrases like 'Aa jao strike rate ke deewano', 'Takht bhi inka, waqt bhi inka', and 'Virat ke bat se virasat pe mohar'. Keep it strictly under 3 lines."
    },
    {
        "role": "user",
        "content": "Commentate on Virat Kohli finishing IPL 2026 with a winning 75* off 42 for RCB!"
    }
]

response = client.chat.completions.create(model=model, messages=messages, max_tokens=20)
print(response.choices[0].message.content)

usage = response.usage
pt = usage.prompt_tokens
ct = usage.completion_tokens
tt = usage.total_tokens

fr = response.choices[0].finish_reason

print("Prompt Tokens: ", pt)
print("Completion Tokens: ", ct)
print("Total Tokens: ", tt)
print("Finish Reason:", fr)