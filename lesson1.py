# Проверка ответа сервера.
# Требования: статус код = 200, время ответа строго меньше 1 секунды.
# Тест PASSED, только если выполнены оба условия.

expected_status = 200
actual_status = 200
response_time = 0.5

has_errors = False

if expected_status != actual_status:
    print(f"Status: FAILED. Неверный статус код - ожидали {expected_status}, получили {actual_status}")
    has_errors = True

if response_time >= 1:
    print(f"Status: FAILED. Время ответа - ожидали < 1 сек, получили - {response_time} сек")
    has_errors = True

if not has_errors:
    print("Status: PASSED")