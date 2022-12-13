def numero_para_binario(x):
  Bin = bin(x)
  print(f'{x} em binário é {Bin}')

def numero_para_hexadecimal(x):
  Hex = hex(x)
  print(f'{x} em hexadecimal é {hex}')

def numero_para_octal(x):
  Oct = oct(x)
  print(f'{x} em octal é {Oct}')

numero = int(input('Digite o número:'))
while True:
  print('''
Converter em
[1]binario
[2]hexadecimal
[3]octal
[4]sair
  ''')
  opç = int(input('Digite:'))
  if opç ==1:
    numero_para_binario(numero)
  elif opç ==2:
    numero_para_hexadecimal(numero)
  elif opç ==3:
    numero_para_octal(numero)
  elif opç ==4:
    break
