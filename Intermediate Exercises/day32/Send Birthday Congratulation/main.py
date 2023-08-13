#------------------------------------------------ SEND Happy Birth day --------------------------------------------
import pandas as pd
import smtplib
import datetime

USERNAME= 'hoseinjamshidian1998@gmail.com'
PASSWORD= "specific password"

individuals= pd.read_csv('birthdays.csv')

NOW=datetime.datetime.now()
MONTH= NOW.month
DAY= NOW.day

#---------------------------------------------- Conditions -----------------------------------------------

for k,v in individuals.iterrows():
    if (v['month']==MONTH) & (v['day']==DAY):
        with open('../006 birthday-wisher-extrahard-start/letter_templates/letter_1.txt') as file:
            let= file.read()
            letter=let.replace('[NAME]',v['name']).replace('Angela','Hosein Jamshidian')

#---------------------------------------------- Send Mail With SMTP Class -------------------------------------

            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=USERNAME, password=PASSWORD)
                connection.sendmail(from_addr=USERNAME,
                                    to_addrs=USERNAME,
                                    msg=f"subject:Happy Birth Day To you\n\n{letter};-)")