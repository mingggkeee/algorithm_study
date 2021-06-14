def solution(s):
    length = []
    result = ""
    if len(s) == 1:
        return 1
    
    for cut in range(1, len(s)//2+1):
        count = 1
        group = s[:cut]
        for i in range(cut,len(s),cut):
            if group == s[i:i+cut]:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + group
                group = s[i:i+cut]
                count = 1
        if count == 1:
            count = ""
        result += str(count) + group
        length.append(len(result))
        result = ""
        
    return min(length)