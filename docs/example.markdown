---
layout: page
title: "Example"
permalink: /example/
order: 6
---
To demonstrate the game, this section will show an example run. The real world in a Kripke model is indicated by a green dot.

## Starting position
This is what the game looks like when it starts from the perspective of player 1. Player 1 considers all worlds possible 
where player 1 has value two on card one and value two on card two, and all possible combinations of cards for player 2. 
![starting_position](/images/ex_start.png)
   *This figure shows the starting position of the example run game.*

This is the full Kripke model at the beginning of the game. All worlds are possible. The Kripke model is unreadable, but the 
important thing to note is that all worlds are connected to all other worlds. Reflexive relations are omitted in the drawings.
![kripke1](/images/ex_kripke1.png)
   *This figure shows the complete Kripke model at the start of the game.*

## Turn 1
Player 1 picked the card with value zero from the discard pile since zero is lower than two, and chooses to replace its second card. 
As a result, the Kripke model from the perspective 
of player 1 changes, as player 1 now considers all worlds possible where its own cards have values two and zero and for
player 2 all possible combinations of cards.
![turn1](/images/ex_turn1.png)
   *This figure shows turn 1 of the example game.*

## Situation after turn 1
Player 2 is at play. Player 2 has received the public announcement that was made in turn 1, namely player 1 taking a 
card with value zero from the discard pile and discarding the card with value two. Therefore, player 2 considers all 
worlds possible where player 1 has either cards with values two and zero, or with values one and zero. 

Player 2 knows 
about the zero because that is the card drawn from the discard pile. Player 2 knows that the other card has value 
one or two because if player 1 would have had two times value zero, they would have called 'Bever', and if they would 
have had a card with value three they would have discarded that card in the previous turn, instead of discarding a two.
![sit_after_turn1](/images/ex_after_turn1.png)
   *This figure shows the situation of the game after turn 1.*
 
The complete Kripke model is updated to contain all worlds where card two of player 1 has value zero.
![kripke2](/images/ex_kripke2.png)
   *This figure shows the complete Kripke model after turn 1.*

## Turn 2
Player 2 picks a card from the discard pile with value two. The Kripke model of player 2 is updated accordingly.
![turn2](/images/ex_turn2.png)
   *This figure shows turn 2 of the example game.*

## Situation after turn 2
Player 1 received the public announcement of player 2 discarding a card with value three. It now knows that the second
card of player 2 has a value of two. All worlds where this is not the case are removed, as can be seen in the updated 
Kripke model.
![sit_after_turn2](/images/ex_after_turn2.png)
   *This figure shows the situation of the game after turn 2.*

The full Kripke model is updated as well. Only the worlds are considered where card two of player 1 is a zero and card two
of player 2 is a two.
![kripke3](/images/ex_kripke3.png)
   *This figure shows the complete Kripke model after turn 3.*

## Turn 3
Player 1 is at turn. The card on the discard pile has value three, so they pick a card from the deck. 
It has value two and they discard that on the discard pile straight away, as it is not lower than their current cards.
![turn3](/images/ex_turn3.png)
   *This figure shows turn 3 of the example game.*

## Situation after turn 3
Player 2 received a public announcement that player 1 does not have cards higher than a two. But player 2 already knew 
this, so the complete Kripke model does not change after this turn.
![sit_after_turn3](/images/ex_after_turn3.png)
   *This figure shows the situation of the game after turn 3.*

## Turn 4
Player 2 picks a card with value two from the discard pile, replaces its first card and discards a card with value three.
![turn4](/images/ex_turn4.png)
   *This figure shows turn 4 of the example game.*

## Situation after turn 4
Player 1 has received a public announcement from player 2 picking a card with value two from the discard pile. Player 1 
now knows the sum of cards of player 2, and they know that their own sum is lower.
![sit_after_turn4](/images/ex_after_turn4.png)
   *This figure shows the situation of the game after turn 4.*

![kripke4](/images/ex_kripke4.png)
   *This figure shows the complete Kripke model at after turn 4.*

In all reachable worlds for player 1 the sum of cards of player 1 
(i.e. 2) is lower than the sum of the cards of player 2 (i.e. 4),  player 1 calls 'Bever'.
