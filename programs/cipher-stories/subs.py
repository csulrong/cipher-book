import copy
from collections import OrderedDict

encrypt_table = {'a': 'P', 'c': 'T', 'b': 'O', 'e': 'Q', 'd': 'L', 'g': 'V', 'f': 'K', 'i': 'N', 'h': 'C', 'k': 'W', 'j': 'Y', 'm': 'U', 'l': 'Z', 'o': 'A', 'n': 'B', 'q': 'M', 'p': 'G', 's': 'F', 'r': 'S', 'u': 'R', 't': 'E', 'w': 'D', 'v': 'H', 'y': 'I', 'x': 'J', 'z': 'X'}

def preprocess():
    with open("hamlet.txt", "r") as f:
        origintext = f.read()

    print("============ origin text ============\n")
    print(origintext)

    plaintext = origintext.lower()

    print("===== lower case of origin text =====\n")
    print(plaintext)

    special_chars = '''!@#$%^&*()_+-={}[]|\:;"'~`<>,.?/'''
    for c in special_chars:
        plaintext = plaintext.replace(c, "", -1)

    plaintext = plaintext.replace("\n", "", -1)
    plaintext = plaintext.replace(" ", "", -1)
    # plaintext = plaintext.replace("\r", " ", -1)
    print("============= plaintext =============\n")
    print(plaintext)

    # line width = 85 chars
    width = 85
    i = 0
    pretty = ""
    while i < len(plaintext):
        pretty += plaintext[i:(i+width)] + "\n"
        i += width

    print("============= plaintext [pretty] =============\n")
    print(pretty)

    return plaintext

def encrypt(plaintext):
    ciphertext = copy.copy(plaintext)
    for k, v in encrypt_table.items():
        ciphertext = ciphertext.replace(k, v, -1)

    # ciphertext = ciphertext.replace("\n", " ", -1)
    # ciphertext = ciphertext.replace(" ", "", -1)
    print("============ ciphertext =============\n")
    print(ciphertext)

    # line width = 85 chars
    width = 85
    i = 0
    pretty = ""
    while i < len(ciphertext):
        pretty += ciphertext[i:(i+width)] + "\n"
        i += width

    print("============= ciphertext [pretty] =============\n")
    print(pretty)

    return ciphertext

def stats(text):
    stats_table = dict()
    for c in text:
        if c not in stats_table.keys():
            stats_table[c] = 1
        else:
            stats_table[c] += 1
    
    # ordered_stats_table = OrderedDict()
    sum = reduce(lambda x, y: x+y, stats_table.values())
    # for c in sorted(stats_table.keys()):
    #     if ord(c) < ord('A') or ord(c) > ord('Z'):
    #         continue

    #     ordered_stats_table[c] = (stats_table[c], stats_table[c]*100.0/sum)

    # print("============ stats =============\n")
    # for k, v in ordered_stats_table.items():
    #     print("\t%s\t%i\t%.2f" % (k, v[0], v[1]))

    sorted_stats_table = []
    for k, v in stats_table.items():
        for i in range(len(sorted_stats_table)):
            if v > sorted_stats_table[i][1]:
                sorted_stats_table.insert(i, (k, v, v*100.0/sum))
                break
        else:
            sorted_stats_table.append((k, v, v*100.0/sum))

    print("============ stats =============\n")
    for c in sorted_stats_table:
        print("\t%s\t%i\t%.2f" % (c[0], c[1], c[2]))


if __name__ == "__main__":
    plaintext = preprocess()

    stats(plaintext)

    ciphertext = encrypt(plaintext)

    stats(ciphertext)
