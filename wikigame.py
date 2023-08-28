def initdata():
    global data
    with open("1.in", "r") as f:
        data = f.read().split("\n")

def main2(data):
    iterations = data[0]
    print(iterations) #debug

#GPT ZONE!

def can_reach(graph, start, end, max_steps):
    if max_steps < 0:
        return False
    if start == end:
        return True
    if start not in graph:
        return False

    for neighbor in graph[start]:
        if can_reach(graph, neighbor, end, max_steps - 1):
            return True
    return False

def process_game(graph, start, end, max_steps):
    if can_reach(graph, start, end, max_steps):
        return "YES"
    else:
        return "NO"

def main():
    with open('1.in', 'r') as file:
        num_games = int(file.readline().strip())

        for _ in range(num_games):
            num_nodes, num_edges = map(int, file.readline().split())
            graph = {}

            for _ in range(num_edges):
                src, dest = map(int, file.readline().split())
                if src not in graph:
                    graph[src] = []
                graph[src].append(dest)

            start, end = map(int, file.readline().split())
            max_steps = 6

            result = process_game(graph, start, end, max_steps)
            print(result)

if __name__ == "__main__":
    main()
    #TODO: all iterations



