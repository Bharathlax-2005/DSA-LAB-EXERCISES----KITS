# s
def sel(n):
    for i in range(len(n)):
        min=i
        for j in range(i+1,len(n)):
            if n[min]>n[j]:
                min=j
        n[i],n[min]=n[min],n[i]
    print(n)
n = input("Enter a comma-separated list of integers: ")
n = [int(x) for x in n.split(",")]
sel(n)