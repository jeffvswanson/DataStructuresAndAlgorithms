import sys
import threading

from collections import defaultdict

threading.stack_size(2 ** 28 - 1) # 256MB
sys.setrecursionlimit(2 ** 20)
print("recursion_limit =", sys.getrecursionlimit())

def main():

    d = defaultdict(bool)
    l = [1,2,3,4]

    for v in l:
        d[v] = False

    d[2] = change_to_true()

    print("d[2] =", d[2])

    limit = find_recursion_limit(1)

    print("The recursion limit was {}.".format(limit))

def change_to_true():

    return True

def find_recursion_limit(recursion_depth):
    try:
        print(recursion_depth)
        find_recursion_limit(recursion_depth+1)
    except:
        return recursion_depth

t = threading.Thread(target=main)
t.start()

if __name__ == "__main__":
    main()