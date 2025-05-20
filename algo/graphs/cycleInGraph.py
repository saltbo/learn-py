def cycleInGraph(edges):
    n = len(edges)
    # 三种状态：未访问(0)，正在访问(1)，已完成访问(2)
    status = [0] * n

    # 对每个未访问的节点进行DFS
    for node in range(n):
        if status[node] == 0:
            if dfs(node, edges, status):
                return True

    return False


def dfs(node, edges, status):
    print(node, status)
    # 标记为正在访问
    status[node] = 1

    # 检查所有邻居
    for neighbor in edges[node]:
        # 如果邻居未访问，继续DFS
        if status[neighbor] == 0:
            if dfs(neighbor, edges, status):
                return True
        # 如果邻居正在被访问，说明找到了环
        elif status[neighbor] == 1:
            return True

    # 标记为已完成访问
    status[node] = 2
    return False


edges = [
    [1, 3],
    [2, 3, 4],
    [0],
    [],
    [2, 5],
    []
]

print(cycleInGraph(edges))
