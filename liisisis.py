user_input = input()
numbers = list(map(int, user_input.split()))
negative_numbers = sorted([num for num in numbers if num < 0], reverse=True)
print(' '.join(map(str, negative_numbers)))
