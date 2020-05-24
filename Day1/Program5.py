player1 = int(input("Enter runs scored by player1 in 60 balls: "))
player2 = int(input("Enter runs scored by player2 in 60 balls: "))
player3 = int(input("Enter runs scored by player3 in 60 balls: "))
strike_rate_1 = player1 * 100/60
strike_rate_2 = player2 * 100/60
strike_rate_3 = player3 * 100/60
print("Strike rate of player1: ",strike_rate_1)
print("Strike rate of player2: ",strike_rate_2)
print("Strike rate of player3: ",strike_rate_3)
print("Runs scored by player1 if they played 60 balls more: ",player1*2)
print("Runs scored by player2 if they played 60 balls more: ",player2*2)
print("Runs scored by player3 if they played 60 balls more: ",player3*2)
print("Maximum number of sixes hit by player1: ",player1//6)
print("Maximum number of sixes hit by player2: ",player2//6)
print("Maximum number of sixes hit by player3: ",player3//6)
