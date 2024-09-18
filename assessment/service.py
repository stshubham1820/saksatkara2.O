import json,re
import requests
from saksatkara.settings import OPENAI_API_KEY

class QuestionService:
    
    def prompt_text(self,skills):
        

        short_summaries = []
        response = None
        max_chunk_length = 4500


        url = "https://api.openai.com/v1/chat/completions"

        payload = json.dumps({
        "model": "gpt-4-turbo",
        "messages": [
            {
            "role": "system",
            "content": """You are a helpful assistant that know how to create Interview Questions for Developers
            The format of the Question will be as mentioned each question should be inside an array so that it can be easily accessible, also make sure that key should be in mentioned case only:
            {"Questions":[]}"""
            },
            {
            "role": "user",
            "content": f"Please Identify 10 very important Interview question on following topics the mentions topics is in sequence of topic and subtopic : {skills}\n"
            }
        ],
        "temperature": 0.5,
        "top_p" : 0.95,
        })
        
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}'
        }


        response = requests.request("POST", url, headers=headers, data=payload)

        choices = response.json().get('choices')
        data = choices[0]
        message = data.get('message')
        content = message.get('content')
        
        short_selling_text = content.strip()

        return short_selling_text