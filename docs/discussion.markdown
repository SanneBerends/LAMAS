---
layout: page
title: "Discussion"
permalink: /discussion/
order: 7
---
This website describes the game Beverbende, which simplifications we made to the game rules, how we implemented the 
game, the logic behind the game (i.e. the formal model) and an example run. In the traditional game, it is always a 
guess whether it is the right time to call ‘Bever’. The aim of the project was to find out whether keeping track of 
all possible worlds allows a player to be certain that it will win if it calls ‘Bever’. The Kripke model guides the 
decision of the player to call ‘Bever’: if in all reachable worlds of a player, the player has a lower sum of card value than its 
opponent, it calls ‘Bever’.

As can be seen in the example run ([Example](example.markdown)), the Kripke model does add valuable knowledge to the game. The run that is shown is 
an example of a game in which the Kripke model allows the player to be certain to win and guides its decision to call 
`Bever’. The conclusion is therefore that in some games, keeping track of all possible worlds in a Kripke model is a 
useful tool to win the game.

However, there are some limitations. As we saw in the obtaining knowledge section of the [Formal Model](formal_model.markdown) section, the 
Kripke model is used to deduce a range of possible card value sums of the opponent. After every public announcement, 
this range can be updated. We saw that there is just one scenario in which the lower bound of this range is updated, 
namely in the case that the opponent picks a card from the discard pile. This is unfortunate, since the lower bound 
of the range is what is needed to know if the player can safely call ‘Bever’. Therefore, the Kripke model does not add 
valuable knowledge in all games, just in those where the opponent happens to pick a card from the discard pile.

Furthermore, ‘Bever’ can only be called based on the Kripke model if the cards of the player are lower to those of 
the opponent. In our simplified game with just four card values, there are also games in which the card values of the 
players are too similar for any of the two to call ‘Bever’. In the original game, this problem would decrease, since 
the differences in card values between players are usually larger.

To conclude: we saw that the use of a Kripke model and public announcements to update this model can guide the 
strategy of a player playing Beverbende. In some cases, the model allows the player to determine when to call ‘Bever’,
and win the game. In some other cases however, the model does not add enough valuable knowledge to change the course 
of the game, and neither of the players will call ‘Bever’, unless they take a guess.
