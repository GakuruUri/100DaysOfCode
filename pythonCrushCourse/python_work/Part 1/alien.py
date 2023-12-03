alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

# Day 13
alien_0 = {"color": "green", "points": 5}

new_points = alien_0["points"]
print(f"\nYou just earned {new_points} points!")

# Adding new key-value pairs
alien_0 = {"color": "green", "points": 5}

print(alien_0)


alien_0["x-position"] = 0
alien_0["y-position"] = 25
print(alien_0)


# Starting with an empty dictionary

print("\n")
alien_0 = {}

alien_0["color"] = "green"
alien_0["points"] = 5

print(alien_0)

# Modifying values in a dictionary
alien_0 = {"color": "green"}
print(f"\nThe alien is {alien_0['color']}.")

alien_0["color"] = "yellow"
print(f"The alien is now {alien_0['color']}.")


# Tracking the position of the alien at different speeds.
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium", "color": "green"}
print(f"Original position: {alien_0['x_position']} and the color is {alien_0['color']}")


# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
alien_0["color"] = "yellow"

# The new position is the old position plus the increment
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New position: {alien_0['x_position']} and alien_0 color is {alien_0['color']}")


# Removing Key_Value pairs
alien_0 = {'color': 'green', 'points': 5}
print("\n")
print(alien_0)

del alien_0['points']
print(alien_0)

























