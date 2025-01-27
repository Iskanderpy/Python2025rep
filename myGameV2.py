import random

# First round of dice rolls
player1_roll1 = random.randint(1, 6) 
player2_roll1 = random.randint(1, 6)  
player3_roll1 = random.randint(1, 6)  

# Second round of dice rolls
player1_roll2 = random.randint(1, 6)  
player2_roll2 = random.randint(1, 6) 
player3_roll2 = random.randint(1, 6)  #

# adds up both roles for each player
player1_score = player1_roll1 + player1_roll2
player2_score = player2_roll1 + player2_roll2
player3_score = player3_roll1 + player3_roll2

#shows both roles and their combined
print(f"Player 1 rolls: {player1_roll1}, {player1_roll2} = Total score: {player1_score}")
print(f"Player 2 rolls: {player2_roll1}, {player2_roll2} = Total score: {player2_score}")
print(f"Player 3 rolls: {player3_roll1}, {player3_roll2} = Total score: {player3_score}")

#max figures out whats the highest 
highest_score = max(player1_score, player2_score, player3_score)

print(f"The highest score is: {highest_score}")
