#*****************************************************  
# 3rd task of Python 101, world 5
# vacuum.py 
# @author: CK  
# @since: Version date 09/05/2023  
# @version: 1.0  
# muutos: CK
#*****************************************************/

# Part 1
for i in range(7):
    agent.move(FORWARD, 1)
    agent.collect_all()
agent.move(RIGHT, 1)

for i in range(7):
    agent.move(BACK, 1)
    agent.collect_all()

# Part 2
for i in range(10):
    for i in range(7):        
        agent.collect_all()
        agent.move(FORWARD, 1)
    agent.move(RIGHT, 1)

    for i in range(7):
        agent.collect_all()
        agent.move(BACK, 1)
    agent.move(RIGHT, 1)
agent.drop_all(FORWARD)