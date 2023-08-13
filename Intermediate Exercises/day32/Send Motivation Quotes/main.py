#------------------------------------------ SEND MOTIVATION QUOTES -------------------------------------------
import random
import smtplib
import datetime as dt

USERNAME= 'hoseinjamshidian1998@gmail.com'
PASSWORD= "specific password"

with open('../quotes.txt') as file:
    quotes= file.readlines()

# ------------------------------------------- Choose Random Quote ------------------------------------------
chosen=random.choice(quotes)
AUTHOR= chosen.split(' - ')[1]
TEXT= chosen.split(' - ')[0]

TIME= dt.datetime.now().weekday()

#------------------------------------------ Connection To mail with smtplib ---------------------------------
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=USERNAME, password=PASSWORD)

    if TIME==5:
        connection.sendmail(from_addr=USERNAME,
                        to_addrs=USERNAME,
                        msg=f'subject:{AUTHOR} says\n\n{TEXT[1:-2]}')
    else:
        print('not yet!')