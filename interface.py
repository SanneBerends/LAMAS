import pygame
import math
from game import *
from kripke_model import *

""" Interface

Implementation of the interface of the game and the Kripke model
"""

pygame.init()
# load images
card0_image = pygame.image.load('images/bb0.jpg')
card1_image = pygame.image.load('images/bb1.jpg')
card2_image = pygame.image.load('images/bb2.jpg')
card3_image = pygame.image.load('images/bb3.jpg')
card4_image = pygame.image.load('images/bb4.jpg')
card_image = pygame.image.load('images/bb.jpg')
card0_image = pygame.transform.scale(card0_image, (110, 171))
card1_image = pygame.transform.scale(card1_image, (110, 171))
card2_image = pygame.transform.scale(card2_image, (110, 171))
card3_image = pygame.transform.scale(card3_image, (110, 171))
card4_image = pygame.transform.scale(card4_image, (110, 171))
card_image = pygame.transform.scale(card_image, (110, 171))
card_images = [card0_image, card1_image, card2_image, card3_image, card4_image]
icon = pygame.image.load('images/icon.png')
icon = pygame.transform.scale(icon, (110, 171))

# initialize normal and bold font
font = pygame.font.SysFont('comicsans', 20, False)
font_bolt = pygame.font.SysFont('comicsans', 20, True)


def render_game_env(window, player1, player2, discard_pile, turn):
    # draw initial cards
    card_places = [(50, 50), (200, 50), (50, 450), (200, 450)]
    cards = [player1.get_card1(), player1.get_card2(),
             player2.get_card1(), player2.get_card2()]
    for i in range(0, 4):
        window.blit(card_images[cards[i].value], card_places[i])

    # create pile
    pile_places = [(550, 250), (553, 253), (556, 256),
                   (559, 259), (562, 262), (565, 265)]
    for pile_place in pile_places:
        window.blit(card_image, pile_place)

    # create discard pile
    window.blit(card_images[discard_pile[-1].value], (400, 257))

    if turn == 1:
        text = font_bolt.render('Player 1', True, (0, 0, 0))
        window.blit(text, (141, 15))
        text = font.render('Player 2', True, (0, 0, 0))
        window.blit(text, (141, 415))
        window.blit(card_image, (50, 450))
        window.blit(card_image, (200, 450))
    else:
        text = font_bolt.render('Player 2', True, (0, 0, 0))
        window.blit(text, (141, 415))
        text = font.render('Player 1', True, (0, 0, 0))
        window.blit(text, (141, 15))
        window.blit(card_image, (50, 50))
        window.blit(card_image, (200, 50))

    return window


def render_kripke_model(window):
    number_of_worlds = 256
    for i in range(0, number_of_worlds):
        theta = 2 * math.pi * i/number_of_worlds
        radius = 340
        x = 1050 + radius * math.cos(theta)
        y = 350 + radius * math.sin(theta)
        pygame.draw.circle(window, (0, 0, 0), (x, y), 1)


def render_interface(player1, player2, discard_pile, turn):
    # create background
    window = pygame.display.set_mode((1400, 700))
    window.fill((220, 220, 220))
    pygame.display.set_caption("Beverbende")
    pygame.display.set_icon(icon)
    pygame.draw.line(window, (0, 0, 0), (700, 0), (700, 700))

    render_game_env(window, player1, player2, discard_pile, turn)
    render_kripke_model(window)
    pygame.display.update()


if __name__ == "__main__":
    '''Play the game by playing multiple rounds until beverbende
       @TODO: er staat nu nog niet in wanneer beverbende wordt geroepen!'''
    deck = Deck()
    card1 = deck.draw_card()
    card2 = deck.draw_card()
    card3 = deck.draw_card()
    card4 = deck.draw_card()
    player1 = Player(card1, card2)
    player2 = Player(card3, card4)

    kripke_model = Beverbende(
        f'{card1.value}{card2.value}{card3.value}{card4.value}')

    beverbende = 0
    turn = 1
    discard_pile = [deck.draw_card()]
    render_interface(player1, player2, discard_pile, turn)
    while not beverbende:
        discard_pile = play_round(
            turn, player1, player2, deck, discard_pile, kripke_model)
        render_interface(player1, player2, discard_pile, turn)
        pygame.time.wait(500)
        if turn == 1:
            turn = 2
        else:
            turn = 1
        render_interface(player1, player2, discard_pile, turn)
