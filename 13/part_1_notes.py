with open("mini_test.txt") as f:
    patterns = f.read().split("\n\n")

pattern_mirror_indexes = []

patterns = [p.split("\n") for p in patterns]
pc = 1
for pattern in patterns:
    # Pattern is an array of # and .
    print(f"checking pattern {pc}")
    print(pattern)
    # Go through each row of the pattern checking for a mirror of elements until one is found/for the length of the pattern
    for l in range(len(pattern)-1):
        # Create new arrays of from slices before and after current iterator
        upper = pattern[:l+1]
        upper.reverse()
        lower = pattern[l+1:]
        
        # by zipping the arrays, pairs are made of the above and below ros of the index, which should match if there is a mirror
        # all() validates all of the pairs are equal. zip discards those which it cannot find a pair for
        result = all(x == y for x, y in zip(upper, lower))
        if result:
            mirror = ("h",l)
            #print(f"line{l} is mirrored")
            break
    
    # go along the top row and check for mirroring
    for l in range(len(pattern[0])-1):
        left = pattern[0][:l+1]
        left = left[::-1]
        right = pattern[0][l+1:]
        
        #print(f"comparing {left} to {right}")

        result = all(x == y for x, y in zip(left, right))
        if result:
            for row in pattern:
                rleft = pattern[0][:l+1]
                rleft = left[::-1]
                rright = pattern[0][l+1:]
                rresult = all(x == y for x, y in zip(left, right))
                if not rresult:
                    break
            if rresult:
                mirror = ("v",l)
                #print(f"col{l} is mirrored")
                break
    
    print(mirror)
    pc += 1
        
        
    


    