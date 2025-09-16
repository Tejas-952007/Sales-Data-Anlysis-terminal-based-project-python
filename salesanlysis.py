import numpy as np
months = [ "jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
months = np.array(months)
months = np.array(months)

sales = []
print("\n------------------------------Tejas Sales Data Analysis output ------------------------------")
for month in months:
    print(f"Enter the sales data for {month}:")
    while True:
        try:
            s = int(input(f"{month}: rupees "))
            sales.append(s)
            break
        except ValueError:
            print("Please enter a valid integer value.")

sales = np.array(sales)
print("\n------------------------------Tejas Sales Data Analysis output ------------------------------")
print("\n---->Monthly Sales Dates ")
for i in range(len(months)):
    print(f"{months[i]}: rupees {sales[i]}")
print(f"\n* Total Sales: rupees {np.sum(sales)}")
print(f"\nAverage Monthly Sales: rupees {np.mean(sales)}")
print(f"\nHighest Sales: rupees {np.max(sales)}")
print(f"\nLowest Sales: rupees {np.min(sales)}")
print(f"\nSales Standard Deviation: rupees {np.std(sales)}")
print(f"\nSales Variance: rupees {np.var(sales)}")
