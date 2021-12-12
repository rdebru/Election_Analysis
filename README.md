# **PyPoll with Python**
	
## **Overview of Election Audit** 
* Colorado board of elections employee, Tom asks you to help with analysis of the election Audit of a local congressional election.
Seth, Tom's Manager wants to automate the process of the election Audit. we will analyze the election data and write a script that calculates and generates the following report 
* The total number of votes cast
* The complete list of candidates who received votes
* Totals number of votes each candidate received
* Percentage of votes each candidate won
* The winner of the election based on popular vote
* The script can be reused not only to audit other congressional states but also senatorial districts and local elections.
 
### Purpose 
* analyze and modify the script to calculate and display (the voter turnout for each county, the percentage of votes from each county out of the total count and the county with the highest turnout) to the terminal screen. As well the results should be saved to `election_analysis` text file. Also, to create a summary report based on the analysis, results of the election data and the script.


## **Election-Audit Results** 

![Election Results Terminal](C:/Users/Ruth/OneDrive/Desktop/Class_Work/Module_3/HW3_Submission_Python/Analysis/Election_Results_Terminal.png) 

* How many votes were cast in this congressional election?
	* Total votes cast in the congressional election were 	369,711 votes

* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
	* The number of votes and the percentage of total votes 
		* For Jefferson county is (38,855) votes and `10.5%` 	
		* For Denver county  is (306,055) votes and `82.8%` 
		* For Arapahoe county is  (24,801) votes and `6.7%` 
		
* Which county had the largest number of votes? 
	* The County that had the largest number of votes is Denver

* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
	* The first candidate is Charles Casper Stockham who 	recieved (85,213) number of votes and `23.0%` of the vote
	* The second candidate is Diana DeGette who recieved 	(272,892) number of votes and `73.8%` of the vote
	* The third candidate is Raymon Anthony Doane who received 	(11,606) number of votes and `3.1%` of the vote

* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
	* The candidate who won the election is Diana DeGette who recieved (272,892) number of votes and `73.8%` of the vote
	 

## **Election Audit Summary** 

* The election Audit process is automated by writing a script. The script calculates the total number of votes cast, (the number of votes and the percentage of total votes for each county), the county with the highest turnout, the number of votes and the percentage of the total votes for each candidate and the winner of the election based on popular vote. The results are displayed into the screen and saved into a text file. You can see from image above for example which county has the lowest turnout, and this helps with the decision making if additional resources are needed to be added to that county for future elections.
* The script can also be used with some modifications for any election. For example, if we want to analyze election data for federal election that uses states instead of counties, first the state election data must be added to the input `election_results` file. Then script can easily be modified by switching county list, dictionary and names into the state. we use same calculations and (for,if) statements. It can also be used for election data with districs in the same way.
* Another example if we want to analyze election data to see the results for each cities and how the candidates performed in each one. First the input file `election_results` has to be updated to include data for cities. Then in the script switch the reference from counties to cities. We use same calculations and (for,if) statements. This will help in determining cities that have largest turnouts and the cities that helped the candidates be the winner of the election.
* Another example is if we want analyze election data that has the profile of the candidates, (Age and Sex and other data). First the data must be added to the input file `election_results` file. Then we can modify our script by adding statements in the if block. Then store the data in `candidate_votes` dictionary with candidate details. This will help with targeting our specific population that those candidates attract or connect with and can used for current or future elections.
		
