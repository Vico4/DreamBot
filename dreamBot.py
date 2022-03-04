import json
from os import environ
import tweepy
import random

API_KEY = environ['KEY']
API_SECRET = environ['SECRET']

ACCESS_TOKEN = environ['TOKEN']
ACCESS_TOKEN_SECRET = environ['TOKEN_SECRET']

#connexion à l'API 

def makeTwitt():
    client = tweepy.Client(
        consumer_key=API_KEY, consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET
    )

# composition de la phrase
    base = "J'ai rêvé que je "
    verbes = ["mangeais", "tapais", "jouais", "rêvais", "buvais", "visais", "regardais", "salissais", "convoitais"]
    complement = ["Paris","des grosses frites", "du code", "une chemise hawaienne", "les élections", "la vie", "le capitalisme", "les hommes", "la gloire", "le soleil"]
    adjectif = ("parfaitement", "timidement", "élégament", "en rythmes", "à l'arrache", "en mode one life", "brusquement", "violemment", "en noir et blanc", "sur du disco", "avec amour", "avec légèreté", "en fredonnant")
    complement2 = ("en compagnie de la Reine d'Angleterre", "aux cotés de mon chat", "avec Michel Drucker", "tout en jouant au scrabble", "et ça passait à la télé", "et après les pompiers arrivaient", "et y avait des mariachis", "et je captais rien", "et en fait c'était une arnaque", "et je me suis réveillé", "sauf que j'étais de droite", "et j'achetais du poulet", "et après j'étais élue miss France", "et après ça partait en cacahuète")
    
    tweet = base + random.choice(verbes) + " " + random.choice(complement) + " " + random.choice(adjectif) + " " + random.choice(complement2) + "."

    response = client.create_tweet(
    text = tweet
    )
    
    return response

def lambda_handler(event, context):
    # TODO implement
    result = makeTwitt()
    return {
        'statusCode': 200,
        'body': json.dumps("j'ai bien twitté mon rêve !")
    }
