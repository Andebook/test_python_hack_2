"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def response(param,flag):
        result =[]
        x=len(param)
        while x > 0:
            if flag==0:
                result.append("{}".format(x))
            else:
                result.append("{}-{}".format(param[x-1],x))
            x-=1
        return result

def fn_hack_8(param):
    
    if len(param)%2==0:

        result = response(param,0)

    else:

        result = response(param,1)
   

    return result

