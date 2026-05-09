# Unit: CCS 2226 Foundations of AI
# Student Name: Moses Kiprono Leleito
# Registration Number: CIT-227-073/2024
# Task: Practical Task Two (b) - Nairobi Sub-counties Coloring (CSP)

from constraint import Problem

def solve_nairobi_coloring():
    problem = Problem()
    
    # Defining the 17 sub-counties of Nairobi
    sub_counties = [
        "Westlands", "Dagoretti North", "Dagoretti South", "Langata", "Kibra", 
        "Ruaraka", "Kasarani", "Embakasi North", "Embakasi South", "Embakasi Central", 
        "Embakasi East", "Embakasi West", "Makadara", "Kamkunji", "Starehe", 
        "Mathare", "Roysambu"
    ]
    
    # Minimum colors to satisfy the Four Color Theorem
    colors = ["Red", "Blue", "Green", "Yellow"] 
    
    problem.addVariables(sub_counties, colors)
    
    # Boundary definitions for sub-counties
    adjacencies = [
        ("Westlands", "Dagoretti North"), ("Westlands", "Starehe"),
        ("Westlands", "Roysambu"), ("Dagoretti North", "Dagoretti South"),
        ("Dagoretti North", "Kibra"), ("Dagoretti South", "Langata"),
        ("Kibra", "Langata"), ("Kibra", "Starehe"),
        ("Langata", "Embakasi South"), ("Langata", "Makadara"),
        ("Starehe", "Kamkunji"), ("Starehe", "Mathare"),
        ("Mathare", "Ruaraka"), ("Roysambu", "Kasarani"),
        ("Kasarani", "Ruaraka"), ("Embakasi North", "Embakasi Central"),
        ("Embakasi Central", "Embakasi East"), ("Embakasi East", "Embakasi South"),
        ("Embakasi West", "Makadara"), ("Makadara", "Embakasi South")
    ]
    
    # Apply non-identical color constraint to neighbors
    for area1, area2 in adjacencies:
        problem.addConstraint(lambda a, b: a != b, (area1, area2))
        
    solution = problem.getSolution()
    
    print("--- Nairobi Sub-counties Coloring Solution ---")
    if solution:
        print(f"Solution found using {len(colors)} colors.")
        for sub_county, color in solution.items():
            print(f"{sub_county}: {color}")
    else:
        print("Constraint could not be satisfied with the current color palette.")

if __name__ == "__main__":
    solve_nairobi_coloring()