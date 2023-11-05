"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(param):
    cont=0
    num=1
    result = []
    while cont < len(param):
        
        if cont%2==0:
            a,b=num, num+1
            result.append({f"{a}":f"{b}"})
        else:
            a,b=num, num+1
            result.append({f"{a}",f"{b}"})
        num+=2
        cont+=1
    return result