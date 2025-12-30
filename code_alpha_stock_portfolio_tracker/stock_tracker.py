# Stock Portfolio Tracker
# CodeAlpha Python Programming Internship

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

print("📈 Welcome to Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))

portfolio = {}
total_investment = 0

import csv

# Hardcoded current stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

portfolio = {}

def buy_stock():
    stock = input("Enter stock name: ").upper()
    if stock not in stock_prices:
        print("❌ Stock not available.")
        return

    try:
        qty = int(input("Enter quantity to buy: "))
        if qty <= 0:
            print("❌ Quantity must be positive.")
            return
    except ValueError:
        print("❌ Invalid quantity.")
        return

    cost = stock_prices[stock] * qty

    if stock in portfolio:
        portfolio[stock]["quantity"] += qty
        portfolio[stock]["invested"] += cost
    else:
        portfolio[stock] = {
            "quantity": qty,
            "invested": cost
        }

    print(f"✅ Bought {qty} shares of {stock}")

def sell_stock():
    stock = input("Enter stock name: ").upper()
    if stock not in portfolio:
        print("❌ You do not own this stock.")
        return

    try:
        qty = int(input("Enter quantity to sell: "))
        if qty <= 0 or qty > portfolio[stock]["quantity"]:
            print("❌ Invalid quantity.")
            return
    except ValueError:
        print("❌ Invalid input.")
        return

    portfolio[stock]["quantity"] -= qty
    portfolio[stock]["invested"] -= stock_prices[stock] * qty

    if portfolio[stock]["quantity"] == 0:
        del portfolio[stock]

    print(f"✅ Sold {qty} shares of {stock}")

def view_portfolio():
    if not portfolio:
        print("📭 Portfolio is empty.")
        return

    print("\n📊 Portfolio Summary")
    total_value = 0
    total_invested = 0

    for stock, data in portfolio.items():
        current_value = stock_prices[stock] * data["quantity"]
        profit_loss = current_value - data["invested"]

        total_value += current_value
        total_invested += data["invested"]

        print(f"{stock} | Shares: {data['quantity']} | "
              f"Invested: ₹{data['invested']} | "
              f"Current: ₹{current_value} | "
              f"P/L: ₹{profit_loss}")

    print("\n💰 Total Invested:", total_invested)
    print("📈 Current Value:", total_value)
    print("📉 Net P/L:", total_value - total_invested)

def save_to_csv():
    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Invested", "Current Value", "Profit/Loss"])

        for stock, data in portfolio.items():
            current_value = stock_prices[stock] * data["quantity"]
            profit_loss = current_value - data["invested"]
            writer.writerow([
                stock,
                data["quantity"],
                data["invested"],
                current_value,
                profit_loss
            ])

    print("📁 Portfolio saved to portfolio.csv")

def main():
    while True:
        print("\n====== Stock Portfolio Tracker ======")
        print("1. Buy Stock")
        print("2. Sell Stock")
        print("3. View Portfolio")
        print("4. Save Portfolio")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            buy_stock()
        elif choice == "2":
            sell_stock()
        elif choice == "3":
            view_portfolio()
        elif choice == "4":
            save_to_csv()
        elif choice == "5":
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice.")

main()
