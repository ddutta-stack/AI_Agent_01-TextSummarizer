# API calling for Deepseek
# import requests
# import json
# gradio is a library used for creating a web interface for the DeepSeek model
import gradio as gr
import requests
# Define the URL for the DeepSeek API and ollama API
ollamaurl = "http://localhost:11434/api/generate"
# Define the function to query the DeepSeek model
def summarize_text(prompt):
    """ Function to summarize text using the DeepSeek model.
    Args:
        prompt (str): The text to be summarized."""
    
    payload = {
        "model": "deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False,
        "temperature": 0.6
    }
    response = requests.post(ollamaurl, json=payload)
    if response.status_code == 200:
        return response.json().get("response", "No response found")
    else:
        return f"Error observed: {response.status_code} - {response.text}"
    
### Logic -- May be we can comment this fo rtime being as we are laready using the Gradio UI Interface---

# if __name__ == "__main__":
#     sample_text=''' Artificial Intelligence (AI) has revolutionized various sectors, enhancing business performance, improving 
#     weather forecasting, accelerating drug discovery, and advancing nuclear fusion research. However, it also poses risks 
#     such as job displacement, ethical concerns, and potential misuse. Addressing these challenges is crucial for 
#     harnessing AI's benefits while mitigating its risks.'''    
# print('### Summary of the text using DeepSeek model ###')
# print(summarize_text(sample_text))  # Print the summary of the sample text

# ---Define the Gradio interface--

interface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=10, label="Enter text to summarize"),
    outputs=gr.Textbox(label="Summary of your text"),
    title="DeepSeek Text Summarizer",
    description="This application uses the DeepSeek model to summarize text input."
)
