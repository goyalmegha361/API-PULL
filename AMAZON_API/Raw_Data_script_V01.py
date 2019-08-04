
# coding: utf-8

# In[ ]:


"""
Spyder Editor

This is a temporary script file.
"""
import csv
import bottlenose
import pandas as pd
import time
from bs4 import BeautifulSoup

df= pd.read_excel("C:\\Users\\Megha115452\\Desktop\\Untitled Folder\\Handset_model_sample (2).xlsx")

access_key = 'AKIAIAVJFFOFPLUDEZ2Q'
secret_key = '9e9/hMi69v0r2MI+Ol7FVcE7CM9HlvLjAtkq/gH4'
associate_tag = 'technonews0ac-20'

amazon = bottlenose.Amazon(access_key,secret_key,associate_tag,Region="US")
dict_product= pd.DataFrame()

asin_temp=[]
title_temp=[]
price_temp=[]
brand_temp=[]
model_temp=[]
formatprice_temp=[]

for k in range(len(df.Insured_Device_Model)): 
    for i in range(1): #Only fetching records on first page out of 10
        response = amazon.ItemSearch(SearchIndex="Electronics" , ResponseGroup="ItemAttributes", BrowseNode ="7072561011",ItemPage=str(i+1), Brand=df.Insured_Device_Make[k], Keyword=df.Insured_Device_Model[k], Title=df.Insured_Device_Model[k])
        result = BeautifulSoup(response)
        asin_temp = result.find_all('asin')
        title_temp=result.find_all('title')
        price_temp = result.find_all('amount')
        brand_temp=result.find_all('brand')
        model_temp=result.find_all('model')
        formatprice_temp=result.find_all('formattedprice')
        if len(asin_temp) > 0 or asin_temp is not None:
            for j in range(len(asin_temp)):
                
                try:
                    
                    asin = asin_temp[j].text
                    title = title_temp[j].text
                    amount = price_temp[j].text
                    
                    try:
                        brand = brand_temp[j].text
                    except Exception as e:
                        brand = "NA"
                    try:
                        model= model_temp[j].text
                    except Exception as e:
                        model = "NA"
                    try:
                        formattedprice = formatprice_temp[j].text
                    except Exception as e:
                        formattedprice = "NA"
                    dict_product=dict_product.append({'MAIN_MODEL':df.Insured_Device_Model[k],'ASIN':asin, 'TITLE':title, 'AMOUNT (Cents)':amount, 'BRAND':brand, 'MODEL':model, 'FORMATTED_PRICE':formattedprice}, ignore_index=True)
                    
                except Exception as e:
                    print(e)
                
                
        time.sleep(2)
            
dict_product.to_csv('C:\\Users\\Megha115452\\Desktop\\Untitled Folder\\Mobile_handesets_new5.csv',index=False,encoding='utf-8')

