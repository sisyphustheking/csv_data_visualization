import csv

import matplotlib.pyplot as plt
from datetime import datetime


sitka = 'data/sitka_weather_2018_simple.csv'
death = 'data/death_valley_2018_simple.csv'


#Open sitka data
with open(sitka) as s:
	reader = csv.reader(s)
	header_row = next(reader)
	print(header_row)

	for index, column_header in enumerate(header_row):
		print(index, column_header)

	sitka_rainfalls, sitka_dates = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			sitka_rainfall = float(row[3])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			sitka_dates.append(current_date)
			sitka_rainfalls.append(sitka_rainfall)

#Open death valley data
with open(death) as d:
	reader = csv.reader(d)
	header_row = next(reader)
	print(header_row)

	for index, column_header in enumerate(header_row):
		print(index, column_header)

	death_rainfalls, death_dates = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			death_rainfall = float(row[3])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			death_dates.append(current_date)
			death_rainfalls.append(death_rainfall)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(sitka_dates, sitka_rainfalls, c='blue', alpha=0.5)
ax.plot(death_dates, death_rainfalls, c='red', alpha=0.5)
#ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


ax.set_title("Daily rainfall in Sitka and Death Valley in 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall (metres)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()