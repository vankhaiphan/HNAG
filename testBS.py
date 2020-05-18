# from bs4 import BeautifulSoup
# import requests
# url = 'http://www.prnewswire.com/news-releases/dutch-philosopher-koert-van-mensvoort-founder-of-the-next-nature-network-writes-a-letter-to-humanity-619925063.html'
# r = requests.get(url)
# html = r.text
# soup = BeautifulSoup(html, 'html.parser')
# # print(soup)
# links = soup.find_all('div', {'class': 'image'})
# print ([i.find('img')['src'] for i in links])
# print ([i.find('img')['title'] for i in links])

# html = """\\u003Cdiv id=\\u0022contenedor\\u0022\\u003E \\u003Ch2 class=\\u0022text-left m-b-2\\u0022\\u003EInformaci\\u00f3n del veh\\u00edculo de patente AA345AA\\u003C\\/h2\\u003E\\n\\n\\n\\n \\u003Cdiv class=\\u0022panel panel-default panel-disabled m-b-2\\u0022\\u003E\\n \\u003Cdiv class=\\u0022panel-body\\u0022\\u003E\\n \\u003Ch2 class=\\u0022table_title m-b-2\\u0022\\u003EInformaci\\u00f3n del Registro Automotor\\u003C\\/h2\\u003E\\n \\u003Cdiv class=\\u0022col-md-6\\u0022\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003ERegistro Seccional\\u003C\\/label\\u003E\\n \\u003Cp\\u003ESAN MIGUEL N\\u00b0 1\\u003C\\/p\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003EDirecci\\u00f3n\\u003C\\/label\\u003E\\n \\u003Cp\\u003EMAESTRO ANGEL D\\u0027ELIA 766\\u003C\\/p\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003EPiso\\u003C\\/label\\u003E\\n \\u003Cp\\u003EPB\\u003C\\/p\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003EDepartamento\\u003C\\/label\\u003E\\n \\u003Cp\\u003E-\\u003C\\/p\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003EC\\u00f3digo postal\\u003C\\/label\\u003E\\n \\u003Cp\\u003E1663\\u003C\\/p\\u003E\\n \\u003C\\/div\\u003E\\n \\u003Cdiv class=\\u0022col-md-6\\u0022\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003ELocalidad\\u003C\\/label\\u003E\\n \\u003Cp\\u003ESAN MIGUEL\\u003C\\/p\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003EProvincia\\u003C\\/label\\u003E\\n \\u003Cp\\u003EBUENOS AIRES\\u003C\\/p\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003ETel\\u00e9fono\\u003C\\/label\\u003E\\n \\u003Cp\\u003E(11)46646647\\u003C\\/p\\u003E\\n \\u003Clabel class=\\u0022control-label\\u0022\\u003EHorario\\u003C\\/label\\u003E\\n \\u003Cp\\u003E08:30 a 12:30\\u003C\\/p\\u003E\\n \\u003C\\/div\\u003E\\n \\u003C\\/div\\u003E\\n\\u003C\\/div\\u003E \\n\\n\\u003Cp class=\\u0022text-center m-t-3 m-b-1 hidden-print\\u0022\\u003E\\n \\u003Ca href=\\u0022javascript:window.print();\\u0022 class=\\u0022btn btn-default\\u0022\\u003EImprim\\u00ed la consulta\\u003C\\/a\\u003E \\u0026nbsp; \\u0026nbsp;\\n \\u003Ca href=\\u0022\\u0022 class=\\u0022btn use-ajax btn-primary\\u0022\\u003EHacer otra consulta\\u003C\\/a\\u003E\\n\\u003C\\/p\\u003E\\n\\u003C\\/div\\u003E"""
# html = "H\u1ec7 th\u1ed1ng Gogi House - Qu\u00e1n N\u01b0\u1edbng H\u00e0n Qu\u1ed1c - \u0110N"
# print(html)
# s = ""
# s = str(html)
# print(s)
# print

# print(type(str("H\u1ec7")))
# city = 'Ribeir\xc3\xa3o Preto'
# print (city.decode('cp1252').encode('utf-8'))
sName = "H\u1ec7 th\u1ed1ng Gogi House - Qu\u00e1n N\u01b0\u1edbng H\u00e0n Qu\u1ed1c - \u0110N"
repl_wrd = "e"
word_list = ["\u1ec7"]
name = ' '.join([repl_wrd if idx in word_list else idx for idx in sName.split()])   
print(name)