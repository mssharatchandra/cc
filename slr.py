from collections import deque
from collections import OrderedDict
from pprint import pprint
from firfol import makeGrammar, findFirsts, findFollows

rules   = ['S->AA', 'A->aA|b']
start   = 'S'
aug     = ''
nt_list = ['S', 'A']
t_list  = ['a', 'b', '$']
g       = makeGrammar(rules)
firsts  = findFirsts(g)
follows = findFollows(g, start)

class State:
    _id=0
    def __init__(self, closure):
        self.closure=closure
        self.no=State._id
        State._id+=1

class Item(str):
    def __new__(cls, item):
        self=str.__new__(cls, item)
        return self
    def __str__(self):
        return super(Item, self).__str__()        

def closure(items):
    def exists(newitem, items):
        for i in items:
            if i==newitem:
                return True
        return False

    global g
    while True:
        flag=0
        for i in items:             
            if i.index('.')==len(i)-1: continue
            Y=i.split('->')[1].split('.')[1][0]
            if i.index('.')+1<len(i)-1:
                lastr=list(firsts[i[i.index('.')+2]]-set(chr(1013)))                
            for prod in g.keys():
                head, body=prod, g[prod]
                if head!=Y: continue
                for b in body:
                    newitem=Item(Y+'->.'+b)
                    if not exists(newitem, items):
                        items.append(newitem)
                        flag=1
        if flag==0: break
    return items

def goto(items, symbol):
    initial=[]
    for i in items:
        if i.index('.')==len(i)-1: continue
        head, body=i.split('->')
        seen, unseen=body.split('.')
        if unseen[0]==symbol and len(unseen) >= 1:
            initial.append(Item(head+'->'+seen+unseen[0]+'.'+unseen[1:]))
    return closure(initial)

def calc_states():
    def contains(states, t):
        for s in states:
            if len(s) != len(t): continue
            if sorted(s)==sorted(t):
                for i in range(len(s)):
                    if s[i]!=t[i]: break
                else: return True
        return False
    global g, nt_list, t_list, aug

    head, body=aug, g[aug]
    for b in body:
        states=[closure([Item(head+'->.'+b)])]
    while True:
        flag=0
        for s in states:
            for e in nt_list+t_list:                
                t=goto(s, e)
                if t == [] or contains(states, t): continue
                states.append(t)
                flag=1
        if not flag: break    
    return states 

def make_table(states):
    global nt_list, t_list
    def getstateno(t):
        for s in states:
            if len(s.closure) != len(t): continue
            if sorted(s.closure)==sorted(t):
                for i in range(len(s.closure)):
                      if s.closure[i]!=t[i]: break
                else: return s.no
        return -1
    def getprodno(closure):
        closure=''.join(closure).replace('.', '')
        return list(g.keys()).index(closure.split('->')[0])
    SLR_Table=OrderedDict()    
    for i in range(len(states)):
        states[i]=State(states[i])
    for s in states:
        SLR_Table[s.no]=OrderedDict()
        for item in s.closure:
            head, body=item.split('->')
            if body=='.': 
                for term in follows[item.split('->')[0]]: 
                    if term not in SLR_Table[s.no].keys():
                        SLR_Table[s.no][term]={'r'+str(getprodno(item))}
                    else: SLR_Table[s.no][term] |= {'r'+str(getprodno(item))}

                continue
            nextsym=body.split('.')[1]
            if nextsym=='':
                if getprodno(item)==0:
                    SLR_Table[s.no]['$']='accept'
                else:
                    for term in follows[item.split('->')[0]]:
                        if term not in SLR_Table[s.no].keys():
                            SLR_Table[s.no][term]={'r'+str(getprodno(item))}
                        else: SLR_Table[s.no][term] |= {'r'+str(getprodno(item))}
                continue
            nextsym=nextsym[0]
            t=goto(s.closure, nextsym)
            if t != []: 
                if nextsym in t_list:
                    if nextsym not in SLR_Table[s.no].keys():
                        SLR_Table[s.no][nextsym]={'s'+str(getstateno(t))}
                    else: SLR_Table[s.no][nextsym] |= {'s'+str(getstateno(t))}
                else: SLR_Table[s.no][nextsym] = str(getstateno(t))
    return SLR_Table

def augment_grammar():
    global start, aug
    for i in range(ord('Z'), ord('A')-1, -1):
        if chr(i) not in nt_list:
            g[chr(i)]=start
            aug = chr(i)
            return

def main():
    global ntl, nt_list, tl, t_list    
    augment_grammar()
    follows[aug] = ['$']
    nt_list = list(g.keys())
    j = calc_states()
    ctr=0
    for s in j: 
        print("Item{}:".format(ctr))
        for i in s:
            print("\t", i)
        ctr+=1
    table=make_table(j)
    print('_________________________________________________________________')
    print("\n\tSLR(1) TABLE\n")
    sym_list = nt_list + t_list
    print('_________________________________________________________________')
    print('\t|  ','\t|  '.join(sym_list),'\t\t|')
    print('_______________________________________________________________')
    for i, j in table.items():            
        print(i, "\t|  ", '\t|  '.join(list(j.get(sym,' ') if type(j.get(sym))in (str , None) else next(iter(j.get(sym,' ')))  for sym in sym_list)),'\t\t|')
        s, r=0, 0
        for p in j.values():
            if p!='accept' and len(p)>1:
                p=list(p)
                if('r' in p[0]): r+=1
                else: s+=1
                if('r' in p[1]): r+=1
                else: s+=1      
    print('_________________________________________________________________')
    return 
main()
