import hashlib

input = "iwrupvqb"
i = 0
while True:
    md5_hash = hashlib.md5((input + str(i)).encode()).hexdigest()
    if md5_hash[0:5] == "00000":
        print(i)
        break
    if md5_hash[0:6] == "000000":
        print(i)
        break
    i += 1

