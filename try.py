data = "merhaba    "


def clearpref(prefcln):
    for i in range(0,10):
        space = str(i*" ") 
        prd = str(prefcln.removeprefix(space))
        if not prd.startswith(" "):
           return str(prd)
        

def clearsuff(suffcln):
    for i in range(0,10):
        space = str(i*" ") 
        prd = str(suffcln.removesuffix(space))
        if not prd.endswith(" "):
            return str(prd)

    
clearsuff(clearpref(data))