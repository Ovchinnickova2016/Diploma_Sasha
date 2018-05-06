import json

def checkAnswer2(num):
    num = json.loads(num)
    print(type(num))
    num = num["num"]
    num = str(num)
    if num == "760":
        jsonData = json.dumps({"answer":"True"}) #ответ клиенту правльный ответ или нет 
        fh = open('data1.json', 'w')#записали ответ в data1.json
        fh.write(jsonData)
        fh.close()
    else:
        jsonData = json.dumps({"answer":"False"}) #ответ клиенту правльный ответ или нет 
        fh = open('data1.json', 'w')#записали ответ в data1.json
        fh.write(jsonData)
        fh.close()