# %%
from pulp import *

# Hourly demand for agents
hourly_demand = [5, 6, 7, 8, 9, 11, 13, 15, 17, 18, 20, 22, 21, 19, 17, 15, 13, 11, 9, 7, 6, 5, 4, 3]

# Create a variable 'x' that represents the number of agents starting at hour i
x = LpVariable.dicts("agents_starting_at_hour", list(range(24)), lowBound=0, cat='Integer')

# Initialize the problem
prob = LpProblem("Call_Center_Scheduling", LpMinimize)

# The objective function is to minimize the total number of agents
prob += lpSum([x[i] for i in range(24)]), "Total_Number_of_Agents"

# Constraint: For each hour, the number of agents working must be at least the demand
for i in range(24):
    agents_working = lpSum([x[(i + j) % 24] for j in range(8)])  # Account for the circular shift pattern
    prob += agents_working >= hourly_demand[i], f"Demand_at_hour_{i}"

# Solve the problem
prob.solve()

# %%

# Output the results
schedule = {}
for v in prob.variables():
    schedule[v.name] = v.varValue

# Total number of agents scheduled
total_agents = sum(v.varValue for v in prob.variables())

# Print the results
print("Schedule:")
for hour, agents in schedule.items():
    print(f"{hour}: {agents}")
print(f"Total number of agents needed: {total_agents}")

# Check if the problem is solved successfully
if LpStatus[prob.status] == 'Optimal':
    print("Solution is optimal.")
else:
    print("Could not find the optimal solution.")

# %%
all_vars = prob.variables()
for i in range(23):
    idxs = []
    sum = 0
    for j in range(8):
        idxt = i-j % 24
        if i-j < 0:
            idxt = 24 - j
        idxs.append(idxt)
        sum += all_vars[idxt].varValue

    print(f"For hour {i} sum = {sum} and demand = {hourly_demand[i]}")

## %% 
#import pulp
#
## Create a linear programming problem
#problem = pulp.LpProblem("My_LP_Problem", pulp.LpMinimize)
#
## Define decision variables
## How many will start at time hour i
#dec_vars = [pulp.LpVariable(f"x{i}", lowBound=0) for i in range(24)]
#
## Define the objeCTive function to maximize
#problem += pulp.lpSum(dec_vars) 
#
## Add constraints
#hourly_demand = [5, 6, 7, 8, 9, 11, 13, 15, 17, 18, 20, 22, 21, 19, 17, 15, 13, 11, 9, 7, 6, 5, 4, 31]
#
#for i in range(23):
#    print("========================")
#    idxs = []
#    for j in range(8):
#        idxt = i-j % 24
#        if i-j < 0:
#            idxt = 24 - j
#        idxs.append(idxt)
#        print(idxt)
#    print(f"i = {i}, j = {j}, idxs = {idxs}")
#    problem += dec_vars[idxs[0]] + dec_vars[idxs[1]] + dec_vars[idxs[2]] + dec_vars[idxs[3]] + dec_vars[idxs[4]] + dec_vars[idxs[5]] + dec_vars[idxs[6]] + dec_vars[idxs[7]] >= hourly_demand[i]
#
## Solve the problem
#problem.solve()
#
## %% # Retrieve results
#print("Optimal Solution:")
#for i, x in enumerate(problem.variables()):
#    print(f"x_{i} = {x.varValue}")
#print(f"Optimal Value = {pulp.value(problem.objective)}")
## %%
#
#all_vars = problem.variables()
#for i in range(23):
#    idxs = []
#    sum = 0
#    for j in range(8):
#        idxt = i-j % 24
#        if i-j < 0:
#            idxt = 24 - j
#        idxs.append(idxt)
#        sum += all_vars[idxt].varValue
#
#    print(f"For hour {i} sum = {sum}")