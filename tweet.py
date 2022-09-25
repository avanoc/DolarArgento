import dotenv
import os
import schedule
from datetime import datetime
from time import sleep
from tweepy import Client
from zoneinfo import ZoneInfo
from dolar import dolarBlue, dolarTC, dolarCripto

# Load environment:
dotenv.load_dotenv()

# Retrieve credentials:
client = Client(bearer_token=os.environ["BEARER"], consumer_key=os.environ["CONSUMER_KEY"], 
consumer_secret=os.environ["CONSUMER_SECRET"], access_token=os.environ["ACCESS_KEY"], 
access_token_secret=os.environ["ACCESS_SECRET"])

# Tweet to be posted in the morning:
def tweet_m():
    today = datetime.now(ZoneInfo("America/Buenos_Aires"))
    blue = dolarBlue()
    tarjeta = dolarTC()
    cripto = dolarCripto()
    client.create_tweet(text=(f"El dólar blue está: {blue}\nEl dólar cripto está: {cripto}\nEl dólar tarjeta está: {tarjeta} \
        \n\n%s/%s/%s 10:00 hs" % (today.day, today.month, today.year)))
    return

# Tweet to be posted in the afternoon:
def tweet_a():
    today = datetime.now(ZoneInfo("America/Buenos_Aires"))
    blue = dolarBlue()
    tarjeta = dolarTC()
    cripto = dolarCripto()
    client.create_tweet(text=(f"El dólar blue está: {blue}\nEl dólar cripto está: {cripto}\nEl dólar tarjeta está: {tarjeta} \
        \n\n%s/%s/%s 16:00 hs" % (today.day, today.month, today.year)))
    return

# Run script in the morning:
schedule.every().day.at("13:00").do(tweet_m)

# Run script in the afternoon:
schedule.every().day.at("18:20").do(tweet_a)

# Wait time:
while True:
    schedule.run_pending() 
    sleep(15) 