phone = 8058791234
line_number = phone % 10000
rest = phone // 10000
prefix = rest % 1000
area_code = rest // 1000
result = f"({area_code}) {prefix}-{line_number}"
print(result)
