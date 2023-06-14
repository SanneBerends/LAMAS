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

# initialize different fonts
font = pygame.font.SysFont('comicsans', 20, False)
font_small = pygame.font.SysFont('comicsans', 10, False)
font_bolt = pygame.font.SysFont('comicsans', 20, True)


def render_game_env(window, player1, player2, discard_pile, turn):
    # draw initial cards
    card_places = [(50, 50), (200, 50), (50, 450), (200, 450)]
    cards = [player1.get_card1(), player1.get_card2(),
             player2.get_card1(), player2.get_card2()]
    for i in range(0, 4):
        window.blit(card_images[cards[i].value], card_places[i])

    # draw pile
    pile_places = [(550, 250), (553, 253), (556, 256),
                   (559, 259), (562, 262), (565, 265)]
    for pile_place in pile_places:
        window.blit(card_image, pile_place)

    # draw discard pile
    window.blit(card_images[discard_pile[-1].value], (400, 257))

    # draw cards for both players
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


def render_kripke_model(window, kripke_model):
    #draw worlds
    number_of_worlds = len(kripke_model.ks.worlds)
    drawn_worlds = {}
    for i,world in enumerate(kripke_model.ks.worlds):
        theta = 2 * math.pi * i / number_of_worlds
        radius = 330
        if number_of_worlds == 1:
            x = 1050
        else:
            x = 1050 + radius * math.cos(theta)
        y = 360 + radius * math.sin(theta)
        pygame.draw.circle(window, (0, 0, 0), (x, y), 5)
        drawn_worlds[world.name] = (x,y)

    #draw relations
    colors = [(220,20,60), (0,0,128)]
    for agent in kripke_model.ks.relations:
        for relation in kripke_model.ks.relations[agent]:
            pygame.draw.line(window, colors[agent-1], drawn_worlds[relation[0]], drawn_worlds[relation[1]])

    #draw legend
    pygame.draw.circle(window, (220,20,60), (1310, 20), 3)
    pygame.draw.circle(window, (0,0,128), (1310, 40), 3)
    text = font_small.render('= Player 1', True, (0, 0, 0))
    window.blit(text, (1320, 11))
    text = font_small.render('= Player 2', True, (0, 0, 0))
    window.blit(text, (1320, 31))


def render_interface(player1, player2, discard_pile, turn, kripke_model):
    # create background
    window = pygame.display.set_mode((1400, 700))
    window.fill((220, 220, 220))
    pygame.display.set_caption("Beverbende")
    pygame.display.set_icon(icon)
    pygame.draw.line(window, (0, 0, 0), (700, 0), (700, 700))

    render_game_env(window, player1, player2, discard_pile, turn)
    render_kripke_model(window, kripke_model)
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
    render_interface(player1, player2, discard_pile, turn, kripke_model)
    while not beverbende:
        print(kripke_model.ks)

        # determine card1 and card2
        if turn == 1:
            card1 = player1.get_card1().get_value()
            card2 = player1.get_card2().get_value()
        if turn == 2:
            card1 = player2.get_card1().get_value()
            card2 = player2.get_card2().get_value()
        discard = discard_pile[-1].get_value()

        discard_pile, type, card = play_round(turn, player1, player2, deck, discard_pile)
        
        if type == 3 or type == 4 or type == 5:
            deck_card = card.get_value()
        else:
            deck_card = None

        kripke_model.public_announcement(type, turn, card1, card2, discard, deck_card)

        render_interface(player1, player2, discard_pile, turn, kripke_model)
        pygame.time.wait(500)
        if turn == 1:
            turn = 2
        else:
            turn = 1
        render_interface(player1, player2, discard_pile, turn, kripke_model)

