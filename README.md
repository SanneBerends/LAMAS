Final project of the course Logical Aspects of Multi Agent Systems. Created by Anniek Theuwissen (s....), Julia Boers (s.....) and Sanne Berends (s3772950)

# Introduction
For this project, a simplified version of the game 'Beverbende' was modelled using epistemic logic for the strategy of the players. Beverbende is a simple Dutch game, where players have 4 cards each, and their goal is to minimize the total worth of their cards. During the game they can interchange their cards with cards from a deck. When they think their total card worth is lower that that of other players, they say 'Bever' and the game ends. We propose the use of a Kripke model to show the knowledge in the game, to guide the decision for a player to call 'Bever'. The Kripke model is updated after public announcements, which will be detailed later. The aim of this project is to examine whether with the use of the Kripke model, a player can be certain to win when it calls 'Bever'. 

This report contains the rules of the original game, the simplifications that were made, details about the implementation, the formal modal, an example run and finally a conclusion.

<!-- 
wat is het spel
wat is het goal van het project -->

# Original game
<!-- uitgebreide uitleg van het spel -->
Beverbende is played with cards that contain 0 to 9 points. The aim of the game is to acquire the lowest sum of points with the four cards that are in front of each player. Each player has four cards, that are laid out face-down on the table in front of them. When the game starts, each player looks at the outer two of their own cards. The rest of the cards are placed face-down in the middle of the table, this is the deck. One card is flipped open next to the deck, this is the discard pile. Then taking turns, each player either takes a closed card from the deck, or an open card from the discard pile, looks at the value without showing the other players, and chooses to switch this card with one of their own. This way, players can reduce their points. When a player is convinced that their cards contain the lowest sum of all players, they say 'Bever'. After that, the other players play one more turn and then all the cards are turned around to count the points.

There are three special cards in the deck, allowing players to view one of their own hidden cards, switch one of their cards with a card of another player (without looking at either of the cards), or take an extra card from the deck if they don't like the card they have drawn the first time.
If, by the time the cards of all players are turned around to reveal the points, players have these special cards in front of them, a card is drawn from the deck to replace that card. 
Games are played with 2 to 6 players. A game consists of four rounds, and the scores are summed at the end to reveal the winner. 

The way to win this game is by keeping track of the cards that are knowable. Obviously, you can know your own cards that you have seen or switched, and you can know cards from the other players if they take open cards from the discard pile. But there are more clues to pay attention to. If a player switches one of their card with a card from the deck, the other players know that the card they drew has a lower point count than the one they discarded. Also, when the special is card played that allows players to switch one of their cards with someone else, the other players can sometimes deduce that a higher-value card is switched for a lower-value card. 

Despite these ways to keep track of cards, after 'Bever' is called by a confident player, the game can still change drastically because all the other players still get to play one round, where a lot can happen. 

# Simplifications of the game
<!-- simplificatie
een plaatje van hoe het eruit ziet -->
In order to model this game using epistemic logic, we simplified the game in a number of ways:

- Two players per game.
- Two cards per player.
- Players can view their own cards throughout the entire game.
- Points on the card go from 0 to 4.
- No special cards.
- Only one round is played per game.
- After 'Bever' is said, the game stops immediately.

We also assume that the players are rational agents, so they only draw cards from the deck or discard pile if this is beneficial to them, meaning that the number of points on that card is lower than the card they are going to switch it with. We also assume no other strategies than reaching the lowest sum of points are used, meaning that no cards are drawn with higher or equal points just to confuse the other player.

# Implementation
van het spel
obtaining knowledge

# Formal model
de logica met Kripke model 
common knowledge (samen met implementation)

# Example 
van een heel spel spelen

# (Experiment en results)

# Discussion
