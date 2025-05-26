# Trust Evolution

This `README.md` was created using my package [README_genie](https://github.com/browshanravan/README_genie).

A Python-based simulation of the [Evolution of Trust](https://ncase.me/trust/) game by Nicky Case. This project recreates the classic iterated Prisoner’s Dilemma tournament using object-oriented agents and evolutionary elimination dynamics, allowing you to explore how different trust strategies fare over repeated interactions.

---

## Table of Contents

- [About This Project](#about-this-project)  
- [Features](#features)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Quickstart](#quickstart)  
- [Project Structure](#project-structure)  
- [Usage](#usage)  
  - [Defining Agents](#defining-agents)  
  - [Running a Basic Tournament](#running-a-basic-tournament)  
  - [Running an Elimination Tournament](#running-an-elimination-tournament)  
- [Implemented Strategies](#implemented-strategies)  
- [Visualization](#visualization)  
- [Development Container](#development-container)  
- [License](#license)  

---

## About This Project

This repository is a Python 3.10 implementation of Nicky Case’s **Evolution of Trust** interactive demonstration. It uses object-oriented programming to model different agent strategies in iterated Prisoner’s Dilemma matches, and provides both a simple round-robin “playbox” and an evolutionary elimination tournament.  

By adjusting payoffs, population sizes, number of rounds, and elimination rules, you can experiment with how cooperation and defection emerge and persist in a population.

---

## Features

- Object-oriented agent classes for classic Prisoner’s Dilemma strategies  
- Round-robin tournaments to compare aggregate performance  
- Evolutionary elimination: remove low-scoring agents and spawn new ones from top performers  
- Automated plotting of population counts and scores over tournament rounds  
- Easy extension: plug in new strategies by subclassing `Character`  

---

## Getting Started

### Prerequisites

- Python 3.10  
- Git  

### Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/browshanravan/trust_evolution.git
   cd trust_evolution
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

### Quickstart

Run the main script to execute a default elimination tournament and view results:

```bash
python main.py
```

This will print the final agent score rankings and pop up two plots:  
1. **Agent population over tournament rounds**  
2. **Agent scores over tournament rounds**

---

## Project Structure

```
.
├── LICENSE
├── README.md
├── requirements.txt
├── main.py
├── trust_evolution/
│   └── src/
│       └── utils.py       # Agent classes & Evolution engine
└── .devcontainer/         # VS Code dev container config
    ├── Dockerfile
    └── devcontainer.json
```

---

## Usage

### Defining Agents

Agents are configured in `main.py` as a list of dicts:

```python
agents = [
    {"agent": CopyCat,           "c_type": "CopyCat",          "agent_numbers": 5,  "payoff": 3, "cost": 1},
    {"agent": AlwaysCheat,       "c_type": "AlwaysCheat",      "agent_numbers": 5,  "payoff": 3, "cost": 1},
    {"agent": AlwaysCooperate,   "c_type": "AlwaysCooperate",  "agent_numbers": 15, "payoff": 3, "cost": 1},
    # ... add more strategies here …
]
```

### Running a Basic Tournament

To run a simple round-robin “playbox” without eliminations:

```python
from trust_evolution.src.utils import Evolution

evo = Evolution(agents=agents, number_of_rounds=10)
df_scores = evo.run_playbox()
print(df_scores)
```

### Running an Elimination Tournament

Set up an evolutionary tournament where, after each full round-robin, the worst performers are eliminated and replaced by clones of the best:

```python
from trust_evolution.src.utils import Evolution

evo = Evolution(
    agents=agents,
    number_of_rounds=10,        # rounds per pair
    number_of_tournament=10,    # total elimination cycles
    number_of_eliminations=5    # agents removed each cycle
)
final_ranking = evo.run_elimination_tournament()
print(final_ranking)

# Visualize dynamics
evo.plot_agent_numbers()
evo.plot_agent_scores()
```

---

## Implemented Strategies

- **AlwaysCooperate**: always cooperates  
- **AlwaysCheat**: always defects  
- **Random**: randomly cooperates or defects each round  
- **CopyCat (Tit-for-Tat)**: starts with cooperate, then mirrors opponent’s last move  
- **CopyKitten**: like Tit-for-Tat but only defects after two consecutive defections by opponent  
- **Simpleton**: repeats last move if opponent cooperated; switches if opponent defected  
- **Grudger**: cooperates until opponent defects once, then defects forever  
- **Detective**: probes first four moves, then adapts to either Tit-for-Tat or AlwaysCheat  

You can easily add new strategies by subclassing the base `Character` class.

---

## Visualization

After an elimination tournament, call:

```python
evo.plot_agent_numbers()  # population counts per strategy over time
evo.plot_agent_scores()   # cumulative scores per strategy over time
```

Plots are generated using Matplotlib with a clean, minimalist style.

---

## Development Container

This repository includes a VS Code Dev Container configuration for reproducible development:

- **`.devcontainer/Dockerfile`**  
- **`.devcontainer/devcontainer.json`**  

It installs Python 3.10 and necessary tools automatically. Simply open the folder in VS Code and reopen in container.

---

## License

This project is released under the **MIT License**. See [LICENSE](LICENSE) for details.