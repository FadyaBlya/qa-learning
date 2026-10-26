# Урок 2: проверка списка ответов сервера.
# Требования к каждому ответу: статус код строго равен 200, время ответа строго меньше 1 секунды.
# Ответ PASSED, только если выполнены оба условия.
# В конце выводится итог: сколько ответов прошло и сколько упало.

EXPECTED_STATUS = 200
RESPONSE_TIME_LIMIT = 1

responses = [
    {"status_code": 200, "response_time": 0.5},
    {"status_code": 200, "response_time": 1},
    {"status_code": 404, "response_time": 0.9},
    {"status_code": 204, "response_time": 3},
    {"status_code": 500, "response_time": 10},
    {"status_code": 200, "response_time": 0.2},
]

# Считаем ответы, а не ошибки: у одного ответа их может быть две
passed_count = 0
failed_count = 0

for response_item in responses:
    print(f"Проверяем: {response_item}")
    has_errors = False # сбрасываем для каждого ответа, чтобы результаты не влияли друг на друга

    if response_item["status_code"] != EXPECTED_STATUS:
        print(f"Status: FAILED. Неверный статус код - ожидали {EXPECTED_STATUS}, получили {response_item['status_code']}")
        has_errors = True

    if response_item["response_time"] >= RESPONSE_TIME_LIMIT:
        print(f"Status: FAILED. Время ответа - ожидали < {RESPONSE_TIME_LIMIT} сек, получили - {response_item['response_time']} сек")
        has_errors = True

    # Счётчик меняем один раз на ответ, после обеих проверок
    if has_errors:
       failed_count += 1

    else:
        print(f"Status: PASSED. Статус код - {response_item['status_code']}, время ответа - {response_item['response_time']}")
        passed_count += 1

# Контроль: passed_count + failed_count должно равняться len(responses)
print(f"Успех - {passed_count}. Упало - {failed_count}")