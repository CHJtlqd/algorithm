import json
# 사전 자료형(dict) 데이터 선언

user ={
    "id":"gildong",
    "password":"12345",
    "age":30,
    "hobby":["football","programming"]
}

# 인코딩: 파이썬 변수를 json 객체로 변환(띄어쓰기 네 칸 들여쓰기 적용)
json_data = json.dumps(user, indent=4)
print(json_data)