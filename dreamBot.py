import tweepy
import random

API_KEY = "***"
API_SECRET = "***"

ACCESS_TOKEN = "***"
ACCESS_TOKEN_SECRET = "***"

#connexion à l'API 
#auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
#auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#api = tweepy.API(auth)

client = tweepy.Client(
    consumer_key=API_KEY, consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET
)

# composition de la phrase
base = "J'ai rêvé que je "
verbes = ["mangeais", "tapais", "jouais", "rêvais", "buvais", "visais", "regardais", "salissais", "convoitais"]
complement = ["Paris","des grosses frites", "du code", "une chemise hawaienne", "les élections", "la vie", "le capitalisme", "les hommes", "la gloire", "le soleil"]
adjectif = ("parfaitement", "élégament", "en rythmes", "à l'arrache", "en mode one life", "brusquement", "violemment", "en noir et blanc", "sur du disco")
complement2 = ("avec la Reine d'Angleterre", "avec François Fillon", "avec Michel Drucker", "tout en jouant au scrabble", "et ça passait à la télé", "et après les pompiers arrivaient", "et y avait des mariachis", "et je captais rien", "et en fait c'était une arnaque", "et je me suis réveillé", "sauf que j'étais de droite", "et j'achetais du poulet", "et après j'étais élue miss France")
def makeTwitt():
    tweet = base + random.choice(verbes) + " " + random.choice(complement) + " " + random.choice(adjectif) + " " + random.choice(complement2) + "."
    return tweet 

#print(makeTwitt())
# pour tweeter 
#api.update_status("C'est moi le bot qui rêve")

response = client.create_tweet(
    text="This Tweet was Tweeted using Tweepy and Twitter API v2!"
)