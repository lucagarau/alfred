#Exemple of a script which use Alfred and send a file every 10 seconds if a process is running

from alfred_bot.alfred import Alfred
import os
import time
import psutil

bot = Alfred(111111111111)
pid = 17812 #pid of the process
timer = 10 #timer in seconds
file_path = R"/home/file.txt" #path del file da inviare

if __name__ == "__main__":
    if not psutil.pid_exists(pid):
        bot.send_message("PID not found")
    else:
        while psutil.pid_exists(pid):
            bot.send_file(file_path)
            time.sleep(timer)
        bot.send_message("Process ended")