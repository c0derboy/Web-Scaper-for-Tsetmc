#Get Data from web page
import requests
from bs4 import BeautifulSoup
from datetime import datetime

#Get the data
link = 'http://www.tsetmc.com/Loader.aspx?ParTree=15131J&i=32097828799138957'
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')


#Time
time = datetime.now()
weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday', 'Sunday')
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
weekday = time.weekday()
day = time.day
month = time.month

#Finding the data Last Time
rf = soup.find_all(class_='box1')
hf = rf[2]
rf = rf[1]
rf = rf.find_all('td')[1]
rf = str(rf)
rf = rf[4:-5]
rf = rf.replace(',', '')
rf = float(rf)


#Finding Low High End Daily
hf = hf.find_all('td')
hf = [hf[1], hf[3]]
hf = [str(i) for i in hf]
hf = [i[4:-5] for i in hf]
hf = [float(i) for i in hf]
rng = hf[0] - hf[1]
movement = rng / rf * 100
final_text = f"{weekdays[weekday]}, {day} of {months[month - 1]}:\tHigh: {hf[0]:,}\tLow: {hf[1]:,}\tLast: {rf:,}\t Range: {rng:,.2f}\t Fluctuation: {movement:.2f}%"
print(f"High: {hf[0]:,}\tLow: {hf[1]:,}\tLast: {rf:,}\t Range: {rng:,.2f}\t Fluctuation: {movement:.2f}%")

#Calculate the trend
past_data = soup.find_all(class_='table1')
past_data = past_data[1]
past_data = past_data.find_all('td')[-3]
past_data = str(past_data)
past_data = past_data[4:-5]
past_data = past_data.replace(',', '')
past_data = float(past_data)

trend10days = rf - past_data
trendfluc = trend10days / rf * 100

trend_text = f'In the past 10 days the market has moved by {round(trend10days /1000 ) * 1000} which is {trendfluc:.2f}%'
print(trend_text)

#Write the data into a txt file
data = open('stockdata.txt', 'a+')
data.write(f'{final_text}\n')
data.write(f'{final_text}\n\n')
data.close()

"""
Features to work on:
1.Automate for every X Hours
2. Increase the number of pages + variables
3. Calculate the trend in 2 weeks
"""