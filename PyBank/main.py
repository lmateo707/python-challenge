import csv
import os

budget_data = os.path.join("resources","02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")


def financial_analysis(budget_data):
    
    date = str(budget_data[0])
    profit_losses = int(budget_data[1])
    
    total_months = len(date)
    net_total = len(profit_losses)
    average_changes = sum(profit_losses) / len(profit_losses)

    
    
    print(f"Financial Analysis")
    print(f"Total Months: {str(date)}")
    print(f"Total:  {int(net_total)}")
    print(f"Average Change: {int(average_change)}")
    print(f"Greatest Increase in Profits: str{greatest_increase}")
    print(f"Greatest Decrease in Profits:  {greatest_decrease}")


with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    
    csv_header = next(csvreader)
    prev_row = next(csvreader)
    com_row = next(csvreader)
    print("Financial Analysis")
    total_months = 1
    profit_losses = int(prev_row[1])
    months = []
    greatest_increase = -1000 * 1000
    greatest_decrease = -1000 * 1000
    
    
    
    for row in csvreader:
        
        total_months += 1
        profit_losses += int(row[1])
        change = int(row[1]) - int(prev_row[1])
        months.append(change)
        prev_row = row
        
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            
        elif int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
        

    average_changes = sum(months) / len(months)
     

    print("------------------------------") 
    print(f"Total Months: {total_months}")
    print(f"Total: {profit_losses}")
    print(f"Average Change: ${average_changes}")
    print(f"Greatest Increase in Profits: ($ {greatest_increase})")
    print(f"Greatest Decrease in Profits: ($ {greatest_decrease})")
    
    
    

    



    
    

        
    