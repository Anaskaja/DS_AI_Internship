import numpy as np

scores = np.random.randint(50,101,size=(5,3))
means=np.mean(scores,axis=0)
centered_scores= scores-means

print("original scores of students:",scores)
print("mean scores:",means)
print("centerd scores", centered_scores)
