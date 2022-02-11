import requests
from discord import Webhook, RequestsWebhookAdapter

discordhook = "" # Discord Webhook URL

def call_dis(message):
        webhook = Webhook.from_url("discordhook", adapter=RequestsWebhookAdapter())
        webhook.send(message)
