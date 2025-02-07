# sliding window
str1 = input()
str2 = input()

window_size = len(str2)

stack = []

for ch in str1 : 
    stack.append(ch)
    if ch == str2[-1] and ''.join(stack[-window_size:]) == str2 : 
        for _ in range(window_size):
            stack.pop()

print(''.join(stack)) if stack else print("FRULA")