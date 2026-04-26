# graph.py

network = {}

def add_connection(user1, user2):
    network.setdefault(user1, []).append(user2)
    network.setdefault(user2, []).append(user1)

def remove_connection(user1, user2):
    if user2 in network[user1]:
        network[user1].remove(user2)
    if user1 in network[user2]:
        network[user2].remove(user1)

def get_friends(user):
    return network.get(user, [])