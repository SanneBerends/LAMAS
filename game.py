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
        replaced_card = 0  # return whether card1 or card2 is replaced
        if self.card1.value < self.card2.value:
            if card.value < self.card2.value:
                discard_card = self.card2
                self.set_card2(card)
                replaced_card = 2
                return discard_card, replaced_card
        else:
            if card.value < self.card1.value:
                discard_card = self.card1
                self.set_card1(card)
                replaced_card = 1
                return discard_card, replaced_card
        return card, replaced_card

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
        for card in [0, 1, 2, 3, 4] * 5:
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


def play_round(turn, player1, player2, deck, discard_pile, kripke_model):
    played = 0
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
                        discard_card, replaced_card = player1.play(card)
                        type = replaced_card + 2  # replaced card == 1 for card 1, so case 3
                        if replaced_card == 1:
                            new_card1 = card.get_value()
                            new_card2 = None
                        else:
                            new_card1 = None
                            new_card2 = card.get_value()
                        kripke_model.public_announcement(type, 1, player1.get_card1(
                        ).get_value(), player1.get_card2().get_value(), discard=discard_card.get_value(), new_card1=new_card1, new_card2=new_card2)
                    else:
                        discard_card, replaced_card = player2.play(card)
                        type = replaced_card + 2  # replaced card == 2 for card 2, so case 4
                        if replaced_card == 1:
                            new_card1 = card.get_value()
                            new_card2 = None
                        else:
                            new_card1 = None
                            new_card2 = card.get_value()
                        kripke_model.public_announcement(type, 2, player2.get_card1(
                        ).get_value(), player2.get_card2().get_value(), discard=discard_card.get_value(), new_card1=new_card1, new_card2=new_card2)
                    discard_pile.append(discard_card)
                    played = 1
                if 400 <= event.pos[0] <= 510 and 257 <= event.pos[1] <= 428 and discard_pile is not None:
                    # discard pile
                    print('player ' + str(turn) + ' picked from discard pile')
                    card = discard_pile[-1]
                    if turn == 1:
                        discard_card, replaced_card = player1.play(card)
                        if replaced_card == 1:
                            new_card1 = card.get_value()
                            new_card2 = None
                        else:
                            new_card1 = None
                            new_card2 = card.get_value()
                        kripke_model.public_announcement(replaced_card, 1, player1.get_card1(
                        ).get_value(), player1.get_card2().get_value(), new_card1=new_card1, new_card2=new_card2)
                    else:
                        discard_card, replaced_card = player2.play(card)
                        if replaced_card == 1:
                            new_card1 = card.get_value()
                            new_card2 = None
                        else:
                            new_card1 = None
                            new_card2 = card.get_value()
                        kripke_model.public_announcement(replaced_card, 2, player2.get_card1(
                        ).get_value(), player2.get_card2().get_value(), new_card1=new_card1, new_card2=new_card2)
                    discard_pile = discard_pile[:-1]
                    discard_pile.append(discard_card)
                    played = 1
    return discard_pile
