def largest_palindrome():
    num1 = 100
    
    palindromes = []
    while num1 < 1000:
        num2 = 100
        while num2 < 1000:
            product = num1 * num2
            if str(product) == str(product)[::-1]:
                palindromes.append(product)
            num2 += 1
        num1+=1
    print(max(palindromes))
largest_palindrome()