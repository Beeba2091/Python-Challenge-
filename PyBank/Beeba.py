#import budget_data.csv

import os
import csv     

budgetdata_csv = "Resources/budget_data.csv"
totalMonth = 0
totalProfit_Losses = 0
previousProfit_Losses = 0
Profit_Losses_change = 0
ProfitLoss_change_list = []
month_change = []
greatestIncrease = 0
greatestDecrease = 999999999999

with open(budgetdata_csv) as profit_lossData:
    reader = csv.DictReader(profit_lossData)
    #loop through the data
    #At initial stage take previousProfit_Losses as first row
    #So skip first row
    index=0
    for row in reader:
        if(index==0):
            totalMonth+=1
            totalProfit_Losses = totalProfit_Losses + int(row["Profit/Losses"])
            previousProfit_Losses = int(row["Profit/Losses"])
            month_change = month_change + [row["Date"]]
            index+=1
            continue
        
        # The total number of months included in the dataset

        totalMonth = totalMonth + 1
        # The net total amount of "Profit/Losses" over the entire period
        totalProfit_Losses = totalProfit_Losses + int(row["Profit/Losses"])
        
        Profit_Losses_change = int(row["Profit/Losses"]) - previousProfit_Losses        
        ProfitLoss_change_list.append(Profit_Losses_change)
        
        previousProfit_Losses = int(row["Profit/Losses"])
        
        month_change = month_change + [row["Date"]]
    greatestDecrease=min(ProfitLoss_change_list)
    greatestIncrease=max(ProfitLoss_change_list)
    #We have to add 1 because month associated with change is the next month
    greatestDecrease_month=ProfitLoss_change_list.index(greatestDecrease)+1
    greatestIncrease_month=ProfitLoss_change_list.index(greatestIncrease)+1

    print("Financial Analysis")

    print("----------------------")

    print(f"Total Months: {totalMonth}\n")

    print(f"Total Profit/Losses: ${totalProfit_Losses}\n")

    print(f"Average Change: ${round(sum(ProfitLoss_change_list)/len(ProfitLoss_change_list),2)}")

    print(f"Greatest increase in Profits: {month_change[greatestIncrease_month]} (${(str(greatestIncrease))})")

    print(f"Greatest decrease in Profits: {month_change[greatestDecrease_month]} (${(str(greatestDecrease))})")

# Print the output