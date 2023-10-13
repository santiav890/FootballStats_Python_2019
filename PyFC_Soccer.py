
##Keeping track of a top striker's goal ratio
Messi_Apps=35
Messi_o_box=8
Messi_Asts=9
Messi_Shots=141
Messi_Goals=30
Messi_Ratio=Messi_Goals/Messi_Shots
MessiGA=Messi_Goals+Messi_Asts
MessiOboxRatio=Messi_o_box/Messi_Goals*100


CR_apps=33
CR_Asts=3
CR_Shots=142
CR_Goals=31
CR_Ratio=CR_Goals/CR_Shots
CRGA=CR_Goals+CR_Asts
CR_in_box=28
CRinBoxRatio=28/31*100

print("Messi's goal/shot ratio is:")
print(Messi_Ratio)
print("CR goal/shot ratio is:")
print(CR_Ratio)

print("Cristiano Ronaldo has a slighly better goal rate than Messi, meaining he is a more effective goalscorer")

print("By adding their assists to their goals their stats look like this:")
print("Messi: "+str(MessiGA) +" GA")
print("Ronaldo: "+str(CRGA)+" GA")

Messi_GoalContribution=MessiGA/Messi_Apps
CR_GoalContribution=CRGA/CR_apps
##print(Messi_GoalContribution)
##print(CR_GoalContribution)
print("Messi has a higher influence in the goal creation, having a goal contribution per match of: "+str(Messi_GoalContribution))
print(" ")
print("Now of course we have to take into consideration the profile of both footballers")
print("Messi likes to play a lot in deep areas, creating chances, key passes and scoring from rigth/central areas of the pitch ")
print("Messi also contributes a lot with long range goals, being a total of " +str(MessiOboxRatio)+ "% of his goals" )
print("On the other hand, Cristiano likes to move around the left/central areas and has a lot of influence while being close to the box")
print("Ronaldo is capable of taking control of the area scoring a " +str(CRinBoxRatio)+"% of his goals from inside the box")
print("Different teams have different needs, we will analyze 2 teams in particular to see which player would be more useful")
print(" ")
print(" ")
print("LIVERPOOL FC:")
print("Liverpool had a very difficult season with a lot of injuries and uneffective playing style")
print("Liverpool FC, scored 97 goals less season, a lot less compared to the 117 that they scored during the 19/20 season")
print("Liverpool also recieved 10 more goals in comparisson to the title-winning season")
print("This caused Liverpool to make 30 points less than the year before and to drop from 1st to 3rd in a single year")
print("Two of the 3 Liverpool main strikers had a very bad season, Mane and Firmino, while Salah, actually improved his numbers")
print("Salah is not the problem and his area of influence is very similar to Messi's")
print("Salah likes to play in the right wing, cutting to the middle, just like Messi")
print("Signing Messi would only cause a problem inside the pitch, having 2 player trying to work in the same areas")
print("On the other hand, Cristiano likes to move from left to central areas, just like Mane and Firmino")
print("Both Mane and Firmino had a very low goal rate last season compared to Ronaldo's")
print("Ronaldo gives you around 20/30 goals per season granted, which would mean Liverpool could have the same numbers as in 19/20")
print("Both Messi and Ronaldo are great players but Liverpool really needs someone like CR the most")
print(" ")
print(" ")
LewanGoalCtrb20=55/159
LewanGoalCtrb21=48/139
print("FC BAYERN:")
print("Bayern had a great year, winning the league one more time, but it was slightly worse than the one before in which they won the sextuple")
print("Looking at the numbers we can quickly notice that Bayern scored 20 goals less than the year before")
print("One of the reasons is that Bayern lost both Coutinho and Perisic who scored 19 goals during the 19/20 season")
print("Also, Gnabry scored 12 goals less and Lewandowski was injured during the key UCL series against PSG")
print("There is a big gap between their top scorer Lewandowski(48) and their second goalscorer, Muller (15)")
print("Bayern's goalscoring capacity depends more and more form Lewandowski")
print("Lewandowski's goal contribution in 19/20: "+str(LewanGoalCtrb20))
print("Lewandowski's goal contribution in 20/21: "+str(LewanGoalCtrb21))
print("Another big factor is that Bayern lost Thiago, who completed 3.6 driblles and created at least 1 big chance per game")
print("Thiago was the brain of FC Bayern and contributed a lot to create chances and key passes to the wingers, specially doing so form deep positions")
print("Lewandowski is probably the best striker in the world, so Bayern do not really need another area player")
print("This really discard Cristiano as a big priority, central area is not Bayern's problem")
print("On the other hand, Bayern could use a hand of a winger who can contribute whith goals, hepling Lewan with that task")
print("But not only that, Messi can actually also help a lot with passes an creativity from deep positions, just like Thiago")



