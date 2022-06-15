def guess_enough(root, target):
    if abs(root ** 3 - target) < 0.0000000001:
        return True

    return False

def improve(root, target):
    return ((target / (root ** 2)) + (2 * root)) / 3

def cub_root(n):
    root = 1

    while not guess_enough(root, n):
        root = improve(root,n)

    return root

print(cub_root(64))                    