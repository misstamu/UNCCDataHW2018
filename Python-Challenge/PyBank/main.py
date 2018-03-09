import os
import csv

rowcount = 0

budgetcsv = os.path.join("raw_data", "budget_data_1.csv")

with open(budgetcsv,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    
    revtotal = 0
    
    revenue = []

    dates = []

    for row in csvreader:
        rowcount += 1
        
        revtotal += int(row[1])

        months = row[0]
        dates.append(months)

        monthlyrev = int(row[1])
        revenue.append(monthlyrev)
 
avgrev = int(revtotal/rowcount)


print ("Financial Analysis")
print ("----------------------------------------------")
print ("Total Months: " + str(rowcount))
print ("Total Revenue: $" +  str(revtotal))
print ("Average Revenue Change: $" + str(avgrev))

print ("Greatest Increase In Revenue: " + str(dates[revenue.index(max(revenue))]) + " ($" + str(max(revenue)) + ")")
print ("Greatest Decrease In Revenue: " + str(dates[revenue.index(min(revenue))]) + " ($" + str(min(revenue)) + ")")


budgetsummary = os.path.join("..", "budgetsummary.txt")
with open('budgetsummary.txt', 'w') as tf:
    tf.writelines('Financial Analysis')
    tf.writelines('\n' + '----------------------------------------------')
    tf.writelines('\n' + "Total Months: " + str(rowcount))
    tf.writelines('\n' + "Total Revenue: $" +  str(revtotal))
    tf.writelines('\n' + "Average Revenue Change: $" + str(avgrev))
    tf.writelines('\n' + "Greatest Increase In Revenue: " + str(dates[revenue.index(max(revenue))]) + " ($" + str(max(revenue)) + ")")
    tf.writelines('\n' + "Greatest Decrease In Revenue: " + str(dates[revenue.index(min(revenue))]) + " ($" + str(min(revenue)) + ")")



