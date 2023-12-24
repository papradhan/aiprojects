![Watermark](https://github.com/papradhan/aiprojects/watermark.png)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 00:25:43 2023

@author: paramitapradhan

COVERLETTER POWERED BY AI

streamlit run /Users/paramitapradhan/Documents/333-Paramita/pythonProject/crashcourse/coverletter.py

"""
import streamlit as st
import openai
from secret_key import openai_key

import warnings
warnings.filterwarnings("ignore",message="Reloaded modules: secret_key")

openai.api_key = openai_key
    

def Build_a_CoverLetter():
    st.markdown("""
    # 📝 AI-Powered Cover Letter Generator
    Paste the JOB DESC to Generate a cover letter
    """
    )

    with st.form('input_form'):
        job_desc = st.text_input('Your Pasted Job Description')
        res_text = st.text_input('Your Key Experience')
        user_name = st.text_input('Your name')
        company = st.text_input('Company name')
        role = st.text_input('Job title/role')
        referral = st.text_input('How did you find out about this opportunity?')
        submitted = st.form_submit_button("Generate Cover Letter")
        
    # if the form is submitted run the openai completion   
    if submitted:
        completion = openai.ChatCompletion.create(
          model = "gpt-4-1106-preview",
          messages = [
            {"role": "user", "content" : f"You will need to generate a cover letter based on specific resume and a job description"},
            {"role": "user", "content" : f"My resume text: {res_text}"},
            {"role": "user", "content" : f"The job description is: {job_desc}"},
            {"role": "user", "content" : f"The candidate's name to include on the cover letter: {user_name}"},
            {"role": "user", "content" : f"The job title/role : {role}"},
            {"role": "user", "content" : f"How you heard about the opportunity: {referral}"},
            {"role": "user", "content" : f"The company to which you are generating the cover letter for: {company}"},
            {"role": "user", "content" : f"The cover letter should have three content paragraphs"},
            {"role": "user", "content" : f""" 
            In the first paragraph focus on the following: you will convey who you are, what position you are interested in, and where you heard
            about it, and summarize what you have to offer based on the above resume
            """},
                {"role": "user", "content" : f""" 
            In the second paragraph focus on why the candidate is a great fit drawing parallels between the experience included in the resume 
            and the qualifications on the job description.
            """},
                    {"role": "user", "content" : f""" 
            In the 3RD PARAGRAPH: Conclusion
            Restate your interest in the organization and/or job and summarize what you have to offer and thank the reader for their time and consideration.
            """},
            {"role": "user", "content" : f""" 
            note that contact information may be found in the included resume text and use and/or summarize specific resume context for the letter
                """},
            {"role": "user", "content" : f"Use {user_name} as the candidate"},
          ]
        )
        response_out = completion['choices'][0]['message']['content']
        st.write(response_out)
        st.download_button('Download the cover_letter', response_out)
    
    
    
if __name__ == '__main__':
    print (
        """
        To view this Streamlit app on a browser, run it with the following command:
        streamlit run /Users/paramitapradhan/Documents/333-Paramita/pythonProject/crashcourse/coverletter.py [ARGUMENTS]")
        """
        )
    Build_a_CoverLetter()
    
    
    
### SAMPLE JD 
"""
Job description
Description and Requirements

Role Value Proposition:
You will be responsible for end-to-end, long-term lifecycle and technical direction of IT product development teams including multi-phased initiatives from original concept through final implementation and maintenance; creating plans, schedules, estimates, allocation of people, and status sharing in an Agile environment. You will be managing full-stack software engineers on a fast-paced team building and running systems that are customer-first, leveraging modern, cloud technologies, cutting edge design, and integrations across the entire software stack. You will also work closely with our Product and Design teams, to help shape the solutions that we deliver to our customers. You will have an opportunity to impact every part of the system, foster and cultivate your curiosity and fill a critical role enabling the team to focus on delivering amazing technology and customer solutions.

Key Responsibilities:
• Application roadmap that allows the product to deliver value in the short and long term
• Managing the overall technical implementation across the Product portfolio
• Remove barriers from Development teams to increase: CI/CD, Test Automation, Integration of Production Mgmt
• Establish and enforce best practices in code control, code reviews, unit testing, DevOps, and application maintenance
• Ensuring secure, high code quality across the entire team
• Identify risk and drive audits to conclusion
• Utilize Agile software development metrics, maintenance metrics and KPIs to help optimize product delivery
• Deeply manages financials and budgets
• People/Resource Management (hiring, development, engaging talent, utilization)
• Vendor accountability

Essential Business Experience and Technical Skills:
Required:
• Bachelor's Degree in Computer Science or related field
• Passion for technology, deliberately bringing technology into your own life and the work that you do
• Experience with activities, tools and techniques for converting business requirements and logical models into a technical application design.
• Knowledge and ability to apply secure coding standards used to prevent security vulnerabilities
• Experience in manage effective teams through development opportunities, recognition and feedback for both onshore and offshore teams.
• Ability to build, deliver and operate complex, cloud-based systems
• Proficiency with Java custom development using Kubernetes, Nano, Groovy, React, Remix
• Proficiency with, at least, one web language such as JavaScript, Typescript, PHP
• Proficiency with various database technologies and solutions such as MongoDB, CosmoDB
• Proficiency with modern web framework such as Node.js, AngularJS or VueJS
• Cross functional leadership: organize, motivate and lead those outside of the team

Preferred:
• Master's Degree in Computer Science or related field
• DevOps practices for CI/CD, release management, and automation using Azure DevOps
• Git-based repositories such as GitHub, Bitbucket or Azure Repos
• Container-based development leveraging Docker and/or Kubernetes
• Microsoft Azure Services: Functions, Kubernetes, CosmosDB,Storage, App Service
• Modern Identity and Access Management and general AppSec practices.
"""
