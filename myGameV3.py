import random

# First round of dice rolls for three players
player1_roll1 = random.randint(1, 6)  
player2_roll1 = random.randint(1, 6) 
player3_roll1 = random.randint(1, 6) 

# Second round of dice rolls for three players
player1_roll2 = random.randint(1, 6)  
player2_roll2 = random.randint(1, 6) 
player3_roll2 = random.randint(1, 6)  

#Calculates the total scores for each of the player
player1_score = player1_roll1 + player1_roll2 
player2_score = player2_roll1 + player2_roll2  
player3_score = player3_roll1 + player3_roll2  

# Calculate averages
average1 = (player1_score + player2_score + player3_score) / 3  # Float division
average2 = (player1_score + player2_score + player3_score) // 3  # Integer division



# Displays the calculated averages
print(f"Average 1 (float division) is: {average1}")
print(f"Average 2 (integer division) is: {average2}")

