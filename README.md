# trust_evolution
This project is inspired by [the evolution of trust](https://ncase.me/trust/) by [Nicky Case](https://ncase.me)!

The original game source material can be found [here](https://github.com/ncase/trust/#play-it-here-httpncasemetrust).


## About this project
The original game references above explores the idea of how different play tactics influence the outcome of the game of trust.

This repo is an attempt to recreate the game in `python 3.10` using `OOP`, `ABM` and the concepts shown in the game above.

This project aims to provide the basic foundations for creating a game, where different agents can get added to it.


## Notes:
The basic tournament dynamics (`run_playbox()` method) matches the game referenced above. 

When, it comes to the elimination/evolutionary tournament dynamics (`.run_elimination_tournament()` method), users might notice some scoring differences between this implementation and the above referenced game. 

This is due to how the code in this repo breaks ties and assigns new agents.


## Getting started
You can pull this package and run it in devcontainers in your VSCode.

Otherwise run the app by installing `python 3.10` using conda.

The easiest way to run the app is to go to the local directory of this repo and execute:

```console
pip3 install -r requirements.txt
```