import  re

email = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')
def email_parse(email):
    found_email = EMAIL.findall(email)[0]
    if found_email:
        name, addr = found_email
    else:
        raise ValueError(f'wrong email: {email}')
    return name, addr

print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))

1