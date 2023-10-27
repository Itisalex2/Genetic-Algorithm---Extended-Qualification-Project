Introduction

Computer science is one of the most rapidly growing fields in modern history. Being my subject of interest, I decided to create an artefact that uses computer programming. The  program was completed after researching and coding over the course of four months. It consists of two sections - an interface which allows the user to input a level, and a genetic algorithm that beats that level. In this essay I’ll talk about the research I did, the important skills I learnt and how my project could improve in the future.

Research

The idea that prevailed in my initial brainstorm was to code a game and a program that could beat that game. There were a few possible options that I could model my game after, but ultimately it was based off of “World’s Hardest Game” (Snubby, 2008) after some research and testing. I chose this game because I played it before and had a good understanding of how its mechanics worked. The objective of the game is to navigate a square around obstacles and enemies in order to travel from a start point to its corresponding end point.
(Code bullet, 2018, 07:53)

List of resources:
Books:
Introduction to Evolutionary Computing (Eiben & Smith, 2016)
Articles:
Using genetic algorithms as a core gameplay mechanic(Kachmar & Terletskyy, 2016)
Applying Genetic Algorithms to Game Search Trees(Hong, Huang, & Lin, 2002)
Using Genetic Learning in Weight-Based Game AI (Kordsmeier, 2015)
Websites:
Neural network + genetic algorithm + game = ❤ (Dutta, 2020)
Genetic algorithm in machine learning using python (Choudhary, 2020)
Videos:
Genetic algorithm playlist (Shiffman, 2016)
Genetic Algorithms Explained By Example (Kie Codes, 2020a)
Genetic Algorithms from Scratch in Python (tutorial with code) (Kie Codes, 2020b)
AI learns to play 2048 (Code Bullet, 2018)
How to program a game! (in Python) (Keith Galli, 2018)
Professional Code Refractor (Cleaning Python Code & Rewriting it to use Classes) (Keith Galli, 2020)

Objectives before research:
Make a game where a user can input their own level
Make an algorithm that can beat that level

My initial EPQ title was “make a code that can beat any level the user suggests”. I wasn’t quite sure of exactly what my code would encompass, but vaguely, my aim was for it to include some sort of game and an algorithm that allows the computer to find a suitable way to beat a level.

Using my Christmas break, I finished all of my planned research. There was a substantial amount of information for the book so I filled a document with notes (see appendix J, page 49) so that I could look back at it more easily. The two methods of beating a game that I looked at were neural networks + game search trees(more mathematical) and genetic algorithms(more simple and visual). After reading the article about neural networks (Dutta, 2020), I realised that neural networks were not the type of approach I was looking for as it emphasised the learning aspect of the genetic algorithm (this is explained in more detail in the reflection section). Similarly, game search trees (Hong, Huang, & Lin, 2002) and graphical weighting (Kordsmeier, 2015) were unnecessary. The videos on the topics of programming a game (Keith Galli, 2018) (Keith Galli, 2020) and genetic algorithms (Shiffman, 2016) (Kie Codes, 2020a) (Kie Codes, 2020b) persuaded me that genetic algorithms were the best way to approach this project and that it was possible within my time frame.

By this point I had a clear grasp of what I wanted for my EPQ project. Using what I learned from my research, my new aim was to create a genetic algorithm that could intelligently find a solution to any problem by simulating through a population. This process would not involve the use of neural networks, game search trees and graphical weighting. Instead, it would purely simulate natural selection by advancing each generation (this process is explained in more detail in the artefact creation section). The game that the user would create would be based off of “World’s Hardest Game” (Snubby, 2008) as mentioned in the previous page. It was at this point that I finalised my EPQ title in order to make it more precise: Genetic Algorithm Sandbox Game

In summary, before my research, I vaguely pointed out that my objectives were to create a game and an algorithm that could beat that game without a solid idea of how to go about doing that. After I finished my research, rather than loosely defining what my algorithm was going to be, I knew exactly that a genetic algorithm was needed for this project. I also knew the specific game that the game I created would be based off of.

Objectives after research:
Make a game using Python based off of “World’s hardest game” where a user can input their own level
Make a genetic algorithm that can find a solution to any level the user inputs
Artefact creation
Game
For the first few days I worked on creating a general framework. I generated, using pygame (Lenard Lindstrom and others, Pygame Front Page¶ 2000), an interactive interface. Then I added pieces of code that allowed the user to move a square around(see appendix A, G & H, pages 14, 39 & 44). This was done by detecting whether the event identifier(anything the user inputs is considered an event) matches that of the arrow keys.

In the following week obstacles, start and end points, and enemies were introduced into the game(see appendix D, F & I, pages 32, 37, 48). This section was mostly taught through the youtube video, “How to program a game! (in Python)”, by Keith Galli (Gailli, 2018). The game detects whether an obstacle touches a player by storing the vertices of all the obstacles, then calculating whether the player passes through. Start and end points mark the areas in which the square spawn at and need to end at respectively. This was relatively simple to code as all I needed to do was generate a square at their location or compare them with where the player is. Enemies travel to and from two points dictated by the user; using trigonometry, the computer finds out the exact path that the enemies need to travel in order to commute between its two destinations. Through a process similar to detecting obstacles, the computer detects whether a player touches an enemy. If true, the player teleports back to its spawn point.

Program controls
Object
How to control/set-up
Player
Arrow keys to move
Enemy
Left shift to initialise the enemy’s position. Right shift to finalise the enemy’s position.
Genetic Algorithm
Space bar to start the genetic algorithm. “R” to remove the genetic algorithm.
Obstacle
Mousedown to initialise the obstacle’s position. Release to finalise the obstacle’s position.

Genetic algorithm
Key term definitions based off of the book “Introduction to evolutionary computing” (Eiben, 2016)
Term
Definition
Gene
A value that acts as a unit of heredity
Member
An object that contains certain genes
Population
A collection of members
Fitness value
A numerical value assigned to each member based on a criteria (e.g. how close the member is to an end point)
Average fitness value
The average fitness value of a subset of a population
Generation
The full set of results for a genetic algorithm iteration (similar to real life)
Generation time limit
The time given for each generation until the members are evaluated and given a fitness value
Static generation time limit
Generation time limit remains constant regardless of generation
Incremental generation time limit
Generation time limit increases as generation count increases. The time limit could stop increasing after a certain number of generations.
Selection
Similar to natural selection, higher fitness members have a higher chance of being selected as a parent for the next generation
Linear ranking
A selection process where the probability of members being selected is proportional to their fitness value
Geometric ranking
A selection process where the probability of members being selected increases exponentially as their fitness value increases
Crossover
The act of producing a new set of genes based off of two existing set of genes
Mutation
A random changing of a gene
Mutation rate
The chance that each gene gets mutated


With the game mechanics finished, I proceeded to work on the genetic algorithm that could beat the level. In summary, a genetic algorithm is a step by step procedure that solves a problem by mimicking natural selection (Katoch et al., 2020).
(Research Gate, 2016)

A post on data science plus by Abhinav Choudhary (Choudhary, 2020) explains this process in a more detailed yet concise way (it helped me understand it a lot better). The genetic algorithm process starts off by randomly initialising the population participating. The clock ticks (similar to how time passes in real life) and this generation is assigned a fitness value based on how well they do. Once the parents are chosen through the selection process, crossover and mutation functions are applied to them, producing the next generation. The clock ticks once again and this cycle repeats until a certain criteria is met (e.g. 100 generations). The member with the highest fitness value is the best solution the computer generated in the given time.

   def populationReset(self):
   def initialisePopulation(self,enemy,finishBlit):
   def fitnessScore(self):
   def selection(self):
   def crossover(self):
   def mutation(self):
   def timeLimitDetection(self,enemy,finishBlit):
Final product

Tweaking variables each time, I ran a few easy test levels. The variable values of test one and two were inspired by the book “Introduction to evolutionary computing” (Eiben, 2016).

Test Number
Mutation rate
Selection strategy
Time limit for each generation
Result
1
30%
Linear ranking
Static (30 seconds)
25% increase in average fitness after 200 generations
2
2%
Geometric ranking
Static (30 seconds)
26% increase in average fitness after 200 generations
3
5%
Geometric ranking
Incremental - Starting with 3 seconds, each generation gets 0.1 seconds more time than the previous. Maximum of 30 seconds.
Solution found after 176 generations



It seemed that the best combination was a low mutation rate, geometric ranking and an incremental time limit. However, this may be unreliable as I didn't have several trials for each variable combination. It may also be inaccurate as multiple variables were changed between tests instead of just one. This should be worked upon in the future.

Having finished tweaking the variables and code, I let the computer run overnight during a school week in order to beat a moderately hard level. This process took a few tries since most of the time the program wasn’t able to find a solution before school started the next day. However, on the fifth day, a solution was found after close to seven hours of simulation. Success!

Reflection and limitations

Many things can be learned from this project. Starting with research, the book that I read, Introduction to Evolutionary Computing (Eiben & Smith, 2016), went into university-level depth after a few hundred pages. This meant that it became hard to understand what was going on. I decided to stop reading since I had already learned the basic concepts. In the future, I will need to take note of the difficulty of the resources that I’m looking at. Citations were also a key learning point in this project. I used the APA-format before but this was the first time that in-text citations were necessary.

Furthermore, this was my first time working on a project of this size. At the start, I had trouble remembering and completing all the tasks. For example, I almost missed a meeting with my supervisor since I didn’t write the date of the meeting down. Realising I had to change my approach to this project, I adopted the use of Gantt charts and to-do-lists. I also recorded exactly what progress was made on the days that I worked. As time passed and I got a better understanding of my program, I updated my timeline. Comparing the timeline from the beginning to the final, a substantial difference can be seen (graphs on the next page). Initially, I thought that the deadline would be around march. This ended up changing to May. The research and artefact creation (in the first graph research meant research + artefact creation) took a lot longer than I expected as well, therefore in the future I should allocate more time to each section of the project. This is because having extra time (starting the project earlier, using more of the break time on the project etc) is much better than running on a tight schedule. A section that I could improve upon in terms of planning is that my plans were often a bit too vague. For example, my to-do-list included “make the code for machine learning” and “make the game”, but I didn’t specify how I was going to go about doing it. Individual plans were only added after my discussion with my supervisor, so this is something that I should initiate in the future.

Lastly, there are quite a few ways that this project can be improved upon. The genetic algorithm simulation took a solid seven hours to complete. This is because I programmed it so that the simulation would run at sixty loops per second (my computer screen’s refresh rate) in order to capture the entire process. Using the computer’s own processing speed, the simulation would be completed in a much shorter time. Therefore, I could have added an option for the program to only display the final solution. Another thing that could have been changed is the magnitude of each square’s movement. In the simulations, the squares seem to vibrate about in a certain position after a while. This might be because for every turn the squares move too little, so on average they don’t move anywhere. By increasing the distance each square moves, there might be more variations and extremities, leading to a solution being found quicker. However, this is only an assumption, which means further testing is required. The final change that I could have made is the nature of the algorithm used to beat the level. Instead of a genetic algorithm that beats a level through natural selection, I could have used a deep learning (machine learning) (Jones, 2019) algorithm that learns how to beat the specific objects inside the game. The program would be trained under an array of different levels, creating a neural network (Dutta, 2020) which allows for decision making. The benefit of a deep learning algorithm is that it is quicker since it finds a solution to any level the user inputs without having to simulate the way the genetic algorithm does. However, it is much more complicated to code and you need to train the algorithm with a huge number of levels, making it time consuming to make.




























References
Anthony Kordsmeier, D. (2015). Using Genetic Learning in Weight-Based Game AI (pp. 1–25) [Undergraduate Dissertation]. https://core.ac.uk/download/pdf/72841392.pdf
Choudhary, A. (2020, May 27). Genetic Algorithm in Machine Learning using Python. DataScience+. https://datascienceplus.com/genetic-algorithm-in-machine-learning-using-python/
Dutta, S. (2020, April 18). Neural Network + Genetic Algorithm + Game = ❤. Medium. https://towardsdatascience.com/neural-network-genetic-algorithm-game-15320b3a44e3
Eiben, A. E. (2016). Introduction To Evolutionary Computing. Springer-Verlag Berlin An.
Evan. (2018, July 6). AI learns to play 2048. www.youtube.com. https://www.youtube.com/watch?v=1g1HCYTX3Rg
Evan, E. (2019, July 14). AI Learns to play the World’s Hardest Game. www.youtube.com. https://www.youtube.com/watch?v=Yo2SepcNyw4&t=246s&ab_channel=CodeBullet
Gailli, K. (2018, March 16). How to Program a Game! (in Python). Www.youtube.com. https://www.youtube.com/watch?v=-8n91btt5d8&t=19s&ab_channel=KeithGalli
Galli, K. (2020, March 23). Professional Code Refactor! (Cleaning Python Code & Rewriting it to use Classes). Www.youtube.com. https://www.youtube.com/watch?v=731LoaZCUjo&feature=youtu.be&ab_channel=KeithGalli
Jones, T. (2019, June 7). Machine learning and gaming. IBM Developer. https://developer.ibm.com/technologies/artificial-intelligence/articles/machine-learning-and-gaming/
Research Gate. (2016). The genetic algorithm process. In Research gate. https://www.researchgate.net/publication/303599913/figure/fig13/AS:669671216934932@1536673468678/The-Genetic-Algorithm-process-16.png
Katoch, S., Chauhan, S. S., & Kumar, V. (2020). A review on genetic algorithm: past, present, and future. Multimedia Tools and Applications. https://doi.org/10.1007/s11042-020-10139-6
Kie. (2020a, June 14). Genetic Algorithms Explained By Example. www.youtube.com. https://www.youtube.com/watch?v=uQj5UNhCPuo&feature=youtu.be&ab_channel=KieCodes
Kie. (2020b, June 21). Genetic Algorithm from Scratch in Python (tutorial with code). Www.youtube.com. https://www.youtube.com/watch?v=nhT56blfRpE&ab_channel=KieCodes
Korstanje, J. (2020, June 1). A Simple Genetic Algorithm from Scratch in Python. Medium.
https://towardsdatascience.com/a-simple-genetic-algorithm-from-scratch-in-python-4e8c66ac3121
Mallawaarachchi, V. (2020, March 1). Introduction to Genetic Algorithms - Including Example Code. Medium. https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3#:~:text=A%20genetic%20algorithm%20is%20a,offspring%20of%20the%20next%20generation.
n Kachmar, B., & Terletskyy, O. (2016). Using genetic algorithms as a core gameplay mechanic (pp. 1–40) [Master Thesis]. https://web.wpi.edu/Pubs/ETD/Available/etd-042816-125758/unrestricted/Kachmar_Terletskyy_MS_Thesis_Final.pdf
Pygame Community. (2000, October 28). Pygame Front Page — pygame v2.0.0.dev15 documentation. Www.pygame.org. https://www.pygame.org/docs/
Shiffman, D. (2016, June 29). 9: Genetic Algorithms - The Nature of Code - YouTube. Www.youtube.com. https://www.youtube.com/playlist?list=PLRqwX-V7Uu6bJM3VgzjNV5YxVxUwzALHV
Snubby, L. (2008). World’s hardest game (online version) [video game]. Snubby Land.

Tzung-Pei, H., Wen-Yang, L., & Ke-Yuan, H. (2002). Applying genetic algorithms to game search trees. 1–26. Research Gate. https://www.researchgate.net/publication/220176829_Applying_genetic_algorithms_to_game_search_trees








