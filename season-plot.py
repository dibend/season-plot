import csv
import sys
import matplotlib.pyplot as plt

years = {}

with open(sys.argv[1], 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        original_close = float(row[5])
        break
    for row in reader:
        year = int(row[0][:4])
        close = float(row[5])
        if year in years:
            years[year].append(close/original_close)
        else:
            years[year] = [1]
            original_close = float(row[5])
for year in years:
    plt.plot(years[year], label=year)
plt.legend()
plt.show()
