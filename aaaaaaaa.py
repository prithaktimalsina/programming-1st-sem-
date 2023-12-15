user_input = ""
while user_input.lower() not in ['done', 'd']:
    user_input = input("")
if user_input.lower() not in ['done', 'd']:
        reversed_text = user_input[::-1]
        print(reversed_text)