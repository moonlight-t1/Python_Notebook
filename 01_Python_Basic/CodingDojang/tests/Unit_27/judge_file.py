with open("words2.txt", "r") as file:

    words = file.read().split()

    for word in words:
        if "c" in word:
            print(word.strip(",."))
        else:
            continue

