#!/bin/python3.6

from requests import get
import collections
import base64


def strxor(a, b):
    return ''.join([chr(x ^ y) for (x, y) in zip(a, b)])


def main():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet += alphabet.lower()
    records = 100
    keysize = 340
    key = [None]*keysize
    key[0] = chr(72)
    key[1] = chr(85)
    key[2] = chr(221)
    key[3] = chr(86)
    key[4] = chr(40)

    ciphers = []
    for i in range(int(records/10)):
        r = get('http://pcocenas.fit.vutbr.cz/?login=xwilla00&cnt=10')
        for t in r.text.split():
            ciphers.append(base64.b64decode(t))

    final_key = []
    with open('xwilla00.txt', 'rb') as f:
        key = f.read()
    for i in key:
        final_key.append(i)

    # for i1, c1 in enumerate(ciphers):
    #     counter = collections.Counter()
    #     for i2, c2 in enumerate(ciphers):
    #         if not i1 == i2:
    #             for index, char in enumerate(strxor(c1, c2)):
    #                 if char in alphabet:
    #                     counter[index] += 1
    #
    #     known_spaces = []
    #     for index, val in counter.items():
    #         if val >= records * 0.7:
    #             known_spaces.append(index)
    #
    #     xor_with_spaces = strxor(c1, bytes(' '.encode())*keysize)
    #     for index in known_spaces:
    #         key[index] = xor_with_spaces[index]
    # final_key = []
    # for k in key:
    #     if k is None:
    #         final_key.append(0)
    #     else:
    #         final_key.append(ord(k))
    # to_save = ''
    # for j, i in enumerate(final_key):
    #     if key[j] is not None:
    #         to_save += chr(i)
    # print(len(to_save))
    # with open('xwilla00.txt', 'wb') as f:
    #     # f.write(to_save)
    #     for i in key:
    #         if i is not None:
    #             f.write(bytes([ord(i)]))

    for i in range(records):
        out = strxor(ciphers[i], final_key)
        out2 = ''
        for j, c in enumerate(out):
            if key[j]:
                out2 += c
        print(f'{i}: {out2}')
    return


if __name__ == '__main__':
    main()
