import os
import time


NUM_FILES = 1000
FILE_SIZE = 4096

FOLDER = "raw_images_folder"
PACKED_FILE = "packed_dataset.tfrecord"


def setup_test_files(num_files, file_size_bytes):
    os.makedirs(FOLDER, exist_ok=True)

    data = b"0" * file_size_bytes

    for i in range(num_files):
        filename = os.path.join(
            FOLDER,
            f"image_{i}.bin"
        )

        with open(filename, "wb") as f:
            f.write(data)

    print(f"Created {num_files} small files.")


def test_random_small_files(num_files):
    start = time.time()

    for i in range(num_files):
        filename = os.path.join(
            FOLDER,
            f"image_{i}.bin"
        )

        with open(filename, "rb") as f:
            f.read()

    end = time.time()

    return end - start


def test_sequential_large_file(num_files, file_size_bytes):
    total_size = num_files * file_size_bytes

    data = b"0" * total_size

    with open(PACKED_FILE, "wb") as f:
        f.write(data)

    start = time.time()

    with open(PACKED_FILE, "rb") as f:
        f.read()

    end = time.time()

    return end - start


def cleanup(num_files):
    for i in range(num_files):
        filename = os.path.join(
            FOLDER,
            f"image_{i}.bin"
        )

        if os.path.exists(filename):
            os.remove(filename)

    if os.path.exists(FOLDER):
        os.rmdir(FOLDER)

    if os.path.exists(PACKED_FILE):
        os.remove(PACKED_FILE)


setup_test_files(NUM_FILES, FILE_SIZE)

small_files_time = test_random_small_files(NUM_FILES)

large_file_time = test_sequential_large_file(
    NUM_FILES,
    FILE_SIZE
)

print("\n=== AI Dataset I/O Test ===")
print(
    f"Small files time: "
    f"{small_files_time:.6f} seconds"
)

print(
    f"Packed file time: "
    f"{large_file_time:.6f} seconds"
)

cleanup(NUM_FILES)