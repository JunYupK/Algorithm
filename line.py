s = input()
start = 0
end = len(s) - 1
check = {}
for c in s:
    if c in check:
        check[c] += 1
    else:
        check[c] = 1


def check_even(check):
    for key, val in check.items():
        if val % 2 != 0:
            return False
    return True


while start < end:
    if check[s[start]] % 2 != 0:
        check[s[start]] -= 1
        start += 1
    elif check[[]]
        100000
