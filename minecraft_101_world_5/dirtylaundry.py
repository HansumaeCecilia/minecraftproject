#*****************************************************  
# 2nd task of Python 101, world 5
# dirtylaundry.py 
# @author: CK  
# @since: Version date 09/05/2023  
# @version: 1.0  
# muutos: CK
#*****************************************************/

#Part 1
agent.collect_all()
agent.move(FORWARD, 7)
agent.drop_all(FORWARD)

for i in range(20):
    agent.turn(LEFT_TURN)


agent.collect_all()
agent.move(BACK, 7)
agent.drop_all(LEFT)

#Part 2
for i in range(3):
    agent.collect_all()
    agent.move(FORWARD, 7)
    agent.drop_all(FORWARD)

    for i in range(20):
        agent.turn(LEFT_TURN)

    agent.collect_all()
    agent.move(BACK, 7)
    agent.drop_all(LEFT)