---
layout: page
title: "Formal Model"
permalink: /formal_model/
order: 4
---
For an agent to be certain that it has a lower sum of points on its own cards than that the opponent has, the agents make use of a Kripke model. The Kripke model is defined as: 
$M = <S, \pi, R_1, R_2 >$ where 
- $ S = \{s_1, s_2, ... s_{625}\}$
- $\pi$ is defined as follows: 
  - $\pi (s_i) (p1\_1 = a)=\textbf{t}$ if player 1 has as card 1 a card valued $a$ in $s_i$.
  -  $\pi (s_i)(p1\_2 = a) =\textbf{t}$ if player 1 has as card 2 a card valued $a$ in $s_i$.
  - $ \pi(s_i)(p2\_1 = a)  =\textbf{t}$ if player 2 has as card 1 a card valued $a$ in $s_i$.
  - $ \pi(s_i) (p2\_2 = a) =\textbf{t}$ if player 2 has as card 2 a card valued $a$ in $s_i$.
- $R_1$ is defined as follows: 
    $(s_i,s_j) \in R_1$ iff
  - $s_i==s_j$, or 
  - For each $a \in \{0,1,2,3,4\}$ and $b \in \{0,1,2,3,4\}$, \\$\pi (s_i) (p1\_1 = a)=\textbf{t}$ iff $\pi (s_j)(p1\_1 = a) =\textbf{t}$, and \\$\pi (s_i)(p1\_2 = b) =\textbf{t}$ iff $\pi (s_j) (p1\_2 = b) =\textbf{t}$. \\
    (Worlds are connected by $R_1$ when player 1 has the same cards in both worlds.)
- $R_2$ is defined as follows: 
    $(s_i,s_j) \in R_2$ iff
  - $s_i==s_j$, or 
  - For each $a \in \{0,1,2,3,4\}$ and $b \in \{0,1,2,3,4\}$, \\$\pi (s_i) (p2\_1 = a)=\textbf{t}$ iff $\pi (s_j)(p2\_1 = a) =\textbf{t}$, and \\$\pi (s_i)(p2\_2 = b) =\textbf{t}$ iff $\pi (s_j) (p2\_2 = b) =\textbf{t}$. \\
    (Worlds are connected by $R_2$ when player 2 has the same cards in both worlds.)

## Obtaining knowledge
The Kripke model is updated after each turn. Public announcements affect the worlds and the relations of the model. After a public announcement is made, all worlds in which the contents of the public announcement are not true, are removed from the model. 
