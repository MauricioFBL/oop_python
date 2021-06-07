# Notacion asintotica
# BIG O
import time
import sys
def f(n):
    for i in range(n):
        print(i)
        
    for i in range(n):
        print(i)

    # O(n)+ O(n) = O(n + n)= O(n)

    
    for i in range(n*n):
        print(i)

    
    # O(n)* O(n*n) = O(n*n)= O(n)**2
def y(n):
	for i in range(n): #n pasos
		for j in range(n): #n pasos
		print(i, j)

#O(n) * O(n) = O(n * n) = O(n**2), la funcion crece en O de n**2