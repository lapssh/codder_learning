# s = 'Hello, world!'
# s = 'A B'
# s = 'Q WERRTYUIOP'
s = input()
sep = s.find(' ')
word1 = s[:sep]
word2 = s[sep + 1:]
print(word2 + ' ' + word1)
