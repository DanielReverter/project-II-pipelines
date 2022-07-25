# W3 Project - Data Pipeline
​
## Premise
​
In the professional chess scene, a player's rank is usually measured by their relative ELO. ELO is a number ranging from 0 to infinity (even though no human is rated above 3000 as of july 2022) such that two players with equal ratings who play against each other are expected to score an equal number of wins, and a player whose rating is 100 points greater than their opponent's is expected to score 64%.

A chess game can differ significantly from another one just because of the time each player has to make all their moves. In classical chess each player has more than 60 minutes to make all of their moves (the actual time depends on the set of rules for each tournament). Even though classical ELO is what is used to rank players, there are other (faster) time controls, and each player has an ELO ranking for each time control. A game is considered rapid if each player has between 15 and 60 minutes to make their moves. Games between 5 and 15 (per player) are considered blitz chess. There are faster time controls but they have no official ratings (bullet for 1 to 5 minute games and ultrabullet for anything less than that).
​
## Hypothesis
​
This project will attempt to prove whether age has any impact on top player performace in faster time controls (the hypothesis being that the younger a pro player is, the better they perform at faster time controls relative to their performance in classic chess).
​
## Project files
​
The main directory has 3 subdirectories:
* Input: The input folder holds the data used to analyze the hypothesis. It is a file containing relevant information for the best 200 chess players in the world (their rank, name, classical ELO, federation, birth year and number of games played). The file was downloaded from https://www.kaggle.com/datasets/surajjha101/fide-chess-rankings-updated.
* Output: Contains files created from the original data (enriched and cleaned dataset, plots, etc.) that are used multiple times through the project.
* src: Contains python files with all functions created specifically for this analysis.

​
In the root directory there are 2 Jupyter Notebook files that include all the code used in the project:
* Enriching and cleaning: In this file the original data is converted into a dataframe, cleaned and enriched with new data. This new data consists of each player's official rapid and blitz rating, scrapped from https://www.chess.com/ratings.
* Visualization: The last file is used to create plots that help visualize the data in order to check the hypothesis.
​
## Conclusion
​
The correlation coefficient between age and the relative performance of a player in different time controls is close to 0. Therefore it can be concluded that there is no correlationand my hypothesis was false.