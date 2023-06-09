---
layout: home
title: "Home"
order: 8

---

Final project of the course Logical Aspects of Multi Agent Systems. Created by Sanne Berends (s3772950), Julia Boers 
(s3632644) and Anniek Theuwissen (s3764818).

# Introduction
For this project, a simplified version of the game 'Beverbende'[^1] was modelled using epistemic logic for the strategy of 
the players. Beverbende is a simple Dutch game, where players have 4 cards each, and their goal is to minimize the total 
worth of their cards. During the game they can interchange their cards with cards from a deck. When they think their total 
card worth is lower than that of other players, they say 'Bever' and the game ends. We propose the use of a Kripke model 
to show the knowledge in the game, to guide the decision for a player to call 'Bever'. The Kripke model is updated after 
public announcements, which will be detailed later. The aim of this project is to examine whether with the use of the 
Kripke model, a player can be certain to win when it calls 'Bever'.

This report contains the rules of the original game, the simplifications that were made, details about the implementation, 
the formal modal, an example run and finally a discussion.

![Beverbende game, taken from https://www.intertoys.nl/beverbende](/images/beverbende_overview.jpeg)

*Figure taken from [here](https://www.intertoys.nl/beverbende) .*

[^1]: 999Games (2009). Beverbende, [https://www.999games.nl/beverbende.html](https://www.999games.nl/beverbende.html)