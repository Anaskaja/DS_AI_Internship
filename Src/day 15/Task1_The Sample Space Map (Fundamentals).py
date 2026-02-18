import random

print("--- Task 1: The Sample Space Map (Fundamentals) ---")

actions = ['Click', 'Scroll', 'Exit']

sample_space = []
for first_action in actions:
    for second_action in actions:
        sample_space.append((first_action, second_action))

print("\n1. Sample Space S (All possible 2-action combinations):")
for outcome in sample_space:
    print(f"   {outcome}")
print(f"Total Outcomes in S: {len(sample_space)}")

event_e = [outcome for outcome in sample_space if 'Click' in outcome]

print("\n2. Event E (At least one 'Click'):")
for outcome in event_e:
    print(f"   {outcome}")

prob_e = len(event_e) / len(sample_space)
print(f"Probability P(E) = {len(event_e)} / {len(sample_space)} = {prob_e:.4f} (or {prob_e*100:.1f}%)")

print("\n--- 3. Dice Simulation (1,000 Rolls) ---")

trials = 1000
sevens_rolled = 0

for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    if die1 + die2 == 7:
        sevens_rolled += 1

experimental_prob = sevens_rolled / trials
theoretical_prob = 6 / 36

print(f"Total times 7 was rolled: {sevens_rolled}")
print(f"Experimental Probability: {experimental_prob:.4f}")
print(f"Theoretical Probability:  {theoretical_prob:.4f}")

if abs(experimental_prob - theoretical_prob) < 0.05:
    print("Observation: The experimental probability is very close to the theoretical probability, which proves the Law of Large Numbers!")