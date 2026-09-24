def simulate_fcfs(processes):
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    print("=== FCFS Scheduling ===")

    for name, burst_time in processes:
        waiting_time = current_time
        turnaround_time = waiting_time + burst_time

        print(
            f"{name}: "
            f"Waiting Time = {waiting_time}, "
            f"Turnaround Time = {turnaround_time}"
        )

        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time

        current_time += burst_time

    print("Average Waiting Time:",
          total_waiting_time / len(processes))

    print("Average Turnaround Time:",
          total_turnaround_time / len(processes))


def simulate_round_robin(processes, quantum):
    remaining = {name: burst for name, burst in processes}

    current_time = 0
    waiting_time = {name: 0 for name, burst in processes}
    last_time = {name: 0 for name, burst in processes}

    print("\n=== Round Robin Scheduling ===")

    queue = [name for name, burst in processes]

    while queue:
        name = queue.pop(0)

        if remaining[name] <= 0:
            continue

        run_time = min(quantum, remaining[name])

        current_time += run_time
        remaining[name] -= run_time

        print(
            f"Running {name} "
            f"for {run_time} units"
        )

        if remaining[name] > 0:
            queue.append(name)

    print("\nRound Robin completed.")


processes = [
    ("P1", 10),
    ("P2", 2),
    ("P3", 3)
]

quantum = 3

simulate_fcfs(processes)
simulate_round_robin(processes, quantum)