#XOR of Hex Strings

a='1c0111001f010100061a024b53535009181c'
b='686974207468652062756c6c277320657965'
a1=int(a,16)
b1=int(b,16)
print(hex(a1^b1)[2:])