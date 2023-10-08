import time
import requests
from transformers import pipeline


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        runtime_str = f"{func.__name__} took {elapsed_time:.2f} seconds to run"
        return result, runtime_str
    return wrapper


@timing_decorator
def classify_image(url):

    image_model = pipeline("image-classification", model="apple/mobilevit-small")
    labels = image_model(url)
    return labels


@timing_decorator
def get_location(type, hf_token):
    

    llm_url = "https://api-inference.huggingface.co/models/google/flan-t5-xxl"
    headers = {"Authorization": f"Bearer {hf_token}"}
    
    payload = {"inputs": f"Suggest a tourist attraction with category: {type}"} 
    response = requests.post(llm_url, headers=headers, json=payload)
    
    return response.json()
	

def show_output(output):

    if 'generated_text' in output[0]:
        return output[0]['generated_text']
    else:
        print(output)
        return "Error received. Please retry."
