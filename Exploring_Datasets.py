# Importing course packages; you can add more too!
import numpy as np
import math

# Import columns as numpy arrays
baseball_names = np.genfromtxt(
    fname="baseball.csv",  # This is the filename
    delimiter=",",  # The file is comma-separated
    usecols=0,  # Use the first column
    skip_header=1,  # Skip the first line
    dtype=str,  # This column contains strings
)
baseball_heights = np.genfromtxt(
    fname="baseball.csv", delimiter=",", usecols=3, skip_header=1
)
baseball_weights = np.genfromtxt(
    fname="baseball.csv", delimiter=",", usecols=4, skip_header=1
)
baseball_ages = np.genfromtxt(
    fname="baseball.csv", delimiter=",", usecols=5, skip_header=1
)

soccer_names = np.genfromtxt(
    fname="soccer.csv",
    delimiter=",",
    usecols=1,
    skip_header=1,
    dtype=str,
    encoding="utf", 
)
soccer_ratings = np.genfromtxt(
    fname="soccer.csv",
    delimiter=",",
    usecols=2,
    skip_header=1,
    encoding="utf", 
)
soccer_positions = np.genfromtxt(
    fname="soccer.csv",
    delimiter=",",
    usecols=3,
    skip_header=1,
    encoding="utf", 
    dtype=str,
)
soccer_heights = np.genfromtxt(
    fname="soccer.csv",
    delimiter=",",
    usecols=4,
    skip_header=1,
    encoding="utf", 
)
soccer_shooting = np.genfromtxt(
    fname="soccer.csv",
    delimiter=",",
    usecols=8,
    skip_header=1,
    encoding="utf", 
)


# My solutions to the problems given below:

# Print out the weight of the first ten baseball players. 
print(baseball_weights[:10])

# What is the median weight of all baseball players in the data? 
bb_median = np.median(baseball_weights)
print(bb_median)

# Print out the names of all players with a height greater than 80 (heights are in inches).
tall_players_height = baseball_heights > 80
tall_players_name = baseball_names[tall_players_height]
print(tall_players_name)

# Who is taller on average? Baseball players or soccer players? Keep in mind that baseball heights are stored in inches!
soccer_heights_in = soccer_heights * 0.3937008
baseball_avg_height = np.mean(baseball_heights)
soccer_avg_height = np.mean(soccer_heights_in)
print(baseball_avg_height, soccer_avg_height)

#The values in `soccer_shooting` are decimals. Convert them to whole numbers (e.g., 0.98 becomes 98).
soccer_shooting_dec = (soccer_shooting*100).astype(int)
print(soccer_shooting_dec)

#Do taller players get higher ratings? Calculate the correlation between `soccer_ratings` and `soccer_heights` to find out!
corr_players = np.corrcoef(soccer_ratings, soccer_heights)
print(corr_players)

#What is the average rating for attacking players (`'A'`)?
att_players = soccer_positions == 'A'
avg_rating = np.mean(soccer_ratings[att_players])

print(avg_rating)

# Who is taller on average? Baseball players or soccer players? Keep in mind that baseball heights are stored in inches!
# Convert soccer heights from centimeters to inches
soccer_heights_in = soccer_heights * 0.3937008

# Calculate average heights
baseball_avg_height = np.mean(baseball_heights)
soccer_avg_height = np.mean(soccer_heights_in)

# Compare and display the result
if baseball_avg_height > soccer_avg_height:
    result = "Baseball players are taller on average."
elif baseball_avg_height < soccer_avg_height:
    result = "Soccer players are taller on average."
else:
    result = "Baseball and soccer players are the same height on average."

baseball_avg_height, soccer_avg_height, result
