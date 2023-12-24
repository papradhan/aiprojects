![Watermark](https://github.com/papradhan/aiprojects/watermark.png)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-  
"""
Created on Tue Oct 31 15:12:32 2023

@author: paramitapradhan

Coverletter Generation

LAUNCH TERMINAL
EXECUTE THIS CMD LINE - 
streamlit run /Users/paramitapradhan/Documents/Paramita/pythonProject/coverletter.py

"""

import streamlit as st
import datetime as dt

st.title('COVER LETTER | http://localhost:8501')
jobrole = st.text_input('ROLE NAME:')
companyname = st.text_input('COMPANY NAME:')
gen_cv_4_display = st.button('DISPLAY COVER LETTER')   

Signature_contents = f"""
Best regards,
Paramita

Personal Values: Customer Focus | Adaptability | Ownership | Intellectual Curiosity | Build Trust | Think Big | High Standards | Proactive Problem Solving | Tangible Outcomes

LinkedIn: https://www.linkedin.com/in/paramitaapradhan/
Mobile: 919-802-3238
Email: paramita.a.pradhan@gmail.com
    
"""

Coverletter_contents = f"""Subject: Application for {jobrole} at {companyname}

Dear Hiring Team,   

I am writing to express my strong interest in the {jobrole} role at {companyname}. With over two decades of experience in the software development industry and a proven track record in leading high-performing teams, I believe I am well-prepared to help build, execute, and communicate {companyname}'s Engineering Vision. 

Your job description resonated with my career journey, particularly my recent role as Product Development Manager at Deutsche Bank, where I successfully managed complex projects, defined clear requirements, and delivered on commitments. I am excited about the opportunity to lead a group of talented engineers and engineering managers as direct reports, providing mentorship and fostering their career growth.

Throughout my career, I have been a staunch advocate for user experience and front-end design, and I have a deep understanding of technical components at a system level. Collaborating with cross-functional teams, such as Product Managers and Engineering groups, to provide technical feasibility, specifications, and estimates for project-level work is a strength I bring to the table.

I'm not only results-driven & lead by example but also a firm believer in data-driven decision-making and focused on the 'why' and 'what', aligning perfectly with {companyname}'s DEI and meritocratic culture. Moreover, I possess a strong sense of urgency towards action and the ability to communicate effectively across all levels of the organization. I have actively participated in producing engineering insights, setting KPIs and OKRs, and writing reports to develop and communicate ideas. While I have gained valuable experience in this area working alongside my co-leaders, I see this as an ongoing learning opportunity where I can continue to grow and enhance my expertise.

In my overall two decades of experience, I have well over eight years of software development experience as an individual contributor, reaching Senior and Staff-level engineering roles at IBM before transitioning into financial services and proceeding into management. I have successfully managed teams of 18-20 individuals thus far, including people leaders, with a focus on motivation, recognition, and trust building. Furthermore, I have a solid grasp of engineering best practices, CI/CD, database management, security product optimization, scaling and go-to-market strategy.

Enclosed is my resume, which provides further details about my professional background. I would welcome the opportunity to discuss how my qualifications align with your needs in more detail. Please feel free to reach out to me at my contact information below.

Thank you for considering my application. I am enthusiastic about the possibility of contributing to {companyname}'s future achievements.

{Signature_contents}  

"""

if gen_cv_4_display:
    st.success("Subject: Application for {} at {}".format(jobrole,companyname))
    st.success("Dear Hiring Team,")
    st.success("I am writing to express my strong interest in the {} role at {}. With over two decades of experience in the software development industry and a proven track record in leading high-performing teams, Ibelieve I am well-prepared to help build, execute, and communicate {}'s Engineering Vision.".format(jobrole,companyname,companyname))
 
    
st.download_button('DOWNLOAD COVER LETTER', Coverletter_contents, 'ParamitaPradhan/CoverLetter/{}'.format(dt.datetime.now()))


