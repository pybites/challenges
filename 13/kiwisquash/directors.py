import collections, csv

with open('../movie_metadata.csv',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    readerList = list(reader)

keyListAll = list(readerList[0].keys())
for i in range(len(keyListAll)):
    print(i, keyListAll[i])

# Actual key names
# 0 color
# 1 director_name # We want this
# 2 num_critic_for_reviews
# 3 duration
# 4 director_facebook_likes
# 5 actor_3_facebook_likes
# 6 actor_2_name
# 7 actor_1_facebook_likes
# 8 gross
# 9 genres
# 10 actor_1_name
# 11 movie_title # We want this
# 12 num_voted_users
# 13 cast_total_facebook_likes
# 14 actor_3_name
# 15 facenumber_in_poster
# 16 plot_keywords
# 17 movie_imdb_link
# 18 num_user_for_reviews
# 19 language
# 20 country
# 21 content_rating
# 22 budget
# 23 title_year # We want this
# 24 actor_2_facebook_likes
# 25 imdb_score # We want this
# 26 aspect_ratio
# 27 movie_facebook_likes        

# Desired indices: 1, 11, 23, 25
indexVector = [1,11,23,25]
keyVector = []
for index in indexVector:
    keyVector.append(keyListAll[index])
movieInfos = collections.namedtuple("movieInfos",f"{keyVector[0]},{keyVector[1]},{keyVector[2]},{keyVector[3]}")



