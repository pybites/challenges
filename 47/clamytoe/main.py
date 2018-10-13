# coding: utf-8
"""
Pybites Community Branch Activity

First of all, I start off with importing everything that I will need.
"""
import json
from collections import Counter

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from dateutil.parser import parse
from matplotlib import rc
from matplotlib.pyplot import figure

# load data
page = "data/events{}.json"
events = []
for p in range(1, 4):
    with open(page.format(p)) as file:
        events.extend(json.loads(file.read()))


# helper function
def parse_data(line):
    if "[" in line:
        data = line.split(": [")[1].replace("]", "").strip()
    else:
        data = line.split(": ")[1].strip()
    return data


# parse data
created = []
devs = []
diff_levels = []
time_spent = []

for event in events:
    if event["type"] == "PullRequestEvent":
        # developer username
        dev = event["actor"]["login"]

        # ignore pybites ;)
        if dev != "pybites":
            # store developer username
            devs.append(dev)
            # store the date
            created.append(event["created_at"].split("T")[0])
            # parse comment from user for data
            comment = event["payload"]["pull_request"]["body"]
            for line in comment.split("\n"):
                # get difficulty level and time spent
                if "Difficulty level (1-10):" in line:
                    diff = parse_data(line)
                elif "Estimated time spent (hours):" in line:
                    spent = parse_data(line)
            # pandas DataFrames require that all columns are the same length
            # so if we have a missing value, enter None in its place
            if diff:
                diff_levels.append(int(diff))
            else:
                diff_levels.append(None)
            if spent:
                time_spent.append(int(spent))
            else:
                time_spent.append(None)


# create the DataFrame
df = pd.DataFrame(
    {
        "Developers": devs,
        "Difficulty_Levels": diff_levels,
        "Time_Spent": time_spent,
        "Date": created,
    }
)
print(df.describe())

# just exploring the data
print(f'\nDevelopers: {len(df["Developers"])}')
print(f'Average Difficulty: {df["Difficulty_Levels"].median()}')
print(f'Time Spent: {df["Time_Spent"].sum()}')

# developer counter
developers = Counter(df["Developers"]).most_common(6)
print(f"\nDevelopers: \n{developers}")

# difficulty counter
bite_difficulty = Counter(df["Difficulty_Levels"].dropna()).most_common()
print(f"\nDifficulty: \n{bite_difficulty}")

# duration counter
bite_duration = Counter(df["Time_Spent"].dropna()).most_common()
print(f"\nDuration: \n{bite_duration}")

# date counter
created_at = sorted(Counter(df["Date"].dropna()).most_common())
print(f"\nDates: \n{created_at}")

# Number of Pull Request per Day
# resize graph
figure(num=None, figsize=(6, 6), dpi=80, facecolor="w", edgecolor="k")

# gather data into a custom DataFrame
dates = [day[0] for day in created_at]
prs = [pr[1] for pr in created_at]
df_prs = pd.DataFrame({"xvalues": dates, "yvalues": prs})

# plot
plt.plot("xvalues", "yvalues", data=df_prs)

# labels
plt.xticks(rotation="vertical", fontweight="bold")

# title
plt.title("Number of Pull Request per Day")

# show the graphic
plt.show()

# Top Blog Challenge Ninjas
# resize graph
figure(num=None, figsize=(6, 6), dpi=80, facecolor="w", edgecolor="k")

# create labels
labels = [dev[0] for dev in developers]

# get a count of the pull requests
prs = [dev[1] for dev in developers]

# pull out top ninja slice
explode = [0] * len(developers)
explode[0] = 0.1

# create the pie chart
plt.pie(prs, explode=explode, labels=labels, shadow=True, startangle=90)

# add title and center
plt.axis("equal")
plt.title("Top Blog Challenge Ninjas")

# show the graphic
plt.show()

# Time Spent/Difficulty Level per Pull Request
# resize graph
figure(num=None, figsize=(15, 6), dpi=80, facecolor="w", edgecolor="k")

# drop null values
df_clean = df.dropna()

# add legend
diff = mpatches.Patch(color="#557f2d", label="Difficulty Level")
time = mpatches.Patch(color="#2d7f5e", label="Time Spent")
plt.legend(handles=[time, diff])

# y-axis in bold
rc("font", weight="bold")

# values of each group
bars1 = df_clean["Difficulty_Levels"]
bars2 = df_clean["Time_Spent"]

# heights of bars1 + bars2
bars = df_clean["Difficulty_Levels"] + df_clean["Time_Spent"]

# position of the bars on the x-axis
r = range(len(df_clean))

# names of group and bar width
names = df_clean["Developers"]
barWidth = 1

# create green bars (bottom)
plt.bar(r, bars1, color="#557f2d", edgecolor="white", width=barWidth)
# create green bars (top), on top of the firs ones
plt.bar(r, bars2, bottom=bars1, color="#2d7f5e", edgecolor="white", width=barWidth)

# custom X axis
plt.xticks(r, names, rotation="vertical", fontweight="bold")
plt.xlabel("Developers", fontweight="bold")

# title
plt.title("Time Spent/Difficulty Level per Pull Request")

# show graphic
plt.show()
