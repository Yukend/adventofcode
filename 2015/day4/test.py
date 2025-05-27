import hashlib


def find_hash_with_leading_zeros(input_string, zero_count):
    """Find the smallest integer such that the MD5 hash of the input string
    concatenated with the integer starts with the specified number of zeros."""
    i = 0
    target_prefix = "0" * zero_count
    while True:
        md5_hash = hashlib.md5(f"{input_string}{i}".encode()).hexdigest()
        if md5_hash.startswith(target_prefix):
            return i
        i += 1


def main():
    input_string = "ckczppom"
    print("Part 1:", find_hash_with_leading_zeros(input_string, 5))
    print("Part 2:", find_hash_with_leading_zeros(input_string, 6))


if __name__ == "__main__":
    main()
