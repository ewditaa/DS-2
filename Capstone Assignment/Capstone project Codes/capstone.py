# profiles.py

users = {}

def add_user(user_id, name, age, interests):
    users[user_id] = {
        "name": name,
        "age": age,
        "interests": interests
    }

def get_profile(user_id):
    return users.get(user_id, "User not found")

def update_profile(user_id, name=None, age=None, interests=None):
    if user_id in users:
        if name:
            users[user_id]["name"] = name
        if age:
            users[user_id]["age"] = age
        if interests:
            users[user_id]["interests"] = interests


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


# search.py

from collections import deque

def bfs_shortest_path(start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbour in network.get(node, []):
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

    return "No Path Found"


def dfs_explore(user, depth, visited=None):
    if visited is None:
        visited = set()

    if depth == 0:
        return visited

    visited.add(user)

    for friend in network.get(user, []):
        if friend not in visited:
            dfs_explore(friend, depth - 1, visited)

    return visited


# recommendation.py

def suggest_friends(user):
    suggestions = {}

    user_interests = set(users[user]["interests"])

    for other in users:
        if other != user and other not in network.get(user, []):
            common = user_interests.intersection(users[other]["interests"])
            suggestions[other] = len(common)

    sorted_users = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)

    return sorted_users


# main.py

# Add Users
add_user(1, "Aduita", 18, ["music", "coding", "travel"])
add_user(2, "Riya", 19, ["music", "dance", "movies"])
add_user(3, "Aryan", 20, ["coding", "gaming", "travel"])
add_user(4, "Karan", 21, ["sports", "movies"])
add_user(5, "Sneha", 18, ["music", "coding"])

# Update Profiles
update_profile(2, age=20)
update_profile(4, interests=["sports", "travel"])

# Connections
add_connection(1,2)
add_connection(1,3)
add_connection(2,4)
add_connection(3,5)
add_connection(4,5)

# Remove one connection
remove_connection(2,4)

# Show Profiles
print(get_profile(1))
print(get_profile(2))
print(get_profile(3))

# BFS
print("Shortest Path:", bfs_shortest_path(1,5))
print("Shortest Path:", bfs_shortest_path(2,5))

# DFS
print("DFS Depth 2:", dfs_explore(1,2))
print("DFS Depth 3:", dfs_explore(1,3))

# Recommendations
print("Suggestions for User 1:")
print(suggest_friends(1))