# hw2/code/kendall_tau.py
from scipy.stats import kendalltau

# Q2 ranking order (TF-IDF)
q2 = [
    "odu.edu",
    "catalyzex.com",
    "weiglemc.github.io",
    "vmasc.org",
    "oducsreu.github.io",
    "ws-dl.blogspot.com",
    "ssrc.org",
    "cornell.edu",
    "txyz.ai",
    "cs.odu.edu",
]

# Q3 ranking order (PageRank)
q3 = [
    "oducsreu.github.io",
    "ssrc.org",
    "odu.edu",
    "weiglemc.github.io",
    "cs.odu.edu",
    "vmasc.org",
    "catalyzex.com",
    "ws-dl.blogspot.com",
    "cornell.edu",
    "txyz.ai",
]

# Map each item to a rank
q2_ranks = {item: i for i, item in enumerate(q2)}
q3_ranks = {item: i for i, item in enumerate(q3)}

# Build aligned vectors
x = [q2_ranks[item] for item in q2]
y = [q3_ranks[item] for item in q2]

tau, p_value = kendalltau(x, y)

print(f"Kendall Tau-b correlation: {tau:.3f}")
print(f"P-value: {p_value:.3f}")
