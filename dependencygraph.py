rules = {
 "S":("E"),
 "E":("T+E", "T*T", "T+T"),
 "T":("d")
}
def getType(a):
 if a in ['1','2','3','4','5','6','7','8','9','0']:
   print('d.val = '+a)
   return 'T'
 for c in rules.keys():
   if a in rules[c]:
   return c
def parse(a):
   if len(a)==1:
     rep = (getType(a), int(a))
     print(rep[0]+'.val =', rep[1])
     return rep
  if '+' in a:
   ind = a.find('+')
   terms = [a[:ind], a[ind+1:]]
   t2 = parse(terms[1])
   t1 = parse(terms[0])
   rep = (getType(t1[0]+'+'+t2[0]), t1[1]+t2[1])
   print(rep[0]+'.val =', rep[1])
   return rep
  if '*' in a:
   ind = a.find('*')
   terms = [a[:ind], a[ind+1:]]
   t2 = parse(terms[1])
   t1 = parse(terms[0])
   rep = (getType(t1[0]+'*'+t2[0]), t1[1]*t2[1])
   print(rep[0]+'.val =', rep[1])
   return rep
inp = input('Enter an expression that follows the regular expression : ([0-9]\+)*\*[0-
9] i.e. a+b+c+...+d*e \nExpression : ')
print('\n\nFlow of actions in dependancy graph : ')
out = parse(inp)
if out[0]=='E':
 print('S.val =', out[1])
