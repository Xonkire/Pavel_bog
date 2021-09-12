

import random


def create_deck():
    deck = []
    for i in range(2, 11):
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
    hand = []
    hand, deck = started_hand(deck)
    while True:
        print_hand(hand)
        print_score(score)
        offer_another_card(hand, deck)


def give_new_card(deck):
    new_card = random.choice(deck)
    deck.remove(new_card)
    return new_card, deck


def offer_another_card(hand, deck):
    response = input("Выдать ещё одну карту? Да/Нет")
    if response.lower() == 'да':
        a = give_new_card(deck)
        hand.append(a[0])
        deck = a[1]
    elif response.lower() == 'нет':
        exit()
    else:
        print("Неверный ввод!")
    
def print_hand(hand):
    for card in hand:
        print(card,end='')
    print()

def print_score(hand):
    for card in hand:
        print(card,end='')
    print()

def print_score(hand):
    costs = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "1":10,
    "J": 2,
    "Q": 3,
    "K": 4,
    "T": 11,

    }
    score = 0
    for card in hand:
        score += costs[card[0]]
    print(score)





start_game()
