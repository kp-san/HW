#HW3

from Queue_for_ALGO import Queue

# Given list of quarterbacks
qbs = [
    'Aaron Rodgers', 'Alex Smith', 'Cam Newton', 'Peyton Manning', 'Derek Carr',
    'Drew Brees', 'Tom Brady', 'Matt Ryan', 'Ryan Tannehill',
    'Ben Roethlisberger', 'Joe Flacco', 'Jared Goff', 'Kirk Cousins',
    'Patrick Mahomes', 'Deshuan Watson', 'Andrew Luck', 'Russell Wilson',
    'Philip Rivers', 'Dak Prescott'
]

# Fill a queue with the list
qb_queue = Queue()
for quarterback in qbs:
    qb_queue.enqueue(quarterback)

# Evaluate all the items in the queue
superbowl_winners = []
while not qb_queue.isEmpty():
    qb = qb_queue.dequeue()
    
    # Check if the quarterback won the Super Bowl
    if qb in ['Aaron Rodgers', 'Peyton Manning', 'Drew Brees', 'Tom Brady', 'Ben Roethlisberger', 'Joe Flacco', 'Patrick Mahomes', 'Russell Wilson']:
        superbowl_winners.append(qb)

# Output the list of Super Bowl quarterback winners
print("Super Bowl quarterback winners:")
for qb in superbowl_winners:
    print(qb)
