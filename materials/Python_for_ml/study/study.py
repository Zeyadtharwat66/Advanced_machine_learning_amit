import os
import random

# print(os.getcwd())
# for i in range(20):
#     open(os.path.join(r"C:/Users/HP/Desktop/AMIT/a", f"{i}.txt"), "w")
x = os.listdir(r"C:/Users/HP/Desktop/AMIT/a")
# for i in x:
#     print(i)

count = len(x)
print(count)

while len(os.listdir(r"C:/Users/HP/Desktop/AMIT/a")) > count/2:
    z=random.randint(0, 20)
    print(z)
    if os.path.exists(fr"C:/Users/HP/Desktop/AMIT/a/{z}.txt"):
        os.remove(fr"C:/Users/HP/Desktop/AMIT/a/{z}.txt")