from re import A
from tkinter import N
from cv2 import multiply
import os
from regex import D


class REF:
    def _init_(self,matrix):
        self.matrix=matrix

    def sort_zero(self):
        def sort(n):
            a=0
            b=0
            for i in n:
                if a==b:
                    if i==0:
                        a+=1
                else:
                    break
                b+=1
            return a
        def ascending(n):
            return n[0]
        nb=list()
        a=len(self.matrix)
        b=0
        while b<a:
            if self.matrix[b][0]==0:
                nb.append(self.matrix[b])
                self.matrix.pop(b)
                b-=1
                a-=1
            b+=1
        self.matrix.sort(key=ascending)
        nb.sort(key=sort)
        for j in nb:
            self.matrix.append(j)
        self.array()

    def check_zeroes(self,rows):
        c=0
        n=0
        for i in rows:
            if i==0:
                n+=1
            else:
                break
        return n

    def array(self):
        d=0
        for i in self.matrix:
            for j in i:
                if len(str(j))>1:
                    d=len(str(j))
        val=1
        for i in self.matrix:
            for j in i:
                if j==0.0 or -0.0:
                    j=int(j)
                print(format(str(j),f"<{str(val+5)}"),end="")
            print()
        print('\n')

    def row_echelon_form(self):
        n=0
        while n<len(self.matrix):
            zero=self.check_zeroes(self.matrix[n])
            z=n+1
            while z<len(self.matrix):
                calculated_zeros=self.check_zeroes(self.matrix[z])
                if calculated_zeros<zero+1 and zero<len(self.matrix[n]):
                    product=self.matrix[n][zero]/self.matrix[z][zero]
                    print(f"(R{str(z+1)} = {product} x R{str(z+1)} - R{str(n+1)})")
                    for g in range(len(self.matrix[z])):
                        self.matrix[z][g]=self.matrix[z][g]*product-self.matrix[n][g]
                    self.array()
                z+=1
            n+=1

    def reduced_row_echelon_form(self):
        n=0
        while n<len(self.matrix):
            b=0
            h=self.check_zeroes(self.matrix[n])
            if(h<len(self.matrix[n])):
                p=self.matrix[n][h]
                while b<len(self.matrix[n]):
                    self.matrix[n][b]=self.matrix[n][b]/p
                    b+=1
            n+=1
        self.array()

matrix=[[1, 2, 3], [4,5,6], [7,8,9]]   #<--Enter a square matrix, in the form of [1,2,3][4,5,6][7,8,9]
solution=REF(matrix)
print("Initial Matrix: ")
solution.array()
solution.sort_zero()
solution.row_echelon_form()
solution.reduced_row_echelon_form()
solution.sort_zero()