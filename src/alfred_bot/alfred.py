import telebot


        
class Alfred:
    def __init__(self, username, token = None):
        self.bordcast_users = dict()
        self.TOKEN = "YOUR_BOT_TOKEN" 
        self.bot = telebot.TeleBot(self.TOKEN)
        #self.user = get_chat_id(username)
        self.user = username

        if token is None:
            raise ValueError("Bot Token is required")
        else:
            self.TOKEN = token

    def add_user(self, name, chat_id):
        self.bordcast_users[name] = self.bot.get_chat(chat_id).id

    def remove_user(self, name):
        self.bordcast_users.pop(name)

    def send_message(self, message = "poho", broadcast = False):
        if broadcast:
            for br_user in self.bordcast_users.values():
                self.bot.send_message(br_user, message)
        else:
            self.bot.send_message(self.user, message)

    def send_photo(self, photo_path, broadcast = False):
        if broadcast:
            for br_user in self.bordcast_users.values():
                self.bot.send_photo(br_user, photo = open(photo_path, 'rb'))
        else:
            self.bot.send_photo(self.user, photo = open(photo_path, 'rb'))

    def send_file(self, file_path, broadcast = False):
        if broadcast:
            for br_user in self.bordcast_users.values():
                self.bot.send_document(br_user, document = open(file_path, 'rb'))
        else:
            self.bot.send_document(self.user, document = open(file_path, 'rb'))
    
