while True:
    resp = input('Salário: R$').strip()
    if resp == '0':
        break
    try:
        salario = float(resp)
        salarios.append(salario)
    except ValueError:
        print('Insira um valor válido!')
