with open("words.txt", "r") as file:
    words = file.readlines()
    for word in words:
        word = word.strip("\n")

        if word == word[::-1]:
            print(word, "is a parlindrome")
        else:
            print(word, "is not a parlindrome")
