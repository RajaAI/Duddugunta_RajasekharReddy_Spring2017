# Final Project
# Data Analysis on the data of Terrorism using Python

In this project, I explored a dataset containing information about global terrorism acts since 1970, and attempted to make the findings as visual as possible. Most of the analysis is done globally, but one of the scripts focuses on terrorism in specific countries. In order to simplify and make the analysis much more efficient, I chose to discard over 100 attributes, and only retain a few of the key variables such as date, attack type, location, and casualties. It should also be noted that all information from 1993 is missing from this database as a result of human error. 

**Analysis 1** :

Packages Used:
Numpy
Pandas
Matplotlib
Seaborn

Read globalterrorismdb_0616dist.CSV in order to create plot.
1. The number of attacks occured each year all over the world is calculated. 

![ana_1-1](https://cloud.githubusercontent.com/assets/25700604/25309992/711db54e-27a8-11e7-9817-693d78c1915b.PNG)

With the help of this, I came to find that 1992 has been the most troublesome year, followed by 2008 and 1991.

2. Finding the percentage of most occured type of attack

![ana_1-2](https://cloud.githubusercontent.com/assets/25700604/25310053/7a1e61d8-27a9-11e7-84d7-b0883296b364.PNG)

This plot provides the information that Bombing/Explosion leads the list with around 44-47% of the total terrorist related cases over the years. Followed by Armed Assault with 25%.

3. Finding the most occured type of attack on the top 3 crime rate years

![ana_1-3](https://cloud.githubusercontent.com/assets/25700604/25310070/d8b0dfc8-27a9-11e7-951f-50b4231c6cf7.PNG)

By taking the output of previous analysis i.e the top 3 years in crime rate, I came to know the trend of most occured attack type.

4. I have divided the data into 4 groups based on the range of years.Then Finds the the most occured attack type in 4 different year groups[(1970-1980),(1980-1990),(1990-2000),(2000-2009)].

![ana_1-4](https://cloud.githubusercontent.com/assets/25700604/25310137/52fae642-27ab-11e7-9b43-3ae86cf1d2e9.PNG)

With the help of this, I Found the most occured attack type of different groups of year range.

5. Finding the most effective way that wounded maximum number of people

![ana_1-5](https://cloud.githubusercontent.com/assets/25700604/25310145/9dcbfb3e-27ab-11e7-99a5-dee55954b4c8.PNG)

As we saw in the previous step, bombing/explosions was the highest form of attack, followed by armed assault. But this is not the case when it comes to number of people killed. Armed assault clearly takes the lead killing 42% of the total people, whereas bombing/explosions killed 38%. In case of people getting wounded, bombing/explosions left 75% of total people wounded, whereas armed assault with 15%. Conclusion: Most effective way that killed maximum number of people is Armed Assault [42%]. Most effective way that wounded maximum number of people is Bombing/Explosions [75%]

6. Finding the percentage of people got killed and wounded of all the four groups of years

![ana_1-6](https://cloud.githubusercontent.com/assets/25700604/25310162/4278d31e-27ac-11e7-92ef-cf62f66e2906.PNG)

This pie chart clearly helps in knowing how Group 4 [2001-2009] dominates in both killed and wounded.

**Analysis 2**:

1. Finding the most troubled regions in the world that got effected by Terrorists.

![ana_2-1](https://cloud.githubusercontent.com/assets/25700604/25310190/daa80c68-27ac-11e7-93f0-cd69d2c5ec22.PNG)

This Analysis gave the information of Most troubled regions which are: 
                          1. South America
                          2. Middle East & North Africa
                          
2. Finding the percentage of people got killed and wounded of each region by the effect of Terrorism

![ana_2-2 1](https://cloud.githubusercontent.com/assets/25700604/25310205/476acd54-27ad-11e7-83b6-1f5ed9d912ac.PNG)
![ana_2-2](https://cloud.githubusercontent.com/assets/25700604/25310207/4a42aa2e-27ad-11e7-97de-3ebfe3d651c9.PNG)

This provides me the Information that in Middle East & N.Africa, 22.91 % people got killed and 33.67 % wounded from the total people killed/wounded by terrorist attacks and in South Asia, 22.29 % killed, 27.02 % wounded.

3. Now we are going deeper into these 2 regions: Taking the top attacked countries from two regions which we evaluated in the previous step for analysis and plotting the graph with attack type

![ana_2-3](https://cloud.githubusercontent.com/assets/25700604/25310247/2c740b9a-27ae-11e7-83cd-454c54b59601.PNG)

We came to know from the above analysis that Iraq from Middle East and India from South Asia have the highest number of terrorist. Now the above plot gives us the percentage of attacks by attack type.

4. Finding the Top 15 dangerous places in world that got effected by terrorists.

![ana_2-4](https://cloud.githubusercontent.com/assets/25700604/25310261/987989fa-27ae-11e7-85a3-528fc2c2c480.PNG)

**Analysis 3** :

Finding the year and the prime minister during those years, where the occurence of terrorism was more. 
We would be splitting terrorism attacks in India, by time in office of each Indian Prime-minister.

![ana_3-1](https://cloud.githubusercontent.com/assets/25700604/25310265/c210ed94-27ae-11e7-828d-bf49a21fcfcd.PNG)

From the above chart I analyzed that in the years of 2008 and 2009 the occurence of terrorist activities was more, during which the prime minister of India was Manmohan singh

**Analysis 4** :

1. Finding the Total acts of Terrorism and average number of deaths per act.

![ana_4-1](https://cloud.githubusercontent.com/assets/25700604/25310316/d32ebd26-27af-11e7-855c-3d9b2eca39c8.PNG)

This analysis provides me the information of Total acts of Terrorism of each year and average number of deaths per act of each year.

2. Finding the average number of people killed per attack by region

This analysis shows that the average number of people killed per attack is more in the region of sub-saharan based on the output.

**Analysis 5** :

In this, the Analysis was done on Terrorism of USA.

1. Finding the Terrorist Attacks happened in US in each Year

![ana_5-1](https://cloud.githubusercontent.com/assets/25700604/25310337/786f8dc4-27b0-11e7-89c2-b25bf263b1f5.PNG)

This analyis gives the year where the the number of terrorist activities in US is high.


2. Finding the Terrorist Attacks in US by each type of categories

![ana_5-2](https://cloud.githubusercontent.com/assets/25700604/25310342/8d64f840-27b0-11e7-93fc-82aeb5c0f058.PNG)

This analyis gives on what specific category the number of terrorist activities is more. So that they can be alerted ahead of time and take some precautionary methods.

3. Terrorist Attacks in US by each type of Weapon Category

![ana_5-3](https://cloud.githubusercontent.com/assets/25700604/25310347/a69e36aa-27b0-11e7-9c3b-e5e1b98cc89c.PNG)

This analyis gives by using which specific type of weapon, the injuries and fatalities occured. With the help of this analyis, the government can restrict the produxtion, use, supplying of arms to other countries and people.


**With the help of this analysis, one can take precautionary measures, actions against particular cities, countries, Strengthening their armed forces, knowing under whose tenure the terrorism occured most, The reasons for occurence of high terrorism.**










