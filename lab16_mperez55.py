from pathlib import Path
import csv
from datetime import datetime

from matplotlib import pyplot as plt

path = Path("OHUR.csv")
lines = path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)
header = next(reader)

dates, rates = [], []
for row in reader:
    current_date = datetime.strptime(row[0], "%Y-%m-%d")
    current_rate = float(row[1])
    dates.append(current_date)
    rates.append(current_rate)


plt.style.use("seaborn-v0_8-pastel")
fig,ax = plt.subplots()
ax.plot(dates, rates)
ax.set_title("Ohio's Unemployment by Month(1976-2022)")
ax.set_xlabel("Date")
ax.set_ylabel("Unemp Rate")

plt.savefig("OHUR.png")
plt.show()