n = int(input())
text = "Python is a programming languaage that lets you work quickly"
words = text.split()

if len(words) < n:
    print("wrong")
else:
    n_gram = zip(*[words[i:] for i in range(n)])
    for i in n_gram:
        print(i)
