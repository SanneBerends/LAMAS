import math
import pygame
from mlsolver.kripke import KripkeStructure, World

pygame.init()
font = pygame.font.SysFont('comicsans', 20, False)
font_small = pygame.font.SysFont('comicsans', 10, False)

def fill_worlds(c1_low, c1_high, c2_low, c2_high, c3_low, c3_high, c4_low, c4_high):
    worlds = []
    for card1 in range(c1_low, c1_high):
        for card2 in range(c2_low, c2_high):
            for card3 in range(c3_low, c3_high):
                for card4 in range(c4_low, c4_high):
                    index = str(card1) + str(card2) + \
                            str(card3) + str(card4)
                    cards = {f'p1_1:{card1}': True, f'p1_2:{card2}': True,
                             f'p2_1:{card3}': True, f'p2_2:{card4}': True}
                    worlds.append(World(index, cards))
    return worlds

def fill_relations(worlds):
    relations = {}
    for key in range(2,0,-1):
        relations_set = set()
        for world in worlds:
            for reachable_world in worlds:
                if key == 1:
                    if world.name[:2] == reachable_world.name[:2]:
                        relations_set.add((world.name, reachable_world.name))
                elif key == 2:
                    if world.name[-2:] == reachable_world.name[-2:]:
                        relations_set.add((world.name, reachable_world.name))
        relations[key] = relations_set
    return relations

def draw_kripke(worlds, relations, current_world, draw_names_world=True):
    window = pygame.display.set_mode((1400, 700))
    window.fill((220, 220, 220))

    number_of_worlds = len(worlds)
    drawn_worlds = {}
    for i, world in enumerate(worlds):
        theta = 2 * math.pi * i / number_of_worlds
        radius = 320
        if number_of_worlds == 1:
            x = 700
        else:
            x = 700 + radius * math.cos(theta)
        y = 350 + radius * math.sin(theta)
        if world.name == current_world:
            pygame.draw.circle(window, (0, 128, 0), (x, y), 5)
        else:
            pygame.draw.circle(window, (0, 0, 0), (x, y), 5)
        drawn_worlds[world.name] = (x, y)
        text = font_small.render(world.name, True, (0, 0, 0))
        if x < 700: x -= 25
        if y < 350: y -= 15
        if draw_names_world:
            window.blit(text, (x, y))

    # render relations
    colors = [(220, 20, 60), (0, 0, 128)]
    for agent in relations:
        for relation in relations[agent]:
            pygame.draw.line(window, colors[agent - 1], drawn_worlds[relation[0]], drawn_worlds[relation[1]], 1)

    # render legend
    pygame.draw.circle(window, (220, 20, 60), (1310, 20), 3)
    pygame.draw.circle(window, (0, 0, 128), (1310, 40), 3)
    text = font_small.render('= Player 1', True, (0, 0, 0))
    window.blit(text, (1320, 11))
    text = font_small.render('= Player 2', True, (0, 0, 0))
    window.blit(text, (1320, 31))

    pygame.display.update()
    pygame.time.wait(10000)


if __name__ == "__main__":
    #initial model
    worlds = fill_worlds(0,4,0,4,0,4,0,4)
    relations = fill_relations(worlds)
    current_world = "2233"

    draw_kripke(worlds, relations, current_world, False)

    #after turn1
    worlds = fill_worlds(0,4,0,1,0,4,0,4)
    relations = fill_relations(worlds)
    current_world = "2033"

    draw_kripke(worlds, relations, current_world)

    #after turn2
    worlds = fill_worlds(0, 4, 0, 1, 0, 4, 2, 3)
    relations = fill_relations(worlds)
    current_world = "2032"

    draw_kripke(worlds, relations, current_world)

    #after turn3: nothing changed
    worlds = fill_worlds(0, 4, 0, 1, 0, 4, 2, 3)
    relations = fill_relations(worlds)
    current_world = "2032"

    draw_kripke(worlds, relations, current_world)

    #after turn4
    worlds = fill_worlds(0, 4, 0, 1, 2, 3, 2, 3)
    relations = fill_relations(worlds)
    current_world = "2022"

    draw_kripke(worlds, relations, current_world)