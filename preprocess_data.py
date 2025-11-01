import csv
from collections import defaultdict

# Read the data
with open('socialMedia.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Part 2.2: Create socialMediaAvg.csv (Platform, PostType, AvgLikes)
platform_posttype = defaultdict(list)
for row in data:
    key = (row['Platform'], row['PostType'])
    platform_posttype[key].append(float(row['Likes']))

avg_data = []
for (platform, posttype), likes_list in platform_posttype.items():
    avg_likes = sum(likes_list) / len(likes_list)
    avg_data.append({
        'Platform': platform,
        'PostType': posttype,
        'AvgLikes': round(avg_likes, 2)
    })

# Sort by Platform then PostType
avg_data.sort(key=lambda x: (x['Platform'], x['PostType']))

with open('socialMediaAvg.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Platform', 'PostType', 'AvgLikes'])
    writer.writeheader()
    writer.writerows(avg_data)

print('Created socialMediaAvg.csv')
for row in avg_data[:10]:
    print(row)

# Part 2.3: Create socialMediaTime.csv (Date, AvgLikes)
date_likes = defaultdict(list)
for row in data:
    date = row['Date']
    date_likes[date].append(float(row['Likes']))

time_data = []
for date, likes_list in sorted(date_likes.items()):
    avg_likes = sum(likes_list) / len(likes_list)
    time_data.append({
        'Date': date,
        'AvgLikes': round(avg_likes, 2)
    })

with open('socialMediaTime.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Date', 'AvgLikes'])
    writer.writeheader()
    writer.writerows(time_data)

print('\nCreated socialMediaTime.csv')
for row in time_data[:10]:
    print(row)

