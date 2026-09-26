"""
Day 04:
Topics: 
    - Pydantic,
    - Structured output,
    - Json Schema,

"""


import os
import json

from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel, ValidationError

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path = env_path)

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found!")

client = Groq(api_key=my_api_key)

class Ticket(BaseModel):
    name: str
    email: str
    category: str
    priority: str
    summary: str

schema = Ticket.model_json_schema()

user_text = """Hi, my name is Mayur.
My email is mayur@gmail.com.

I cannot login to my account since yesterday.
This is urgent because I need to access my account today."""


system_prompt = f"""
You are a customer Support ticket Extractor.

Extract the following information from the customer's message:
- name 
- email 
- category 
- priority 
- summary 

Return only valid JSON.

Your output must follow this schema:
{json.dumps(schema, indent=2)}
"""

response = client.chat.completions.create(
    model = "openai/gpt-oss-120b",

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },

        {
            "role": "user",
            "content": user_text
        }
    ],

    response_format = {
        "type": "json_object"
    }
)


raw_output = response.choices[0].message.content
print(raw_output)
