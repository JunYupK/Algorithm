def Binary(num):
    result = []
    while num != 0:
        result.insert(0, str(num % 2))
        num = num // 2
    return "".join(result)
def BinaryToInt(num):
    s = 1
    result = 0
    while len(num) != 0:
        result += int(num[-1]) * s
        num = num[0:len(num)-1]
        s *= 2
    return result
def B트inaryToHex(num):
    result = []
    Hex_dic = {0:'0', 1:'1', 2:'2' ,3:'3', 4:'4',5:'5',6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    while len(num) != 0:
        result.insert(0, Hex_dic[BinaryToInt(num[-4:])])
        num = num[0:-4]
    return "".join(result)
data = 15860
data = Binary(data)
print(data)
print(BinaryToHex(data))