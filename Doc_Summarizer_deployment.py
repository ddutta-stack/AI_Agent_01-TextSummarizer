from fastapi import FastAPI
import requests
from typing Union
# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
# It is easy to use and allows for automatic generation of OpenAPI documentation.
#creating an object of FastAPI
app = FastAPI() 
ollama_url = "http://localhost:11434/v1/chat/completions"
@app.post("/summarize")
def summarize_document(text_document: str):
    payload = {
        "model": "deepseek-r1:1.5b",
        "prompt": f"summarize this text in formal style but in technical summary format ** two sentences with bullet points** :\n\n {text_document}",
        "stream": False,
        }
    response = requests.post(ollama_url, json=payload)
    return response.json().get("response", "No response found")
## to run this use this command in terminal -> 1. pip install uvicorn 2. uvicorn app: Doc_Summarizer_deployment.py --reload