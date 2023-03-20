# python3

def parallel_processing(n, m, Data):
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
        output.append (list2[x])
        
        while True :
            list2[x] = list2[x] + 1 
            Data[i] = Data[i] - 1
            if Data[i] == 0:
                break
        x +=1
        if x == len(list1):
            x = 0
            y +=1
        
    return output

def main():
    nm = input()
    nm_split = nm.split()
    # n - thread count 
    n = int(nm_split[0])
    # m - job count
    m = int(nm_split[1])
    
    Data = list(map(int, input().split()))
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    #data = []

    # TODO: create the function
    result = parallel_processing(n,m,Data)
    
    # TODO: print out the results, each pair in it's own line

    for i in range (0,len(result),2):
        print(result[i], result[i+1])



if __name__ == "__main__":
    main()
