---
layout: page
title: "Implementation"
permalink: /implementation/
order: 3
---
To model the simplified version of Beverbende, the Python language is used. The Python library Pygame [^1] is used to 
create an interface in which the game can be played. The framework MLsolver [^2] is used to create and update the 
Kripke model during the game. This section explains the implementation details.

## Interface 
The implemented interface is divided into two sections: one for the game and one for the Kripke model (described in [Formal Model](formal_model.markdown)). 
The game side shows the deck, the discard pile, two closed cards for the opponent and two open cards for the player whose turn it is. The
Kripke model that is shown is not the complete Kripke model, but a decreased model, explained in the subsection Strategy.
 ![interface](/images/interface.png)
*This image shows the interface.*

## The agent's actions
The two agents (i.e. the players) are at turn alternately. In an agent's turn, the agent has two options:
- Pick the upper card from the discard pile
- Pick a card from the deck

When picking the upper card from the discard pile, the agent knows the number on the card beforehand. Since all agents 
are rational agents, an agent will only choose this option when the number on this card is lower than the number on one 
of its own cards. When picking a card from the deck, the agent does not know the number on the card beforehand. Picking 
a card from the deck is therefore always a guess. When the card on the discard pile is lower than the number of one of its 
own cards and the agent thus has the option to pick the card from the discard pile, the agent always chooses this safe 
option.

## Strategy
The strategy implemented for the agents is to only call 'Bever' when the agent is certain that it has a lower sum of points 
on its own two cards than the opponent has. To be certain that they can 
call 'Bever', the agents need knowledge about their own cards and about the cards of the opponent. During the game, 
the agents obtain new knowledge after each turn. To keep track of their knowledge, the agents make use of a Kripke 
model. This model keeps track of all possible combinations of cards and is updated after new knowledge is obtained. The 
Kripke model is explained in more detail in the section [Formal Model](formal_model.markdown). However, the 
number of possible worlds is large (256) and the agent only uses a small part of the Kripke model. Therefore, a decreased model
is used by the agent, which is also the model that is shown in the interface. The interface only shows the states that 
are relevant for the agent whose turn it is. This means that only worlds are included where the cards of the agent whose
turn it is are equal to the real values of those cards. This reduces the Kripke model to a model with less worlds, and only
relations for the playing agent, and thus not for the opponent. The section [Example](example.markdown) shows an example
run, including images of both the complete and decreased Kripke model for clarity.


## Obtaining knowledge
As the strategy of the agent relies on their knowledge, the agents have to expand their knowledge during the game. 
The agent obtains knowledge during the opponent's turn. There are multiple scenarios that can happen in which the 
agent obtains knowledge, and they are listed below. The formal definitions of the public announcements induced by the
scenarios can be found in the section [Formal Model](formal_model.markdown).

### Scenario 1
The opponent picks the upper card from the discard pile and replaces one of its own 
cards with this card. In this situation, the agent obtains new knowledge about the cards of the opponent as it can 
see the value of the card that the opponent picks. The agent now knows the value of one of the cards of the opponent. 
   - For example, when the opponent takes a card with value two from the discard pile, the agent knows that the opponent 
   has one card with value two and that the sum of points on the cards of the opponent can range between 2 and 5.
   ![case1](/images/case1.png)
   *This figure shows scenario 1, including the knowledge of the agent about the opponent's cards after the opponent's 
   turn.*

### Scenario 2
The opponent picks a card from the deck and replaces one of its own cards with this card. In this situation, 
the agent also obtains new knowledge about the cards of the opponent. When the opponent 
replaces a card with one of its own cards, the opponent adds its old card that is replaced to the discard pile. The 
agent can see the number on this card and now knows that the opponent replaced this card by a card that is at least 
one value lower. 
   - For example, when the opponent takes a card from the deck and replaces a card with value one by the new card, 
   the agent knows that the new card of the opponent has value zero.
   ![case2](/images/case2.png)
   *This figure shows scenario 2, including the knowledge of the agent about the opponent's cards after the opponent's 
   turn.*

### Scenario 3
In both situations 1 and 2, the opponent replaced a card with one of its own cards. In these situations, 
the agent obtains even more knowledge about the cards of the opponent. The opponent adds its old card that is replaced 
to the discard pile. The agent can see the number on this card. As the opponent is a rational agent, the opponent would 
always replace a picked card with its own highest card (if the two differ in value) as this reduces the sum of points the most. Therefore, the card 
that the opponent adds to the discard pile was the highest card that the opponent had at that moment. These situations,
thus, also give information about the card that the opponent did not replace. 
   - For example, when the opponent replaces 
   one of its cards and discards a card with value three, the agent knows that the highest card of the opponent has at 
   most the value three. The sum of points on the cards of the opponent can therefore range between 0 and 5.
   ![case3](/images/case3.png)
   *This figure shows scenario 3, including the knowledge of the agent about the opponent's cards after the opponent's 
   turn.*

### Scenario 4
The opponent picks a card from the deck but does not replace one of its own cards 
with the picked card. In this situation, the agent still obtains knowledge about the cards of the opponent. When the opponent 
does not replace one of its own cards with the picked card, the opponent adds this card to the discard pile. The agent can 
see the number on this card. As the opponent is a rational agent, the opponent would only not take this card when it 
is not lower than one of its own cards. Therefore, the agent now knows that all cards of the opponent have a lower or 
equal value than the value of the card added to the discard pile. 
   - For example, when the opponent draws a card from the 
   deck with value two and does not replace it with one of its own cards but adds it to the discard pile, the agent knows 
   that all cards of the opponent have a value of at most two. The sum of points on the cards of the opponent can therefore 
   range between 0 and 4.
   ![case4](/images/case4.png)
   *This figure shows scenario 4, including the knowledge of the agent about the opponent's cards after the opponent's 
   turn.*

### Scenario 5
In both situations 2 and 4, the opponent picked a card from the deck. In these situations, the agent obtains even 
more knowledge about the cards of the opponent. When the opponent picks a card from the deck this means that the 
upper card on the discard pile was not beneficial for the opponent. The agent can see the number of the upper card 
on the discard pile. Therefore, the agent knows that both cards of the opponent have a value lower or equal than the 
upper card on the discard pile. 
   - For example, when the card on the discard pile has value two and the opponent picks a 
   card from the deck, the agent knows that all cards of the opponent have a value of two or lower.
   ![case5](/images/case5.png)
   *This figure shows scenario 5, including the knowledge of the agent about the opponent's cards after the opponent's 
   turn.*

### Additional notes
For each action taken by the opponent, the agent obtains knowledge about the cards of the opponent. For each action 
taken by the agent, the opponent obtains knowledge about the cards of the agent in exactly the same way. Therefore, 
the agents can also reason about what knowledge the opponent obtained about the cards of the agent. 
- For example, when
the agent picks a card with value three from the deck and does not replace it with one of its own cards and adds this card
to the discard pile, the opponent knows that all cards of the agent have a value of at most three. Besides, the agent knows
that the opponent knows that all cards of the agent have a value of at most three.

Hence, when one of the agents takes an action, the opponent obtains knowledge by this. Besides, the agent obtains the
knowledge that the opponent obtained this knowledge. Therefore, the agent and the opponent both have this same knowledge.
This means that this knowledge became common knowledge. Each action taken by one of the agents can therefore also be 
described as a public announcement. 


[^1]: Pete Shinners (2011). PyGame - Python Game Development. Retrieved from [http://www.pygame.org](http://www.pygame.org)
[^2]: Modal logic solver (2017). GitHub repository. Retrieved from [https://github.com/erohkohl/mlsolver](https://github.com/erohkohl/mlsolver)

