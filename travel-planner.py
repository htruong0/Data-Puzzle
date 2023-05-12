import pandas as pd
from geopy.distance import distance
from itertools import combinations

capitals_df = pd.read_csv('https://raw.githubusercontent.com/hyperc54/data-puzzles-assets/master/features/travel/worldcapitals_light.csv')

# Kingston is a capital in two countries so give them a number each
mask = capitals_df["city"].duplicated(keep=False)
capitals_df.loc[mask, "city"] += capitals_df.groupby("city").cumcount().add(1).astype(str)

capitals_df["pos"] = capitals_df.apply(lambda x: [x["lat"], x["lng"]], axis=1)
pairs = list(combinations(capitals_df["city"], 2))

# pair-wise distance
distance_dict = {}
for pair in pairs:
    d = distance(
        capitals_df[capitals_df["city"] == pair[0]]["pos"],
        capitals_df[capitals_df["city"] == pair[1]]["pos"]
    )
    distance_dict["-".join(pair)] = d

max_dist_pair = max(distance_dict, key=distance_dict.get)
max_dist = distance_dict[max_dist_pair]
print(f"Max distance pair is {max_dist_pair} at a distance of {max_dist}.")

# Pair with lowest distance is in the same place
# sort and pick second instead
sorted_dist = sorted(distance_dict, key=distance_dict.get)
min_dist_pair = sorted_dist[1]
min_dist = distance_dict[min_dist_pair]
print(f"Min distance pair is {min_dist_pair} at a distance of {min_dist}.")
