with open('Mail Merge Project Start/Input/Letters/starting_letter.txt') as file:
    letter= file.read()
# TODO: read letter

with open('Mail Merge Project Start/Input/Names/invited_names.txt') as file:
    names=file.read().split()

# TODO: list of names

for name in names:
    mail=letter.replace('[name]', name)
    with open(f'Mail Merge Project Start/Output/ready_mails/invitation_{name}.txt',mode='w') as file:
        file.write(f'{mail}')
# TODO: Make mails ready.