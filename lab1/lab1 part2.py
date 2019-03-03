base10= 128
base2= base10*10**3*10**3*10**3/(2**10*2**10*2**10)
difference= base10-base2
print base10, "GB in base 10 is actually", base2,"GB in base 2,", difference, "GB less than advertised"