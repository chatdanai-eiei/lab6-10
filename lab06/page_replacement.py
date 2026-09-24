def simulate_fifo(reference_string, num_frames):
    frames = []
    page_faults = 0

    for page in reference_string:
        if page not in frames:
            page_faults += 1

            if len(frames) < num_frames:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)

        print(f"Page {page}: Frames = {frames}")

    return page_faults


def simulate_lru(reference_string, num_frames):
    frames = []
    page_faults = 0

    for page in reference_string:
        if page not in frames:
            page_faults += 1

            if len(frames) < num_frames:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)

        else:
            frames.remove(page)
            frames.append(page)

        print(f"Page {page}: Frames = {frames}")

    return page_faults


reference_string = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
num_frames = 3

print("=== FIFO ===")
fifo_faults = simulate_fifo(reference_string, num_frames)
print("FIFO Page Faults:", fifo_faults)

print("\n=== LRU ===")
lru_faults = simulate_lru(reference_string, num_frames)
print("LRU Page Faults:", lru_faults)