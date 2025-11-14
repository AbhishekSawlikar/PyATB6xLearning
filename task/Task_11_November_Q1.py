#Question - ✅ Count vowels and consonants in a String

input_string= input("Enter your string \n")

vowel="aeiou"

vowel_count=0
consonent=0
result=list()

for char in input_string:
    if char in vowel:
        vowel_count=vowel_count+1
    else:
        consonent=consonent+1



print(vowel_count)
print(consonent)