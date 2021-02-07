import pandas as pd
from matplotlib import pyplot as plt

# TODO
# Use matplotlib to build line plots of the 10 most awarded countries for time span 1896-2012.
# Use the 10 most popular summer Olympics disciplines where most popular you can define yourself.

# DONE
# Create a barplot which shows the total medals won for each sport during the summer Olympics.


def get_most_medals(data):
    grouped_data = data.groupby(['Gender', 'Athlete'])["Medal"].count().reset_index(name='count')
    men_category = grouped_data[grouped_data["Gender"] == "Men"].sort_values("count", ascending=False).head(1)
    print(men_category["Athlete"])
    women_category = grouped_data[grouped_data["Gender"] == "Women"].sort_values("count", ascending=False).head(1)
    print(women_category["Athlete"])


def get_top_countries(olympics_data):
    country_data = olympics_data.groupby(['Gender', 'Country'])['Medal'].count().reset_index(name='count')
    men_top10_countries = country_data[country_data["Gender"] == "Men"].sort_values("count", ascending=False).head(10)
    print(men_top10_countries)
    female_top10_countries = country_data[country_data["Gender"] == "Women"].sort_values("count", ascending=False).head(10)
    print(female_top10_countries)


def plot_total_medals_per_sport(medals_data):
    medal_count = medals_data.groupby(['Sport'])['Medal'].count().reset_index(name='count')
    sport = medal_count["Sport"].tolist()
    medals = medal_count["count"].tolist()
    plt.bar(sport, medals)
    plt.show()


if __name__ == '__main__':
    olympic_data = pd.read_csv('summer.csv')
    get_most_medals(olympic_data)
    get_top_countries(olympic_data)
    plot_total_medals_per_sport(olympic_data)
