import csv

import matplotlib.pyplot as plt
from datetime import datetime


sitka = 'data/sitka_weather_2018_simple.csv'
death = 'data/death_valley_2018_simple.csv'


#Open sitka data
with open(sitka) as s:
	reader = csv.reader(s)
	header_row = next(reader)

	sitka_highs, sitka_lows, sitka_dates = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			sitka_high = int(row[5])
			sitka_low = int(row[6])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			sitka_dates.append(current_date)
			sitka_highs.append(sitka_high)
			sitka_lows.append(sitka_low)


#Open death valley data
with open(death) as d:
	reader = csv.reader(d)
	header_row = next(reader)

	death_highs, death_lows, death_dates = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			death_high = int(row[5])
			death_low = int(row[6])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			death_dates.append(current_date)
			death_highs.append(death_high)
			death_lows.append(death_low)




plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(sitka_dates, sitka_highs,  c='blue', alpha=0.5)
ax.plot(death_dates, death_highs,  c='red', alpha=0.5)
#ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


ax.set_title("Daily temp in Sitka and Death Valley in 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Tempurature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()