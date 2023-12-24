![Watermark](https://github.com/papradhan/aiprojects/watermark.png)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 20:24:56 2023
@author: paramitapradhan
"""
# Import prerequisite libraries
import openai
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
#from langchain.prompts import ChatPromptTemplate
#from langchain.schema import BaseOutputParser

from secret_key import openai_key
openai.api_key = openai_key
llm = OpenAI(openai_api_key=(openai.api_key))   # integrate langchain with openai

text = """
response = llm.invoke("List all the chinese zodiac animals")
print ("Lets play Langchain")
print (response)
"""

# chatbot
chat = ChatOpenAI(openai_api_key=(openai.api_key))     # frequently used - HumanMessage, AIMessage, and SystemMessage
from langchain.schema.messages import HumanMessage, SystemMessage, AIMessage
messages = [
    SystemMessage(content="You are Deutsche Bank"),
    HumanMessage(content="What line of business are you associated with"), # AS A HUMAN 
    ]
response = chat.invoke(messages)
print(response)

messages = [
    SystemMessage(content="You are Deutsche Bank"),
    AIMessage(content="What can you tell me about yourself") # AN AN AI LM
    ]
response = chat.invoke(messages)
print(response)
