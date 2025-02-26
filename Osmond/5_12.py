import random

actors_a=["Ned Stark","Robert Baratheon","Jaime Lannister","Catelyn Stark","Cersei Lannister"]
actors_b=["Sean Bean","Mark Addy","Nikolaj Coster-Waldau","Michelle Fairley","Lena Headey"]

index=random.randint(0,4)
print("Who plays "+actors_a[index])
for i in range(5):
    print(str(i+1)+". "+actors_b[i])
x=int(input("Enter your answer: "))
if x==index+1:
    print("Correct")
else:
    print("Incorrect")
