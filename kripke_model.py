# Partly taken from https://github.com/erohkohl/mlsolver

""" Beverbende

Module contains data model for Beverbende game as Kripke strukture and agents announcements as modal logic
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
        # relations.update(add_symmetric_edges(relations))

        self.ks = KripkeStructure(worlds, relations)
        self.current_world = current_world

    def fill_worlds(self):
        worlds = []
        for card1 in range(0, 5):
            for card2 in range(0, 5):
                for card3 in range(0, 5):
                    for card4 in range(0, 5):
                        index = str(card1) + str(card2) + \
                            str(card3) + str(card4)
                        cards = {f'p1_1:{card1}': True, f'p1_2:{card2}': True,
                                 f'p2_1:{card3}': True, f'p2_2:{card4}': True}
                        worlds.append(World(index, cards))
        return worlds
    
    def fill_relations(self, worlds):
        relations = {}
        for key in range(1,3):
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

def add_symmetric_edges(relations):
    """Routine adds symmetric edges to Kripke frame
    """
    result = {}
    for agent, agents_relations in relations.items():
        result_agents = agents_relations.copy()
        for r in agents_relations:
            x, y = r[1], r[0]
            result_agents.add((x, y))
        result[agent] = result_agents
    return result


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