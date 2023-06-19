import pygame
import random

""" Game

Implementation of the game
"""

class Player:
    """
    This class describes a Player with its two cards
    """

    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def play(self, card):
        ''' plays a picked card, replaces it by its highest card if the picked card is smaller
            returns the discarded card and a number representing for which card it is replaced'''
        if self.card1.value < self.card2.value:
            if card.value < self.card2.value:
                discard_card = self.card2
                self.card2 = card
                return discard_card, 2
        elif self.card2.value < self.card1.value:
            if card.value < self.card1.value:
                discard_card = self.card1
                self.card1 = card
                return discard_card, 1
        else:
            if card.value < self.card1.value:
                rndm = random.randint(1,10)
                if rndm > 5:
                    discard_card = self.card2
                    self.card2 = card
                    return discard_card, 2
                else:
                    discard_card = self.card1
                    self.card1 = card
                    return discard_card, 1
        return card, 0


class Card:
    """
    This class describes a Card with its value
    """
    def __init__(self, value):
        self.value = value


class Deck:
    """
    This class describes a Deck with each card 5 times in it
    """
    def __init__(self, num_dif_cards):
        self.num_dif_cards = num_dif_cards
        self.cards = []
        for card in list(range(0,self.num_dif_cards)) * 5:
            self.cards.append(Card(card))
        self.shuffle()

    def shuffle(self):
        ''' shuffles the deck '''
        random.shuffle(self.cards)

    def draw_card(self):
        ''' returns a card drawn from the deck and removes this card from the deck '''
        if len(self.cards) == 0:
            print('Deck is empty. Game stops!')
            pygame.quit()
            quit()
            return 0
        return self.cards.pop()


def play_round(turn, player1, player2, deck, discard_pile):
    ''' Plays one round of the game
        Returns the new discard pile, the type of the move, and the card that is played '''
    played = 0
    while not played:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # player clicked on close window
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 550 <= event.pos[0] <= 675 and 250 <= event.pos[1] <= 436:
                    # player clicked on deck
                    print('player ' + str(turn) + ' picked from deck')
                    card = deck.draw_card()
                    if turn == 1:
                        discard_card, card_number = player1.play(card)
                    else:
                        discard_card, card_number = player2.play(card)
                    type = card_number + 2
                    if card_number == 0: type = 5
                    
                    discard_pile.append(discard_card)
                    played = 1
                if 400 <= event.pos[0] <= 510 and 257 <= event.pos[1] <= 428 and discard_pile is not None:
                    # player clicked on discard pile
                    if (turn == 1 and (discard_pile[-1].value >= player1.card1.value and discard_pile[-1].value >= player1.card2.value)) or \
                        (turn == 2 and (discard_pile[-1].value >= player2.card1.value and discard_pile[-1].value >= player2.card2.value)):
                        print("Taking a card from the discard pile is not a rational move. Pick another card")
                    else:
                        print('player ' + str(turn) + ' picked from discard pile')
                        card = discard_pile[-1]
                        if turn == 1:
                            discard_card, card_number = player1.play(card)
                        else:
                            discard_card, card_number = player2.play(card)
                        type = card_number

                        discard_pile = discard_pile[:-1]
                        discard_pile.append(discard_card)
                        played = 1

    return discard_pile, type, card

