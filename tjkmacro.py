import win32clipboard , keyboard , time , win32con

print("space cleaner baslatildi...")

def clearpref(prefcln):
    for i in range(0,10):
        space = str(i*" ") 
        prd = str(prefcln.removeprefix(space))
        if not prd.startswith(" "):
           return str(prd)

def clearsuff(suffcln:str):
    for i in range(0,10):
        space = str(i*" ") 
        prd = str(suffcln.removesuffix(space))
        if not prd.endswith(" "):
            return str(prd)

while True:
    time.sleep(0.001)
    try:
        if keyboard.is_pressed("ctrl+c"):
            win32clipboard.OpenClipboard()
            data = str(win32clipboard.GetClipboardData())
            new = clearsuff(clearpref(data))
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT,new)
            win32clipboard.CloseClipboard()
    except:pass