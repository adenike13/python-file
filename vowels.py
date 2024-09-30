vowels = "aeiou"
str = "This is a sentence"

count = {}.fromkeys(vowels, 0)

for bestfriend in str:
    if bestfriend in vowels:
        count[bestfriend] += 1
        
print(count)
