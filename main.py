import logging
import os
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.events import UserUpdate
from logging.handlers import RotatingFileHandler

# loads env varaibles from file if required environment variable not found
if not os.environ.get('TELEGRAM_API_ID'):
    load_dotenv('./config.env')

client = TelegramClient(
    session=os.environ.get('TELEGRAM_SESSION_NAME', 'StatusTracker'),
    api_id=os.environ['TELEGRAM_API_ID'],
    api_hash=os.environ['TELEGRAM_API_HASH'],
)

logger = logging.getLogger("")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s]:%(levelname)s - %(message)s')

rotate_handler = RotatingFileHandler(
    os.environ.get('LOGGING_FILE_PATH', 'logs.log'),
    maxBytes=int(os.environ.get('LOGGING_FILE_MAXBYTES', 1000 * 100)),
    backupCount=int(os.environ.get('LOGGING_BACKUPCOUNT', 10)),
)
rotate_handler.setFormatter(formatter)
console_output_handler = logging.StreamHandler()
console_output_handler.setFormatter(formatter)

logger.addHandler(rotate_handler)
logger.addHandler(console_output_handler)


@client.on(UserUpdate)
async def handler(event):

    if event.status:
        id = event.user_id

        if str(id) in users_ids or (not users_ids and id != my_id):
            try:
                user = await client.get_entity(id)
            except Exception as e:
                logging.error(e)
            else:
                logging.info('{0} | {1} {2} {3} is {4}'.format(
                    f'id {id}',
                    f'@{user.username} |' if user.username else '',
                    user.first_name,
                    user.last_name or '',
                    'online' if event.online else 'offline',
                ))


async def init():
    global my_id, users_ids

    users_ids = os.environ['USERS_IDS'].split()
    if not users_ids:
        logging.warning(
            'No USERS_IDS where specified, so all online status changes in '
            'your contacts will be logged')

    me = await client.get_me()
    my_id = me.id
    # we need this to get entities by id without ValueError
    return await client.get_dialogs()


if __name__ == "__main__":
    try:
        client.start()
        client.loop.run_until_complete(init())
        client.run_until_disconnected()
    except Exception as e:
        logging.critical(e)
