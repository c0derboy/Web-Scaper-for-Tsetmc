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
final_text = f"{weekdays[weekday]}, {day} of {months[month - 1]}:\tHigh: {hf[0]:,}\tLow: {hf[1]:,}\tLast: {rf:,}\t Range: {rng:,.2f}\t Fluctuation: {movement:.2f}%\n"
print(final_text)

#Write the data into a txt file
data = open('stockdata.txt', 'a+')
data.write(final_text)
data.close()

"""
1.Automate for every X Hours
2. Increase the number of pages + variables
"""