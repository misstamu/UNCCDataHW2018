import os
import csv
import pandas as pd

electioncsv = os.path.join("raw_data", "election_data_2.csv")

elections = pd.read_csv(electioncsv)


nvotes = pd.DataFrame(elections["Candidate"].value_counts())
nvotes = nvotes.rename(columns={"Candidate":"Total Votes"})

totalvotes = elections["Candidate"].count()


percentagevotes = pd.DataFrame((nvotes/totalvotes)*100)
percentagevotes = percentagevotes.rename(columns={"Total Votes":"% of Votes"})

results = pd.concat([nvotes, percentagevotes], axis=1)

winner = nvotes.idxmax()

print ("Election Results")
print ("------------------------------")
print ("Total Vote Count: " + str(totalvotes))
print ("------------------------------")
print (results)
print ("------------------------------")
print("The winner is " + winner['Total Votes'])

election_results = os.path.join("..", "election_results.txt")
with open('election_results.txt', 'w') as tf:
    tf.writelines('Election Results')
    tf.writelines('\n' + '-------------------------------')
    tf.writelines('\n' + "Total Vote Count: " + str(totalvotes))
    tf.writelines('\n' + '-------------------------------')
    tf.writelines('\n' + str(results))
    tf.writelines('\n' + '-------------------------------')
    tf.writelines('\n' + "The winner is " + winner['Total Votes'])
