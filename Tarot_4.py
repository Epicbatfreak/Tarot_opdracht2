# Import libraries met Tarot kaarten, twee libraries om de betekenis van de kaarten te scheiden. Eén voor wanneer ze rechtop worden getrokken en één voor wanneer ze ondersteboven worden getrokkenfrom reverse en de random module zodat we deze kunnen gebruiken.
from reversed import Tarot_r
from upright import Tarot_u
from LuckyOrUnlucky import Luck_Unlucky
import random

# Om één deck te creeëren voegen we de verschillende kaarten samen, we willen hier alleen de namen van de kaarten hebben zodat we later de betekenis op kunnen vragen. Daarom vragen we alleen de keys op, omdat dit later handig is converteren we ze gelijk naar lijsten.
deck_A = list(Tarot_u.keys())
deck_B = list(Tarot_r.keys())

# Om alle kaarten en hun betekenis in één stapel te hebben zodat we de index kunnen gebruiken maken we hier een apparte tupple van
deck_meaning = {}
deck_meaning.update(Tarot_u)
deck_meaning.update(Tarot_r)

# In deze lijst komen alle kaarten gekoppeld aan een waarde van 1, 0 of -1 om te bepalen of ze wel of geen geluk brengen
Luck_or_not = Luck_Unlucky


# Om te voorkomen dat steeds de eerste kaart van de stapel pakken is er een uitgebreide functie gecreeërd die bepaald welke kaart van welke stapel wordt gepakt.
# Hieronder zien we het begin van dit proces door middel van een coinflip bepalen we of we van stapel A of B pakken
def deckAorB():
    flipped_coin = random.randint(0, 1)
    if flipped_coin == 0:
        return "A"
    if flipped_coin == 1:
        return "B"


# Deze functie bepaald welke kaarten we trekken en voegt deze kaarten aan de stapel toe die hij ons daarna terug geeft
def draw_cards(X):
    card_total = 0
    card_pile = []
    while card_total < X:
        deck_type = deckAorB()
        if card_total <= X:
            if deck_type == "A":
                card_pile.append(random.choice(deck_A))
            if deck_type == "B":
                card_pile.append(random.choice(deck_B))
        if card_total == X:
            break
        card_total += 1
    return card_pile


# Zodat we de betekenis van de kaarten kunnen opvragen hebben we ook een functie geschreven die je kunt aanroepen. Deze functie zoekt de betekenis bij de key die we hem geven vanuit de vorige functie(Deze is geschikt voor 3 kaarten).
def card_meaning3(card_list):
    reading1 = [card_list[0], ]
    reading2 = [card_list[1], ]
    reading3 = [card_list[2], ]
    reading1.append(deck_meaning.get(card_list[0]))
    reading2.append(deck_meaning.get(card_list[1]))
    reading3.append(deck_meaning.get(card_list[2]))
    return reading1, reading2, reading3


# Deze is geschikt voor 5 kaarten.
def card_meaning5(card_list):
    reading1 = [card_list[0], ]
    reading2 = [card_list[1], ]
    reading3 = [card_list[2], ]
    reading4 = [card_list[3], ]
    reading5 = [card_list[4], ]
    reading1.append(deck_meaning.get(card_list[0]))
    reading2.append(deck_meaning.get(card_list[1]))
    reading3.append(deck_meaning.get(card_list[2]))
    reading4.append(deck_meaning.get(card_list[3]))
    reading5.append(deck_meaning.get(card_list[4]))
    return reading1, reading2, reading3, reading4, reading5


def card_luck5(card_list):
    are_you_lucky = []
    luck_list = []
    are_you_lucky.append(Luck_or_not.get(card_list[0]))
    are_you_lucky.append(Luck_or_not.get(card_list[1]))
    are_you_lucky.append(Luck_or_not.get(card_list[2]))
    are_you_lucky.append(Luck_or_not.get(card_list[3]))
    are_you_lucky.append(Luck_or_not.get(card_list[4]))
    for i in are_you_lucky:
        luck_list += i
    luck_total = (sum(luck_list))
    if luck_total == 0:
        return "Your future is undecided"
    elif luck_total <= 1:
        return "It's your lucky day!"
    else:
        return "Better luck next time"


# print(draw_cards(3))
# print(card_meaning5(draw_cards(5)))
print(card_luck5(draw_cards(5)))
