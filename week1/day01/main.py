"""
Day 01:
Topics: 
    - Start the basics in AI Engineering Field.
    - User role, 
    - example: simple single response generate by AI.
    
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

env_path = Path(__file__).resolve().parents[2] /".env"
load_dotenv(dotenv_path = env_path)

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found!")

client = Groq(api_key = my_api_key)
model = "llama-3.1-8b-instant"
role = "user"
prompt = "Who is Virat Kohli?"

message = {
    "role": role,
    "content": prompt
}

messages = [message]

response = client.chat.completions.create(model=model, messages=messages)
print(response.choices[0].message.content)