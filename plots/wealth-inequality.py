import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.ticker import FuncFormatter

from matplotlib import patheffects
import matplotlib as mpl
import csv
import datetime as dt

import matplotlib.patches as mpatches
import matplotlib.dates as mdates

def parse(url):
    with open(url, 'r') as infile:
        reader = csv.DictReader(infile, delimiter=';')

        top1 = []
        top1_year = []
        middle40 = []
        middle40_year = []
        for row in reader:
            print(row)
            v = row['shweal_z_US']
            if v:
                percentile = row['Percentile']
                if percentile == 'p99p100':
                    top1.append(float(v))
                    top1_year.append(int(row['Year']))
                elif percentile == 'p50p90':
                    middle40.append(float(v))
                    middle40_year.append(int(row['Year']))
                else:
                    exit("bad percentile: " + percentile)
            #date.append(dt.datetime.strptime(row['Date'], '%b %Y'))
            #value.append(float(row['Federal debt']))
        return (top1, top1_year, middle40, middle40_year)

# https://wid.world/
(top1, top1_year, middle40, middle40_year) = parse('data/WID_Data_Metadata/WID_Data_29102019-070448.csv')

# It's just for the high level understanding. Plus xkcd style is pretty
plt.xkcd()

mycol = '#343535'

plt.rcParams["font.family"] = "Concourse T4"
plt.rcParams["axes.linewidth"] = 1
plt.rcParams["axes.edgecolor"] = mycol
plt.rcParams["text.color"] = mycol
plt.rcParams["xtick.color"] = mycol
plt.rcParams["ytick.color"] = mycol
plt.rcParams["ytick.minor.width"] = 0

# Removes remaining white lines after xkcdifying the plot.
# Changing the background didn't fix it.
mpl.rcParams['path.effects'] = [patheffects.withStroke(linewidth=0)]

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(1, 1, 1)

def y_fmt(y, pos):
    return ' {:,.0f}%'.format(y*100)
ax.get_yaxis().set_major_formatter(FuncFormatter(y_fmt))
# ax.get_xaxis().set_major_formatter(mdates.DateFormatter('%Y'))

# def y_fmt(y, pos):
    # return '${:,.0f}'.format(int(y/1000000))
# ax.get_yaxis().set_major_formatter(FuncFormatter(y_fmt))
#ax.get_xaxis().set_major_formatter(mdates.DateFormatter('%Y'))
#ax.set_ylabel("Debt in trillions")

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_tick_params(width=2)
ax.yaxis.set_tick_params(width=2)

# ax.set_xticks([dt.date(y, 1, 1) for y in [1970, 1980, 1990, 2000, 2010, 2018]])
#ax.set_yticks((0, 25, 50, 75, 100, 125))
ax.set_ylim(0.2, 0.4)
ax.set_xlim(1962, 2015)
ax.set_xticks((1962, 1970, 1980, 1990, 2000, 2010))
#ax.set_xticks([dt.datetime(y, 01, 01) for y in [1966, 1980, 1990, 2000, 2010, 2019]])
#ax.set_xticks([dt.datetime(y, 01, 01) for y in [1970, 1980, 1990, 2000, 2010, 2019]])
#ax.set_ylim(0, 25000000)
#ax.set_yticks((0, 20, 40, 60, 80, 100))

# #396AB1
# #DA7C30
# #3E9651
# #CC2529
# #535154
# #6B4C9A
# #922428
# #948B3D

# For different y-axis:
# https://stackoverflow.com/questions/9103166/multiple-axis-in-matplotlib-with-different-scales
ax.plot(top1_year, top1, '#6B4C9A', label='Top 1%')
ax.plot(middle40_year, middle40, '#CC2529', label='Middle 40%')

ax.legend(loc='best')

plt.savefig('wealth-inequality.svg', format="svg", transparent=True, bbox_inches='tight')
print "done"

