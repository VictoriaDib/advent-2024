def pt1():
    unsafe = 0
    count  = 0

    with open('input.txt') as f:
        for line in f:
            s = list(line.strip("\n").split(" "))
            count += 1
            inc = False
            dec = False
            for i in range(len(s)-1):
                if int(s[i]) <= int(s[i+1]):
                    dif = int(s[i+1]) - int(s[i])
                    if 1 <= dif <= 3:
                        inc = True
                    else:
                        dec = True
                        inc = True
                        break                        
                        
                elif int(s[i]) >= int(s[i+1]):
                    dif = int(s[i]) - int(s[i+1])
                    if 1 <= dif <= 3:
                        dec = True
                    else:
                        dec = True
                        inc = True    
                        break                    
                    
            if dec and inc:
                unsafe +=1

    safe = count - unsafe

    print("pt 1: ", safe)

pt1()

# 428
def is_safe(levels):
    inc = False
    dec = False
    for i in range(len(levels) - 1):
        if levels[i] <= levels[i + 1]:
            dif = levels[i + 1] - levels[i]
            if 1 <= dif <= 3:
                inc = True
            else:
                return False
        elif levels[i] >= levels[i + 1]:
            dif = levels[i] - levels[i + 1]
            if 1 <= dif <= 3:
                dec = True
            else:
                return False
    return not (inc and dec)  # Must be either all increasing or all decreasing


def pt2():
    unsafe = 0
    count = 0

    with open('input.txt') as f:
        for line in f:
            s = list(map(int, line.strip("\n").split(" ")))
            count += 1
            
            if is_safe(s):
                continue  
            
            # make it safe xd
            found_safe = False
            for i in range(len(s)):
                dampened = s[:i] + s[i + 1:] 
                if is_safe(dampened):
                    found_safe = True
                    break
            
            if not found_safe:
                unsafe += 1

    safe = count - unsafe

    print("pt 2: ", safe)

pt2()
