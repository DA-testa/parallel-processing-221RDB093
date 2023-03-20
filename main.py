# python3

def parallel_processing(n, m, data):
    output = []
    list1 = []
    list2 = []
    for i in range (n):
        list1.append(i)
        list2.append(0)
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    x = 0
    y = 0
    for i in range (m):
        output.append (list1[x])
        output.append (list2[y])
        x = x+ 1
        while True :
            list2[x] = list2[x] + 1 
            inputList[i] = inputList[i] - 1
            if inputList[i] == 0:
                break
        if x == len(list1):
            x = 0
            y = y + 1

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    nm = input()
    nm_split = nm.split()
    # n - thread count 
    n = int(nm_split[0])
    # m - job count
    m = int(nm_split[1])
    n = 0
    m = 0

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    inputList = list(map(int, input().spli()))
    # TODO: print out the results, each pair in it's own line

    for j in range (0,len(result),2):
        print(result[i], result[i+1])



if __name__ == "__main__":
    main()
