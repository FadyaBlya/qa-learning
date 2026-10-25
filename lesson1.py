# Проверка ответа сервера.
# Требования: статус код = 200, время ответа строго меньше 1 секунды.
# Тест PASSED, только если выполнены оба условия.

EXPECTED_STATUS = 200
RESPONSE_TIME_LIMIT = 1

actual_status = 200
response_time = 0.5

has_errors = False

if actual_status != EXPECTED_STATUS:
    print(f"Status: FAILED. Неверный статус код - ожидали {EXPECTED_STATUS}, получили {actual_status}")
    has_errors = True

if response_time >= RESPONSE_TIME_LIMIT:
    print(f"Status: FAILED. Время ответа - ожидали < {RESPONSE_TIME_LIMIT} сек, получили - {response_time} сек")
    has_errors = True

if not has_errors:
    print("Status: PASSED")