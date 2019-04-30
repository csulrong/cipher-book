import random
import copy
from collections import OrderedDict

orig_chars = [chr(i) for i in range(ord('a'), ord('z')+1)]

def gen_subs_map():
    input_chars = copy.deepcopy(orig_chars)
    subs_map = OrderedDict()

    while True:
        random.shuffle(input_chars)

        for i, c in enumerate(input_chars):
            if c == orig_chars[i]:
                break
        else:
            print("find a correct subs map")
            break
    
    # find a correct substitution map
    for i, c in enumerate(input_chars):
        subs_map[orig_chars[i]] = c.upper()

    print(subs_map)
    return subs_map

def print_each(subs_map):
    i = 0
    seq_str = ""
    pairs_str = ""
    for k, v in subs_map.items():
        seq = "{}/{}".format(v, i)
        pair = "{}/{}".format(k, v)
        if i == 0:
            seq_str += seq
            pairs_str += pair
        else:
            seq_str += ", " + seq
            pairs_str += ", " + pair
        i += 1

    print("mapped sequence")
    print(seq_str)

    print("substitution map")
    print(pairs_str)

if __name__ == "__main__":
    print_each(gen_subs_map())