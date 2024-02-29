def readFile(text):
    f = open(text, 'r', encoding="UTF-8")
    words = []
    while True:
        line = f.readline().strip()
        if not line:
            break
        words.append(line)
    if len(words)%2==0:
        return words
    else:
        raise ValueError("Количество строк поступивших на вход нечетное")

def normalPermutation(words):
    for i in range(1, len(words), 2):
        answ = []
        a = list(words[i-1])
        b = list(words[i])
        for j in a:
            if j in b:
                answ.append(j)
                b.pop(b.index(j))
        print("".join(sorted(answ)))

from os import listdir, getcwd

print(getcwd())
files = [i for i in listdir(getcwd()) if ".txt" in i]

for i, file in enumerate(files, start=1):
    try:
        print(f"Тест {i}")
        normalPermutation(readFile(file))
    except Exception as e:
        print(e)
