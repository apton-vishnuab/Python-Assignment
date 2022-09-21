def fix_start(s):
    n = len(s)
    s1 = s[0]
    for i in range(1, n):
        if s[i] == s1:
            s = s.replace(s[i], "*")
    return(s)
            
    
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main(): 
    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

if __name__ == '__main__':
  main()