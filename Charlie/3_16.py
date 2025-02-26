def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

Grade = []

print("Please enter the player's speed (m/s):")
for i in range(10):
    speed = float(input("Player {}: ".format(i+1)))
    Grade.append(speed)

bubble_sort(Grade)

print("=================================")
print("First place: ", Grade[-1])
print("Second place: ", Grade[-2])