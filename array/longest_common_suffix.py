def longestCommonSuffix(strs):
    if not strs or not strs[0]: 
        return ""
    
    min_len = min(len(s) for s in strs)
    suffix = ""
    
    for i in range(1, min_len + 1):
        char = strs[0][-i] 
      
        if all(s[-i] == char for s in strs):
            suffix += char
        else:
            break
    
    return suffix[::-1]


print(longestCommonSuffix(["glow", "flow", "throw"]))
print(longestCommonSuffix(["dog", "racecar", "car"]))


