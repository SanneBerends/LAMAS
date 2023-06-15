# Partly taken from https://github.com/erohkohl/mlsolver

""" Beverbende

Module contains data model for Beverbende game as Kripke structure and agents announcements as modal logic
formulas
"""

from mlsolver.kripke import KripkeStructure, World
from mlsolver.formula import Atom, And, Not, Or, Box_a, Box_star


class Beverbende:
    """
    Class models the Kripke structure of the Beverbende game.
    """
    card_values = 5  # number of different card-values, so if this is 2 the values of the cards are 0 and 1

    def __init__(self, current_world, agent):
        self.current_world = current_world

        # fill worlds and relationships per agent
        worlds = self.fill_worlds(agent)
        relations = self.fill_relations(worlds, agent)
        relations.update(add_reflexive_edges(worlds, relations))

        self.ks = KripkeStructure(worlds, relations)
        self.current_world = current_world

    def fill_worlds(self, agent):
        worlds = []

        if agent == 1:
            for card3 in range(0, self.card_values):
                for card4 in range(0, self.card_values):
                    index = self.current_world[0] + self.current_world[1] + \
                            str(card3) + str(card4)
                    cards = {f'p2_1:{card3}': True, f'p2_2:{card4}': True}

                    worlds.append(World(index, cards))
        elif agent == 2:
            for card1 in range(0, self.card_values):
                for card2 in range(0, self.card_values):
                    index = str(card1) + str(card2) + \
                            self.current_world[2] + self.current_world[3]
                    cards = {f'p1_1:{card1}': True, f'p1_2:{card2}': True}

                    worlds.append(World(index, cards))

        return worlds

    def fill_relations(self, worlds, agent):
        relations = {}
        relations_set = set()
        for world in worlds:
            for reachable_world in worlds:
                if agent == 1:
                    if world.name[:2] == reachable_world.name[:2]:
                        relations_set.add((world.name, reachable_world.name))
                elif agent == 2:
                    if world.name[-2:] == reachable_world.name[-2:]:
                        relations_set.add((world.name, reachable_world.name))
        relations[agent] = relations_set
        return relations

    def obtain_knowledge(self, knowledge_base, type, player, card1, card2, discard=None, deck_card=None):
        # delete knowledge from knowledge_base if needed
        for (i,item) in knowledge_base:
            if type == 1 or type == 3:
                if i == 1:
                    knowledge_base.remove((i,item))
            if type == 2 or type == 4:
                if i == 2:
                    knowledge_base.remove((i, item))

        # add everywhere options with higher values
        if type == 1:  # card from discard: replaces card1
            # card1 known: cards1 larger than discard removed
            if player == 1:
                knowledge_base.append((1,Box_star((Atom(f'p{player}_1:{discard}')))))
            else:
                knowledge_base.append((1,Box_star((Atom(f'p{player}_1:{discard}')))))
            # card2 <= card1 (old): cards2 larger than card1 removed
            for i in range(card1 + 1, self.card_values):
                if player == 1:
                    knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_2:{i}')))))
                else:
                    knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_2:{i}')))))

        elif type == 2:  # card from discard: replaces card2
            # card2 known: card2 larger than discard removed
            if player == 1:
                knowledge_base.append((2,Box_star((Atom(f'p{player}_2:{discard}')))))
            else:
                knowledge_base.append((2,Box_star((Atom(f'p{player}_2:{discard}')))))
            # card1 <= card2 (old): cards1 larger than card2 removed
            for i in range(card2 + 1, self.card_values):
                if player == 1:
                    knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_1:{i}')))))
                else:
                    knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_1:{i}')))))

        elif type == 3:  # card from deck: replaces card1
            # new card1 < card1
            for i in range(card1, self.card_values):
                if player == 1:
                    knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_1:{i}')))))
                else:
                    knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_1:{i}')))))
            # card2 <= card1 (old)
            for i in range(card1 + 1, self.card_values):
                if player == 1:
                    knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_2:{i}')))))
                else:
                    knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_2:{i}')))))
            # card1 <= discard
            for i in range(discard + 1, self.card_values):
                if player == 1:
                    knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_1:{i}')))))
                else:
                    knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_1:{i}')))))
            # card2 <= discard
            for i in range(discard + 1, self.card_values):
                if player == 1:
                    knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_2:{i}')))))
                else:
                    knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_2:{i}')))))

        elif type == 4:  # card from deck: replaces card2
            # new card2 < card2
            for i in range(card2, self.card_values):
                if player == 1:
                    knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_2:{i}')))))
                else:
                    knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_2:{i}')))))
            # card1 <= card2
            for i in range(card2 + 1, self.card_values):
                if player == 1:
                    knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_1:{i}')))))
                else:
                    knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_1:{i}')))))
            # card1 <= discard and card2 <= discard
            for i in range(discard + 1, self.card_values):
                if player == 1:
                    knowledge_base.append(
                        (0,Box_star(And(Not(Atom(f'p{player}_1:{i}')), Not(Atom(f'p{player}_2:{i}'))))))
                else:
                    knowledge_base.append(
                        (0,Box_star(And(Not(Atom(f'p{player}_1:{i}')), Not(Atom(f'p{player}_2:{i}'))))))

        elif type == 5:  # card from deck: discards this deck_card
            # c1 <= discard and c2 <= discard
            for i in range(discard + 1, self.card_values):
                if player == 1:
                    knowledge_base.append(
                        (0,Box_star(And(Not(Atom(f'p{player}_1:{i}')), Not(Atom(f'p{player}_2:{i}'))))))
                else:
                    knowledge_base.append(
                        (0,Box_star(And(Not(Atom(f'p{player}_1:{i}')), Not(Atom(f'p{player}_2:{i}'))))))
            # c1 <= new_discard and c2 <= new_discard
            for i in range(deck_card + 1, self.card_values):
                if player == 1:
                    knowledge_base.append(
                        (0,Box_star(And(Not(Atom(f'p{player}_1:{i}')), Not(Atom(f'p{player}_2:{i}'))))))
                else:
                    knowledge_base.append(
                        (0,Box_star(And(Not(Atom(f'p{player}_1:{i}')), Not(Atom(f'p{player}_2:{i}'))))))

        # new current worlds
        if player == 1:
            if type == 1:
                self.current_world = f'{discard}' + self.current_world[1] + self.current_world[2] + self.current_world[
                    3]
            elif type == 2:
                self.current_world = self.current_world[0] + f'{discard}' + self.current_world[2] + self.current_world[
                    3]
            elif type == 3:
                self.current_world = f'{deck_card}' + self.current_world[1] + self.current_world[2] + \
                                     self.current_world[3]
            elif type == 4:
                self.current_world = self.current_world[0] + f'{deck_card}' + self.current_world[2] + \
                                     self.current_world[3]
        elif player == 2:
            if type == 1:
                self.current_world = self.current_world[0] + self.current_world[1] + f'{discard}' + self.current_world[
                    3]
            elif type == 2:
                self.current_world = self.current_world[0] + self.current_world[1] + self.current_world[
                    2] + f'{discard}'
            elif type == 3:
                self.current_world = self.current_world[0] + self.current_world[1] + f'{deck_card}' + \
                                     self.current_world[3]
            elif type == 4:
                self.current_world = self.current_world[0] + self.current_world[1] + self.current_world[
                    2] + f'{deck_card}'
        return knowledge_base


def add_reflexive_edges(worlds, relations):
    """Routine adds reflexive edges to Kripke frame
    """
    result = {}
    for agent, agents_relations in relations.items():
        result_agents = agents_relations.copy()
        for world in worlds:
            result_agents.add((world.name, world.name))
            result[agent] = result_agents
    return result

###### TO TEST THE PUBLIC ANNOUNCEMENT ##########
#################################################
# beverbende = Beverbende('1111')
# print("ks1: ", beverbende.ks_1)
# print("\n")
# print("\n")
# print("ks2: ", beverbende.ks_2)
# print("\n")
# print("----\n")
# print("\n")
# beverbende.public_announcement(1,1,1,1)
# print("ks1: ", beverbende.ks_1)
# print("ks2: ", beverbende.ks_2)
# print("\n")
# beverbende.public_announcement(2,2,1,1,0,0)
# print("ks1: ", beverbende.ks_1)
# print("ks2: ", beverbende.ks_2)
# print("\n")
