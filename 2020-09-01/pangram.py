import string, sys
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
 
print ( ispangram("How vexingly quick daft zebras jump"))
print ( ispangram("abcd efgh ijk lmn opqr stuv wxyz"))
print ( ispangram("yo, pangrams fam"))
print ( ispangram("or not"))
print ( ispangram("Waxy and quivering jocks fumble the pizza"))