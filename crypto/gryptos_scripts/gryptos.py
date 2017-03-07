from g1and2 import GRYPTO_TABLE, CIPHER_1, CIPHER_2
from g3 import CIPHER_3
from g4 import CIPHER_4

left = CIPHER_1 + CIPHER_2 + CIPHER_3 + CIPHER_4
right = GRYPTO_TABLE

print(left, right)