import json
from os import environ
import tweepy
import random

API_KEY = environ['KEY']
API_SECRET = environ['SECRET']

ACCESS_TOKEN = environ['TOKEN']
ACCESS_TOKEN_SECRET = environ['TOKEN_SECRET']


# composition de la phrase
def createDream():
    base = "J'ai rêvé que "
    sujet = "je "
    verbes = ['acceptais', 'rentrais dans', 'préparais', 'achetais', 'envoyais', 'présentais', 'aidais', 'espérais', 'priais', 'aimais', 'essayais', 'prononçais', 'ajoutais', 'existais', 'quittais', 'appelais', 'expliquais', 'racontais', 'apportais', 'exprimais', 'rappelais', 'approchais', 'fermais', 'refusais', 'appuyais', 'formais', 'regardais', 'arrêtais', 'frappais', 'rencontrais', 'arrivais vers', 'gagnais', 'rentrais', 'assurais', 'gardais', 'répétais', 'avancais', 'glissais', 'ressemblais', 'brillais', 'jetais', 'restais', 'brûlais', 'jouais', 'retournais', 'cachais', 'jugeais', 'retrouvais', 'levais', 'rêvais', 'mangeais', 'roulais', 'changeais', 'manquais', 'sauvais', 'chantais', 'marchais',
              'semblais', 'chargeais', 'montais', 'tirais', 'cherchais', 'montrais', 'tombais', 'commençais', 'nommais', 'touchais', 'comptais sur', 'occupais', 'tournais', 'oubliais', 'travaillais', 'couchais', 'parlais', 'traversais', 'criais sur', 'passais', 'trompais', 'décidais', 'payais', 'trouvais', 'demandais', 'pensais', 'tuais', 'devinais', 'plaçais', 'volais', 'donnais', 'pleurais', 'écoutais', 'portais', 'élevais', 'posais', 'embrassais', 'possédais', 'emportais', 'poussais', "allumais", "arrangeais", "énervais", "oubliais", "évitais", "irriguais", "écrivais", "utilisais", "inventais", "bidouillais", "mangeais", "tapais", "jouais", "rêvais", "buvais", "visais", "regardais", "salissais", "convoitais"]
    complement = ['Londres', 'Melbourne', 'New York', 'Los Angeles', 'Tokyo', 'Madrid', 'Paris', 'Stockholm', 'Singapour', 'Zurich', 'Amsterdam', 'Toronto', 'Séoul', 'Francfort', 'Berlin', 'San Francisco', 'Hong Kong', 'Dubaï', 'Sydney', 'Copenhague', "des grosses frites", "du code", "une chemise hawaienne", "les élections", "la vie", "le capitalisme", "les hommes", "la gloire", "le soleil", 'un balcon', 'un bureau', 'un couloir', 'un escalier', 'un évier', 'un four', 'un four à micro-ondes', 'un jardin', 'un lavabo', 'un lave-vaisselle', 'un lavoir', 'un lit', 'un miroir', 'un plafond', 'un réfrigérateur', 'un salon', 'un sous-sol', 'une armoire', 'une baignoire', 'une chaise', 'une fenêtre', 'une machine à laver', 'une porte', 'une salle à manger', 'une salle de bains', 'une table', 'une terrasse', 'un aigle', 'un bouc', 'une chèvre', 'un chevreau', 'un canard', 'une cane', 'un caneton', 'un canari', 'un chameau',
                  'un chat', 'un chaton', 'un cheval', 'une jument', 'un poulain', 'un chien', 'un chiot', 'un chimpanzé', 'un cobra', 'un coq', 'une poule', 'un poussin', 'un crocodile', 'un dauphin', 'un écureuil', 'un éléphant', 'une éléphante', 'un éléphanteau', 'un faucon', 'un hippopotame', 'un insecte', 'un kangourou', 'un lapin', 'une lapine', 'un lapereau', 'un lion', 'une lionne', 'un lionceau', 'un loup', 'une louve', 'un louveteau', 'un mouton', 'une brebis', 'un agneau', 'un oiseau', 'un ours', 'une ourse', 'un ourson', 'un panda', 'un pélican', 'un perroquet', 'un phoque', 'un pingouin', 'un poisson', 'un porc', 'une truie', 'un porcelet', 'un renard', 'un requin', 'un serpent', 'un taureau', 'une vache', 'un veau', 'un tigre', 'une tigresse', 'une abeille', 'une araignée', 'une fourmi', 'une girafe', 'un girafeau', 'une grenouille', 'une mouche', 'une souris', 'une tortue', 'une truite']
    adverbe = ['lentement', 'vite', 'rapidement', 'admirablement', 'calmement', 'doucement', 'gentiment', 'méchamment', 'confusément', 'innocemment', 'vulgairement', 'tant bien que mal', 'n’importe comment', 'à la va-vite', 'précipitamment', 'à tort', 'à raison', "parfaitement", "timidement", "élégament", "en rythmes", "à l'arrache", "en mode one life", "brusquement", "violemment", "en noir et blanc", "sur du disco", "avec amour", "avec légèreté", "en fredonnant", 'en priant',
               'en avançant', 'en glissant', 'en brillant', 'en brûlant', 'en jouant', 'en jugeant', 'en rêvant', 'en mangeant', 'en roulant', 'en chantant', 'en marchant', 'en montant', 'en tombant', 'en comptant', 'en tournant', 'en oubliant', 'en travaillant', 'en parlant', 'en criant', 'en passant', 'en volant', 'en donnant', 'en pleurant', 'en voyageant', 'en poussant', 'en oubliant', 'en évitant', 'en écrivant', 'en bidouillant', 'en mangeant', 'en jouant', 'en rêvant', 'en buvant']
    complement2 = ("en compagnie de la Reine d'Angleterre", "aux cotés de mon chat", "avec Michel Drucker", "avec Céline Dion", "avec Nicolas Cage", "avec Jean-Claude Van Damme", "avec Dwayne Johnson", "avec Taylor Swift", "avec un chien", "avec un capybara", "avec un dauphin", "avec des oies", "avec un wombat", "avec des kangourous", "avec des huitres", "avec Rihanna",
                   "avec Bruce Willis", "avec Kim Kardashian", "tout en jouant au scrabble", "et ça passait à la télé", "et après les pompiers arrivaient", "et y avait des mariachis", "et je captais rien", "et en fait c'était une arnaque", "et je me suis réveillé", "sauf que j'étais de droite", "et j'achetais du poulet", "et après j'étais élue miss France", "et après ça partait en cacahuète")

    verbe = random.choice(verbes)
    if verbe[0] == "a" or verbe[0] == "e" or verbe[0] == "i" or verbe[0] == "u" or verbe[0] == "y" or verbe[0] == "h" or verbe[0] == "é" or verbe[0] == "è" or verbe[0] == "ê":
        sujet = "j'"

    dream = base + sujet + verbe + " " + \
        random.choice(complement) + " " + random.choice(adverbe) + \
        " " + random.choice(complement2) + "."
    return dream

# connexion à l'API


def makeTwitt():
    client = tweepy.Client(
        consumer_key=API_KEY, consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET
    )
    tweet = createDream()

    response = client.create_tweet(
        text=tweet
    )

    return response


def lambda_handler(event, context):
    # implement
    result = makeTwitt()
    return {
        'statusCode': 200,
        'body': json.dumps("j'ai bien twitté mon rêve !")
    }
