import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("https://pynative.com/wp-content/uploads/2019/01/company_sales_data.csv")

# ---- Exercise 1: Total profit line plot ----
plt.figure(figsize=(8,5))
plt.plot(data['month_number'], data['total_profit'], marker='o', color='b')
plt.title("Company Profit per Month")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.grid(True)
plt.show()

# ---- Exercise 2: Bathing soap & Facewash in subplot ----
fig, ax = plt.subplots(2, 1, figsize=(8,6))

# Bathing soap
ax[0].plot(data['month_number'], data['bathingsoap'], marker='o', color='g')
ax[0].set_title("Bathing Soap Sales")
ax[0].set_ylabel("Units Sold")
ax[0].grid(True)

# Facewash
ax[1].plot(data['month_number'], data['facewash'], marker='o', color='r')
ax[1].set_title("Facewash Sales")
ax[1].set_xlabel("Month Number")
ax[1].set_ylabel("Units Sold")
ax[1].grid(True)

plt.tight_layout()
plt.show()