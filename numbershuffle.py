import random
num_list = list(range(1,75))
# k = []
# for i in range(1):
#     random.shuffle(num_list)
#     k.append(list(num_list))
random.shuffle(num_list)
three_num = num_list[:4]
print("Your lucky numbers are", three_num)
