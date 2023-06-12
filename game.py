import pygame
import random

""" Game

Implementation of the game
"""

class Player:
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def play(self, card):
        if self.card1.value < self.card2.value:
            if card.value < self.card2.value:
                discard_card = self.card2
                self.set_card2(card)
                return discard_card, 2
        else:
            if card.value < self.card1.value:
                discard_card = self.card1
                self.set_card1(card)
                return discard_card, 1
        return card, 0 #TODO: wat is card nummer hier? 

    def get_card1(self):
        return self.card1

    def get_card2(self):
        return self.card2

    def set_card1(self, card):
        self.card1 = card

    def set_card2(self, card):
        self.card2 = card

class Card:
    def __init__(self, value):
        self.value = value
    
    def get_value(self):
        return self.value

class Deck:
    def __init__(self):
        self.cards = []
        #  for card in [0, 1, 2, 3, 4] * 5:
        for card in [0, 1] * 5:
            self.cards.append(Card(card))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if self.get_number_of_cards() == 0:
            print('Deck is empty. Game stops!')
            pygame.quit()
            quit()
            return 0
        return self.cards.pop()

    def get_number_of_cards(self):
        return len(self.cards)

def play_round(turn, player1, player2, deck, discard_pile):
    played = 0
    type = 0
    card = 0
    while not played:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 550 <= event.pos[0] <= 675 and 250 <= event.pos[1] <= 436:
                    # deck
                    print('player ' + str(turn) + ' picked from deck')
                    card = deck.draw_card()
                    if turn == 1:
                        discard_card, card_number = player1.play(card)
                        if card_number == 1:
                            type = 3
                        if card_number == 0:
                            type = 5

                    else:
                        discard_card, card_number = player2.play(card)
                        if card_number == 2:
                            type = 4
                        if card_number == 0:
                            type = 5
                    
                    discard_pile.append(discard_card)
                    played = 1
                if 400 <= event.pos[0] <= 510 and 257 <= event.pos[1] <= 428 and discard_pile is not None:
                    # discard pile
                    print('player ' + str(turn) + ' picked from discard pile')
                    card = discard_pile[-1]
                    if turn == 1:
                        discard_card, card_number = player1.play(card)
                        if card_number == 1:
                            type = 1

                    else:
                        discard_card, card_number = player2.play(card)
                        if card_number == 2:
                            type = 2
                        
                    discard_pile = discard_pile[:-1]
                    discard_pile.append(discard_card)
                    played = 1
    return discard_pile, type, card

