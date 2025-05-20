from trust_evolution.src.utils import(
    CopyCat,
    # playbox,
)


# players=[
#     {"character": CopyCat, "number":1},
#     {"character": CopyCat, "number":1},
#     ]
    

cc_1= CopyCat(name="cc_1")
cc_2= CopyCat(name="cc_2")


for x in range(5):
    cc_1.number_of_rounds= x
    cc_2.number_of_rounds= x
    cc_1.play(target= cc_2)
    # print(cc_1)
    cc_2.play(target= cc_1)
    print(cc_1)
    print(cc_2)