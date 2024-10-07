def extraction(input):
    extracted = ""
    for x in input:
        if (64 < ord(x) < 123 or ord(x) == 32):
            extracted += x
    return extracted


def reverseWord(input):
    reversed = ""
    reversed = input[-1:-(len(extracted)):-1]
    return reversed


def replaceLetters(input):
    vowels = "EU"
    output = ""
    for x in input:
        if (x not in vowels):
            output += x
        else:
            if (x == 'E'):
                output += 'A'
            elif (x == 'U'):
                output += 'O'
    return output


input = "##$$$@!yalpstcejorp EPUVT****9887"
extracted = extraction(input)
words = extracted.split()
output = reverseWord(words[0])
output += " "
output += replaceLetters(words[1])
print(output)
