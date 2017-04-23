Question 1: Analysis of Enron scandal
Summary about the scandal
The Enron scandal, publicized in October 2001, eventually led to the bankruptcy of the Enron Corporation, an American energy company based in Houston, Texas, and the de facto dissolution of Arthur Andersen, which was one of the five largest audit and accountancy partnerships in the world. In addition to being the largest bankruptcy reorganization in American history at that time, Enron was cited as the biggest audit failure.
Analysis 1:
Getting the most sent mails to and from CEO Jeff Skilling
Steps:
# import all required libraries
# creates a new file if doesn't exist else moves to the required file
# Parse the file using parser
# returns the mail id where ever the string 'To' presents
# appends to mailTo list
# returns the mail id where ever the string 'From' presents
# appends to mailFrom list
Analysis 1 Result:
Top email sent by CEO Jeffery Skilling:
pallen@enron.com, stagecoachmama@hotmail.com, ina.rangel@enron.com, jsmith@austintx.com, pallen70@hotmail.com, k..allen@enron.com.
Top email recieved to CEO Jeffery Skilling:
phillip.allen@enron.com, k..allen@enron.com, arsystem@mailman.enron.com, no.address@enron.com, webmaster@earnings.com.
Analysis 2:
Finding the top 10 frequent words of CEO Jeffery Skilling
Steps :
# imports all required libraries
# Walks through the given path
# creates a new file if doesn't exist else moves to the required file
# imports stop words
# import reg expression
# Counts all the word count and returns top 10 words
Analysis 2 Result:
Top 10 words in the CEO email are: good, enron.com, need, bob, phillip, would, screens, time, oct, x-to.
Analysis 3:
    Finding the number of mails sent on each day
Steps :
# imports all required libraries
# Walks through the given path
# creates a new file if doesn't exist else moves to the required file
# Initialize 7 variables to value 0
# Analysis was done on 2500 mails
# Loops and increments the value for each day

Analysis 3 Result:
​
    In 2500 mails
    
1. Mails sent by enron on Monday: 571
    
2. Mails sent by enron on Tuesday: 515
    
3. Mails sent by enron on Wednesday: 564
    
4. Mails sent by enron on Thursday: 417
    
5. Mails sent by enron on Friday: 345
    
6. Mails sent by enron on Saturday: 33
    
7. Mails sent by enron on Sunday: 55
Question 2: Analysis on Data on NYT
Data Collection and Storing :
Input: Article Search API from NYT API NYT API Documentation
Downloading Sports content for the year 2016
Storing the json data sorted with respect to the sport name
Analysis 1:
# Finding the number of articles printed by every source during 2016 in the category Sports

# Determining which Sport had the most number of articles printed for each month in the year 2016

# Writing the results to a csv file
Steps:
 # import all required libraries

 # collects required data by hitting the NYT API

#  Walks through the link

# Reads all the Json files

# Counts all the articles for each month in the year of 2016
Analysis 1 Result:
{1: 307,
2: 294, 3: 207, 4: 359, 5: 169, 6: 212, 7: 297, 8: 280, 9: 318, 10: 159, 11: 474, 12: 456}
Analysis 2:
# import all required libraries

# Parse the data in one Json file

# Collect different types of section names based on the section name

# plot the graph with different section names
Analysis 2 Result:
![daup](https://cloud.githubusercontent.com/assets/25700604/25116193/2fe21836-23d9-11e7-9b58-8ab85f4e9033.png)

Analysis 3:
# Analyzing the percentage of category of articles that make up the front page story
# Displaying the results using matplotlib and pie chart
Steps:
# collects data from all json files 

# figure out the category of articles based on the category name 

# Counts the number of times the particular category made up the front story

# plot the data in pie chart accordingly
In [ ]:

Analysis 3 Result:

![pie](https://cloud.githubusercontent.com/assets/25700604/25116219/56904c5a-23d9-11e7-9662-3b37ca62ff20.png)
