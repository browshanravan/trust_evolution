



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
            target.target_payoff(amount= target.payoff)
        else:
            target.target_payoff(amount= 0)
    
    def target_payoff(self, amount):
        self.reward += amount
    
    def __str__(self):
        return f"Name: {self.name}\nCharacter: {self.c_type}\n Reward: {self.reward}"
    

class CopyCat(Character):
    def __init__(self, name="CopyCat" ,c_type="CopyCat", payoff=3, cost=1, number_of_rounds=5):
        super().__init__(name, c_type, payoff, cost, number_of_rounds)
        self.reward= 0
        self.cooperate= True
    
    def play(self, target):
        print(f"{self.name} played {self.number_of_rounds+1} rounds")
        if self.number_of_rounds == 0:
            self.cooperate= True
        else:
            self.cooperate= True if target.cooperate else False
        
        super().play(target= target)


# class playbox:
#     def __init__(self, players):
#         self.players= players
    

#     def play_game(self):
#         for i in self.players:
#             i.character.self_play()