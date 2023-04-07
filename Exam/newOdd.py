numberOfTestCases = int(input())

for i in range(numberOfTestCases):
    n, m = map(int, input().split())
    topics = list(map(int, input().split()))

    unique_topics = set(topics)

    if len(unique_topics) == m:
        print("Yes")
    else:
        print("No")




