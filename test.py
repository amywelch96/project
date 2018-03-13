def save_email(email_address):
    with open('emails_file.txt', 'a') as file_handle:
        file_handle.write(email_address + '\n')


email=raw_input('enter your email address')
save_email(email)