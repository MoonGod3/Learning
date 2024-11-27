def is_palindrome(teststr):
    
    # Your code goes here.
    
    tmp = 0


    #first remove punctuations
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for ele in teststr:
        if ele in punc:
            teststr = teststr.replace(ele, "")

    teststr = teststr.replace(" ", "")
    
    for i, ltr in enumerate(teststr):
        if teststr[i].lower() == teststr[-(i+1)].lower():
            tmp += 1
            #print(i, -(i+1), teststr[(i)].lower(), teststr[-(i+1)].lower(), "they are equal", "value of tmp is", tmp)
        else:
            continue
            #print(i, -(i+1), teststr[(i)].lower(), teststr[-(i+1)].lower(), "they are not equal", "value of tmp is", tmp)
      
#print("Final value of tmp is:", tmp)

      
    if tmp == len(teststr):
        return 1 #"Yes, a Palindrome"
    else:
        return 0 #"No, not a Palindrome"

test_words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.","Race car!"]

total = 0
correct_answer = 3

for string in test_words:
    total += is_palindrome(string)

if total == correct_answer:
    print("There were ", total, "Palindromes in test_words")