def flip(seq: list, index: int) -> list:
    return seq[:index - 1] + list(reversed(seq[index-1:]))

def pancakes(stackPancakes):
    # stackPancakes = list(reversed(stackPancakes))
    while(True):
        for i in range(len(stackPancakes)-1):
            print(stackPancakes)
            if abs(stackPancakes[i+1]-stackPancakes[i])==1:
                if (stackPancakes[i] >= stackPancakes[i+1]):
                    pass
                else:
                    stackPancakes = flip(stackPancakes, i+2)
            else:
                stackPancakes = flip(stackPancakes, i + 2)
        print(list(reversed(stackPancakes)))
        break


l3 = [10, 40, 228, 9, 13]
l2 = [5, 4, 3, 2, 1]
l =  [5, 1, 2, 3, 4]
# print(flip(l, 1))
# print(flip(l, 2))
pancakes(l3)
