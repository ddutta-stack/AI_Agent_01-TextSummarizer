import requests
#Define the url for the DeepSeek API and ollama API -- 11434
ollamaurl=https://localhost:11434/api/generate

def deepseek(prompt):
    payload={
        "model":"deepseek-r1:1.5b",
        "prompt":prompt, 
        "stream":False 
        #temperature=0.7,
        #top_p=0.9
    }
