def longestCommonPrefix(strs):
    if not strs or not strs[0]: 
        return ""
    
    min_len = min(len(s) for s in strs)
    prefix = ""
    
    for i in range(min_len):
        char = strs[0][i] 
      
        if all(s[i] == char for s in strs):
            prefix += char
        else:
            break
    
    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"])) 
print(longestCommonPrefix(["dog", "racecar", "car"]))


