import heapq

def nextMove(r, c, pacman_r, pacman_c, food_r, food_c, grid):
    def get_neighbors(node):
        neighbors = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c = node[0] + dr, node[1] + dc
            if 0 <= new_r < r and 0 <= new_c < c and grid[new_r][new_c] != '%':
                neighbors.append((new_r, new_c))
        return neighbors
    
    def ucs():
        visited = set()
        priority_queue = [(0, (pacman_r, pacman_c))]
        parent = {}

        while priority_queue:
            cost, node = heapq.heappop(priority_queue)
            if node in visited:
                continue
            visited.add(node)

            if node == (food_r, food_c):
                return parent

            for neighbor in get_neighbors(node):
                if neighbor not in visited:
                    new_cost = cost + 1 if grid[neighbor[0]][neighbor[1]] == '.' else cost
                    heapq.heappush(priority_queue, (new_cost, neighbor))
                    parent[neighbor] = node

    parents = ucs()

    path = []
    current_node = (food_r, food_c)
    while current_node != (pacman_r, pacman_c):
        path.append(current_node)
        current_node = parents[current_node]
    path.append((pacman_r, pacman_c))
    
    print(len(path) - 1)
    for node in reversed(path):
        print(node[0], node[1])

# Read input
pacman_r, pacman_c = map(int, input().strip().split())
food_r, food_c = map(int, input().strip().split())
r, c = map(int, input().strip().split())
grid = []
for _ in range(r):
    grid.append(input())

# Call the function to solve the problem
nextMove(r, c, pacman_r, pacman_c, food_r, food_c, grid)
