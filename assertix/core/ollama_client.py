import requests
from assertix.config import MODEL, OLLAMA_URL

def query_ollama(prompt):
    res = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    })
    return res.json()["response"]