fibo = [0,1]
n = input("¿Cuantos términos Fibonacci quieres obtener? ")
n = int(n)
for i in range (n-2):
    fibo.append(fibo[-1]+fibo[-2])
    print(fibo[i])