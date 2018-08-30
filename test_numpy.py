import json

list1 = []
with open("C:/Users/Rutuja/PycharmProjects/asapp/sample_conversations.json", encoding="utf8") as f:
    data = json.load(f)
    for jsondata in data["Issues"]:
        for i in jsondata["Messages"]:
            r = i["Text"]
            list1.append(r)

with open("C:/Users/Rutuja/PycharmProjects/asapp/processed.txt", 'w') as g:
    g.write(str(list1))

st = input("enter string")
flag = False
list2 = []
for k in list1:
    if k.find(st) == 0:
        list2.append(k)

json123 = json.dumps(list2)
print(json123)

