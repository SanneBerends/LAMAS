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

![Formal model](/images/formalmodel.png)


## Obtaining knowledge
After each turn, the Kripke model is updated. Each scenario that can happen during a turn corresponds to one or more 
public announcements that are made. These public announcements affect the worlds and relations of the Kripke model: all worlds
in which the contents of the public announcement are not true, are removed from the model. The section [Implementation](implementation.markdown)
contains a more intuitive and less formal description of the public announcements.

### Initialization
![Initialization](/images/Initialization.png)

### Public announcement scenario 1
![Announcement1](/images/announcement1.png)

### Public announcement scenario 2
![Announcement2](/images/announcement2.png)

### Public announcement scenario 3
![Announcement3](/images/announcement3.png)

### Public announcement scenario 4
![Announcement4](/images/announcement4.png)

### Public announcement scenario 5
![Announcement5](/images/announcement5.png)

## Calling Bever
The number of worlds in the Kripke model decreases as the game progresses. The game ends when a player can call 'Bever'. 
This is the case when in all wolds that the player can reach in the Kripke model, its sum of card values is lower
than that of the opponent.