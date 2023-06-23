# LAMAS
**Authors**: Sanne Berends (s3772950), Julia Boers (s3632644) & Anniek Theuwissen (s3764818) \
The code models the game Beverbende, as well as a Kirpke model that is used for the strategy of the player.
More information about the rules of the game can be found on [the website](https://sanneberends.github.io/LAMAS/).

### Execution
Running the interface and starting the game Beverbende is done by running the following command: \
'python interface.py' \
On the left part of the interface, the game environment will be displayed. \
On the right part of the interface, the current relevant part of the kripke model will be displayed.

### Game Instructions
You alternately play for agent 1 and agent 2. Which agent's turn it is can be seen on the interface: only the cards of 
The agent whose turn it is are visible. \ 
To execute an action for the agent currently at turn, you have to click on either the deck or the discard pile to get this card. \
The game ends when the deck is empty, or when one of the agents calls 'Bever'.

### Strategy
The strategy of the players is described on [the website](https://sanneberends.github.io/LAMAS/). To play according to this
strategy, you should always click on the discard pile when this card is lower than one of your own cards. If not, you should
always click the deck. 'Bever' is called automatically by the program, and when it is called is based on the Kripke model.
