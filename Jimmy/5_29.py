import matplotlib.pyplot as plt

days = list(range(1, 21))  # 20 days
infections = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

plt.figure(figsize=(10, 5))
plt.bar(days, infections, color='skyblue', edgecolor='black')
plt.xlabel("Day")
plt.ylabel("New Infected Patients")
plt.title("Daily COVID-19 New Infected Patients")
plt.xticks(days)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
