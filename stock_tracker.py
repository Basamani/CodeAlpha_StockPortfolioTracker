# Stock Portfolio Tracker

# Step 1: Predefined stock prices (dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

# Step 2: Initialize total investment
total_investment = 0

print("📊 Stock Portfolio Tracker\n")

# Step 3: Ask user for number of stocks
n = int(input("Enter number of stocks: "))

# Step 4: Loop to take stock input
for i in range(n):
    print(f"\nStock {i+1}")
    
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))
    
    # Step 5: Check if stock exists
    if stock_name in stock_prices:
        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment
        
        print(f"{stock_name} price: ₹{price}")
        print(f"{stock_name} value: ₹{investment}")
    else:
        print("❌ Stock not found!")

# Step 6: Display total investment
print("\n---------------------------")
print(f"Total Investment: ₹{total_investment}")
print("---------------------------")

# Step 7: Optional - Save to file
choice = input("\nDo you want to save result to file? (yes/no): ").lower()

if choice == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("---------------------------\n")
        file.write(f"Total Investment: ₹{total_investment}\n")
    
    print("✅ Data saved to portfolio.txt")
else:
    print("Data not saved.")