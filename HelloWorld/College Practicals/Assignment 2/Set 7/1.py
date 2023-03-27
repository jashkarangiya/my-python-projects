# 7.1 Write a program that asks the user how many Fibonacci numbers to generate and then
# generates them. Take this opportunity to think about how you can use functions. Make sure to
# ask the user to enter the number of numbers in the sequence to generate. (Hint: The Fibonacci
# sequence is a sequence of numbers where the next number in the sequence is the sum of the
# previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibonacciSeries(number):
    for i in range(2, number-2):
        fibonacciSeries = []
        for fibonacciSeries[0] in fibonacciSeries:
            fibonacciSeries[0] = 0
            fibonacciSeries[1] = 1
        fibonacciSeries.append(fibonacciSeries[i-2]+fibonacciSeries[i-1])
        print(fibonacciSeries)
    return fibonacciSeries
fibonacciSeries(5)