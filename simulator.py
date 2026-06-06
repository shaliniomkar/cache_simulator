with open("memory.txt", "r") as file:
    lines = file.readlines()

memory = []

for i in lines:
    memory.append(int(i.strip()))

def simulate_fifo(memory, cache_size):
    cache_dict = {}
    hits = 0
    misses = 0
    queue = []
    timestamp = 0
    for access in memory:
        timestamp += 1
        if access not in cache_dict: # miss
            misses += 1
            if len(cache_dict) >= cache_size:
                del cache_dict[queue[0]]
                del queue[0]
                queue.append(access)
                cache_dict[access] = timestamp
            else:
                queue.append(access)
                cache_dict[access] = timestamp
        else: # hit
            hits += 1
    return hits, misses

def simulate_lru(memory, cache_size):
    cache_dict = {}
    hits = 0
    misses = 0
    timestamp = 0
    for access in memory:
        timestamp += 1
        if access not in cache_dict: # miss
            misses += 1
            if len(cache_dict) >= cache_size:
                min_time = min(cache_dict, key=cache_dict.get)
                del cache_dict[min_time]
                cache_dict[access] = timestamp
            else:
                cache_dict[access] = timestamp
        else: # hit
            hits += 1
            del cache_dict[access]
            cache_dict[access] = timestamp
    return hits, misses