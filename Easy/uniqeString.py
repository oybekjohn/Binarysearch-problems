def solve(s):
        li = []
        k = True
        if s != '':
            for i in s:
                if i not in li:
                    li.append(i)
                else:
                    k = False
        else:
            return k
        
        return k
    

print(solve('qwertyuiopaq'))