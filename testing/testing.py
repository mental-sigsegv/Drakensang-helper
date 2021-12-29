import json


with open("settings.json", "r+") as jfile:
    data = json.load(jfile)
    data['opacity'] = 1.4
    jfile.seek(0)
    json.dump(data, jfile)
    jfile.truncate()

print(data['opacity'])
