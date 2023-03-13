 Tracking Financial and Election Data in Python\

-Overview:
In this project, I was given two .csv files, which respectively contained a company\'92s profits and losses and recent election results. I was assigned to use Python to parse these .csv files and summarize them in an easily digestible analyses. In both .csv files, I was asked to find the total number of months and votes recorded. In the financial analysis program, I was asked to find the total profits or losses over multiple years; the average change in profits and losses between months in those years; and months when profits increased or decreased the most. In the election analysis, I was asked to list the candidates, find the number and percentage of votes they received, and to determine which candidate won the election. \

Each of these projects contained their own unique challenges and required unique solutions, as well. These challenges, their solutions, and the processes I used to come to these solutions will be explained below.


- Pybank:
To find the total number of months in the budget_data.csv file, I used a simple strategy. After opening the csv reader and programming Python to skip the headers of the .csv file, I created a 'for' statement to have my program iterate through the file. By writing 'num_months += 1', I told the program to add 1 to the num_months variable for each row it read, thereby calculating the number of months recorded in the .csv file. I used a similar method to calculate the profits and losses the company experienced over the given months, telling the program to then read the next row and add each value to the variable '91profit_loss', thereby adding all profits and subtracting all losses found in that row (profit_loss += int(row[1]).

To find the greatest increase and decrease in profits required a rather lengthy series of lists and if statements. By writing current_pl = int(row[1]), I told my program that each row it read would automatically become the current profit/loss value, which it would compare to the one that came before. Beginning my 'if' statements, I took into account that I could not compare the first value of row[1] to any value, so I set previous_pl to zero and started the comparison with the next value by writing 'if previous_pl != 0\'. To find the change in profits and losses for each month, I then simply told the program to subtract the current value from the previous, then to add the result of that calculation to a list:
			
			monthly_change = current_pl - previous_pl
            	change_list.append(monthly_change)


Next, I set the program to search for the greatest monthly increase in profits. To do this required another 'if' statement, which I placed below the first. Setting the initial value of 'greatest_increase' to 0, I told the program to compare each value in row[1] to the value of 'greatest_increase\'92. If that value was greater than the one stored in 'greatest_increase', it would become the new value stored in 'greatest_increase'. This cycle would continue as the program iterated through row[1]. As the program found the greatest increase, it was also told to find the value in row[0] that represented the month in which the greatest increase in profits happened. I used a similar process to find the greatest decrease in profits, setting the 'greatest_decrease' value to 0, comparing monthly change values to it, and storing the row[0] value; however, this time I told the program to see if the monthly change was less than the current value stored in 'greatest_decrease'.

Finally, I was able to use the list of change values I created before the beginning of the 'if' statements to find the average change in profits and losses over the given months. I simply told the program to add together all the values in that list and divide them by the number of values in the list.

I formatted these values to display in a summary in the terminal and used the writer function in Python to also create a text file for them. When this project is downloaded from GitHub, there will already be a budget_data.txt file included in the pybank 'Analysis' folder, but if it is deleted and the program is run again, a new one should be created.


-Pypoll:
To find the total number of votes in the election_data.csv file, I applied the same instructions as I did for the budget_data.csv file. As the program iterated through the .csv file, it added a value of 1 to the total_votes variable, thereby recording the sum total of the recorded votes.

Then, I moved on to list each candidate in the race by instructing the program to move to row[2] of the .csv file, where the names of each candidate are recorded. I used an if statement to record candidates' names to an empty list that I initialized with my other variables. First, I told the program to record candidates' names if they were not the same '!=' as the candidate name that came before. To avoid repeated names, I then told the program to add the names to the list only if they were not in the list already.

To find the number of votes each candidate received, I created three separate lists connected to each candidate. To avoid index errors, I first told my program to make sure that the first candidate list had 1 or more, then 2 or more, then 3 or more values. Then, using an 'if...and' statement, I had the program track the current candidate in each row, as it iterated through the .csv file. If that current candidate matched a candidate in the first candidate list, the program would append that row to the candidate's individual list. The length of that individual list is set to provide the number of votes each candidate received. To find the percentage of the vote each candidate received, the program divides the length of their individual list by the total number of votes found at the beginning of the 'for' statement.

Finally, to find the winner, a series of 'if' and 'elif' statements tells the program to compare each candidates vote percentages to one another. If one candidates vote percentage is greater than the other two, their name is recorded under the variable winner, then printed at the end of the code.

I formatted these values to display in a summary in the terminal and used the writer function in Python to also create a text file for them. When this project is downloaded from GitHub, there will already be a budget_data.txt file included in the pybank \'91Analysis\'92 folder, but if it is deleted and the program is run again, a new one should be created.\


Authors: 
Daniel Adamson
