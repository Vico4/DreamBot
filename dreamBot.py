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
verbes = ["mangeais", "tapais", "jouais", "rêvais", "buvais", "visais", "regardais", "fatiguais", "convoitais"]
complement = ["Paris","des grosses frites", "du code", "une chemise hawaienne", "les élections", "la vie", "le capitalisme", "les hommes", "la gloire", "le soleil"]
#adjectif = ("magnifique", "")
#complement2 = ()
def makeTwitt():
    tweet = base + random.choice(verbes) + " " + random.choice(complement)
    return tweet 

#print(makeTwitt())
# pour tweeter 
#api.update_status("C'est moi le bot qui rêve")

response = client.create_tweet(
    text="This Tweet was Tweeted using Tweepy and Twitter API v2!"
)