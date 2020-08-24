import csv

import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data/sitka_weather_2018_simple.csv'
filename = 'data/death_valley_2018_simple.csv'
place_name = ''


#Open sitka data
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)


	date_index = header_row.index('DATE')
	high_index = header_row.index('TMAX')
	low_index = header_row.index('TMIN')
	name_index = header_row.index('NAME')

	highs, lows, dates = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
		try:
			high = int(row[high_index])
			low = int(row[low_index])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)




plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs,  c='blue', alpha=0.5)
ax.plot(dates, lows,  c='red', alpha=0.5)
#ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


ax.set_title("Daily temp in Sitka and Death Valley in 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Tempurature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()