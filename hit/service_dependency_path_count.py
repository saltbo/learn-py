from collections import defaultdict, deque


def solution(service_list, entrypoint):
    deps = {}
    for item in service_list:
        svc, right = item.split("=")
        if not right:
            deps[svc] = []
            continue
        deps[svc] = right.split("|")
    print(deps)

    calls = defaultdict(int)
    calls[entrypoint] = 1

    queue = deque([entrypoint])
    while queue:
        curr = queue.popleft()
        for d in deps.get(curr, []):
            calls[d] += calls[curr]
            queue.append(d)

    return ["{}*{}".format(name, calls) for name, calls in calls.items()]


service_list = ["logging=",
                "orders=products|logging",
                "products=logging",
                "scarts=users|products|logging",
                "dashboard=orders|scarts",
                "users=logging",
                ]
entrypoint = "dashboard"
res = solution(service_list, entrypoint)
print(res)
