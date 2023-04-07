numberOfTestCases = int(input())

for i in range(numberOfTestCases):
    list1 = []
    list2 = []
    list3 = []
    topics = []

    for j in range(2):
        string = input()
        string2 = input()
        list1 = string.split()
        list3 = string2.split()

        for element in list1:
            list2.append(int(element))
        for element in list3:
            topics.append(int(element))
        # print(list2)
        # print(topics)

        # print(list2[1])
        uniqueTopics = set(topics)
        # print(uniqueTopics)

        if len(topics) == list2[1]:
            print("YES")
        else:
            print("NO")