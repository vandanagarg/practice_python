''' Min cost to get the projects completed?
** Note: If any project has no bids, return -1
Example:
numProjects = 3 projects.
projectId = [2, 0, 1, 2]
bid - [8, 7, 6, 9]

• projectId[i] is aligned with bid[i]
• The first web developer bid 8 currency units for project 2
• The second web developer bid 7 currency units for project O
• The third web developer bid 6 currency units for project 1
• The fourth web developer bid 9 currency units for project 2

There is only one choice of who to hire for project 0,
and it will cost 7.
Likewise, there is only one choice for project 1,
which will cost 6.
For project 2, it is optimal to hire the first web developer,
Instead of the fourth, hence will cost 8.
So the final answer Is 7 + 6 + 8 = 21.

If instead there were n=4 projects, the answer would be -1
since there were no bids received on the fourth project.

Function Description:
Complete the function mInCost in the editor below

minCost has the following parameters:
int numProjects: the total num. of projects posted by the
client (labeled from 0 to n)
int projectID[n]: an array of integers denoting the projects
that the freelancers bid on
int bid[n]: an array, Integers denoting the bid amounts posted
by the freelancers

Returns:
long: the minimum cost the client can spend to complete
all projects, or -1 if any project has no bids
'''
from collections import defaultdict


def min_cost(numProjects, project_id, bid):
    if numProjects != len(set(project_id)):
        return -1
    else:
        project_bid_dict = defaultdict(lambda: [])
        for i in range(0, len(project_id)):
            project_bid_dict[project_id[i]].append(bid[i])
    # return project_bid_dict
    total_bid = 0
    for i in project_bid_dict:
        total_bid = total_bid + min(project_bid_dict[i])
        print(project_bid_dict[i])
    return total_bid


numProjects = 3
project_id = [2, 0, 1, 2]
bid = [8, 7, 6, 9]
print(min_cost(numProjects, project_id, bid))
