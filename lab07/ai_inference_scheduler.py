class AIRequest:
    def __init__(self, user_id, tokens_required):
        self.user_id = user_id
        self.tokens_required = tokens_required


def simulate_ai_fcfs(requests):
    print("=== AI FCFS ===")

    for request in requests:
        print(
            f"Serving {request.user_id} "
            f"for {request.tokens_required} tokens"
        )


def simulate_ai_round_robin(requests):
    print("\n=== AI Round Robin ===")

    remaining = {
        request.user_id: request.tokens_required
        for request in requests
    }

    queue = [request.user_id for request in requests]

    while queue:
        user_id = queue.pop(0)

        if remaining[user_id] <= 0:
            continue

        print(f"{user_id}: 1 token")

        remaining[user_id] -= 1

        if remaining[user_id] > 0:
            queue.append(user_id)


requests = [
    AIRequest("User A", 10),
    AIRequest("User B", 2)
]

simulate_ai_fcfs(requests)
simulate_ai_round_robin(requests)