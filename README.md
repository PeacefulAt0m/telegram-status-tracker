# Description

Userbot, which logs changes in online status of specified Telegram users.

## Installation

```bash
git clone https://github.com/peacefulat0m/telegram-status-tracker.git
cd telegram-status-tracker/
chmod +x ./scripts/install.sh
./scripts/install.sh
```

## Configuration

In "Privacy and Security" setting in Telegram you should enable "Last Seen & Online" setting for everyone. In addition, the person you are tracking must also have this setting enabled

You should specify such settings in config.env file:

1. TELEGRAM_SESSION_NAME
   Name of session file, where telethon saves credentials for accessing telegram api with your account

2. TELEGRAM_API_ID
   Id, which should be taken in Telegram "Api development tools". Learn more in [Telethon docs](https://docs.telethon.dev/en/stable/basic/signing-in.html) or in [Telegram docs](https://core.telegram.org/api/obtaining_api_id)

3. TELEGRAM_API_HASH
   Hash, which should be taken in Telegram "Api development tools". Learn more in [Telethon docs](https://docs.telethon.dev/en/stable/basic/signing-in.html) or in [Telegram docs](https://core.telegram.org/api/obtaining_api_id)

4. LOGGING_FILE_PATH
   Path to file where logs will be saved.

   Note: all directories in this path must exist, but the file may not exist

5. LOGGING_FILE_MAXBYTES
   How many bytes of logs will the file contain before rotating

6. LOGGING_BACKUPCOUNT
   Maximum number of log files. When max number is reached, existing files will be overwritten with new logs

7. USERS_IDS
   String with telegram IDs of users separated by space. If no IDs is specified, all dialogs will be tracked.
   Userbot trackes changes in online status of this user and writes this information in log file.

   Note: It's allowed to track users with whom you have contacted (had a dialogue) at least once.

## Running

```bash
./scripts/run.sh
```
