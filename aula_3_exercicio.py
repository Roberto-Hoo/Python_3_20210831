import modulo as mod_1

mod_1.fib(515000)
print("")
mod_1.fib2(30)
k = 1 or False
print('')
print(k)

for n in range(2, 20):
        resultado=mod_1.eh_primo(n)
        if resultado==True:
            print(n, 'é um número primo')
        else:
            print(n, 'igual', resultado, '*', n // resultado)

print('\n***************************************************************************\n')

mod_1.lista_numeros_primos(20)