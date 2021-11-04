def fizzbuzz(n):
    answer = []
    for i in range(1, n+1):
        if i % 5 == 0 and i % 3 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        elif i % 3 != 0 and i % 5 != 0:
            answer.append(str(i))
    return answer


if __name__ == "__main__":
    print(fizzbuzz(3))
    print(fizzbuzz(5))
    print(fizzbuzz(15))
