import sys
input = sys.stdin.readline

alphabet = input().rstrip()

strings = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
result = 0
alone_count = len(alphabet)

for i in strings:
    if i in alphabet:
        strings_count = alphabet.count(i)
        result = result + (1*strings_count)
        alphabet = alphabet.replace(i, "0")
        alone_count = alone_count - (len(i) * strings_count)

result += alone_count
print(result)
