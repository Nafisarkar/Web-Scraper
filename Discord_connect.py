import requests
from discord import Webhook, RequestsWebhookAdapter

def call_dis(message):
        webhook = Webhook.from_url("https://discordapp.com/api/webhooks/939764940208766996/HK20LPcvUEQK09KrzpqnjOSryaEQAmBaoGGFsAPLo97s0jLBXU7SMJ3x72qw9nqq7RUv", adapter=RequestsWebhookAdapter())
        webhook.send(message)


