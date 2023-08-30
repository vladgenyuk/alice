import sys


def my_decode(s: str) -> str:
    stack = [0]
    for i in s:
        if stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    return ''.join(stack[1:])


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        print(my_decode(f.read()))
