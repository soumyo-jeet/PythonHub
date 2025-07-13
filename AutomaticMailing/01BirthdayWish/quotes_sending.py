import smtplib
import datetime as dt
import random

with open ("32_DAY/quotes.txt") as qm:
    quote = qm.readlines()

quote_list = [q.strip() for q in quote]

now= dt.datetime.now()
today = now.weekday()
hour = now.hour


my_email = "soumyo460@gmail.com"
password = "************"

motivation = random.choice(quote_list)
print(motivation)

if today == 5 and hour == 20:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(from_addr= my_email, to_addrs="samajdarsoumyajeet0@gmail.com", msg=f"subject : Motivation!!\n\n {motivation}")
    print("Sent")