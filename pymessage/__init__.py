import smtplib
import logging
import os
from dotenv import load_dotenv

load_dotenv()
DEFAULT_PHONE_NUMBER = os.getenv('DEFAULT_PHONE_NUMBER')
DEFAULT_EMAIL = os.getenv('DEFAULT_EMAIL')
DEFAULT_EMAIL_PASSWORD = os.getenv('DEFAULT_EMAIL_PASSWORD')

logging.basicConfig(level=logging.INFO)
logging.warning('Not sure if this method with stop working after May 30th, 2022')

credientials = (DEFAULT_EMAIL, DEFAULT_EMAIL_PASSWORD)


carriers = {'att': '@mms.att.net',
            'tmobile': '@tmomail.net',
            'verizon': '@vtext.com',
            }

def send(message: str, to: str=DEFAULT_PHONE_NUMBER, carrier: str='att') -> dict:
    recipient = f'{to}{carriers[carrier]}'
    logging.info(recipient)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(credientials[0], credientials[1])

    server.sendmail(credientials[0], recipient, message)
    return {'status': 200}