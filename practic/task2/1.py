#task 2
from re import match

def check_email(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{1,}$'
    return bool(match(pattern, email))

# Примеры корректных и некорректных адресов
test_emails = ["a@b.c", "a-b@c.d.e", "a-b_c.d@e_f-g.h", "a+@b.c", "a_b.c", "a_b@.c-d", "rwDS123.-_@gm.ru"]


for email in test_emails:
    if check_email(email):
        print(f"{email} - Верно")
    else:
        print(f"{email} - Неверно")
