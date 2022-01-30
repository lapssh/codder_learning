# В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики:
# они говорили каким-то странным набором звуков.
#
# В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный
# шифр, т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли
# ключ к шифру и теперь нуждаются в помощи:
#
# Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки
# одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного
# алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую
# нужно расшифровать.
#
# Пусть, например, на вход программе передано:
# abcd
# *d%#
# abacabadaba
# #*%*d*%
#
# Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
# Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки,
# # которые и передаём на вывод программы:
# *d*%*d*#*d*
# dacabac
#
# Sample Input 1:
#
# abcd
# *d%#
# abacabadaba
# #*%*d*%
# Sample Output 1:
#
# *d*%*d*#*d*
# dacabac
# Sample Input 2:
#
# dcba
# badc
# dcba
# badc
# Sample Output 2:
#
# badc
# dcba

# a_input = 'abcd'
# shifr_input = '*d%#'
# open_message = 'abacabadaba'
# close_message = '#*%*d*%'
# a_input = 'dcba'
# shifr_input = 'badc'
# open_message = 'dcba'
# close_message = 'badc'
a_input = input()
shifr_input = input()
open_message = input()
close_message = input()


def create_crypto_dict(message, crypto):
    shifr = {}
    for i in range(0, len(message)):
        shifr[message[i]] = crypto[i]
    return (shifr)


def crypto_algorytm(message):
    crypto_message = ''
    for i in message:
        crypto_message = crypto_message + str(shifr[i])
    return crypto_message


def decrypto_algorytm(message):
    decrypto_message = ''
    for i in message:
        decrypto_message = decrypto_message + str(deshifr[i])
    return decrypto_message


shifr = create_crypto_dict(a_input, shifr_input)
deshifr = {v: k for k, v in shifr.items()}
# print(shifr, deshifr)
closed_messege = crypto_algorytm(open_message)
print(closed_messege)
print(decrypto_algorytm(close_message))
