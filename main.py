num = int(input('Digite um numero: '))
print('''Escola uma das bases para conversão:
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL ''')

opcao = int(input('Sua opção: '))
if opcao == 1:
   print('o numero {} em BINARIO é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
   print('O numero {} em OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
   print('O numero {} em HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
  print('Opção invalida:')