# Navigate to instabot\bot\bot-filter.py -> comment from line 164 to 178
# To remove restrictions for following private,business,verified users.

from instabot import Bot  
from flask import Flask

app = Flask(__name__)

bot = Bot()       # click Bot() to see the default values like max limit, delay etc.

user_name = "digiadverts"
password ="subhashselvam121996"
bot.login(username=user_name, password=password)


# To get details about the user 
user_id = bot.get_user_id_from_username("rajaamanii")
user_info = bot.get_user_info(user_id)
print("biography of rajaamanii is {}".format(user_info['biography']))

# Read list of users from .txt file. add username in separate line to follow.
users_list = bot.read_list_from_file("users.txt")
print(users_list)
# To follow list of users.
if users_list:
    bot.follow_users(users_list)

# To DM list of users
# message delay is set to 60s by default
if users_list:
    for user in users_list:
        directMessage = "Hello {}. This is {}!".format(user,user_name)
        print(bot.send_message(directMessage, user))

if __name__ == "__main__":
    app.run()