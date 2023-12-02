def sum_of_squares(limit):
    return (sum([i**2 for i in range(1, limit+1)]))
def square_of_sum(limit):
    return (sum([i for i in range(1, limit+1)]) ** 2)


print(square_of_sum(100) - sum_of_squares(100))