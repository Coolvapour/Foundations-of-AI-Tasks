# Unit: CCS 2226 Foundations of AI
# Student Name: Moses Kiprono Leleito
# Registration Number: CIT-227-073/2024
# Task: Practical Task Two (a) - Australia Map Coloring (CSP)

from constraint import Problem

def solve_australia_map():
    # Instantiate the Constraint Satisfaction Problem
    problem = Problem()
    
    # Defining the Variables (Regions of Australia)
    regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    
    # Defining the Domain (Permitted colors)
    colors = ['Blue', 'Red', 'Green']
    
    problem.addVariables(regions, colors)
    
    # Defining constraints: Adjacent regions must not have the same color
    adjacencies = [
        ('WA', 'NT'), ('WA', 'SA'),
        ('NT', 'SA'), ('NT', 'Q'),
        ('SA', 'Q'), ('SA', 'NSW'), ('SA', 'V'),
        ('Q', 'NSW'),
        ('NSW', 'V')
    ]
    
    for r1, r2 in adjacencies:
        problem.addConstraint(lambda a, b: a != b, (r1, r2))
        
    # Solve for a valid configuration
    solution = problem.getSolution()
    
    print("--- Australia Map Coloring Solution ---")
    if solution:
        for region, color in solution.items():
            print(f"{region}: {color}")
    else:
        print("No valid coloring found.")

if __name__ == "__main__":
    solve_australia_map()