def optimalFreelancing(jobs):
    # Write your code here.
    jobs.sort(key=lambda job: job["payment"], reverse=True)

    days = 7
    profits = 0
    timeline = [False] * days
    for job in jobs:
        deadline = min(job["deadline"], days)
        for idx in reversed(range(deadline)):
            if (timeline[idx] == False):
                timeline[idx] = True
                profits += job["payment"]
                break

    return profits


jobs = [
    {"deadline": 1, "payment": 1},
    {"deadline": 2, "payment": 1},
    {"deadline": 2, "payment": 2}
]
print(optimalFreelancing(jobs))
