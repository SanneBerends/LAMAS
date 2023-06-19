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
font_big = pygame.font.SysFont('comicsans', 100, True)


def render_game_env(window, player1, player2, discard_pile, turn):
    '''
    Renders the game environment (left part of the interface)
    '''
    # render cards of the players
    card_places = [(50, 50), (200, 50), (50, 450), (200, 450)]
    cards = [player1.card1, player1.card2,
             player2.card1, player2.card2]
    for i in range(0, 4):
        window.blit(card_images[cards[i].value], card_places[i])

    # render pile
    pile_places = [(550, 250), (553, 253), (556, 256), (559, 259), (562, 262), (565, 265)]
    for pile_place in pile_places:
        window.blit(card_image, pile_place)

    # render discard pile
    window.blit(card_images[discard_pile[-1].value], (400, 257))

    # render back of cards for one of the players and text based on current turn
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


def render_kripke_model(window, turn, kripke_model1, kripke_model2):
    '''
    Renders part of the Kripke Model relevant at the current turn (right part of the interface)
    '''
    # determine whose part of the Kripke Model to render
    if turn == 1:
        kripke_worlds = kripke_model1.ks.worlds
        kripke_relations = kripke_model1.ks.relations
        current_world = kripke_model1.current_world
    else:
        kripke_worlds = kripke_model2.ks.worlds
        kripke_relations = kripke_model2.ks.relations
        current_world = kripke_model2.current_world

    # render worlds placed in a circle
    number_of_worlds = len(kripke_worlds)
    drawn_worlds = {}
    for i,world in enumerate(kripke_worlds):
        theta = 2 * math.pi * i / number_of_worlds
        radius = 320
        if number_of_worlds == 1: x = 1050
        else:x = 1050 + radius * math.cos(theta)
        y = 350 + radius * math.sin(theta)
        if world.name == current_world: pygame.draw.circle(window, (0, 128, 0), (x, y), 5)
        else: pygame.draw.circle(window, (0, 0, 0), (x, y), 5)
        drawn_worlds[world.name] = (x, y)
        text = font_small.render(world.name, True, (0, 0, 0))
        if x < 1050: x -= 25
        if y < 350: y -= 15
        window.blit(text, (x,y))

    # render relations
    colors = [(220,20,60), (0,0,128)]
    for agent in kripke_relations:
        for relation in kripke_relations[agent]:
            pygame.draw.line(window, colors[agent-1], drawn_worlds[relation[0]], drawn_worlds[relation[1]])

    # render legend
    pygame.draw.circle(window, (220,20,60), (1310, 20), 3)
    pygame.draw.circle(window, (0,0,128), (1310, 40), 3)
    text = font_small.render('= Player 1', True, (0, 0, 0))
    window.blit(text, (1320, 11))
    text = font_small.render('= Player 2', True, (0, 0, 0))
    window.blit(text, (1320, 31))


def render_interface(player1, player2, discard_pile, turn, kripke_model1, kripke_model2, bever):
    '''
    Renders the whole interface
    '''
    # render background and name of interface
    window = pygame.display.set_mode((1400, 700))
    window.fill((220, 220, 220))
    pygame.display.set_caption("Beverbende")
    pygame.display.set_icon(icon)
    pygame.draw.line(window, (0, 0, 0), (700, 0), (700, 700))

    # render game environment and kripke model
    render_game_env(window, player1, player2, discard_pile, turn)
    render_kripke_model(window, turn, kripke_model1, kripke_model2)

    # render 'Bever' when it is called
    if bever == 1:
        text = font_big.render('Player '+str(turn)+': Bever!', True, (0, 0, 0))
        window.blit(text, (300, 300))

    pygame.display.update()


if __name__ == "__main__":
    '''
    Play the whole game by playing multiple rounds until 'Bever' is called by one of the players
    '''
    # initialize the game by drawing cards
    num_dif_cards = 4
    deck = Deck(num_dif_cards)
    card1 = deck.draw_card()
    card2 = deck.draw_card()
    card3 = deck.draw_card()
    card4 = deck.draw_card()
    player1 = Player(card1, card2)
    player2 = Player(card3, card4)
    discard_pile = [deck.draw_card()]

    # initialize the relevant parts of the kripke model and both players' knowledge bases
    kripke_model1 = Beverbende(
        f'{card1.value}{card2.value}{card3.value}{card4.value}', num_dif_cards, 1)
    kripke_model2 = Beverbende(
        f'{card1.value}{card2.value}{card3.value}{card4.value}', num_dif_cards, 2)
    knowledge_base1 = []
    knowledge_base2 = []

    bever = 0
    turn = 1
    render_interface(player1, player2, discard_pile, turn, kripke_model1, kripke_model2, bever)
    while not bever:
        #TODO: verwijderen dat dit geprint wordt
        if turn == 1: print(kripke_model1.ks)
        else: print(kripke_model2.ks)
        print(kripke_model1.current_world, kripke_model2.current_world)

        # play round
        if turn == 1:
            card1 = player1.card1.value
            card2 = player1.card2.value
        if turn == 2:
            card1 = player2.card1.value
            card2 = player2.card2.value
        discard = discard_pile[-1].value

        discard_pile, type, card = play_round(turn, player1, player2, deck, discard_pile)
        
        if type == 3 or type == 4 or type == 5:
            deck_card = card.value
        else:
            deck_card = None

        # obtain knowledge from played round
        if turn == 1:
            knowledge_base2 = kripke_model2.obtain_knowledge(knowledge_base2, type, turn, card1, card2, discard, deck_card)
            kripke_model1 = Beverbende(
                f'{player1.card1.value}{player1.card2.value}{player2.card1.value}{player2.card2.value}', num_dif_cards, 1)
            for (i,formula) in knowledge_base1: kripke_model1.ks = kripke_model1.ks.solve(formula)
            kripke_model2 = Beverbende(
                f'{player1.card1.value}{player1.card2.value}{player2.card1.value}{player2.card2.value}', num_dif_cards, 2)
            for (i,formula) in knowledge_base2: kripke_model2.ks = kripke_model2.ks.solve(formula)
        elif turn == 2:
            knowledge_base1 = kripke_model1.obtain_knowledge(knowledge_base1, type, turn, card1, card2, discard, deck_card,)
            kripke_model1 = Beverbende(
                f'{player1.card1.value}{player1.card2.value}{player2.card1.value}{player2.card2.value}', num_dif_cards, 1)
            for (i,formula) in knowledge_base1: kripke_model1.ks = kripke_model1.ks.solve(formula)
            kripke_model2 = Beverbende(
                f'{player1.card1.value}{player1.card2.value}{player2.card1.value}{player2.card2.value}', num_dif_cards, 2)
            for (i,formula) in knowledge_base2: kripke_model2.ks = kripke_model2.ks.solve(formula)

        render_interface(player1, player2, discard_pile, turn, kripke_model1, kripke_model2, bever)

        # determine if the player can call 'Bever'
        if turn == 1:
            cards_total = player1.card1.value + player1.card2.value
            bever = 1
            if cards_total != 0:
                for world in kripke_model1.ks.worlds:
                    if int(world.name[2]) + int(world.name[3]) <= cards_total:
                        bever = 0
        elif turn == 2:
            cards_total = player2.card1.value + player2.card2.value
            bever = 1
            if cards_total != 0:
                for world in kripke_model2.ks.worlds:
                    if int(world.name[0]) + int(world.name[1]) <= cards_total:
                        bever = 0

        # go to next round or stop the game when 'Bever' is called
        if not bever:
            pygame.time.wait(2000)
            if turn == 1:
                turn = 2
            else:
                turn = 1
            render_interface(player1, player2, discard_pile, turn, kripke_model1, kripke_model2, bever)
        else:
            print('Player ' + str(turn) + ': Bever!')
            print('Player ' + str(turn) + ' won')
            render_interface(player1, player2, discard_pile, turn, kripke_model1, kripke_model2, bever)
            pygame.time.wait(5000)