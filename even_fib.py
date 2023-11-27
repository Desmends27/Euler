# 1 2 3 5 8
 # @TODO: update method and use dynamic programming
def fib()-> int:
    prev = 0
    current = 1
    sum = 0
    while current < 4000000:
        prev, current = current, current+prev
        if (current % 2 == 0):
            sum += current
    print(sum)

fib()