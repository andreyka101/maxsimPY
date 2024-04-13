import json
# data = open("file_json.json","r")
# file = json.load(data)
# print(file["key"])


# dataRead = open("file_json.json","r").read()
# file = json.loads(dataRead)
# print(file)



# file = open("file_json.json",'w')
# file.write(json.dumps({
#     "key": "qwerty",
#     "key2": 4555,
#     "key3": [1,2,3,4],
#     "444": 454,
#     "55": 999
# }))
# file.close()

# s = json.dumps({
#     "key": "qwerty",
#     "key2": 4555,
#     "key3": [1,2,3,4],
#     "444": 454,
#     "55": 999
# })
# print(s+s)



file = open("file_json.json",'w')
json.dump({
    "key": "qwerty",
    "key2": 4555,
    "key3": [1,2,3,4],
    "444": 454,
    "hi": "rgrg",
    "55": 999
} , file)
file.close()