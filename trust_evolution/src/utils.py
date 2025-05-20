
class Character:
    def __init__(self, name="base", c_type="base", payoff=3, cost=1, number_of_rounds=5):
        self.name= name
        self.c_type= c_type
        self.payoff= payoff
        self.cost= cost
        self.number_of_rounds= number_of_rounds
        self.reward= 0
        self.cooperate= True


    def play(self, target):
        if self.cooperate:
            self.reward -= self.cost
        else:
            self.reward -= 0

        if target.cooperate:
            self.reward += target.payoff
        else:
            self.reward += 0
    
    
    def __str__(self):
        return f"Name: {self.name}\nCharacter: {self.c_type}\nReward: {self.reward}\n"
    

class CopyCat(Character):
    def __init__(self, name="CopyCat" ,c_type="CopyCat", payoff=3, cost=1, number_of_rounds=5):
        super().__init__(name, c_type, payoff, cost, number_of_rounds)
        self.reward= 0
        self.cooperate= True
    
    def _strategy(self, target):
        if self.number_of_rounds == 0:
            self.cooperate= True
        else:
            self.cooperate= True if target.cooperate else False

    def play(self, target):
        self._strategy(target= target)
        super().play(target= target)



class AlwaysCheat(Character):
    def __init__(self, name="AlwaysCheat" ,c_type="AlwaysCheat", payoff=3, cost=1, number_of_rounds=5):
        super().__init__(name, c_type, payoff, cost, number_of_rounds)
        self.reward= 0
        self.cooperate= False
    
    def _strategy(self):
        self.cooperate= False

    def play(self, target):
        self._strategy()
        super().play(target= target)



class AlwaysCooperate(Character):
    def __init__(self, name="AlwaysCheat" ,c_type="AlwaysCheat", payoff=3, cost=1, number_of_rounds=5):
        super().__init__(name, c_type, payoff, cost, number_of_rounds)
        self.reward= 0
        self.cooperate= True
    
    def _strategy(self):
        self.cooperate= True

    def play(self, target):
        self._strategy()
        super().play(target= target)



class playbox:
    def __init__(self, players, number_of_rounds):
        self.players= players
        self.number_of_rounds= number_of_rounds
        self.total_players= self._unpack()


    def _unpack(self):
        total_players= []
        for i in self.players:
            for x in range(i["agent_numbers"]):
                agent= i["agent"]()
                agent.name= f"{agent.c_type}_{x+1}"
                agent.payoff= i["payoff"]
                agent.cost= i["cost"]
                total_players.append(agent)
        
        return total_players


    def simulate(self):
        for i in range(len(self.total_players)):
            target_players= list(range(len(self.total_players)))
            target_players.remove(i)
            for x in range(self.number_of_rounds):
                self.total_players[i].number_of_rounds= x
                for j in target_players:
                    self.total_players[j].number_of_rounds= x
                    self.total_players[i].play(target= self.total_players[j])
                    self.total_players[j].play(target= self.total_players[i])
        
        for i in range(len(self.total_players)):
            print(self.total_players[i])

