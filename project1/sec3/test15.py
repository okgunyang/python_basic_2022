# dict : 키와 값을 동시에 저장하려고 할 경우 활용 = Dictionary
dct1 = {"name":"kim", "age":40, "height":173.8, "weight":78.4}
print(dct1)
print(dct1["name"])     # 특정 원소 읽기 - 변수명["키명"]
dct1["name"] = "lee"    # 특정 원소의 값 변경
print(dct1)
# del dict1["weight"]   # 원소 제거
# dct1.clear()          # 모든 원소 제거
for key in dct1:
    print(key, " : ", dct1[key])
# 열거형 = 이더레이터 = 컬렉션
# list=목록[], tuple=불변데이터(), set=모음 또는 집합{}, dict=사전{}
dct2 = {"지은":100,"병수":90,"송윤":100,"태헌":70}
print(dct2)
# list -> set, tuple, set -> list, tuple, tuple -> list, set
# list의 tuple 이중 구조로서 순서쌍으로만 구성되어 있어야 함
lst0 = [("이해나", 80),("김태엽", 90),("김기태", 100)]
print(lst0)
dct3=dict(lst0)
print(dct3)