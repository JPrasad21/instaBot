# Navigate to instabot\bot\bot-filter.py -> comment from line 164 to 178
# To remove restrictions for following private,business,verified users.

from instabot import Bot  
from flask import Flask
import csv

app = Flask(__name__)

bot = Bot()       # click Bot() to see the default values like max limit, delay etc.

user_name = "digiadverts"
password ="subhashselvam121996"
bot.login(username=user_name, password=password)


# To read users from CSV file.
def readUsersFromCSV(file):
    with open(file,'rt')as f:
        data = csv.reader(f)
        user_list = []
        for row in data:
            if row[0] != "username":
                print(row[0])
                user_list.append(row[0])
        return user_list
users = readUsersFromCSV("users.csv")

# Read list of users from .txt file. add username in separate line to follow.
users_list = bot.read_list_from_file("users.txt")
print(users_list)


# To get details about the user 
user_id = bot.get_user_id_from_username("rajaamanii")
user_info = bot.get_user_info(user_id)
print("biography of rajaamanii is {}".format(user_info['biography']))


# To follow list of users.
if users:
    bot.follow_users(users)

# To DM list of users
# message delay is set to 60s by default
if users:
    for user in users:
        directMessage = "Hello {}. This is {}!".format(user,user_name)
        print(bot.send_message(directMessage, user))

if __name__ == "__main__":
    app.run()