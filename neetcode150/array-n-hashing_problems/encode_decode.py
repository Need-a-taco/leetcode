def encode(strs: list[str]) -> str:
        encoded_str = ""
        delimiter = "#"
        for s in strs:
            n = len(s)
            encoded_str += str(n) + delimiter + s
        return encoded_str
    
def decode(s: str) -> list[str]:
    decoded_lst = []
    # Hilarious implementation, psuedo for loop using 
    # while loop nested inside a while loop, LOL
    
    while s != "":
        n = ""
        i = 0
        
        # Find length of str by reading until # symbol
        while s[i] != "#":
            n += s[i]
            i += 1
        str_len = int(n)
        digits = len(n)
        
        decoded_str = s[digits + 1 : len(n) + 1 + int(n)]
        decoded_lst.append(decoded_str)
        s = s[str_len + digits + 1 :]
    return decoded_lst


s = ["asdfasdfasdf", "asdf"]

encoded_s = encode(s)
print(encoded_s)
back_to_s = decode(encoded_s)
print(back_to_s)


