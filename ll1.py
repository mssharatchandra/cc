from firfol import makeGrammar, findFirsts, findFollows
prods = makeGrammar(['A->BC', 'C->+BC|eps', 'B->DE', 'E->*DE|eps', 'D->a'])
nonterminals = set(prods.keys())
firsts = findFirsts(prods)
follows = findFollows(prods, 'A')
print('LL(1) Parsing table :')
print('---------------------')
for nt in nonterminals:
 print('\t',nt,":")
 ntprods = prods[nt]
 if 'eps' in ntprods:
 for ntfol in follows[nt]:
 print('\t\t'+ntfol+' : '+nt+'->eps')
 ntprods.remove('eps')
 if ntprods==[]:
 continue
 for ntfir in firsts[nt]:
 if ntfir=='eps':
 continue
 print('\t\t'+ntfir+' : '+nt+'->'+ntprods[0])
