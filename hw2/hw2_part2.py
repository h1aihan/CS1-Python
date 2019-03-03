import math
cipher=raw_input("Enter cipher text ==> ")
print cipher
def decrypt(word):
    word=word.replace("rxr", " a")
    word=word.replace("vw", "he")
    word=word.replace("az az", "e")
    word=word.replace("eie", "y")
    word=word.replace('yyy','u')
    word=word.replace("uq","an")
    word=word.replace("aige","th")
    word=word.replace("tzzt", "o")
    return word
print "\nDeciphered as ==>", decrypt(cipher)
print "Difference in length ==>", str(abs(len(cipher)-len(decrypt(cipher))))
regular= raw_input("\nEnter regular text ==> ")
print regular
def encrypt(word):
    word=word.replace(" a","rxr")
    word=word.replace("he","vw")
    word=word.replace("e","az az")
    word=word.replace("y","eie")
    word=word.replace("u","yyy")
    word=word.replace("an","uq")
    word=word.replace("th","aige")
    word=word.replace("o","tzzt")
    return word
print "\nEncrypted as ==>", encrypt(regular)
print "Difference in length ==>", str(abs(len(regular)-len(encrypt(regular))))