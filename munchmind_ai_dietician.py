#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 11:25:43 2023

@author: paramitapradhan

An AI DIETICIAN App that helps you build a mindful approach to eating, guided by Intelligent Insights

streamlit run 
/Users/paramitapradhan/Documents/333-Paramita/pythonProject/crashcourse/ai_dietician_munchmind.py

"""
import streamlit as st
import openai
from secret_key import openai_key

import warnings
warnings.filterwarnings("ignore",message="Reloaded modules: secret_key")

openai.api_key = openai_key
    

def Launch_MunchMind():
    st.markdown("""
    # 📝 Welcome to MunchMind, Your Personalized AI-Powered Dietician!
    Embark on a Mindful Journey Towards a Healthier Lifestyle with Guided Intelligent Insights.
    """
    )

    with st.form('input_form'):
        name = st.text_input('Your Name')
        weight = st.text_input('Your Weight in LBs')
        height = st.text_input('Your Height')
        age = st.text_input('Your Age')
        triglycerides = st.text_input('Your Triglycerides')
        cuisine = st.text_input('Your usual choice of Cuisine at home')
        submitted = st.form_submit_button("Generate My Personalized Nutrition Plan")
        
    # if the form is submitted run the openai completion   
    if submitted:
        completion = openai.ChatCompletion.create(
          model = "gpt-3.5-turbo",
          messages = [
            {"role": "user", "content" : f"You will need to generate a Personalized Nutrition Plan based on Health Info"},
            {"role": "user", "content" : f"My weight is {weight}"},
            {"role": "user", "content" : f"My height is {height}"},
            {"role": "user", "content" : f"I'm {age} years old"},
            {"role": "user", "content" : f"My Triglycerides are {triglycerides}"},
            {"role": "user", "content" : f"My Nutrition Plan ..."},
            {"role": "user", "content" : f""" 
            In the first paragraph, focus on suggestions for me to reduce my carbohydrate intake, and summarize it
            """},
                {"role": "user", "content" : f""" 
            In the second paragraph focus on how exercise can help me reduce my weight.
            """},
                {"role": "user", "content" : f""" 
            In the third paragraph recommend some {cuisine} food choices that would be best for me.
            """},
                    {"role": "user", "content" : f""" 
            In the fourth paragraph: Conclusion
            Restate your commitments towards better health and summarize your next steps and thank the user {name} for using MunchMind.
            """},
          ]
        )
        response_out = completion['choices'][0]['message']['content']
        st.write(response_out)
        st.download_button('Download Your Personalized Nutrition Plan', response_out)
    
    
    
if __name__ == '__main__':
    print (
        """
        To view this Streamlit app on a browser, run it with the following command:
        streamlit run /Users/paramitapradhan/Documents/333-Paramita/pythonProject/crashcourse/ai_dietician_munchmind.py [ARGUMENTS]")
        """
        )
    Launch_MunchMind()
