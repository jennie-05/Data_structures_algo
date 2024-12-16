
test_cases = int(input())

for _ in range(test_cases):
    n=int(input())
    data = list(map(int, input().split()))
    for i in range(len(data)):
        while (data[i]+1)>data[i+1]:
            if (data[i]+1)>data[i+1]:
                for j in range(len(data)):
                    if j+i+1==n-1:
                        break
                    data[j+i]=data[j+i+1]

                data[n-1]=data[i+1]+1
    data1=" ".join(data)
    print (data1)
            
                
                 
    
    



    


