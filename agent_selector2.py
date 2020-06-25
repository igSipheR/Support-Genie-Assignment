import sys
import random

def Record_issue():
    confirmation = input("is there any issue? yes or no: ")
    if(confirmation == 'y' or 'yes' or 'YES' or 'Yes'):
            cust_name = input("Enter customer name: ")
            cust_age = int(input("Enter age: "))
            issue_category = input("Enter type of issue: ")
            issue_des = input("Issue description: ")

            print("issue recorded")    
            
    elif(confirmation == 'n' or 'no' or 'No' or 'NO' or ''):
        sys.exit(0)

    else:
        return confirmation
      
Record_issue()

#=============================================================================

class agent_info:
    def __init__(self, name, is_available, mode, available_since, role):
        self.name = name
        self.is_available = is_available
        self.mode = mode
        self.available_since = available_since
        self.role = role


#creating some examples of agents info
#available_since value has been count in "days"
        
agnt1 = agent_info('Rohan','yes','all_available',25,'maintainance')
agnt2 = agent_info('Mike','yes','all_available',5, 'Accounitng')
agnt3 = agent_info('jiya','no','all_available',0, 'networking')
agnt4 = agent_info('Karan','no','all_available',0, 'development, support')
agnt5 = agent_info('Krisan','yes','all_available',7, 'networking, maintainance')
print("                         ")
agnt6 = agent_info('mika','yes','least_busy',0,'maintenance')
agnt7 = agent_info('shiro','no','least_busy',0,'support')
agnt8 = agent_info('nik','yes','least_busy',0,'networking')
agnt9 = agent_info('ankita','no','least_busy',0,'development, support')
agnt10 = agent_info('steve','yes','least_busy',0,'networking, maintainance')

#creating an empty dictionary
agents = {}


#fuction for displaying information
def all_agntInfo(agentList):
    for item in agentList:
        agents[item.name] = (item.is_available, item.mode, item.available_since, item.role)


#calling function
all_agntInfo([agnt1, agnt2, agnt3, agnt4, agnt5, agnt6, agnt7, agnt8, agnt9, agnt10])


#printting ouput in following format   
for key, val in agents.items():
    print(str(key) +":"+ str(val))


#=============================================================================
#function for comparing agents & returning lists accordingly

def getAgents(agents, mode):
    mode = all_agntInfo.is_available
    agents = all_agntInfo

    if (mode == 'all_available'):
        return(all_agntInfo.mode == 'all_avaliable')
    
    elif(mode == 'least_busy'):
        return(all_agntInfo.mode == 'least_busy')

       
    for agent in all_agntInfo :
        if(all_agntInfo.is_available == 'yes' and all_agntInfo.role == issue_category):
            return (all_agntInfo.role == issue_category)
   
        elif (mode == 'random'):
            all_agntInfo = random.choice(agents)
            print(all_agntInfo)

#calling function
getAgents(agents, mode)




    
