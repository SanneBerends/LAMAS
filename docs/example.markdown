---
layout: page
title: "Example"
permalink: /example/
order: 6
---
To demonstrate a run of the game, this section will demonstrate an example run. The values of the cards range from 0 to 3.

## Starting position
This is what the game looks like when it starts. Player 1 considers all worlds possible where player 1 has cards 3, 3 and player 2 has all other possible combinations of cards. 
![starting_position](/images/ex_starting_position.png)
   *This figure shows the starting position of the example run game.*

## Turn 1
Now player 1 picks a card from the discard pile, as 0 is lower than 3. The Kripke model now changed, as player 1 now considers all worlds possible where they have cards 3, 0 and player 2 has all other possible combinations of cards.
![turn1](/images/ex_player1_turn1.png)
   *This figure shows turn 1 of the example game.*

## Situation after turn 1
Player 2 is at play. Player 2 has received the public announcement that was made in turn 1, namely player 1 taking a 0 from the discard pile and discarding a 3 on the discard pile. Therefore, player 2 considers all worlds possible where player 1 has either cards 2, 0 or 3, 0 (0 because that is the card drawn from the discard pile, 1, 2 or 3 because if player 1 would have had a 0 they would not have replaced it with a 0, and player 1 would have called 'Bever'.).
![sit_after_turn1](/images/ex_sit_after_turn1.png)
   *This figure shows the situation of the game after turn 1.*

## Turn 2
Player 2 picks a card from the deck. This is a 2. The Kripke model is updated accordingly.
![turn2](/images/ex_turn2.png)
   *This figure shows turn 2 of the example game.*

## Situation after turn 2
Player 1 received the public announcement of player 2 discarding a 3. It now does not considere the worlds possible where one of the cards of player 2 is a 3, as can be seen in the updated Kripke model.
![sit_after_turn2](/images/ex_sit_after_turn2.png)
   *This figure shows the situation of the game after turn 2.*

## Turn 3
Player 1 picks a card from the deck. This is a 0. Now the sum of cards of player 1 is 0 cand player 1 calls 'Bever'.
![bever](/images/ex_bever.png)
   *This figure shows the situation of the game after player 1 calls 'Bever'.*