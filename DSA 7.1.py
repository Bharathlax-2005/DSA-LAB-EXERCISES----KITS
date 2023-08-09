def ins(n):
  for i in range(len(n)):
    key=n[i]
    j=i-1
    while j>=0 and key<n[j]:
      n[j+1]=n[j]
      j=j-1
    n[j+1]=key
  print(n)

n = input("Enter a comma-separated list of integers: ")
n = [int(x) for x in n.split(",")]
ins(n)
