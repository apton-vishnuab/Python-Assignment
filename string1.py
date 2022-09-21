def donuts(count):
  if count < 10:
    return("Number of donuts: {}".format(count))
  else:
    return("Number of donuts: many")
  
def both_ends(s):
  count = len(s)
  if count < 2:
    return('')
  else:
    newString = s[ 0:2 ] + s[count - 2: count ]
    return(newString)

def fix_start(s):
  n = len(s)
  s1 = s[0]
  s2 = s[1:n]
  s2 = s2.replace(s1, "*")
  s = s1+s2
  return(s)


def mix_up(a, b):
  return(b[0:2] + a[2:len(a)] + " " + a[0:2] + b[2:len(b)])

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
  print('donuts')
# Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')
 
 
  print('both_ends')
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')
 
 
 
  print('fix_start')
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')
 
 
  print ('mix_up')
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')
 
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
