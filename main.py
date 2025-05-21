from trust_evolution.src.utils import(
    CopyCat,
    AlwaysCheat,
    AlwaysCooperate,
    Grudger,
    Random,
    Simpleton,
    CopyKitten,
    Detective,
    Evolution,
)


# #Basic gameplay setup (one vs one)
# cc_1= CopyCat(name="cc_1")
# ac_1= Grudger(name="ac_1")

# for x in range(10):
#     cc_1.number_of_rounds= x
#     ac_1.number_of_rounds= x
#     cc_1.decide(target= ac_1)
#     ac_1.decide(target= cc_1)
#     cc_1.play(target= ac_1)
#     ac_1.play(target= cc_1)
#     # print(cc_1)
#     # print(ac_1)

# print(cc_1.target_coop_hist)
# print(cc_1)
# print(ac_1.target_coop_hist)
# print(ac_1)




#Advanced game play setup (one vs many)
agents=[
    {"agent": CopyCat, "c_type": "CopyCat", "agent_numbers": 5, "payoff": 3, "cost": 1},
    {"agent": AlwaysCheat, "c_type": "AlwaysCheat", "agent_numbers": 5, "payoff": 3, "cost": 1},
    {"agent": AlwaysCooperate, "c_type": "AlwaysCooperate", "agent_numbers": 15, "payoff": 3, "cost": 1},
    # {"agent": Grudger, "c_type": "Grudger", "agent_numbers": 1, "payoff": 3, "cost": 1},
    # {"agent": Detective, "c_type": "Detective", "agent_numbers": 1, "payoff": 3, "cost": 1},
    # {"agent": CopyKitten, "c_type": "CopyKitten", "agent_numbers": 1, "payoff": 3, "cost": 1},
    # {"agent": Random, "c_type": "Random", "agent_numbers": 1, "payoff": 3, "cost": 1},
    # {"agent": Simpleton, "c_type": "Simpleton", "agent_numbers": 1, "payoff": 3, "cost": 1},
    ]
    

# #Simple match
# df= Evolution(agents= agents, number_of_rounds=10).run_playbox()
# print(df)



#Elimination match
trust= Evolution(
    agents= agents, 
    number_of_rounds=10, #how many rounds each pair of agents play against each other
    number_of_tournament=10, #how many full cycles all agents play against each other
    number_of_eliminations=5, #how many low scoring agents get eliminated by tournament
    )

trust.run_elimination_tournament()
trust.plot_agent_numbers()
trust.plot_agent_scores()