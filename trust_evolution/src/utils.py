



class Character:
    def __init__(self, c_type="base", payoff=3, cost=1, number_of_rounds=5):
        self.c_type= c_type
        self.payoff= payoff
        self.cost= cost
        self.number_of_rounds= number_of_rounds
        self.reward= 0
        self.honest= True


    def self_play(self):
        if self.honest:
            self.reward -= self.cost
        else:
            self.reward -= 0

    def target_play(self, target):
        if target.honest:
            target.target_payoff(amount= target.payoff)
        else:
            target.target_payoff(amount= 0)
    
    def target_payoff(self, amount):
        self.reward += amount
    

class CopyCat(Character):
    def __init__(self, c_type="CopyCat", payoff=3, cost=1, number_of_rounds=5):
        super().__init__(c_type, payoff, cost, number_of_rounds)
        self.reward= 0
        self.honest= True
    
    def _strategy(self, target):
        for i in self.number_of_rounds:
            print(f"{self.c_type} played {i+1} rounds")
            self.honest=True if target.honest else self.honest=False


