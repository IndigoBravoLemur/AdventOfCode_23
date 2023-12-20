from itertools import zip_longest

with open("mini_test.txt") as f:
    patterns = f.read().split("\n\n")

patterns = [p.split("\n") for p in patterns]
pc = 1
total = 0
for pattern in patterns:
    mirror = ()
    #print(f"checking pattern {pc}")
    #print(pattern)
    for l in range(len(pattern)-1):
        upper = pattern[:l+1]
        upper.reverse()
        lower = pattern[l+1:]
        print(f"line {l} comparing {upper} to {lower}")
        #if len(upper) == 0 or len(lower) == 0:
        result = all(x == y for x, y in zip(upper, lower))
        #else:
            #result = False
        #result = all(x == y for x, y in zip_longest(upper, lower, fillvalue=''))
        print(result)
        if result:
            mirror = ("h",l)
            total += (l+1)*100
            #break
    
    if not mirror or mirror[1]==0:

        for l in range(1,len(pattern[0])):
            left = pattern[0][:l+1]
            left = left[::-1]
            right = pattern[0][l+1:]
            #print(f"line {l} comparing {left} to {right}")
            result = all(x == y for x, y in zip(left, right))
            #result = all(x == y for x, y in zip_longest(upper, lower, fillvalue=''))
            if result:
                #print("Testing the vertical")
                for row in pattern:
                    rleft = pattern[0][:l+1]
                    rleft = left[::-1]
                    rright = pattern[0][l+1:]
                    #rresult = all(x == y for x, y in zip_longest(upper, lower, fillvalue=''))
                    rresult = all(x == y for x, y in zip(rleft, rright))
                    #print(f"result - {rresult}")
                    if not rresult:
                        break
                if rresult:
                    mirror = ("v",l)
                    total += l+1
                    break
    if mirror:
        print(mirror)
    else :
        print(f"No mirror found for pattern {pc}")
    
    pc += 1

print(total)
        
        
    


    