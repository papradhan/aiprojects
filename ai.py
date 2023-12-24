![Watermark](https://github.com/papradhan/aiprojects/raw/main/watermark.png)
#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Create GPTs using Openai API calls

@author: paramitapradhan

https://platform.openai.com/account/limits
"""
cls = lambda: print("\033[2J\033[;H", end='')
cls()
import openai
from secret_key import openai_key
import warnings
warnings.filterwarnings("ignore",message="Reloaded modules: secret_key")

openai.api_key = openai_key

messages_list=[
    {'role' : 'system',   'content' : 'Hi there! Anything i can help you with today?'},
    {'role' : 'user',     'content' : 'Payments Tracker isnt loading. Can you help?'},
    {'role' : 'assistant','content' : 'Thank you for catching that! Let me restart the Payments Tracker for you'},
    {'role' : 'assistant','content' : 'I have opened an Incident for our team to look into it'},
    {'role' : 'assistant','content' : 'The Payments Tracker has been restarted. Please let us know if you see the issue again'},
    {'role' : 'user',     'content' : 'Thanks for your help! The Tracker is working for me now.'},
    {'role' : 'assistant','content' : 'Glad its working for you. Please let me know if there\'s anything else i can help with'}
]

def Job_sample():
    response = openai.ChatCompletion.create(                                #Api call
        model = 'gpt-3.5-turbo',
        messages=[
            {'role' : 'user','content' : 'the American flag has colors -'}  # dict - key value pair
        ],
        max_tokens = 50,                                # max words for API to send back in response
        n=10,                                            # num of responses sent back by API model
        temperature=2                                   # make resp random(2) or predictable(0)
    )
    
    response.to_dict()                                  # Api resp in hierarchical JSON format
    
    # the choices field is what holds the response from this language model
    # here we're interested in the CONTENT of the first element at index 0
    # this is equivalent to going to ChatGPT and typing in 'Get the company name and job role'
    print(response.choices[0]['message']['content'])
    


def Chatbot_sample():
    
    for r in range(10): 
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages_list,
            max_tokens = 15,
            n=1,
            temperature=0
        )
        
        print(response.choices[0].message.content)
    
    
    
if __name__ == '__main__':
    #print(openai.Model.list())      # no api calls via token made here
    Job_sample()
    #Chatbot_sample()
