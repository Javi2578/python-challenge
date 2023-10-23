import os
import pandas as pd 

def financial_analysis(file_path):
    # Reading the CSV file into a DataFrame
    data_file_df = pd.read_csv(file_path)
    
    # Calculate the total number of months
    total_months = len(data_file_df)
    
    # Calculate the total profit/loss
    total_profit_loss = data_file_df["Profit/Losses"].sum()
    
    # Calculate the average change between months
    data_file_df["Monthly Change"] = data_file_df["Profit/Losses"].diff()
    avg_change = data_file_df["Monthly Change"].mean()

    # Find the greatest increase and decrease in profits
    max_increase = data_file_df["Monthly Change"].max()
    max_decrease = data_file_df["Monthly Change"].min()

    # Find the month corresponding to the greatest increase and decrease
    max_increase_month = data_file_df.loc[data_file_df["Monthly Change"] == max_increase, "Date"].values[0]
    max_decrease_month = data_file_df.loc[data_file_df["Monthly Change"] == max_decrease, "Date"].values[0]

    # Print out the financial analysis
    print("Financial Analysis")
    print("-" * 30)
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${avg_change:.2f}")
    print(f"Greatest Increase in Profits: {max_increase_month} (${int(max_increase)})")
    print(f"Greatest Decrease in Profits: {max_decrease_month} (${int(max_decrease)})")

if __name__ == "__main__":
    file_path = os.path.join("Resources", "budget_data.csv")
    financial_analysis(file_path)



