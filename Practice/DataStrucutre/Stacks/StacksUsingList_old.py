# USer defined data structre in python
# Push˜
# Pop
# Peek or top
# isEmpty

# Implement stack using list
# LIFO

# push -> list.append
# pop -> list.pop
Stack = []


def push(input):
    Stack.append(input)


def pop():
    if not isEmpty():
        return Stack.pop()
    return None


def peek():
    if not isEmpty():
        return Stack[-1]
    return None


def isEmpty():
    return len(Stack) == 0


def clear():
    global Stack
    Stack = []
