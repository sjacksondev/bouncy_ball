"""
PROGRAM: bouncy.py
NAME: Sabrina
DATE: 9/5/19

Program calculate the total difference travelled by a bouncing ball.
User will input:
	The starting height of the ball
	How bouncy the ball is
	How many bounces the ball will make
Output will be the total distance the ball travels
"""

# Request the inputs
height = float(input("Enter the starting height of the ball: >>> "))
index = float(input("Enter the bounciness index of the ball: >>> "))
bounces = int(input("How many bounces do you want to observe? >>> "))

# Accumulator for total distane
totalDistance = 0

# For loop to determine total distance travelled
for count in range(bounces):
	totalDistance += height
	height += index
	totalDistance += height

# Output of total distance
print()
print("The totakl distance travelled by the ball is", totalDistance)

