#!/usr/bin/env python

""" FizzBuzz parcial, parte 2
    Receba um número inteiro na entrada e 
    imprima Buzz se o número for divisível por 5. 
    Caso contrário, imprima o mesmo número que foi dado na entrada.
"""

def fizz(number):
    if((number%5) == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    number = int(input('Informe um numero '))
    if(fizz(number)) :
        print('Buzz')
    else :
        print(number)
        