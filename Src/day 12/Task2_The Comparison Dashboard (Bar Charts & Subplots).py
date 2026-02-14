import matplotlib.pyplot as plt
categories=['Electronics','Clothing','Home']
sales=[300,450,200]

days = [1,2,3,4,5]
daily_visitors =[10,25,45,65,40]

plt.subplot(1,2,1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Department")
plt.ylabel("Revenue")
plt.subplot(1,2,2)
plt.plot(days, daily_visitors)
plt.title("Visitor Trend (Last 5 Days)")
plt.xlabel("Day")
plt.ylabel("Visitors")
plt.tight_layout()
plt.show()