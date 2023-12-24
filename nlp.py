![Watermark](https://github.com/papradhan/aiprojects/watermark.png)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 20:24:56 2023

@author: paramitapradhan

EXPLORE NATURAL LANG PROCESSING

THIS PROGRAM SHOULD BE ABLE TO IDENTIFY IF ITS A PRO / CON / POSITIVE / NEGATIVE FROM THE SENTENCE PROVIDED
"""
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#import nlp
#nltk.download(('vader_lexicon'))

sentences = [
"The only pro that I was able to identify in this organization was that work life balance is good.",
"People are great and super friendly",
"Good benefits including health insurance and number of annual leaves",
"Good Working Culture and good for Work",
"They might offer you good salary but that could be a trap in your career.",
"Management is poor with little vision of the future and work in silos only caring about their own areas.",
"Low hikes and effectively no bonuses",
"long hours; at times unrealistic expectations; overly complex procedures just to perform daily necessary tasks.",
"Not all managers are good",
"Late working hours which at times get frustrating"
    ]


for sentens in sentences:
    print(sentens)

senti = SentimentIntensityAnalyzer()

def is_sent_a_pro_or_con(sentens):
    sentiment_score = senti.polarity_scores(sentens)
    print(sentiment_score)
    if sentiment_score['compound'] >= 0.2:
        return "PRO", sentiment_score['compound'], sentiment_score['neg'], sentiment_score['pos']
    if sentiment_score['compound'] <= -0.2:
        return "CON", sentiment_score['compound'], sentiment_score['neg'], sentiment_score['pos']
    else:
        return "CAN'T SAY", sentiment_score['compound'], sentiment_score['neg'], sentiment_score['pos']
    

# assign positive or negative to each sentence
posi_nega_sentences = [(sentens, is_sent_a_pro_or_con(sentens)) for sentens in sentences]

for sentens, label in posi_nega_sentences:
    print(f"Sentence: '{sentens}' -- {label}\n")



