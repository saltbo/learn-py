def taskAssignment(k, tasks):
    pairedTasks = [(task, idx) for idx, task in enumerate(tasks)]
    pairedTasks.sort(key=lambda x: x[0])
    print(pairedTasks)

    result = []
    for i in range(k):
        print(i, pairedTasks[i], pairedTasks[k*2-i-1])
        result.append([pairedTasks[i][1], pairedTasks[k*2-i-1][1]])
    return result


k = 3
tasks = [1, 3, 5, 3, 1, 4]
print(taskAssignment(k, tasks))
