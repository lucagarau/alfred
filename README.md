# alfred
Alfred is a python library that allows you to send messages or files via telegram directly from your pyhton code
## install

```bash
git clone https://github.com/lucagarau/alfred
pip install alfred-bot.tar.gz
```

## get start
To start receiving messages from Alfred, create a telegram bot and get the bot token.

Create a bot.py file to start sending messages.


```python
  from alfred_bot import Alfred

  chat_id = 123445667
  token = "Your Bot Token"
  bot = Alfred(chat_id,token)
  bot.send_message("poho")
  
```

## Send file or photo
To send files or photos use the bot's dedicated methods
```python
  from alfred_bot import Alfred

  photo_path = "/home/photo.png"
  file_path = "/home/document.txt"

  chat_id = 123445667
  token = "Your Bot Token"

  bot = Alfred(chat_id,token)
  bot.send_photo(photo_path)
  bor.send_file(file_path)
```

## Send broadcast
To send messages, files or photos to multiple users at the same time, you must first add the users to the recipient list and then call the broadcast methods
```python
  from alfred_bot import Alfred

 
  chat_id_broadcast_1 = 1244614141
  chat_id_broadcast_2 = 1231412412

  chat_id = 123445667
  token = "Your Bot Token"
  bot = Alfred(chat_id,token)


  alfred.add_user("Nolan", chat_id_broadcast_1)
  alfred.add_user("Chazelle", chat_id_broadcast_2)

  bot.send_message("poho", broadcast = True)
 
```
