print("--- Task 2: The Logic of Dependency ---")

#INDEPENDENT EVENTS

p_heads = 1 / 2
p_six = 1 / 6

p_independent = p_heads * p_six
print(f"Independent Probability (Heads AND 6): {p_independent:.4f}")

#DEPENDENT EVENTS
p_first_red = 5 / 10
p_second_red = 4 / 9

p_dependent = p_first_red * p_second_red
print(f"Dependent Probability (Both Red): {p_dependent:.4f}")