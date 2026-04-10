import itertools

"""
OPERATIONS
A = add
a = substract
M = multiply
m = multiply by negative
D = divide
d = divide by negative
"""

MULT_FACTOR = 1/10
DIV_FACTOR = 1/10

def op_A(c: str) -> int:
    return lambda base: base + ord(c)

def op_a(c: str) -> int:
    return lambda base: base - ord(c)

def op_M(c: str) -> int:
    return lambda base: round(base * (MULT_FACTOR * ord(c)))

def op_m(c: str) -> int:
    return lambda base: -1 * round(base * (MULT_FACTOR * ord(c)))

def op_D(c: str) -> int:
    return lambda base: round(base / (DIV_FACTOR * ord(c)))

def op_d(c: str) -> int:
    return lambda base: -1 * round(base / (DIV_FACTOR * ord(c)))

SEQ_BASE = 'AMDamd'

OPS = {
    'A': op_A,
    'a': op_a,
    'M': op_M,
    'm': op_m,
    'D': op_D,
    'd': op_d
}

SEQ = ''

def make_sequence():
    global SEQ
    SEQ = ''
    for p in itertools.permutations(SEQ_BASE):
        SEQ += ''.join(p)

def make_sum(s: str) -> int:
    base = 1
    for i_c in range(len(s)):
        i_o = i_c % len(OPS)
        op = OPS[SEQ[i_o]](s[i_c])
        base = op(base)
    return base

def check_sum(s: str, check: int) -> bool:
    return make_sum(s) == check

def check_sums(s1: str, s2: str) -> bool:
    return check_sum(s1, make_sum(s2))

'''
PROGRAMS
'''

def test():
    for word in 'this is a test sith si a sett'.split():
        print(f'{word:<5} {make_sum(word)}')
    
    test1 = 'Extraordinarily long phrase!'
    test2 = 'ndl!tyaEhsliraoeixrr nrao pg'
    print(test1, make_sum(test1))
    print(test2, make_sum(test2))

def summarize():
    s = input('Enter a string: ').strip()
    print(make_sum(s))

def compare():
    check = int(input('Enter a checksum: ').strip())
    s = input('Enter a string: ').strip()

    if check_sum(s, check):
        print('Checksum passed')
    else:
        print(f'Checksum failed. Sum of string is {make_sum(s)}')

'''
CORE
'''

def run():
    make_sequence()
    compare()

if __name__ == '__main__':
    run()
