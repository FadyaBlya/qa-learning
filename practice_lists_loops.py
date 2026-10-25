# Практика: списки, циклы и словари

# 1. Сколько значений времени меньше 1 секунды
times = [0.5, 1.2, 0.8, 2.0]

count = 0

for response_time in times:
    if response_time < 1:
        count += 1
print(f"Значений < 1: {count}")


# 2. Ответы, у которых статус не равен 200
responses = [
    {"status": 200, "time": 0.5},
    {"status": 201, "time": 1},
    {"status": 404, "time": 0.9},
    {"status": 204, "time": 10},
    {"status": 500, "time": 5},
]

for response_item in responses:
    if response_item["status"] != 200:
        print(response_item["status"])
