# Unit: CCS 2226 Foundations of AI
# Student Name: Moses Kiprono Leleito
# Registration Number: CIT-227-073/2024
# Task: Practical Task Two (b) - Nairobi Sub-counties (Simulative Map)

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from constraint import Problem

def solve_nairobi_simulative():
    problem = Problem()
    
    # The 17 sub-counties of Nairobi
    sub_counties = [
        "Westlands", "Dagoretti North", "Dagoretti South", "Langata", "Kibra", 
        "Ruaraka", "Kasarani", "Embakasi North", "Embakasi South", "Embakasi Central", 
        "Embakasi East", "Embakasi West", "Makadara", "Kamkunji", "Starehe", 
        "Mathare", "Roysambu"
    ]
    
    # Four colors are sufficient for any map
    colors = ["#FF9999", "#99FF99", "#9999FF", "#FFFF99"] 
    
    problem.addVariables(sub_counties, colors)
    
    # These must match the visual layout exactly to avoid rule violations
    adjacencies = [
        # Westlands Neighbors
        ("Westlands", "Dagoretti North"), ("Westlands", "Kibra"), ("Westlands", "Starehe"), 
        ("Westlands", "Mathare"), ("Westlands", "Roysambu"),
        # North-West cluster
        ("Dagoretti North", "Dagoretti South"), ("Dagoretti North", "Kibra"),
        ("Dagoretti South", "Langata"), ("Kibra", "Langata"), ("Kibra", "Starehe"),
        # Central & North cluster
        ("Starehe", "Mathare"), ("Starehe", "Kamkunji"), ("Starehe", "Ruaraka"),
        ("Mathare", "Ruaraka"), ("Ruaraka", "Roysambu"), ("Ruaraka", "Kasarani"),
        ("Roysambu", "Kasarani"),
        # East cluster
        ("Kasarani", "Embakasi West"), ("Embakasi West", "Embakasi North"), 
        ("Embakasi West", "Embakasi Central"), ("Embakasi North", "Embakasi Central"),
        ("Embakasi North", "Makadara"), ("Embakasi Central", "Embakasi East"), 
        ("Embakasi Central", "Embakasi South"), ("Embakasi East", "Embakasi South"),
        # Southern/Central connectors
        ("Kamkunji", "Makadara"), ("Kamkunji", "Starehe"), ("Makadara", "Embakasi South"),
        ("Langata", "Makadara"), ("Langata", "Embakasi South")
    ]
    
    # Rule: Neighbor 1 != Neighbor 2
    for area1, area2 in adjacencies:
        problem.addConstraint(lambda a, b: a != b, (area1, area2))
        
    solution = problem.getSolution()
    
    if solution:
        print("Valid CSP Solution Found. Refreshing Visualization...")
        draw_simulative_map(solution)
    else:
        print("No solution found with these constraints.")

def draw_simulative_map(solution):
    fig, ax = plt.subplots(figsize=(12, 9))
    
    # Layout coordinates (x, y, width, height, name)
    layout = [
        (1, 4, 2, 2, "Westlands"), (0, 3, 1, 1, "Dagoretti North"), (0, 2, 1, 1, "Dagoretti South"),
        (1, 1, 1, 2, "Langata"), (1, 3, 1, 1, "Kibra"), (4, 4, 1, 1, "Ruaraka"),
        (5, 4, 1, 2, "Kasarani"), (5, 2, 1, 1, "Embakasi North"), (5, 0, 2, 1, "Embakasi South"),
        (6, 2, 1, 1, "Embakasi Central"), (7, 1, 1, 1, "Embakasi East"), (6, 3, 1, 1, "Embakasi West"),
        (4, 1, 1, 1, "Makadara"), (3, 2, 1, 1, "Kamkunji"), (2, 3, 2, 1, "Starehe"),
        (3, 4, 1, 1, "Mathare"), (4, 5, 1, 1, "Roysambu")
    ]

    for x, y, w, h, name in layout:
        color = solution.get(name, "#CCCCCC")
        rect = patches.Rectangle((x, y), w, h, linewidth=2, edgecolor='black', facecolor=color)
        ax.add_patch(rect)
        plt.text(x + w/2, y + h/2, name, ha='center', va='center', fontsize=9, fontweight='bold')

    plt.xlim(-1, 9)
    plt.ylim(-1, 7)
    plt.title("Nairobi Sub-counties: Validated Simulative Constraint Map", fontsize=15, pad=20)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    solve_nairobi_simulative()