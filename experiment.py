import simulator
import pandas as pd
import plotly.express as px

cache_size_tests = [2, 3, 4, 5, 8]

print("FIFO Simulation On Different Cache Sizes: ")
print("-----------------------------------------")

cache_size_list = []
hit_rate_list = []
policy_list = []

for i in cache_size_tests:
    hits, misses = simulator.simulate_fifo(simulator.memory, i)
    cache_size_list.append(i)
    hit_rate_list.append(hits / (hits + misses) * 100)
    policy_list.append("FIFO")
    print(f"Cache size = {i} \t\t Hit rate = {hits / (hits + misses) * 100:.2f}%")

print()
print("LRU Simulation On Different Cache Sizes: ")
print("-----------------------------------------")

for i in cache_size_tests:
    hits, misses = simulator.simulate_lru(simulator.memory, i)
    cache_size_list.append(i)
    hit_rate_list.append(hits / (hits + misses) * 100)
    policy_list.append("LRU")
    print(f"Cache size = {i} \t\t Hit rate = {hits / (hits + misses) * 100:.2f}%")

data = {
    "Cache Size": cache_size_list,
    "Hit Rate": hit_rate_list,
    "Policy": policy_list
}

df = pd.DataFrame(data)

fig = px.line(df, x="Cache Size", y="Hit Rate", color="Policy", title="FIFO vs. LRU")
fig.show()