clos = {'{': '}', '(': ')', '[': ']'}

ch = input().strip()
l=['{','(',"'",'[',"`",'"',')',']','}']
j=0
for i in ch:
    if i in l:
        if i in ['(','{','[']:
            if ch.count(i)!=ch.count(clos[i]):
                print("SYNTAX_ERROR")
                j=1
                break
            
        if  ch.count(i)%2!=0:
            continue
        else:
            j+=1
if j==0:
    print("SYNTAX_ERROR")

l = []
i = 0
chi = ''
while i < len(ch) :
    
    if ch[i] in ["'", '"', '`']:
        j=i
        while ch[j]!=ch[i]:
            chi+=ch[j]
            j+=1
        chi+=ch[i]
        l.append(chi)
    
    
    elif ch[i] in ['{', '(', '[']:
        j=i
        _in = 1
        _out = 0
        while j < len(ch) :
            if _in == _out and ch[j]==clos[ch[i]]:
                break
            chi+=ch[j]
            
            if ch[j] == ch[i]:
                _in += 1
            elif ch[j] == clos[ch[i]]:
                _out += 1
            j+=1
    
    i+=1
    
            
    l.append(chi)
print(l)
