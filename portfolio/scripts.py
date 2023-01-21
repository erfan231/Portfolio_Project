# sent details to discord
from discord_webhook import DiscordWebhook
import os

# SCript to send message to discord via discord webhook
def SendMessage(name, email, message):
    msg = 'Name: {} \nEmail: {} \nMessage: {}' .format(name, email, message)
    webhook = DiscordWebhook(url=os.environ.get('DISCORD_WEBHOOK'), content='@everyone {}' .format(msg))
    webhook.execute()
