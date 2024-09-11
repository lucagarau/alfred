import telebot


        
class Alfred:
    def __init__(self,token,default_chat_id = None):
        self.TOKEN = token 
        self.bot = telebot.TeleBot(self.TOKEN)
        self.user = default_chat_id

    def send_message(self,message, chat_id = None):
        #if chat_id is not specified, send to default chat_id if available
        if chat_id is None and self.user is not None:
            recipient = self.user
        elif chat_id is not None:
            recipient = chat_id
        elif self.user is None and chat_id is None:
            raise ValueError("No chat_id specified")
        
        self.bot.send_message(recipient, message)

    def send_photo(self,photo_path, chat_id = None):
        #if chat_id is not specified, send to default chat_id if available
        if chat_id is None and self.user is not None:
            recipient = self.user
        elif chat_id is not None:
            recipient = chat_id
        elif self.user is None and chat_id is None:
            raise ValueError("No chat_id specified")
        
        try:
            self.bot.send_photo(recipient, photo = open(photo_path, 'rb'))
        except FileNotFoundError:
            raise FileNotFoundError("Photo not found")
        except Exception as e:
            print("an error occured: ", e)


    def send_file(self,file_path, chat_id = None):
        #if chat_id is not specified, send to default chat_id if available
        if chat_id is None and self.user is not None:
            recipient = self.user
        elif chat_id is not None:
            recipient = chat_id
        elif self.user is None and chat_id is None:
            raise ValueError("No chat_id specified")
        
        try:
            self.bot.send_document(recipient, document= open(file_path, 'rb'))
        except FileNotFoundError:
            raise FileNotFoundError("Photo not found")
        except Exception as e:
            print("an error occured: ", e)

    

    
