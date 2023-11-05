"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(param):
    cad = "abcde"
    result=[]
    cont = 0
    if param==[] or param==[0]  :
        result = [0]
    else:
        while cont < len(param):
            if param[cont] in cad:
                if cont %2==0:
                    result.append(f"{cont + 1}")
                else:
                    result.append(cont + 1)   
                cont+=1


    return result

print(fn_hack_7([]))
