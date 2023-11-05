"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(result):
    
    lista=[('a','@'), ('e','3'), ('i','¡'), ('o','0'),('u','v'),('V','v'),('U','v')]

    if len(result)<=2: result = result.upper()
    if len(result)>2: result = result[0].upper() + result[1:-1] + result[-1].upper()

    for caracter in result:
        for item in lista:
            if caracter in item[0]: result = result.replace(caracter,item[1])

        


    return result

print(fn_hack_3('barziman'))