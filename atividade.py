def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        # Adicionando verificação para evitar divisão por zero
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return 0

# Exemplos de uso:
resultado = calculadora(5, 3, 1)  # Soma
print("Resultado da Soma:", resultado)

resultado = calculadora(5, 3, 2)  # Subtração
print("Resultado da Subtração:", resultado)

resultado = calculadora(5, 3, 3)  # Multiplicação
print("Resultado da Multiplicação:", resultado)

resultado = calculadora(5, 3, 4)  # Divisão
print("Resultado da Divisão:", resultado)

resultado = calculadora(5, 3, 5)  # Operação inválida, retorna 0
print("Resultado de Operação Inválida:", resultado)
