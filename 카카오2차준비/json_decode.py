import json

# 사전 자료형(dict) 데이터 선언
user ={
    "id":"gildong",
    "password":"12345",
    "age":30,
    "hobby":["football","programming"]
}

# 인코딩: 파이썬 변수를 JSON 객체로 변환
json_data = json.dumps(user)

# 디코딩: JSON 객체를 파이썬 변수로 변환
data = json.loads(json_data)
print(data)