# G1 Solution based on http://www.thekryptosproject.com/kryptos/k0-k5/k1.php
# Theme / Template: http://www.elonka.com/kryptos/transcript.html

# G1 Expected ciphertext shape (from K1)
#
# EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJ (32)
# YQTQUXQBQVYUVLLTREVJYQTMKYRDMFD  (31)
#
# Key: PALIMPSEST
#
# Plaintext: BETWEENSUBTLESHADINGANDTHEABSENCEOFLIGHTLIESTHENUANCEOFIQLUSION
# Plain-er text: BETWEEN SUBTLE SHADING AND THE ABSENCE OF LIGHT LIES THE NUANCE OF IQLUSION
#
# 63 characters for message one
# Should include a typo
msg1 = "historyhastaughtyoutoseektheflagsinplainsightlikefeephiphothumb".upper()
assert len(msg1) == 63
# (History has taught you to seek the flags in plain sight like feephiphothumb)
#
# G2 Expected Ciphertext shape
# VFPJUDEEHZWETZYVGWHKKQETGFQJNCE   (31)
# GGWHKK?DQMCPFQZDQMMIAGPFXHQRLG    (30)
# TIMVMZJANQLVKQEDAGDVFRPJUNGEUNA   (31)
# QZGZLECGYUXUEENJTBJLBQCRTBJDFHRR  (32)
# YIZETKZEMVDUFKSJHKFWHKUWQLSZFTI   (31)
# HHDDDUVH?DWKBFUFPWNTDFIYCUQZERE   (31)
# EVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDX  (32)
# FLGGTEZ?FKZBSFDQVGOGIPUFXHHDRKF   (31)
# FHQNTGPUAECNUVPDJMQCLQUMUNEDFQ    (30)
# ELZZVRRGKFFVOEEXBDMVPNFQXEZLGRE   (31)
# DNQFMPNZGLFLPMRJQYALMGNUVPDXVKP   (31)
# DQUMEBEDMHDAFMJGZNUPLGESWJLLAETG  (32)
#
# 373 characters for message two
# G2 Key ABSCISSA


msg2 = "".join("""
It was made of pure gold how is that possible
They couldnt ration it out properly
They skipped and gathered round and round until the resting place was found
The riches were gathered up and transferred by ship to an unknown location who knows the exact location
Only OL This was his last message
forty five degrees twenty eight minutes twenty point one seconds north
One hundred twenty six degrees fifty eight minutes thirty two point one seconds west
""".strip().split()).upper()
assert len(msg2) == 373

GRYPTO_ALPHA = "GRYPTOABCDEFHIJKLMNQSUVWXZ"
GRYPTO_TABLE = [GRYPTO_ALPHA[n:] + GRYPTO_ALPHA[:n] for n in range(len(GRYPTO_ALPHA))]


def encrypt(message, key, table):
    rows = {s[0]: s for s in table}
    encrypted = ""
    index = 0
    for ch in message:
        if ch in GRYPTO_ALPHA:
            enc = rows[key[index].upper()][table[0].index(ch.upper())]
            if ch.isupper():
                encrypted += enc.upper()
            else:
                encrypted += enc.lower()
        else:
            encrypted += ch
        index += 1
        index %= len(key)

    return encrypted


def decrypt(cipher, key, table):
    rows = {s[0]: s for s in table}
    decrypted = ""
    index = 0
    for ch in cipher:
        if ch in GRYPTO_ALPHA:
            dec = table[0][rows[key[index].upper()].index(ch.upper())]
            if ch.isupper():
                decrypted += dec.upper()
            else:
                decrypted += dec.lower()
        else:
            decrypted += ch
        index += 1
        index %= len(key)

    return decrypted

CIPHER_1 = encrypt(msg1, "PALIMPSEST", GRYPTO_TABLE)
CIPHER_2 = encrypt(msg2, "ABSCISSA", GRYPTO_TABLE)
