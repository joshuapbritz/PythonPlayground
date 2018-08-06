from json import loads

with open('data.json', mode="r") as file:
    FILE_RESULT = loads(file.read())

result_file = list(filter(lambda obj: obj > obj['albumId'] == 3, FILE_RESULT))

print(result_file)