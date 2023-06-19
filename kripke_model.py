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

    def __init__(self, current_world, num_cards, agent):
        self.current_world = current_world
        self.card_values = num_cards

        # fill worlds and relationships per agent
        worlds = self.fill_worlds(agent)
        relations = self.fill_relations(worlds, agent)
        relations.update(add_reflexive_edges(worlds, relations))

        self.ks = KripkeStructure(worlds, relations)
        self.current_world = current_world

    def fill_worlds(self, agent):
        """
        Creates all possible worlds for the agent containing all different combinations of values for the cards of the opponent.
        """
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
        """
        Creates all possible relations between the worlds for the agent
        """
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
        '''
        Adds and, if necessary, deletes knowledge from the knowledge base of the agent after a turn of its opponent.
        Returns updated knowledge base
        '''
        # delete knowledge from knowledge_base if information about a specific card changes when replaced by a new card
        for (i,item) in knowledge_base:
            if ((type == 1 or type == 3) and i == 1) or ((type == 2 or type == 4) and i == 2):
                knowledge_base.remove((i,item))

        # add knowledge to knowledge base after a turn of the opponent: there are 5 different types of turns
        if type == 1: # opponent took card from discard pile and replaced this one with its card1
            # card1 of opponent is known
            knowledge_base.append((1,Box_star((Atom(f'p{player}_1:{discard}')))))
            # card2 of opponent is smaller than the previous card1 of opponent
            for i in range(card1 + 1, self.card_values):
                knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_2:{i}')))))

        elif type == 2: # opponent took card from discard pile and replaced this one with its card2
            # card2 of opponent is known
            knowledge_base.append((2,Box_star((Atom(f'p{player}_2:{discard}')))))
            # card1 of opponent is smaller or equal to the previous card2 of opponent
            for i in range(card2 + 1, self.card_values):
                knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_1:{i}')))))

        elif type == 3: # opponent took card from deck and replaced this one with its card1
            # card1 of the opponent is now smaller than the previous card1 of opponent
            for i in range(card1, self.card_values):
                knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_1:{i}')))))
            # card2 of the opponent is smaller of equal to the previous card1 of opponent
            for i in range(card1 + 1, self.card_values):
                knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_2:{i}')))))
            # card1 of the opponent is smaller of equal to the card that was on the discard pile
            for i in range(discard + 1, self.card_values):
                knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_1:{i}')))))
            # card2 of the opponent is smaller or equal to the card that was on the discard pile
            for i in range(discard + 1, self.card_values):
                knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_2:{i}')))))

        elif type == 4:  # opponent took card from deck and replaced this one with its card2
            # card2 of the opponent is now smaller than the previous card2 of opponent
            for i in range(card2, self.card_values):
                knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_2:{i}')))))
            # card1 of the opponent is smaller of equal to the previous card2 of opponent
            for i in range(card2 + 1, self.card_values):
                knowledge_base.append((0,Box_star(Not(Atom(f'p{player}_1:{i}')))))
            # card1 and card2 of the opponent are smaller or equal to the card that was on the discard pile
            for i in range(discard + 1, self.card_values):
                knowledge_base.append(
                    (0,Box_star(And(Not(Atom(f'p{player}_1:{i}')), Not(Atom(f'p{player}_2:{i}'))))))

        elif type == 5:  # opponent took card from deck and discarded this card
            # card1 and card2 of the opponent are smaller or equal to the card that was on the discard pile
            for i in range(discard + 1, self.card_values):
                knowledge_base.append(
                    (0,Box_star(And(Not(Atom(f'p{player}_1:{i}')), Not(Atom(f'p{player}_2:{i}'))))))
            # card1 and card2 of the opponent are smaller or equal to the card that it picked from the deck and discarded
            for i in range(deck_card + 1, self.card_values):
                knowledge_base.append(
                    (0,Box_star(And(Not(Atom(f'p{player}_1:{i}')), Not(Atom(f'p{player}_2:{i}'))))))

        # update current worlds after action taken
        if player == 1:
            cw = list(self.current_world)
            if type == 1 or type == 2:
                cw[type-1] = f'{discard}'
            elif type == 3 or type == 4:
                cw[type-3] = f'{deck_card}'
            self.current_world = "".join(cw)
        elif player == 2:
            cw = list(self.current_world)
            if type == 1 or type == 2:
                cw[type + 1] = f'{discard}'
            elif type == 3 or type == 4:
                cw[type - 1] = f'{deck_card}'
            self.current_world = "".join(cw)

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

