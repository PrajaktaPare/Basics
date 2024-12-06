skills_A = {'Python', 'Java', 'SQL'}
skills_B = {'Python', 'HTML', 'CSS'}

#Skills that are in both sets

print(skills_A.intersection(skills_B))

#Skills that are unique to skills_A.

print(skills_A.difference(skills_B))

#The union of both skill sets.

print(skills_A.union(skills_B))