# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the missing second character
# of the final pair with an underscore ('_').
#
# Examples:
#
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']
import codewars_test as test
# from codewars import test as test
def solution(s):
    _ = []
    while True:
        if len(s) > 1:
            _.append(s[:2])
            s = s[2:]
            print(_)
        elif len(s) == 1:
            _.append(s[:1] + '_')
            print('нечетное')
            return _
        else:
            print('конец цикла', _)
            return _




tmp = "asdfadsf"
print(solution(tmp))
tmp = "asdfads"
print(solution(tmp))
test.describe("Example Tests")
tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    test.assert_equals(solution(inp), exp)
