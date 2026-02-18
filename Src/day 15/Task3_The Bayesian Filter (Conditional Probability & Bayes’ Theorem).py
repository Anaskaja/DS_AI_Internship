print("--- Task 3: The Bayesian Filter ---")
p_spam = 0.10
p_ham = 0.90

p_free_given_spam = 0.90


p_free_given_ham = 0.05


p_free = (p_free_given_spam * p_spam) + (p_free_given_ham * p_ham)
print(f"P(Free): {p_free:.4f}")


p_spam_given_free = (p_free_given_spam * p_spam) / p_free
print(f"P(Spam | Free): {p_spam_given_free:.4f}")