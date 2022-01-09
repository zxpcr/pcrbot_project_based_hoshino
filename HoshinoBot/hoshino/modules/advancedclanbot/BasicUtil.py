import re


def isNullSet(list) -> bool:
    if (len(list) > 0):
        return False
    else:
        return True

def getRawDmInfo(ev) -> str:
    raw = ev['message'].extract_plain_text().split()
    if (type(raw) != str):
        raw = raw[0]
    dm = re.match("(\d+w)|\d+",raw)
    if dm is None:
        return ""
    else:
        print(dm.group())
        return str(dm.group())

def dmstr2dmint(s:str) -> int:
    s = s.replace('w', '0000')
    return int(s)

def isEmptyStr(s) -> bool:
    if (s == ""):
        return True
    else:
        return False

def getAt(ev):
    print(ev['at'])