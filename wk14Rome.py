# List of flight connections
connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
]

# Initialize variables for count and total time
count = 0
totaltime = 0

# Iterate through each flight connection
for flight in connections: 
    depart, arrive, time = flight  # Unpack the tuple into variables
    if arrive == 'Rome':  # Check if the destination is Rome
        count = count + 1  # Increment the count
        totaltime = time + totaltime  # Add the time to the total time

# Calculate the average time
avgtime = totaltime / count

# Print the result
print(str(count) + " connections lead to Rome with an average flight time of " + str(avgtime) + " minutes")
