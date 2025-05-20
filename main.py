from trust_evolution.src.utils import(
    CopyCat,
    AlwaysCheat,
    AlwaysCooperate,
    playbox,
)


# #Basic gameplay (one vs one)
# cc_1= CopyCat(name="cc_1")
# cc_2= CopyCat(name="cc_2")

# for x in range(5):
#     cc_1.number_of_rounds= x
#     cc_2.number_of_rounds= x
#     cc_1.play(target= cc_2)
#     cc_2.play(target= cc_1)
#     # print(cc_1)
#     # print(cc_2)

# print(cc_1)
# print(cc_2)



#Advanced game play (one vs many)
players=[
    {"agent": CopyCat, "agent_numbers":3, "payoff":3, "cost":1},
    {"agent": AlwaysCheat, "agent_numbers":5, "payoff":3, "cost":1},
    {"agent": AlwaysCooperate, "agent_numbers":5, "payoff":3, "cost":1},
    ]
    


playbox(players= players, number_of_rounds=5).simulate()