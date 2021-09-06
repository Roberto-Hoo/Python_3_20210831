import modulo as m1

m1.fib(515000)
print("")
m1.fib2(30)
k = 1 or False
print('')
print(k)

m1.nl()
for n in range(2, 20):
    resultado = m1.eh_primo(n)
    if resultado == True:
        print(n, 'é um número primo')
    else:
        print(n, 'igual', resultado, '*', n // resultado)

m1.nl()
m1.lista_numeros_primos(20)

m1.nl()
m1.lista_numeros_primos2(20)

m1.nl()
for c in range(-100, 201, 20):
    print(f'{c:>7.2f} Celsius = {m1.celsius_to_fahrenheit(c):>7.2f} Fahrenheit')

m1.nl()
for f in range(-200, 401, 20):
    print(f'{f:>7.2f} Fahrenheit = {m1.fahrenheit_to_celsius(f):>7.2f} Celsius')

m1.nl()
for c in range(-100, 201, 20):
    print(f'{c:>7.2f} Celsius = {m1.fahrenheit_to_celsius(m1.celsius_to_fahrenheit(c)):>7.2f} Celsius')

m1.nl()
a, b, c = 1, -1, -2
print(f'As raízes de {a:>5.1f}x**2 + {b:>5.1f}x + {c:>5.1f} são:\n')
m1.Baskara(a,b,c)

m1.nl()
a, b, c = 1, -1, 2.5
print(f'As raízes de {a:>5.1f}x**2 + {b:>5.1f}x + {c:>5.1f} são:\n')
m1.Baskara(a,b,c)
