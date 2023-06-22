---
layout: page
title: "Example"
permalink: /example/
order: 6
---
To demonstrate the game, this section will show an example run. The values of the cards range from 0 to 3 instead 
of 0 to 4 because of runtime and more readable Kripke models.

## Starting position
This is what the game looks like when it starts from the perspective of player 1. Player 1 considers all worlds possible 
where player 1 has a value two on card one and a value two on card two, and player 2 has all other possible combinations of cards. 
![starting_position](/images/ex_start.png)
   *This figure shows the starting position of the example run game.*

This is the full Kripke model at the beginning of the game. Both players consider all worlds possible that contain their own cards.
![kripke1](/images/ex_kripke1.png)
   *This figure shows the complete Kripke model at the start of the game.*

## Turn 1
Now player 1 picks the card from the discard pile, as 0 is lower than 2. The Kripke model now changed, as player 1 now considers all worlds possible where they have cards 2, 0 and player 2 has all other possible combinations of cards.
![turn1](/images/ex_turn1.png)
   *This figure shows turn 1 of the example game.*

## Situation after turn 1
Player 2 is at play. Player 2 has received the public announcement that was made in turn 1, namely player 1 taking a 0 from the discard pile and discarding a 2 on the discard pile. Therefore, player 2 considers all worlds possible where player 1 has either cards 2, 0 or 1, 0 (0 because that is the card drawn from the discard pile, 1 or 2 because if player 1 would have had two times 0 they would have called 'Bever', and not a 3 because then in the previous turn player 1 would have discarded the 3).
![sit_after_turn1](/images/ex_after_turn1.png)
   *This figure shows the situation of the game after turn 1.*

![kripke2](/images/ex_kripke2.png)
   *This figure shows the complete Kripke model after turn 1.*

## Turn 2
Player 2 picks a card from the deck. This is a 2. The Kripke model of player 2 is updated accordingly.
![turn2](/images/ex_turn2.png)
   *This figure shows turn 2 of the example game.*

## Situation after turn 2
Player 1 received the public announcement of player 2 discarding a 3. It now does not consider the worlds possible where one of the cards of player 2 is a 3, as can be seen in the updated Kripke model.
![sit_after_turn2](/images/ex_after_turn2.png)
   *This figure shows the situation of the game after turn 2.*

The full Kripke model is updated as well. The relations of player 2 are still the same apart from the own cards of player 2. Player 1 now know the second card of player 2, so it only considers possible the worlds where the first card differs.
![kripke3](/images/ex_kripke3.png)
   *This figure shows the complete Kripke model after turn 3.*

## Turn 3
Player 1 is at turn. The card on the discard pile is a 3, so they pick a card from the deck. It is a 2 and they discard that on the discard pile straight away, as it is not lower than their current cards.
![turn3](/images/ex_turn3.png)
   *This figure shows turn 3 of the example game.*

## Situation after turn 3
Player 2 received a public announcement that player 1 does not have cards higher than a 2. But player 2 already knew this, so the complete Kripke model does not change after this turn.
![sit_after_turn3](/images/ex_after_turn3.png)
   *This figure shows the situation of the game after turn 3.*

## Turn 4
Player 2 picks a 2 from the discard pile and discards a 3.
![turn4](/images/ex_turn4.png)
   *This figure shows turn 4 of the example game.*

## Situation after turn 4
Player 1 has received a public announcement from player 2 picking a 2 from the discard pile. Player 1 now knows the sum of cards of player 2, and they know that their own sum is lower.
![sit_after_turn4](/images/ex_after_turn4.png)
   *This figure shows the situation of the game after turn 4.*

![kripke4](/images/ex_kripke4.png)
   *This figure shows the complete Kripke model at after turn 4.*

Now the sum of cards of player 1 lower than the sum of player 2, therefore player 1 calls 'Bever'.
