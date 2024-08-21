s1 = "asdf"
s2 = "qwerty"

# Setting up our hashmaps to keep track of character counts
s1_map = {}
s2_map = {}

for i in range(97, 123):
    s1_map[chr(i)] = 0
    s2_map[chr(i)] = 0

for c in s1:
    s1_map[c] += 1

for c in s2[0:len(s1)]:
    s2_map[c] += 1
    
print(s1_map)
print(s2_map)
# Initialize and find our matches var
matches = 0
for i in range(97, 123):
    if (s1_map[chr(i)] == s2_map[chr(i)]):
        matches += 1
print(matches)
