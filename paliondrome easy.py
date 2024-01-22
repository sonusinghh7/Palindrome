

word1 = str(input("Enter the text to cheak palindrome or not: "))
word2=(word1[ : :-1])
if word2==word1:
    print(word1,"is a palindrome word")
else:
    print(word1, "is not a palindrome word")