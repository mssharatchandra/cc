prods = {
 'S':('ABd', 'CBd'),
 'A':('aB','kB'),
 'B':('b'),
 'C':('c')
}
nonterminals = set(prods.keys())
start = 'S'
firsts = {k:[] for k in nonterminals}
follows = {k:set() for k in nonterminals}
def fillfirst(symbol):
 if firsts[symbol]!=[]:
 return
 prodcases = prods[symbol]
 anslist = set()
 for case in prodcases:
 if case=='epsilon':
 anslist.add('epsilon')
 continue
 while case!='':
 if case[0] in nonterminals:
 fillfirst(case[0])
 anslist = anslist.union(firsts[case[0]])
 if 'epsilon' in prods[case[0]]:
 case = case[1:]
 else:
 case = ''
 else:
 anslist.add(case[0])
 case = ''
 firsts[symbol]=anslist
for symbol in nonterminals:
 fillfirst(symbol)
for k in prods.keys():
 print('FIRST(',k,") : ",firsts[k],sep='')
for key in prods.keys():
 anslist = set()
 for symbol in prods.keys():
 if symbol==key:
 continue
 prodcases = prods[symbol]
 for case in prodcases:
 if key not in case:
 continue
 if case.find(key)==len(case)-1:
 anslist = anslist.union(follows[symbol])
 else:
 rem = case[case.find(key)+1:]
 while rem!="":
 nextsym = rem[0]
 if nextsym in nonterminals:
 anslist = anslist.union(firsts[nextsym])
 if 'epsilon' in firsts[nextsym]:
 rem = rem[1:]
 continue
 else:
 break
 else:
 anslist.add(nextsym)
 break
 if rem=="":
 anslist = anslist.union(follows[symbol])
 if 'epsilon' in anslist:
 anslist.remove('epsilon')
 if key==start:
 anslist.add('$')
 follows[key] = anslist
print('\n\n')
for k in prods.keys():
 print('FOLLOWS(',k,") : ",follows[k],sep='')
