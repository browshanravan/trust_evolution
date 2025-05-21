import numpy as np


class Character:
    def __init__(self, name="base", c_type="base", payoff=3, cost=1, number_of_rounds=5):
        self.name= name
        self.c_type= c_type
        self.payoff= payoff
        self.cost= cost
        self.number_of_rounds= number_of_rounds
        self.reward= 0
        self.cooperate= None

    def play(self, target):
        if self.cooperate:
            self.reward -= self.cost
        elif not self.cooperate:
            self.reward -= 0

        if target.cooperate:
            self.reward += target.payoff
        elif not target.cooperate:
            self.reward += 0

    def __str__(self):
        return f"Name: {self.name}\nCharacter: {self.c_type}\nReward: {self.reward}\n"



class AlwaysCheat(Character):
    def __init__(self, name="AlwaysCheat" ,c_type="AlwaysCheat", payoff=3, cost=1, number_of_rounds=5):
        super().__init__(name, c_type, payoff, cost, number_of_rounds)
        self.reward= 0
        self.cooperate= None
        self.target_coop_hist= []
        self.self_coop_hist= []
    
    def _strategy(self, target):
        self.cooperate= False
    
    def decide(self, target):
        self._strategy(target= target)

    def play(self, target):
        super().play(target= target)
        self.target_coop_hist.append(target.cooperate)
        self.self_coop_hist.append(self.cooperate)



class AlwaysCooperate(Character):
    def __init__(self, name="AlwaysCooperate" ,c_type="AlwaysCooperate", payoff=3, cost=1, number_of_rounds=5):
        super().__init__(name, c_type, payoff, cost, number_of_rounds)
        self.reward= 0
        self.cooperate= None
        self.target_coop_hist= []
        self.self_coop_hist= []
    
    def _strategy(self, target):
        self.cooperate= True
    
    def decide(self, target):
        self._strategy(target= target)

    def play(self, target):
        super().play(target= target)
        self.target_coop_hist.append(target.cooperate)
        self.self_coop_hist.append(self.cooperate)



class Random(Character):
    def __init__(self, name="Random" ,c_type="Random", payoff=3, cost=1, number_of_rounds=5):
        super().__init__(name, c_type, payoff, cost, number_of_rounds)
        self.reward= 0
        self.cooperate= None
        self.target_coop_hist= []
        self.self_coop_hist= []
    
    def _strategy(self, target):
        self.cooperate= np.random.choice([True, False])
    
    def decide(self, target):
        self._strategy(target= target)

    def play(self, target):
        super().play(target= target)
        self.target_coop_hist.append(target.cooperate)
        self.self_coop_hist.append(self.cooperate)



class CopyCat(Character):
    """
    This agent starts by cooperating. Then it copies the opponent's last move from there onwards.
    """
    def __init__(self, name="CopyCat" ,c_type="CopyCat", payoff=3, cost=1, number_of_rounds=5):
        super().__init__(name, c_type, payoff, cost, number_of_rounds)
        self.reward= 0
        self.cooperate= None
        self.target_coop_hist= []
        self.self_coop_hist= []
    
    def _strategy(self, target):
        if self.number_of_rounds == 0:
            self.cooperate= True
        else:
            self.cooperate= target.self_coop_hist[-1]
        
    def decide(self, target):
        self._strategy(target)

    def play(self, target):
        super().play(target= target)
        self.target_coop_hist.append(target.cooperate)
        self.self_coop_hist.append(self.cooperate)



class CopyKitten(Character):
    """
    This agent is like CopyCat. It only cheats if another agent cheats twice in a row.
    This gets over the issue of a mistaken lack of cooperation.
    """
    def __init__(self, name="CopyKitten" ,c_type="CopyKitten", payoff=3, cost=1, number_of_rounds=5):
        super().__init__(name, c_type, payoff, cost, number_of_rounds)
        self.reward= 0
        self.cooperate= None
        self.target_coop_hist= []
        self.self_coop_hist= []
    
    def _strategy(self, target):
        if self.number_of_rounds < 2:
            self.cooperate= True
        elif target.self_coop_hist[-1] == False and target.self_coop_hist[-2] == False:
            self.cooperate= False
        else:
            self.cooperate= True
        
    def decide(self, target):
        self._strategy(target)

    def play(self, target):
        super().play(target= target)
        self.target_coop_hist.append(target.cooperate)
        self.self_coop_hist.append(self.cooperate)



class Simpleton(Character):
    """
    This agent reacts based on how the opponent responded to its own last move. If 
    opponent cooperated, simpleton agent repeats its own last move; if opponent cheated, 
    simpleton agent switches its move.
    """
    def __init__(self, name="Simpleton" ,c_type="Simpleton", payoff=3, cost=1, number_of_rounds=5):
        super().__init__(name, c_type, payoff, cost, number_of_rounds)
        self.reward= 0
        self.cooperate= None
        self.target_coop_hist= []
        self.self_coop_hist= []
    
    def _strategy(self, target):
        if self.number_of_rounds == 0:
            self.cooperate= True
        elif target.self_coop_hist[-1]:
            self.cooperate= self.self_coop_hist[-1]
        elif not target.self_coop_hist[-1]:
            self.cooperate= not self.self_coop_hist[-1]
        
    def decide(self, target):
        self._strategy(target)

    def play(self, target):
        super().play(target= target)
        self.target_coop_hist.append(target.cooperate)
        self.self_coop_hist.append(self.cooperate)



class Grudger(Character):
    """
    This agent starts by cooperating. However if the oponent agent does not cooperate at any point,
    this agent will refuse to cooperate from that point onwards.
    This implementation does not holds memory of an agent being previously encountered.
    """
    def __init__(self, name="Grudger" ,c_type="Grudger", payoff=3, cost=1, number_of_rounds=5):
        super().__init__(name, c_type, payoff, cost, number_of_rounds)
        self.reward= 0
        self.cooperate= None
        self.target_coop_hist= []
        self.self_coop_hist= []

    def _strategy(self, target):
        if self.number_of_rounds == 0:
            self.cooperate= True
        elif self.number_of_rounds != 0 and False not in target.self_coop_hist:
            self.cooperate= True
        elif self.number_of_rounds != 0 and False in target.self_coop_hist:
            self.cooperate= False

    def decide(self, target):
        self._strategy(target= target)

    def play(self, target):
        super().play(target= target)
        self.target_coop_hist.append(target.cooperate)
        self.self_coop_hist.append(self.cooperate)



class Detective(Character):
    """
    This agent test the other agents 4 times through Cooperate → Cheat → Cooperate → Cooperate
    If the oposing agent retaliates at any of the points, I become CopyCat. If not, I become AlwaysCheat.
    This implementation does not holds memory of an agent being previously encountered.
    """
    def __init__(self, name="Detective" ,c_type="Detective", payoff=3, cost=1, number_of_rounds=5):
        super().__init__(name, c_type, payoff, cost, number_of_rounds)
        self.reward= 0
        self.cooperate= None
        self.target_coop_hist= []
        self.self_coop_hist= []
    
    def _strategy(self, target):
        if self.number_of_rounds == 0:
            self.cooperate= True
        elif self.number_of_rounds == 1:
            self.cooperate= False
        elif self.number_of_rounds in [2,3]:
            self.cooperate= True
        else:
            if False in target.self_coop_hist:
                self.cooperate= target.self_coop_hist[-1]
            else:
                self.cooperate= False

    def decide(self, target):
        self._strategy(target= target)

    def play(self, target):
        super().play(target= target)
        self.target_coop_hist.append(target.cooperate)
        self.self_coop_hist.append(self.cooperate)



class Evolution:
    def __init__(self, agents, number_of_rounds=5):
        self.agents= agents
        self.number_of_rounds= number_of_rounds
        self.total_agents= self._unpack()

    def _unpack(self):
        total_agents= []
        for i in self.agents:
            for x in range(i["agent_numbers"]):
                agent= i["agent"]()
                agent.name= f"{agent.c_type}_{x+1}"
                agent.payoff= i["payoff"]
                agent.cost= i["cost"]
                total_agents.append(agent)
        
        return total_agents

    def run_playbox(self):
        for round_num in range(self.number_of_rounds):
            for i in range(len(self.total_agents)):
                self.total_agents[i].number_of_rounds = round_num
            for i in range(len(self.total_agents)):
                for j in range(i + 1, len(self.total_agents)):
                    p1 = self.total_agents[i]
                    p2 = self.total_agents[j]
                    
                    p1.decide(target= p2)
                    p2.decide(target= p1)
                    
                    p1.play(target= p2)
                    p2.play(target= p1)
        
        for i in range(len(self.total_agents)):
            print(self.total_agents[i])


    # def run_tournament(self):