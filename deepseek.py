import requests
#Define the url for the DeepSeek API and ollama API -- 11434
ollamaurl="https://localhost:11434/api/generate"

# Define the function to query the DeepSeek model
def deepseek_query01(prompt):
    payload={
        "model":"deepseek-r1:1.5b",
        "prompt":prompt, 
        "stream":False 
        #temperature=0.7,
        #top_p=0.9
    }
    response= requests.post(ollamaurl, json=payload)
    if response.status_code == 200:
        return response.json().get("response", "No response found")
    else:
        return f"Error observed : {response.status_code} - {response.text}"   


# Example usage or testing the model
test_prompt = '''The development of Artificial Intelligence (AI) has brought about significant advancements and transformations across various sectors. However, it also poses certain risks and challenges that need to be addressed.

Benefits of AI
Increased Business Performance: AI has been credited with enhancing business performance by automating repetitive tasks, improving decision-making processes, and streamlining operations. For instance, AI-powered business intelligence tools enable data-driven decision-making, leading to increased revenues and profits
1.
Weather Forecasting and Disaster Prediction: AI models have been used to analyze data on natural disasters, such as floods and wildfires, helping scientists predict and mitigate their impacts. For example, IBM and NASA collaborated on a model that provides accurate rainfall forecasts and flood warnings
2.
Drug Discovery: AI has accelerated the process of drug discovery by predicting the three-dimensional shapes of proteins and generating potential antiviral drugs. This has been particularly useful in responding to the COVID-19 pandemic
3.
Nuclear Fusion Research: AI has been instrumental in advancing nuclear fusion research by predicting and avoiding instabilities in tokamaks, which are devices used to contain superheated plasma for nuclear fusion
1'''
response = deepseek_query01(test_prompt)
print("Response from DeepSeek model starts here:")
print(response)  # Print the response from the DeepSeek model   

