# OpenAI-based summarization logic

import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_with_gpt(text: str, prompt_instruction: str = "Summarize the following text in a clear and concise way:") -> str:
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful academic assistant."},
            {"role": "user", "content": f"{prompt_instruction}\n\n{text}"}
        ],
        temperature=0.4,
        max_tokens=1024
    )
    return response.choices[0].message.content.strip()