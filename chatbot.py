from fastapi import FastAPI
from openai import OpenAI

app = FastAPI()

OPENAI_API_KEY = "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"

@app.post("/chatbot/")
def chatbot_response(user_input: str):
    response = OpenAI(api_key=OPENAI_API_KEY).chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    return {"response": response.choices[0].message["content"]}
