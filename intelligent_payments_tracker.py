![Watermark](https://github.com/papradhan/aiprojects/watermark.png)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 04:40:56 2023

@author: paramitapradhan

INTELLIGENT PAYMENTS TRACKER

"""
import csv
import openai
from langchain.llms import OpenAI
from secret_key import openai_key
openai.api_key = openai_key
llm = OpenAI(openai_api_key=(openai.api_key))

column_names = ['PaymentDate',	'PaymentID',	'PaymentActivity',	'TransferCurrency',
	'TransferAmount',	'DollarAmount',	'Client',	'PaymentMethod',
	'PaymentType',	'ClientID',	'ClientAcctID',	'ClientClearingSysID',
	'Beneficiary',	'BeneAcctID',	'ReasonText',	'ReasonCode',
	'Status',	'SubStatus',	'MsgID',	'OrigMsgID',	'CustomerPaymentStatus']

# list to hold the updated rows
updated_rows = []

csv_file = './PI.csv'


with open(csv_file, 'r', newline='') as file:
    reader = csv.DictReader(file)
    
    updated_rows.append(column_names)
    
    for col in reader:
        if 'Payment Completion Received' in col['PaymentActivity']:
            if 'ACCP' in col['CustomerPaymentStatus']:
                col['Status'] = 'Completed'
                col['SubStatus'] = 'Confirmed'
                
        if 'Payment Instruction Received' in col['PaymentActivity']:
                col['Status'] = 'OnTrack'
                col['SubStatus'] = 'Processing'
                
        if 'Payment Status Received' in col['PaymentActivity']:
            if 'ACCP' in col['CustomerPaymentStatus']:
                col['Status'] = 'OnTrack'
                col['SubStatus'] = 'Processing'
           
            if 'RJCT' in col['CustomerPaymentStatus']:
                col['Status'] = 'Exception'
                col['SubStatus'] = 'Rejected'
            
                if not col['ReasonText']:
                    col['ReasonText'] = 'Processing Failed'
                if not col['ReasonCode']:
                    col['ReasonCode'] = 'NARR'
            
            elif 'RTRN' in col['CustomerPaymentStatus']:
                col['Status'] = 'Exception'
                col['SubStatus'] = 'Returned'
            
                if not col['ReasonText']:
                    col['ReasonText'] = 'Payment Returned'
                if not col['ReasonCode']:
                    col['ReasonCode'] = 'NARR'
            
        updated_rows.append([col[column] for column in column_names])
        
        
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerows(updated_rows)


print("CSV updated successfully.")
