import hashlib

key = "ckczppom"
n = 1
while not hashlib.md5((key + str(n)).encode("utf-8")).hexdigest().startswith("00000"):
    n += 1
print(n)

while not hashlib.md5((key + str(n)).encode("utf-8")).hexdigest().startswith("000000"):
    n += 1
print(n)