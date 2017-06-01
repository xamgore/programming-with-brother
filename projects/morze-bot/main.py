# import re
# extractMorze = re.compile(r"([—·]+( +[—·]+)*)")
# print(extractMorze.findall('a·—· kekek ·—·k keke ·—· ·—· ·—··—·———— kek'))


alph = {
    'a': '·−',
    'b': '−···',
    'c': '−·−·',
    'd': '−··',
    'e': '·',
    'f': '··−·',
    'g': '−−·',
    'h': '····',
    'i': '··',
    'j': '·−−−',
    'k': '−·−',
    'l': '·−··',
    'm': '−−',
    'n': '−·',
    'o': '−−−',
    'p': '·−−·',
    'q': '−−·−',
    'r': '·−·',
    's': '···',
    't': '−',
    'u': '··−',
    'v': '···−',
    'w': '·−−',
    'x': '−··−',
    'y': '−·−−',
    'z': '−−··',
}

ralph = {alph[k]: k for k in alph}

s = 'kakadu'
converted = " ".join([alph[n] for n in s])
print(converted)

l = (converted.split(' '))

# ralph = { '−−··' : 'z' }

def fromMorze(n):
    return ralph[n] if n in ralph else '???'


print("".join([fromMorze(st) for st in l]))


def toBottom(n):
    if n == '·':
        n = '.'
    elif n == '−':
        n = '_'
    return n


print(''.join([toBottom(e) for e in converted]))
