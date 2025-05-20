def cycleInGraph(edges):
    n = len(edges)
    # 三种状态：未访问(0)，正在访问(1)，已完成访问(2)
    status = [0] * n

    # 对每个节点尝试进行DFS，dfs内部会判断是否需要继续搜索
    for node in range(n):
        if dfs(node, edges, status):
            return True

    return False


def dfs(node, edges, status):
    # 如果节点已经完成访问，不需要再处理
    if status[node] == 2:
        return False

    # 如果节点正在访问中，说明找到了环
    if status[node] == 1:
        return True

    # 标记为正在访问
    status[node] = 1

    # 检查所有邻居
    for neighbor in edges[node]:
        if dfs(neighbor, edges, status):
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
