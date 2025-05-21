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


# #Basic gameplay (one vs one)
# cc_1= CopyCat(name="cc_1")
# ac_1= AlwaysCheat(name="ac_1")

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




#Advanced game play (one vs many)
agents=[
    {"agent": CopyCat, "agent_numbers":1, "payoff":3, "cost":1},
    {"agent": AlwaysCheat, "agent_numbers":1, "payoff":3, "cost":1},
    {"agent": AlwaysCooperate, "agent_numbers":1, "payoff":3, "cost":1},
    {"agent": Grudger, "agent_numbers":1, "payoff":3, "cost":1},
    {"agent": Detective, "agent_numbers":1, "payoff":3, "cost":1},
    # {"agent": CopyKitten, "agent_numbers":1, "payoff":3, "cost":1},
    # {"agent": Random, "agent_numbers":1, "payoff":3, "cost":1},
    # {"agent": Simpleton, "agent_numbers":1, "payoff":3, "cost":1},
    ]
    


Evolution(agents= agents, number_of_rounds=10).run_playbox()