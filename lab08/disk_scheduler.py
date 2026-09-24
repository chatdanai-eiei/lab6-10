def simulate_fcfs(requests, initial_position):
    current_position = initial_position
    total_movement = 0

    print("=== FCFS Disk Scheduling ===")
    print("Start position:", current_position)

    for request in requests:
        movement = abs(request - current_position)
        total_movement += movement

        print(
            f"Move from {current_position} "
            f"to {request} = {movement}"
        )

        current_position = request

    print("Total Head Movement:", total_movement)

    return total_movement


def simulate_scan(requests, initial_position, max_cylinder=199):
    current_position = initial_position
    total_movement = 0

    print("\n=== SCAN Disk Scheduling ===")
    print("Start position:", current_position)

    # Move upward first
    upper = sorted(
        [r for r in requests if r >= initial_position]
    )

    lower = sorted(
        [r for r in requests if r < initial_position],
        reverse=True
    )

    for request in upper:
        movement = abs(request - current_position)
        total_movement += movement

        print(
            f"Move from {current_position} "
            f"to {request} = {movement}"
        )

        current_position = request

    # Move to the end of the disk
    if current_position != max_cylinder:
        movement = max_cylinder - current_position
        total_movement += movement

        print(
            f"Move from {current_position} "
            f"to {max_cylinder} = {movement}"
        )

        current_position = max_cylinder

    # Reverse direction
    for request in lower:
        movement = abs(request - current_position)
        total_movement += movement

        print(
            f"Move from {current_position} "
            f"to {request} = {movement}"
        )

        current_position = request

    print("Total Head Movement:", total_movement)

    return total_movement


requests = [98, 183, 37, 122, 14, 124, 65, 67]
initial_position = 53

simulate_fcfs(requests, initial_position)

simulate_scan(
    requests,
    initial_position,
    max_cylinder=199
)