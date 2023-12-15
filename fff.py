phone_number = int(input())

area_code = phone_number % 10000000
print(area_code)
prefix = phone_number // 10000000
line_number = prefix % 1000
new_phone_number = prefix //  1000
result = f"({new_phone_number}) {line_number} - {area_code}"
print(result)