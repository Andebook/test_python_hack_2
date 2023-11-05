"""
generic script

text: "fooziman" output => "fzmn" 
text: "c" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(result):
    vocales = ('a','e','i','o','u')
    
    for caracter in result:
        if caracter in vocales: result = result.replace(caracter,'')
   
    return result



print(fn_hack_2("fooziman"))