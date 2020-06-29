# string = "\n\r\n                                        Hệ thống Gogi House - Quán Nướng Hàn Quốc - ĐN\r\n                                    \n"
# s2 = "\n\r\n                                        Hệ thống Pizza Hut - Đà Nẵng\r\n                                    \n"
# s3 = "\r\n                                    7.6\r\n                                "
# print(len(s3))
# s3.strip("\n\r\n")
# print(s3)
# print(s3[38:len(s3) - 32])
# string.strip(" ")
# print(len(string[43:89]))
# print(string[43:len(string) - 39])
# print(s2[43:len(s2) - 39])
# print(string.find("ĐN"))
# 43:87
from underthesea import ner, chunk, word_tokenize
text = "176 Nguyễn Chí Thanh"
# print(ner(text))
# print(word_tokenize(text))
rs = chunk(text)
print(rs)
mon = []
duong = []
checkduong = ['Đường', 'đường']
# print(type(rs))
for i in range(len(rs)):
    if rs[i][1] == 'Np' and rs[i-1][0] in checkduong:
        duong.append(rs[i][0])
    if rs[i][1] == 'Np' and str(rs[i-1][0]).isnumeric():
        soduong = rs[i-1][0] + " " + rs[i][0]
        duong.append(soduong)
    elif rs[i][1] == 'Np':
        mon.append(rs[i][0])   
print(mon)
print(duong)
# print(rs[len(rs)-1][1])
# print(rs)