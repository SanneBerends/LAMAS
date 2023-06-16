---
layout: page
title: "Formal Model"
permalink: /formal_model/
order: 4
---
## Kripke model
For an agent to be certain that it has a lower sum of points on its own cards than that the opponent has, the agents 
make use of a Kripke model. The Kripke model is defined as: 


![Model definition](/images/Model_formula.png), where 

- ![States definition](/images/States_formula.png)

- π is defined as follows: 

  - ![pi_p1_1 definition](/images/pi_p1_1.png) if player 1 has as card 1 a card valued $a$ in $s_i$.

  -  $\pi (s_i)(p1\_2 = a) =\textbf{t}$ if player 1 has as card 2 a card valued $a$ in $s_i$.

  - $ \pi(s_i)(p2\_1 = a)  =\textbf{t}$ if player 2 has as card 1 a card valued $a$ in $s_i$.

  - $ \pi(s_i) (p2\_2 = a) =\textbf{t}$ if player 2 has as card 2 a card valued $a$ in $s_i$.

- $ R_1 $ is defined as follows: 

    $(s_i,s_j) \in R_1$ iff

  - $s_i==s_j$, or 

  - For each $a \in \{0,1,2,3,4\}$ and $b \in \{0,1,2,3,4\}$, $\pi (s_i) (p1\_1 = a)=\textbf{t}$ iff $\pi (s_j)(p1\_1 = a) =\textbf{t}$, and $\pi (s_i)(p1\_2 = b) =\textbf{t}$ iff $\pi (s_j) (p1\_2 = b) =\textbf{t}$. \\

    (Worlds are connected by $R_1$ when player 1 has the same cards in both worlds.)

- $R_2$ is defined as follows: 

    $(s_i,s_j) \in R_2$ iff

  - $s_i==s_j$, or 

  - For each $a \in \{0,1,2,3,4\}$ and $b \in \{0,1,2,3,4\}$, $\pi (s_i) (p2\_1 = a)=\textbf{t}$ iff $\pi (s_j)(p2\_1 = a) =\textbf{t}$, and $\pi (s_i)(p2\_2 = b) =\textbf{t}$ iff $\pi (s_j) (p2\_2 = b) =\textbf{t}$. \\

    (Worlds are connected by $R_2$ when player 2 has the same cards in both worlds.)

## Obtaining knowledge
After each turn, the Kripke model is updated. Each scenario that can happen during a turn corresponds to one or more 
public announcement that is made. These public announcements affect the worlds and relations of the Kripke model: all worlds
in which the contents of the public announcement are not true, are removed from the model. The section [Implementation](implementation.markdown))
contains a more intuitive and less formal description of the public announcements

### Initialization
Initially a player (p1) has information about the value of its opponent's (p2) cards. Since the cards can range from 0 to 4, 
the agent considers it possible that the opponent has a 0, 1, 2, 3 or 4 for card 1: 
M_p1 'p2_1 = 0' and M_p1 'p2_1 = 1' and M_p1 'p2_1 = 2' and M_p1 'p2_1 = 3' M_p1 'p2_1 = 4'.\
The same holds for card 2 of the opponent:\
M_p1 'p2_2 = 0' and M_p1 'p2_2 = 1' and M_p1 'p2_2 = 2' and M_p1 'p2_2 = 3' M_p1 'p2_1 = 4'.\
The player knows that the opponent's cards must both be either one of the five value options, so also:\
K_p1 ('p2_1 = 0' \lor 'p2_1 = 1' \lor 'p2_1 = 2' \lor 'p2_1 = 3' \lor 'p2_1 = 4') \
and \
K_p1 ('p2_2 = 0' \lor 'p2_2 = 1' \lor 'p2_2 = 2' \lor 'p2_2 = 3' \lor 'p2_2 = 4') \
In other words: a player is certain that both of the opponent's cards are in the range [0,4]

### Public announcement scenario 1
In scenario 1, the opponent replaces one of its cards with a visible card 
from the discard pile. Both players can see the value of this new card, so it can be considered a public announcement
that e.g. card 1 of player 2 now has a value of $n$, where n is the value of the card taken from the discard pile.\
Logically, this can be written as: \
['p2_a = n'], where $a$ is 2 in the example, and $n$ is the value of the new card \
After this public announcement, it is common knowledge that player 2 has as card $a$ a card with value $n$:\
C('p2_a = n')\
The Kripke model is updated by removing all wolds with 'p2_a = m', where $m$ > $n$. Worlds where $m$ < $n$ are not removed, since 
in a later turn these (TODO!!) So the possible value range [0,4] of card $a$ is updated to [$n$,$n$].

### Public announcement scenario 2
In scenario 2, the opponent picks a card from the deck and replaces one of its own cards with this card. The card the opponent
then places on the discard pile can be seen as a public announcement. The opponent announces that the new card has a value
lower than the value of the discarded card ($d$). Logically, this can be written as:\
['p2_a = n_1' \lor 'p2_a = n_2' ... \lor 'p2_a = n_m'], where $a$ is the index of which card was replaced and $n_i$ < $d$. \
After this public announcement, it is common knowledge that player 2 has a card with a value $n_i$ < $d$: \
C('p2_a = n_1' \lor 'p2_a = n_2' ... \lor 'p2_a = n_m')\
The Kripke model is updated by removing all worlds with 'p2_a = m', where $m$ \geq $d$. So the upper bound of the possible
value range of card $a$ [0,4] is updated to [0,d-1]

### Public announcement scenario 3
In scenario 3, which applies both in scenario 1 and 2, the opponent replaces one of its cards by another card. This
gives additional information about the card that was not replaced, since always the card with the highes value is chosen
to be replaced. It is therefore publicly announced that the non-replaced card has a value lower than or equal to the
discarded card ($d$). Logically, this can be written as:\
['p2_b = n_1' \lor 'p2_b = n_2' ... \lor 'p2_b = n_m'], where $b$ is the index of the card that was not replaced, and 
$n_i$ \leq $d$. \
After this public announcement, it is common knowledge that player 2 has a non-replaced card with a value $n_i$ \leq $d$:\
C('p2_b = n_1' \lor 'p2_b = n_2' ... \lor 'p2_b = n_m')\
The Kripke model is updated by removing all worlds with 'p2_b = m', where $m$ > $d$. So the upper bound of the possible
value range [0,4] of card $b$ is updated to [0,d].

### Public announcement scenario 4
In scenario 4, the opponent picks a card from the deck but does not replace one of its own cards. This can be seen as
a public announcement that both cards of the opponent have a value smaller or equal to the deck card ($d$) that is directly
discarded. Logically, this can be written as:\
[('p2_1 = n_1' \lor 'p2_1 = n_2' ... \lor 'p2_1 = n_m') \land ('p2_2 = n_1' \lor 'p2_2 = n_2' ... \lor 'p2_2 = n_m')],
where $n_i$ \leq $d$. \
After this public announcement, it is common knowledge that player 2 has two cards with a value $n_i$ \leq $d$:\
C(('p2_1 = n_1' \lor 'p2_1 = n_2' ... \lor 'p2_1 = n_m') \land 'p2_2 = n_1' \lor 'p2_2 = n_2' ... \lor 'p2_2 = n_m'))\
The Kripke model is updated by removing all worlds with 'p2_1 = m' and all worlds with 'p2_2 = m'
where $m$ > $d$. So the upper bound of the possible value range [0,4] of both cards is updated to [0,d].

### Public announcement scenario 5
In scenario 5, which applies both in scenario 2 and 4, the opponent decides to pick a card from the deck. This shows that
the card on the discard pile ($d$) was lower than or equal to the values of both of the opponent's cards. This can
be seen as a public announcement:\
[('p2_1 = n_1' \lor 'p2_1 = n_2' ... \lor 'p2_1 = n_m') \land ('p2_2 = n_1' \lor 'p2_2 = n_2' ... \lor 'p2_2 = n_m')],
where $n_i$ \leq $d$. \ 
Note that the difference with scenario 4 is that here $d$ represents the card from the discard pile, and in scenario 4 $d$ 
was the deck card.\
After this public announcement, it is common knowledge that player 2 has two cards with a value $n_i$ \leq $d$:\
C(('p2_1 = n_1' \lor 'p2_1 = n_2' ... \lor 'p2_1 = n_m') \land 'p2_2 = n_1' \lor 'p2_2 = n_2' ... \lor 'p2_2 = n_m'))\
The Kripke model is updated by removing all worlds with 'p2_1 = m' and all worlds with 'p2_2 = m'
where $m$ > $d$. So the upper bound of the possible value range [0,4] of both cards is updated to [0,d].

## Calling Bever
The number of worlds in the Kripke model decreases as the game progresses. The game ends when a player can call Bever. 
This is the case when in all wolds that the player can reach in the Kripke model, its sum of card values is lower
than that of the opponent.