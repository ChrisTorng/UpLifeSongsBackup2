import json
from collections import defaultdict

# 讀取 JSON 文件
with open('songsList.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 建立字典來存儲 name 和 youtubeId 的對應，以及其所屬的 subTitle
name_to_ids = defaultdict(lambda: defaultdict(set))
id_to_names = defaultdict(lambda: defaultdict(set))

# 遍歷 JSON 資料，收集 name 和 youtubeId 的對應以及所屬的 subTitle
for group in data['groups']:
    sub_title = group['subTitle']
    for song in group['songs']:
        name = song['name']
        youtube_id = song['youtubeId']
        
        name_to_ids[name][youtube_id].add(sub_title)
        id_to_names[youtube_id][name].add(sub_title)

# 找出 name 相同但 youtubeId 不同的項目
print("Name 相同但 youtubeId 不同的項目:")
for name, ids in name_to_ids.items():
    if len(ids) > 1:
        print(f"\n{name}:")
        for youtube_id, sub_titles in ids.items():
            print(f"  YouTube ID: {youtube_id}, SubTitles: {', '.join(sub_titles)}")

# 找出 youtubeId 相同但 name 不同的項目
print("\nYoutubeId 相同但 name 不同的項目:")
for youtube_id, names in id_to_names.items():
    if len(names) > 1:
        print(f"\nYouTube ID: {youtube_id}")
        for name, sub_titles in names.items():
            print(f"  Name: {name}, SubTitles: {', '.join(sub_titles)}")

# 找出 name/youtubeId 相同，但位於多個 subTitle 內的項目
print("\nName/YoutubeId 相同，但位於多個 subTitle 內的項目:")
for name, ids in name_to_ids.items():
    for youtube_id, sub_titles in ids.items():
        if len(sub_titles) > 1:
            print(f"\nName: {name}, YouTube ID: {youtube_id}, SubTitles: {', '.join(sub_titles)}")
