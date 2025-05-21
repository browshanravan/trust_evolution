import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
    def __init__(self, agents, number_of_rounds=5, number_of_tournament=2, number_of_eliminations=5):
        self.agents= agents
        self.number_of_rounds= number_of_rounds
        self.number_of_tournament= number_of_tournament
        self.number_of_eliminations= number_of_eliminations
        self.total_agents= []
        self.tournament_results= []

    def _basic_unpack(self):
        total_agents= []
        for i in self.agents:
            for x in range(i["agent_numbers"]):
                agent= i["agent"]()
                agent.name= f"{agent.c_type}_{x+1}"
                agent.payoff= i["payoff"]
                agent.cost= i["cost"]
                total_agents.append(agent)
        
        return total_agents

    def basic_tournament(self, unpacking=True):
        if unpacking:
            self.total_agents= self._basic_unpack()
        
        database=[]
        for i in list(range(len(self.total_agents)))[:-1]:
            for j in range(i+1, len(self.total_agents)):
                for x in range(self.number_of_rounds):
                    self.total_agents[i].number_of_rounds = x
                    self.total_agents[j].number_of_rounds = x

                    p1 = self.total_agents[i]
                    p2 = self.total_agents[j]

                    p1.decide(target= p2)
                    p2.decide(target= p1)
                    
                    p1.play(target= p2)
                    p2.play(target= p1)
                
                agent_1_scores={
                    "agent_type": p1.c_type,
                    "agent_name": p1.name,
                    "agent_reward": p1.reward,
                }
                database.append(agent_1_scores)
                
                agent_2_scores={
                    "agent_type": p2.c_type,
                    "agent_name": p2.name,
                    "agent_reward": p2.reward,
                }
                database.append(agent_2_scores)
                
                p1.reward = 0
                p1.self_coop_hist= []
                p1.target_coop_hist= []
                
                p2.reward = 0
                p2.self_coop_hist= []
                p2.target_coop_hist= []

        return database

    def run_playbox(self, unpacking=True):
        database= self.basic_tournament(unpacking=unpacking)
        df= pd.DataFrame(data= database)
        df= df.groupby(["agent_type"])["agent_reward"].sum()
        
        return df
    
    def run_elimination_tournament(self, unpacking=False):
        for tournament_round in range(self.number_of_tournament):
            if tournament_round == 0:
                 #We only want to unpack the agents on round 0
                 self.total_agents= self._basic_unpack()
            
            database= self.basic_tournament(unpacking= unpacking)
            df= pd.DataFrame(data= database)
            data= df.groupby(["agent_name"])["agent_reward"].sum().sort_values(ascending= False)
            self.tournament_results.append(data)
            
            ##There are no tie breaking strategy. Just using the top and bottom list
            ##Get the best x and worst x performing agents
            bottom_list= data.iloc[-self.number_of_eliminations:].index.tolist()
            top_list= data.iloc[:self.number_of_eliminations].index.tolist()
            eliminated_data= data.drop(labels= bottom_list)

            ##Get the max_value of the new dataframe so any new numbering for agents will be +1
            max_value= max([int(x.split("_")[1]) for x in eliminated_data.index.tolist()])

            ##drop bottom agents from self.total_agents
            total_agents= []
            for i in self.total_agents:
                if i.name not in bottom_list:
                    total_agents.append(i)

            self.total_agents= total_agents
            
            ##add the new agents
            for i in range(len(top_list)):
                c_type= top_list[i].split("_")[0]
                for x in self.agents:
                    if x["c_type"] == c_type:
                        y= x["agent"]()
                        y.name= f"{c_type}_{max_value+(i+1)}"
                        self.total_agents.append(y)
                        break

        return data
    
    def processing_data_for_plot(self):
        database= []
        for i in range(len(self.tournament_results)):
            df= self.tournament_results[i].to_frame()
            df= df.reset_index()
            df["agent_type"]= df["agent_name"].str.split("_").apply(lambda x: x[0])
            df["tournament_round"]= i
            database.append(df)
        
        df= pd.concat(database).reset_index(drop=True)
        
        df_agent_number= df.groupby(["tournament_round", "agent_type"])["agent_type"].count().reset_index(name="agent_counts")
        df_agent_number_pivot= df_agent_number.pivot_table(values= "agent_counts", columns= "agent_type", index="tournament_round", aggfunc="mean").fillna(value=0)
        df_agent_number_pivot.columns.name= None

        df_agent_score= df.groupby(["tournament_round", "agent_type"])["agent_reward"].sum().reset_index(name="agent_scores")
        df_agent_score_pivot= df_agent_score.pivot_table(values= "agent_scores", columns= "agent_type", index="tournament_round", aggfunc="mean").fillna(value=0)
        df_agent_score_pivot.columns.name= None
        
        return df_agent_number_pivot, df_agent_score_pivot
    
    def plot_agent_numbers(self):
        df_agent_number_pivot, _= self.processing_data_for_plot()
        
        plt.rcParams['axes.spines.left'] = False
        plt.rcParams['axes.spines.right'] = False
        plt.rcParams['axes.spines.top'] = False
        plt.rcParams['axes.spines.bottom'] = False
        plt.rcParams['xtick.bottom'] = False
        plt.rcParams['ytick.left'] = False
        
        for column in df_agent_number_pivot.columns:
            plt.plot(df_agent_number_pivot[column], label= column)
        
        plt.title(f"Evolution of Trust")
        plt.xlabel("Number of Tournaments")
        plt.ylabel("Number of Agents")
        plt.legend(loc="best")
        plt.tight_layout()
        plt.show()

    def plot_agent_scores(self):
        _, df_agent_score_pivot= self.processing_data_for_plot()
        
        plt.rcParams['axes.spines.left'] = False
        plt.rcParams['axes.spines.right'] = False
        plt.rcParams['axes.spines.top'] = False
        plt.rcParams['axes.spines.bottom'] = False
        plt.rcParams['xtick.bottom'] = False
        plt.rcParams['ytick.left'] = False
        
        for column in df_agent_score_pivot.columns:
            plt.plot(df_agent_score_pivot[column], label= column)
        
        plt.title(f"Evolution of Trust")
        plt.xlabel("Number of Tournaments")
        plt.ylabel("Scores of Agents")
        plt.legend(loc="best")
        plt.tight_layout()
        plt.show()
