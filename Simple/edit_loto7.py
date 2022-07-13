# import random
# lotto = []
#
# rnd_num = random.randint(1,37)
#
# for i in range(6):
#     while rnd_num in lotto:
#         rnd_num = random.randint(1, 37)
#     lotto.append(rnd_num)
#
#
# lotto.sort()
# print("loto7: {}".format(lotto))

# simple loto app
import random

loto = random.sample(range(1, 37), 6)

print("loto : {}".format(loto))
