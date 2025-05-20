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
        self.self_coop_hist.append(self.cooperate)
    
    def decide(self, target):
        self._strategy(target= target)

    def play(self, target):
        super().play(target= target)
        self.target_coop_hist.append(target.cooperate)



class AlwaysCooperate(Character):
    def __init__(self, name="AlwaysCooperate" ,c_type="AlwaysCooperate", payoff=3, cost=1, number_of_rounds=5):
        super().__init__(name, c_type, payoff, cost, number_of_rounds)
        self.reward= 0
        self.cooperate= None
        self.target_coop_hist= []
        self.self_coop_hist= []
    
    def _strategy(self, target):
        self.cooperate= True
        self.self_coop_hist.append(self.cooperate)
    
    def decide(self, target):
        self._strategy(target= target)

    def play(self, target):
        super().play(target= target)
        self.target_coop_hist.append(target.cooperate)


class Random(Character):
    def __init__(self, name="Random" ,c_type="Random", payoff=3, cost=1, number_of_rounds=5):
        super().__init__(name, c_type, payoff, cost, number_of_rounds)
        self.reward= 0
        self.cooperate= None
        self.target_coop_hist= []
        self.self_coop_hist= []
    
    def _strategy(self, target):
        self.cooperate= np.random.choice([True, False])
        self.self_coop_hist.append(self.cooperate)
    
    def decide(self, target):
        self._strategy(target= target)

    def play(self, target):
        super().play(target= target)
        self.target_coop_hist.append(target.cooperate)



class CopyCat(Character):
    """
    Starts by cooperating. Always copies the opponent's last move from then onwards.
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
        elif target.cooperate:
            self.cooperate= True
        elif not target.cooperate:
            self.cooperate= False
        
        self.self_coop_hist.append(self.cooperate)

    def decide(self, target):
        self._strategy(target)

    def play(self, target):
        super().play(target= target)
        self.target_coop_hist.append(target.cooperate)


class Simpleton(Character):
    """
    Reacts based on how the opponent responded to its own last move — if 
    opponent cooperated, repeat your last move; if opponent cheated, switch your move.
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
        elif self.target_coop_hist[-1]:
            self.cooperate= self.self_coop_hist[-1]
        elif not self.target_coop_hist[-1]:
            self.cooperate= not self.self_coop_hist[-1]
        
        self.self_coop_hist.append(self.cooperate)

    def decide(self, target):
        self._strategy(target)

    def play(self, target):
        super().play(target= target)
        self.target_coop_hist.append(target.cooperate)



class Grudger(Character):
    def __init__(self, name="Grudger" ,c_type="Grudger", payoff=3, cost=1, number_of_rounds=5):
        super().__init__(name, c_type, payoff, cost, number_of_rounds)
        self.reward= 0
        self.cooperate= None
        self.target_coop_hist= []
        self.self_coop_hist= []
    
    def _strategy(self, target):
        if self.number_of_rounds == 0:
            self.cooperate= True
        elif self.number_of_rounds != 0 and False not in self.target_coop_hist:
            self.cooperate= True
        elif self.number_of_rounds != 0 and False in self.target_coop_hist:
            self.cooperate= False
        
        self.self_coop_hist.append(self.cooperate)

    def decide(self, target):
        self._strategy(target= target)

    def play(self, target):
        super().play(target= target)
        self.target_coop_hist.append(target.cooperate)



class playbox:
    def __init__(self, agents, number_of_rounds):
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

    def simulate(self):
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

