print("Simple Stock Tracker")
a=input("Enter the name of the stock: ")
b=float(input("ENTER THE Quantity of the stock: "))
price={"AAPL": 150.00, "GOOGL": 2800.00, "AMZN": 3400.00, "MSFT": 300.00, "TSLA": 700.00}
print(f"THE NAME OF STOCK IS {a} ")
print(f"THE QUANTITY OF STOCK IS {b} ")
print(f"THE PRICE OF STOCK IS {price.get(a, 0)} ")
print(f"THE TOTAL VALUE OF STOCK IS {b * price.get(a, 0)} ")
