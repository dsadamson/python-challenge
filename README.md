{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red140\green211\blue254;\red23\green23\blue23;\red202\green202\blue202;
\red212\green214\blue154;}
{\*\expandedcolortbl;;\cssrgb\c61176\c86275\c99608;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
\cssrgb\c86275\c86275\c66667;}
\margl1440\margr1440\vieww11520\viewh16040\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Tracking Financial and Election Data in Python\
\
-Overview:\
In this project, I was given two .csv files, which respectively contained a company\'92s profits and losses and recent election results. I was assigned to use Python to parse these .csv files and summarize them in an easily digestible analyses. In both .csv files, I was asked to find the total number of months and votes recorded. In the financial analysis program, I was asked to find the total profits or losses over multiple years; the average change in profits and losses between months in those years; and months when profits increased or decreased the most. In the election analysis, I was asked to list the candidates, find the number and percentage of votes they received, and to determine which candidate won the election. \
\
Each of these projects contained their own unique challenges and required unique solutions, as well. These challenges, their solutions, and the processes I used to come to these solutions will be explained below.\
\
\
- Pybank:\
To find the total number of months in the budget_data.csv file, I used a simple strategy. After opening the csv reader and programming Python to skip the headers of the .csv file, I created a \'91for\'92 statement to have my program iterate through the file. By writing \'91num_months += 1\'92, I told the program to add 1 to the num_months variable for each row it read, thereby calculating the number of months recorded in the .csv file. I used a similar method to calculate the profits and losses the company experienced over the given months, telling the program to then read the next row and add each value to the variable \'91profit_loss\'92, thereby adding all profits and subtracting all losses found in that row (profit_loss += int(row[1]).\
\
To find the greatest increase and decrease in profits required a rather lengthy series of lists and \'91if\'92 statements. By writing current_pl = int(row[1]), I told my program that each row it read would automatically become the current profit/loss value, which it would compare to the one that came before. Beginning my \'91if\'92 statements, I took into account that I could not compare the first value of row[1] to any value, so I set previous_pl to zero and started the comparison with the next value by writing \'91if previous_pl != 0\'92. To find the change in profits and losses for each month, I then simply told the program to subtract the current value from the previous, then to add the result of that calculation to a list:\
\pard\pardeftab720\partightenfactor0

\f1 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 			monthly_change\cf4 \strokec4  = \cf2 \strokec2 current_pl\cf4 \strokec4  - \cf2 \strokec2 previous_pl\cf4 \cb1 \strokec4 \
\cb3             	\cf2 \strokec2 change_list\cf4 \strokec4 .\cf5 \strokec5 append\cf4 \strokec4 (\cf2 \strokec2 monthly_change\cf4 \strokec4 )\
\cb1 \
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0 \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 Next, I set the program to search for the greatest monthly increase in profits. To do this required another \'91if\'92 statement, which I placed below the first. Setting the initial value of \'91greatest_increase\'92 to 0, I told the program to compare each value in row[1] to the value of \'91greatest_increase\'92. If that value was greater than the one stored in \'91greatest_increase\'92, it would become the new value stored in \'91greatest_increase\'92. This cycle would continue as the program iterated through row[1]. As the program found the greatest increase, it was also told to find the value in row[0] that represented the month in which the greatest increase in profits happened. I used a similar process to find the greatest decrease in profits, setting the \'91greatest_decrease\'92 value to 0, comparing monthly change values to it, and storing the row[0] value; however, this time I told the program to see if the monthly change was less than the current value stored in \'91greatest_decrease\'92.\
\
Finally, I was able to use the list of change values I created before the beginning of the \'91if\'92 statements to find the average change in profits and losses over the given months. I simply told the program to add together all the values in that list and divide them by the number of values in the list.\
\
I formatted these values to display in a summary in the terminal and used the writer function in Python to also create a text file for them. When this project is downloaded from GitHub, there will already be a budget_data.txt file included in the pybank \'91Analysis\'92 folder, but if it is deleted and the program is run again, a new one should be created.\
\
\
-Pypoll:\
To find the total number of votes in the election_data.csv file, I applied the same instructions as I did for the budget_data.csv file. As the program iterated through the .csv file, it added a value of 1 to the total_votes variable, thereby recording the sum total of the recorded votes.\
\
Then, I moved on to list each candidate in the race by instructing the program to move to row[2] of the .csv file, where the names of each candidate are recorded. I used an if statement to record candidates\'92 names to an empty list that I initialized with my other variables. First, I told the program to record candidates\'92 names if they were not the same (\'91!=\'92) as the candidate name that came before. To avoid repeated names, I then told the program to add the names to the list only if they were not in the list already.\
\
To find the number of votes each candidate received, I created three separate lists connected to each candidate. To avoid index errors, I first told my program to make sure that the first candidate list had 1 or more, then 2 or more, then 3 or more values. Then, using an \'92if\'85and\'92 statement, I had the program track the current candidate in each row, as it iterated through the .csv file. If that current candidate matched a candidate in the first candidate list, the program would append that row to the candidate\'92s individual list. The length of that individual list is set to provide the number of votes each candidate received. To find the percentage of the vote each candidate received, the program divides the length of their individual list by the total number of votes found at the beginning of the \'91for\'92 statement.\
\
Finally, to find the winner, a series of \'91if\'92 and \'91elif\'92 statements tells the program to compare each candidates vote percentages to one another. If one candidates vote percentage is greater than the other two, their name is recorded under the variable winner, then printed at the end of the code.\
\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 I formatted these values to display in a summary in the terminal and used the writer function in Python to also create a text file for them. When this project is downloaded from GitHub, there will already be a budget_data.txt file included in the pybank \'91Analysis\'92 folder, but if it is deleted and the program is run again, a new one should be created.\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 \
Authors: \
Daniel Adamson\
\
}