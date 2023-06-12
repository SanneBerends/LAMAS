---
layout: page
title: "Formal Model"
permalink: /formal_model/
order: 4
---
For an agent to be certain that it has a lower sum of points on its own cards than that the opponent has, the agents make use of a Kripke model. The Kripke model is defined as: 

![Kripke model](/images/Kripke.png)

[//]: # ($M = <S, \pi, R_1, R_2 >$ where )

[//]: # (- $ S = \{s_1, s_2, ... s_{625}\}$)

[//]: # (- $\pi$ is defined as follows: )

[//]: # (  - $\pi &#40;s_i&#41; &#40;p1\_1 = a&#41;=\textbf{t}$ if player 1 has as card 1 a card valued $a$ in $s_i$.)

[//]: # (  -  $\pi &#40;s_i&#41;&#40;p1\_2 = a&#41; =\textbf{t}$ if player 1 has as card 2 a card valued $a$ in $s_i$.)

[//]: # (  - $ \pi&#40;s_i&#41;&#40;p2\_1 = a&#41;  =\textbf{t}$ if player 2 has as card 1 a card valued $a$ in $s_i$.)

[//]: # (  - $ \pi&#40;s_i&#41; &#40;p2\_2 = a&#41; =\textbf{t}$ if player 2 has as card 2 a card valued $a$ in $s_i$.)

[//]: # (- $ R_1 $ is defined as follows: )

[//]: # (    $&#40;s_i,s_j&#41; \in R_1$ iff)

[//]: # (  - $s_i==s_j$, or )

[//]: # (  - For each $a \in \{0,1,2,3,4\}$ and $b \in \{0,1,2,3,4\}$, $\pi &#40;s_i&#41; &#40;p1\_1 = a&#41;=\textbf{t}$ iff $\pi &#40;s_j&#41;&#40;p1\_1 = a&#41; =\textbf{t}$, and $\pi &#40;s_i&#41;&#40;p1\_2 = b&#41; =\textbf{t}$ iff $\pi &#40;s_j&#41; &#40;p1\_2 = b&#41; =\textbf{t}$. \\)

[//]: # (    &#40;Worlds are connected by $R_1$ when player 1 has the same cards in both worlds.&#41;)

[//]: # (- $R_2$ is defined as follows: )

[//]: # (    $&#40;s_i,s_j&#41; \in R_2$ iff)

[//]: # (  - $s_i==s_j$, or )

[//]: # (  - For each $a \in \{0,1,2,3,4\}$ and $b \in \{0,1,2,3,4\}$, $\pi &#40;s_i&#41; &#40;p2\_1 = a&#41;=\textbf{t}$ iff $\pi &#40;s_j&#41;&#40;p2\_1 = a&#41; =\textbf{t}$, and $\pi &#40;s_i&#41;&#40;p2\_2 = b&#41; =\textbf{t}$ iff $\pi &#40;s_j&#41; &#40;p2\_2 = b&#41; =\textbf{t}$. \\)

[//]: # (    &#40;Worlds are connected by $R_2$ when player 2 has the same cards in both worlds.&#41;)

## Obtaining knowledge
The Kripke model is updated after each turn. Public announcements affect the worlds and the relations of the model. After a public announcement is made, all worlds in which the contents of the public announcement are not true, are removed from the model. 
