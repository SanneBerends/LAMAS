import pygame
import random

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

class Player:
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def play(self, card):
        if self.card1.value < self.card2.value:
            if card.value < self.card2.value:
                self.set_card2(card)
                return 1
        else:
            if card.value < self.card1.value:
                self.set_card1(card)
                return 1
        return 0

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

def init_game_env(player1, player2):
    # create background
    pygame.init()
    window = pygame.display.set_mode((1400, 700))
    window.fill((220, 220, 220))
    pygame.display.set_caption("Beverbende")
    pygame.display.set_icon(icon)
    pygame.draw.line(window, (0, 0, 0), (700, 0), (700, 700))
    text = font_bolt.render('Player 1', True, (0, 0, 0))
    window.blit(text, (141, 15))
    text = font.render('Player 2', True, (0, 0, 0))
    window.blit(text, (141, 415))

    #draw initial cards
    card_places = [(50,50), (200,50), (50,450), (200,450)]
    cards = [player1.get_card1(), player1.get_card2(), player2.get_card1(), player2.get_card2()]
    for i in range(0,4):
        window.blit(card_images[cards[i].value], card_places[i])

    # create pile
    pile_places = [(550, 250), (553, 253), (556, 256), (559, 259), (562, 262), (565, 265)]
    for pile_place in pile_places:
        window.blit(card_image, pile_place)
    pygame.display.update()

    return window

def play_game(window, player1, player2, deck):
    turn = 1
    beverbende = 0
    while not beverbende:
        played = 0
        while not played:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 550 <= event.pos[0] <= 675 and 250 <= event.pos[1] <= 436:
                        print('player '+str(turn)+' played')
                        card = deck.draw_card()
                        if turn == 1:
                            placed = player1.play(card)
                        else:
                            placed = player2.play(card)
                        if not placed:
                            window.blit(card_images[card.value], (400, 257))
                        played = 1

        # change turns
        if turn == 1: turn = 2
        else: turn = 1

        # update screen
        card_places = [(50, 50), (200, 50), (50, 450), (200, 450)]
        cards = [player1.get_card1(), player1.get_card2(), player2.get_card1(), player2.get_card2()]
        for i in range(0, 4):
            window.blit(card_images[cards[i].value], card_places[i])

        window.fill((220, 220, 220), (141, 15, 150, 35))
        window.fill((220, 220, 220), (141, 415, 150, 35))
        if turn == 1:
            text = font_bolt.render('Player 1', True, (0, 0, 0))
            window.blit(text, (141, 15))
            text = font.render('Player 2', True, (0, 0, 0))
            window.blit(text, (141, 415))
        else:
            text = font_bolt.render('Player 2', True, (0, 0, 0))
            window.blit(text, (141, 415))
            text = font.render('Player 1', True, (0, 0, 0))
            window.blit(text, (141, 15))
        pygame.display.update()



if __name__ == "__main__":
    deck = Deck()
    card1 = deck.draw_card(); card2 = deck.draw_card(); card3 = deck.draw_card(); card4 = deck.draw_card()
    player1 = Player(card1, card2)
    player2 = Player(card3, card4)
    window = init_game_env(player1, player2)
    play_game(window, player1, player2, deck)



