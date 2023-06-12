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

    knowledge_base = []

    def __init__(self, current_world):
        worlds = self.fill_worlds()
        relations = self.fill_relations(worlds)

        relations.update(add_reflexive_edges(worlds, relations))

        self.ks = KripkeStructure(worlds, relations)
        self.current_world = current_world

    def fill_worlds(self):
        worlds = []
        for card1 in range(0, 2):
            for card2 in range(0, 2):
                for card3 in range(0, 2):
                    for card4 in range(0, 2):
                        index = str(card1) + str(card2) + \
                            str(card3) + str(card4)
                        cards = {f'p1_1:{card1}': True, f'p1_2:{card2}': True,
                                 f'p2_1:{card3}': True, f'p2_2:{card4}': True}
                        worlds.append(World(index, cards))
        return worlds

    def fill_relations(self, worlds):
        relations = {}
        for key in range(1, 3):
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

    def public_announcement(self, type, player, card1, card2, discard=None, deck_card=None):
        #add everywhere options with higher values
        if type == 1: #card from discard: replaces card1
            #card1 known: card1 larger than card1 removed
            for i in range (discard+1, 2):
                self.ks = self.ks.solve(Box_star(Not(Atom(f'p{player}_1:{i}'))))
            #card2 <= card1 (old): cards2 larger than card1 removed
            for i in range(card1+1, 2):
                self.ks = self.ks.solve(Box_star(Not(Atom(f'p{player}_2:{i}'))))

        elif type == 2:  # card from discard: replaces card2
            # card2 known: card2 larger than card2 removed
            for i in range(discard+1, 2):
                self.ks = self.ks.solve(
                    Box_star(Not(Atom(f'p{player}_2:{i}'))))
            # card1 <= card2 (old): cards1 larger than card2 removed
            for i in range(card2+1, 2):
                self.ks = self.ks.solve(
                    Box_star(Not(Atom(f'p{player}_1:{i}'))))

        elif type == 3:  # card from deck: replaces card1
            # new card1 < card1
            for i in range(card1, 2):
                self.ks = self.ks.solve(
                    Box_star(Not(Atom(f'p{player}_1:{i}'))))
            #card2 <= card1 (old)
            for i in range(card1+1, 2):
                self.ks = self.ks.solve(
                    Box_star(Not(Atom(f'p{player}_2:{i}'))))
            #c1 <= discard
            for i in range(discard+1, 2):
                self.ks = self.ks.solve(
                    Box_star(Not(Atom(f'p{player}_1:{i}'))))
            #c2 <= discard
            for i in range(discard+1, 2):
                self.ks = self.ks.solve(Box_star(Not(Atom(f'p{player}_2:{i}'))))

        elif type == 4:  # card from deck: replaces card2
            # new card2 < card2
            for i in range(card2, 2):
                self.ks = self.ks.solve(
                    Box_star(Not(Atom(f'p{player}_2:{i}'))))
            #card1 <= card2
            for i in range(card2+1, 2):
                self.ks = self.ks.solve(
                    Box_star(Not(Atom(f'p{player}_1:{i}'))))
            #c1 <= discard and c2 <= discard
            for i in range(discard+1, 2):
                self.ks = self.ks.solve(
                    Box_star(And(Not(Atom(f'p{player}_1:{i}')), Not(Atom(f'p{player}_2:{i}')))))

        elif type == 5:  # card from deck: discards this deck_card
            # c1 <= discard and c2 <= discard
            for i in range(discard+1, 2):
                self.ks = self.ks.solve(
                    Box_star(And(Not(Atom(f'p{player}_1:{i}')), Not(Atom(f'p{player}_2:{i}')))))
            # c1 <= new_discard and c2 <= new_discard
            for i in range(deck_card+1, 2):
                self.ks = self.ks.solve(
                    Box_star(And(Not(Atom(f'p{player}_1:{i}')), Not(Atom(f'p{player}_2:{i}')))))


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
# print(beverbende.ks)
# print("\n")
# beverbende.public_announcement(1,1,1,1,0,0)
# print(beverbende.ks)
# print("\n")
# beverbende.public_announcement(2,2,1,1,0,None,0)
# print(beverbende.ks)
# print("\n")
# beverbende.public_announcement(4,1,0,1,1,None,0,0)
# print(beverbende.ks)
# print("\n")
# beverbende.public_announcement(3,2,1,0,1,0)
# print(beverbende.ks)
