import random



def create_deck():
    deck = []
    for i in range(2,11):
        for j in ('C', 'P', 'B', 'X'):
            deck.append(str(i)+j)
    for i in ('J','Q','K', 'T'):
        for j in ('C', 'P', 'B', 'X'):
            deck.append(i+j)
    return deck



def started_hand(deck):
    hand = []
    for i in range(2):
        hand.append(random.choice(deck))
        deck.remove(hand[-1])
    return hand, deck
    

def start_game():
    deck = create_deck()
    hand[]
    started_hand(deck)
    hand, deck = started_hand(deck)




start_game()
    
    
