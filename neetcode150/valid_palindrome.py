def isPalindrome(s):
    replacements = [('!', ''), ('?', ''), 
                    (',', ''), ('.', ''), 
                    (' ', '')]
    
    for c, r in replacements:
        if c in s:
            s = s.replace(c, r)
    s = s.lower()
    n = len(s)
    
    for i in range(0, (n // 2)):
        if s[i] != s[n - i - 1]:
            return False
    return True
    
# This seems to work, it just 
