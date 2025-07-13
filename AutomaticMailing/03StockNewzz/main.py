import requests
from twilio.rest import Client
import os
from dotenv import load_env
load_env()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
acc_sid = os.getenv('TWILIO_ACCOUNT_SID')
acc_sid = ""
acc_token = ""

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "apikey" : "***************",
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
}

stock_response= requests.get(url=STOCK_ENDPOINT, params= stock_params)
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key , value) in stock_data.items()]
print(stock_data_list[0]["4. close"])
print(stock_data_list[1]["4. close"])


diff = float(stock_data_list[0]["4. close"]) - float(stock_data_list[1]["4. close"])
percentage_diff = diff / float(stock_data_list[0]["4. close"]) * 100

print(percentage_diff)




if percentage_diff > 0 or percentage_diff < 0 :
    
    news_params = {
        "apiKey" :"****************",
        "q" : STOCK
    }

    news_response = requests.get(url= NEWS_ENDPOINT, params= news_params)
    data = news_response.json()
    articles = data["articles"][:3]

    msgs_list = [f"Headline: {each['title']}\nBrief: {each['description']}" for each in articles]

    for i in range(len(msgs_list)) :
        client = Client(acc_sid, acc_token)
        if percentage_diff >= 0 :
            msg = client.messages.create(body=f"TSLA: 🔺{int(percentage_diff)}%\n{msgs_list[i]}", from_="+19046010428", to="+918910048803")
            print(msg.status)
        else :
            msg = client.messages.create(body=f"TSLA: 🔻{int(percentage_diff)}%\n{msgs_list[i]}", from_="+19046010428", to="+918910048803")
            print(msg.status)








## STEP 1: Use https://newsapi.org/docs/endpoints/everything

# 





# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

