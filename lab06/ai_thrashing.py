import time
import os


def fast_ram_access(iterations):
    data = [0] * 1000

    start = time.time()

    for _ in range(iterations):
        data[0] += 1

    end = time.time()

    return end - start


def slow_swap_thrashing_access(iterations, filename="swap_file.bin"):
    start = time.time()

    with open(filename, "wb") as f:
        f.write(b"\x00" * 4096)

    for _ in range(iterations):
        with open(filename, "r+b") as f:
            f.seek(0)
            f.write(b"\x01")

    end = time.time()

    if os.path.exists(filename):
        os.remove(filename)

    return end - start


iterations = 10000

ram_time = fast_ram_access(iterations)
thrashing_time = slow_swap_thrashing_access(iterations)

print("=== Memory Access Simulation ===")
print(f"RAM access time: {ram_time:.6f} seconds")
print(f"Thrashing access time: {thrashing_time:.6f} seconds")

if ram_time > 0:
    slowdown = thrashing_time / ram_time
    print(f"Thrashing is approximately {slowdown:.2f}x slower")