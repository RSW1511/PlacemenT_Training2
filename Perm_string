def permutation(perm, word):
    if len(word) == 0:
        print(perm)
    else:
        for i in range(len(word)):
            permutation(perm + word[i], word[:i] + word[i+1:])

def find_permutations(input_string):
    permutation("", input_string)

find_permutations("RSW")
