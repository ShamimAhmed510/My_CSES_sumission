def camelcase(s):
    if not s:
        return 0
        
    word_count = 1 
    
    for char in s:
        if char.isupper():
            word_count += 1
            
    return word_count

input = input()

result = camelcase(input)

print(result)
