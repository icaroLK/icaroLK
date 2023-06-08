a = int(input('Digite um valor para "a": '))
b = int(input('Digite um valor para "b": '))
c = int(input('Digite um valor para "c": '))
print('\nA equação ficou: {}x² + {}x + {} = 0\n'.format(a, b, c))
delta = b**2 - 4 * a * c
print('Δ = {}\n'.format(delta))
if delta < 0:
    print('x1 = {}'. format('O delta é negativo, logo não existe solução real para a equação'))
else:
    print("x' = {:.2f}\nx'' = {:.2f}".format((-b + (delta)**0.5)/2*a, (-b - (delta)**0.5)/2*a))
