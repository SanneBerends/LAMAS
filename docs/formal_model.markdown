---
layout: page
title: "Formal Model"
permalink: /formal_model/
order: 4
---
## Kripke model
For an agent to be certain that it has a lower sum of points on its own cards than that the opponent has, the agents 
make use of a Kripke model. During the game, the interface does not show the entire Kripke model, due to time complexity
of the visualization. See [Implementation](implementation.markdown) for more information about the interface. The Kripke 
model described in this section is the complete Kripke model. The Kripke model is defined as: 


![Model definition](/images/math/math1.png), where 

- ![States definition](/images/math/math2.png)

- π is defined as follows: 

  - ![pi_p1_1 definition](/images/math/math3.png) if player 1 has as card 1 a card valued *a* in ![s_i](/images/math/math4.png)

  - ![pi_p1_2 definition](/images/math/math5.png) if player 1 has as card 2 a card valued *a* in ![s_i](/images/math/math4.png)

  - ![pi_p2_1 definition](/images/math/math6.png) if player 2 has as card 1 a card valued *a* in ![s_i](/images/math/math4.png)

  - ![pi_p2_2 definition](/images/math/math7.png) if player 2 has as card 2 a card valued *a* in ![s_i](/images/math/math4.png)

- ![R_1](/images/math/math8.png) is defined as follows:
    ![s_i=s_j in R_1](/images/math/math9.png) iff

  - ![s_i==s_j](/images/math/math10.png), or 

  - For each ![a in range [0,4]](/images/math/math11.png) and ![b in range [0,4]](/images/math/math12.png) \
  ![pi_p1_1 definition](/images/math/math3.png) iff ![pi_p1_1 definition for s_j](/images/math/math13.png)  and \
  ![pi_p1_2 definition](/images/math/math14.png) iff ![pi_p1_2 definition for s_j](/images/math/math15.png) 

  (Worlds are connected by ![R_1](/images/math/math8.png) when player 1 has the same cards in both worlds.)

- ![R_2](/images/math/math16.png) is defined as follows:
    ![s_i=s_j in R_2](/images/math/math17.png) iff

  - ![s_i==s_j](/images/math/math10.png), or 

  - For each ![a in range [0,4]](/images/math/math11.png) and ![b in range [0,4]](/images/math/math12.png)  
  ![pi_p2_1 definition](/images/math/math6.png) iff ![pi_p2_1 definition for s_j](/images/math/math18.png) and \
  ![pi_p2_2 definition](/images/math/math19.png) iff ![pi_p2_2 definition for s_j](/images/math/math20.png) 

  (Worlds are connected by ![R_2](/images/math/math16.png) when player 2 has the same cards in both worlds.)

## Obtaining knowledge
After each turn, the Kripke model is updated. Each scenario that can happen during a turn corresponds to one or more 
public announcements that are made. These public announcements affect the worlds and relations of the Kripke model: all worlds
in which the contents of the public announcement are not true, are removed from the model. The section [Implementation](implementation.markdown)
contains a more intuitive and less formal description of the public announcements.

### Initialization
Initially a player (![p_1](/images/math/math21.png)) has information about the value of its opponent's (![p_2](/images/math/math22.png)) cards. Since the cards can range from 0 to 4, 
the agent considers it possible that the opponent has a 0, 1, 2, 3 or 4 for card 1: 
![inital M knowledge card 1](/images/math/math23.png)![inital M knowledge card 1, part 2](/images/math/math24.png)\
The same holds for card 2 of the opponent:\
![inital M knowledge card 2](/images/math/math25.png)![inital M knowledge card 2, part 2](/images/math/math26.png)\
The player knows that the opponent's cards must both be either one of the five value options, so also:\
![inital K knowledge card 1](/images/math/math27.png) \
and \
![inital K knowledge card 2](/images/math/math28.png) \
In other words: a player is certain that both of the opponent's cards are in the range [0,4].

### Public announcement scenario 1
In scenario 1, the opponent replaces one of its cards with a visible card 
from the discard pile. Both players can see the value of this new card, so it can be considered a public announcement
that e.g. card 1 of player 2 now has a value of *n*, where *n* is the value of the card taken from the discard pile.\
Logically, this can be written as: \
![scenario 1 announcement](/images/math/math29.png), where *a* is 1 in the example, and *n* is the value of the new card. \
After this public announcement, it is common knowledge that player 2 has as card *a*, a card with value *n*:\
![scenario 1 C](/images/math/math30.png)\
The Kripke model is updated by removing all wolds with ![scenario 1 worlds removed](/images/math/math31.png).  So the 
possible value range [0,4] of card *a* is updated to [*n*,*n*].

### Public announcement scenario 2
In scenario 2, the opponent picks a card from the deck and replaces one of its own cards with this card. The card the opponent
then places on the discard pile can be seen as a public announcement. The opponent announces that the new card has a value
lower than the value of the discarded card (*d*). Logically, this can be written as:\
![scenario 2 announcement](/images/math/math32.png), where *a* is the index of which card was replaced and ![scenario 2 n_i<d](/images/math/math33.png). \
After this public announcement, it is common knowledge that player 2 has a card with a value ![scenario 2 n_i<d](/images/math/math33.png): \
![scenario 2 C](/images/math/math34.png).\
The Kripke model is updated by removing all worlds with ![scenario 2 worlds removed](/images/math/math35.png), where ![scenario 2 M>=d](/images/math/math36.png). So the upper bound of the possible
value range of card *a* [0,4] is updated to [0,*d-1*].

### Public announcement scenario 3
In scenario 3, which applies both in scenario 1 and 2, the opponent replaces one of its cards by another card. This
gives additional information about the card that was not replaced, since always the card with the highest value is chosen
to be replaced. It is therefore publicly announced that the non-replaced card has a value lower than or equal to the
discarded card (*d*). Logically, this can be written as:\
![scenario 3 announcement](/images/math/math37.png), where *b* is the index of the card that was not replaced, and 
![scenario 3 n_i<=d](/images/math/math38.png). \
After this public announcement, it is common knowledge that player 2 has a non-replaced card with a value ![scenario 3 n_i<=d](/images/math/math38.png):\
![scenario 2 C](/images/math/math39.png).\
The Kripke model is updated by removing all worlds with ![scenario 3 worlds removed](/images/math/math40.png), where *m* > *d*. So the upper bound of the possible
value range [0,4] of card *b* is updated to [0,*d*].

### Public announcement scenario 4
In scenario 4, the opponent picks a card from the deck but does not replace one of its own cards. This can be seen as
a public announcement that both cards of the opponent have a value smaller or equal to the deck card  that is directly
discarded (*d*). Logically, this can be written as:\
![scenario 4 announcement](/images/math/math41.png) ![scenario 4 announcement part 2](/images/math/math42.png),
where ![scenario 4 n_i<=d](/images/math/math38.png). \
After this public announcement, it is common knowledge that player 2 has two cards with a value ![scenario 4 n_i<=d](/images/math/math38.png):\
![scenario 4 C](/images/math/math43.png)![scenario 4 C part 2](/images/math/math44.png).\
The Kripke model is updated by removing all worlds with ![scenario 4 worlds removed](/images/math/math45.png) 
and all worlds with ![scenario 4 worlds removed part 2](/images/math/math46.png),
where *m* > *d*. So the upper bound of the possible value range [0,4] of both cards is updated to [0,*d*].

### Public announcement scenario 5
In scenario 5, which applies both in scenario 2 and 4, the opponent decides to pick a card from the deck. This shows that
the card on the discard pile (*d*) was lower than or equal to the values of both of the opponent's cards. This can
be seen as a public announcement:\
![scenario 5 C](/images/math/math47.png)![scenario 5 C part 2](/images/math/math48.png)
where ![scenario 5 n_i<=d](/images/math/math38.png).\
Note that the difference with scenario 4 is that here *d* represents the card from the discard pile, and in scenario 4 *d*
was the deck card.\
After this public announcement, it is common knowledge that player 2 has two cards with a value ![scenario 5 n_i<=d](/images/math/math38.png):\
![scenario 5 C](/images/math/math49.png)![scenario 5 C part 2](/images/math/math50.png)\
The Kripke model is updated by removing all worlds with ![scenario 4 worlds removed](/images/math/math45.png) and all worlds with 
![scenario 4 worlds removed part 2](/images/math/math46.png), where *m* > *d*. So the upper bound of the possible value 
range [0,4] of both cards is updated to [0,*d*].

## Calling Bever
The number of worlds in the Kripke model decreases as the game progresses. The game ends when a player can call 'Bever'. 
This is the case when in all wolds that the player can reach in the Kripke model, its sum of card values is lower
than that of the opponent.