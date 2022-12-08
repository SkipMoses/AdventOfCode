# Read in the tests
with open("test.txt") as f:
    tests = [l.strip() for l in f.readlines()]
    f.close()

# Read in the input

with open("input.txt") as f:
    inpu = [l.strip() for l in f.readlines()][0]
    f.close()

# Create memory for which letters we have seen

alph = [0]*27 # First element of list ignored for indexing

t = tests[1]
for start in range(len(t)-3):
    beg = t[start]
    # Flag this letter 
    alph[ord(beg)-96] = 1
    for cur in range(1,4):
        check = t[start + cur]
        num = ord(check)-96
        print("checking " + check)
        if alph[num]: # duplicate found
            # Reset memory
            alph = [0]*27
            print("double found for " + check)  
            # Move start forward
            break
        else:
            # Flag new letter
            print(check + " is new")  
            alph[num] = 1

    # Check if we found 4 unique letters
    print("Found a run of " + str(sum(alph)))          
    if sum(alph) == 4: # Found it
        print(start + cur + 1)
        break

# Part 2    
for start in range(len(t)-3):
    beg = t[start]
    # Flag this letter 
    alph[ord(beg)-96] = 1
    for cur in range(1,14):
        check = t[start + cur]
        num = ord(check)-96
        if alph[num]: # duplicate found
            # Reset memory
            alph = [0]*27
            # Move start forward
            break
        else:
            # Flag new letter
            alph[num] = 1

    # Check if we found 4 unique letters
    if sum(alph) == 14:
        print(start + cur + 1)
        break
