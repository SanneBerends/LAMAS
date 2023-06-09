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

    def __init__(self):
        worlds = self.fill_worlds()

        worlds = [
            World('1111', {'1:1': True, '2:1': True,
                  '3:1': True, '4:1': True}),
            World('1011', {'1:1': True, '2:0': True,
                  '3:1': True, '4:1': True}),
            World('0111', {'1:0': True, '2:1': True,
                  '3:1': True, '4:1': True}),
            World('0011', {'1:0': True, '2:0': True,
                  '3:1': True, '4:1': True}),
            World('1110', {'1:1': True, '2:1': True,
                  '3:1': True, '4:0': True}),
            World('1010', {'1:1': True, '2:0': True,
                  '3:1': True, '4:0': True}),
            World('0110', {'1:0': True, '2:1': True,
                  '3:1': True, '4:0': True}),
            World('0010', {'1:0': True, '2:0': True,
                  '3:1': True, '4:0': True}),
            World('1101', {'1:1': True, '2:1': True,
                  '3:0': True, '4:1': True}),
            World('1001', {'1:1': True, '2:0': True,
                  '3:0': True, '4:1': True}),
            World('0101', {'1:0': True, '2:1': True,
                  '3:0': True, '4:1': True}),
            World('0001', {'1:0': True, '2:0': True,
                  '3:0': True, '4:1': True}),
            World('1100', {'1:1': True, '2:1': True,
                  '3:0': True, '4:0': True}),
            World('1000', {'1:1': True, '2:0': True,
                  '3:0': True, '4:0': True}),
            World('0100', {'1:0': True, '2:1': True,
                  '3:0': True, '4:0': True}),
            World('0000', {'1:0': True, '2:0': True,
                  '3:0': True, '4:0': True}),
        ]

        relations = {
            '1': {('1111', '1110'), ('1111', '1101'), ('1111', '1100'), ('1011', '1010'), ('1011', '1001'), ('1011', '1000'),
                  ('0111', '0110'), ('0111', '0101'), ('0111', '0100'), ('0011', '0010'), ('0011', '0001'), ('0011', '0000')},
            '2': {('1111', '1011'), ('1111', '0111'), ('1111', '0011'), ('1110', '1010'), ('1110', '0110'), ('1110', '0010'),
                  ('1101', '1001'), ('1101', '0101'), ('1101', '0001'), ('1100', '1000'), ('1100', '0100'), ('1100', '0000')},
        }

        relations.update(add_reflexive_edges(worlds, relations))
        relations.update(add_symmetric_edges(relations))

        self.ks = KripkeStructure(worlds, relations)

    def fill_worlds(self):
        worlds = []
        for card1 in range(0, 4):
            for card2 in range(0, 4):
                for card3 in range(0, 4):
                    for card4 in range(0, 4):
                        index = str(card1) + str(card2) + \
                            str(card3) + str(card4)
                        cards = {f'1:{card1}': True, f'2:{card2}': True,
                                 f'3:{card3}': True, f'4:{card4}': True}
                        worlds.append(World(index, cards))
        return worlds
    
    def fill_relations(self):
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
