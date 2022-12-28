import os
from random import choice

kamus = ['indonesia', 'australia', 'china', 'singapura', 'malaysia', 'vietnam', 'portugal', 'belanda', 'jepang', 'korea',
         'india', 'maroko', 'nigeria', 'nepal', 'palestina', 'prancis', 'qatar', 'laos', 'denmark', 'jerman']

kata = choice(kamus)

nyawa = 5
GameOver = False
tebakan = []
hasil = [' ~ '] * len(kata)

os.system('clear')

print('''
    ******************************
    |   AYO BERMAIN TEBAK KATA   |  
    |      <<NAMA NEGARA>>       |
    ******************************
''')

while not GameOver:
  print("Kesempatan : {}".format(u'\u2665' * nyawa))
  print("Huruf tertebak : {}".format(tebakan))

  hidden_word = ''.join(hasil)
  print("Tebak kata berikut : {}".format(hidden_word))
  print("Ketik 'exit' untuk berhenti bermain")
  huruf = input("Tebak 1 huruf : ").lower()
  print("....................................")


  if huruf == 'exit':
    print("Thanks for playing")
    break
  elif huruf in kata and huruf not in tebakan:
    print("Tebakan anda benar!")
    for i in range(len(kata)):
      if kata[i] == huruf:
        hasil[i] = huruf
  elif huruf in tebakan:
    print("Huruf sudah ditebak sebelumnya, coba lagi..")
  else:
    nyawa -= 1
    print("Tebakan anda salah..")

  if huruf not in tebakan:
    tebakan.append(huruf)

  if nyawa == 1:
    print("Ini kesempatan terakhir anda, ...")
  elif nyawa == 0:
    print("Kesempatan anda telah habis, anda KALAH")
    print("HA"*20+"!!")
    GameOver = True
  elif kata == ''.join(hasil):
    print("Anda berhasil menebak kata tersembunyi : {}".format(''.join(hasil)))
    GameOver = True
