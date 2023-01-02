import cmd
import random

class Game(cmd.Cmd):
  # constructor
  def __init__(self):
    super().__init__()
    self.intro = 'Selamat datang di game misteri pembunuhan! Ketik "bantuan" untuk memulai.'
    self.prompt = 'Apakah yang akan kamu lakukan? > '
    self.kemungkinan_pembunuh = ['Tuan X', 'Tuan Y', 'Tuan Z']
    self.pembunuh = random.choice(self.kemungkinan_pembunuh)
    self.location = 'rumah'
  
  # memulai game baru
  def do_mulai(self, args):
    print('Kamu telah memulai game baru.')
    self.pembunuh = random.choice(self.kemungkinan_pembunuh)
    self.location = 'rumah'
  
  # menampilkan bantuan
  def do_bantuan(self, args):
    print('''
      Perintah yang tersedia:
      mulai - Mulai game baru
      lanjutkan - Lanjutkan game yang tersimpan
      simpan - Simpan game saat ini
      keluar - Keluar dari game
      bantuan - Menampilkan bantuan ini
      
      Perintah untuk berinteraksi dengan game:
      pergi [lokasi] - Pergi ke lokasi yang ditentukan
      lihat - Lihat sekelilingmu
      interogasi [tuan] - Interogasi tuan yang ditentukan
    ''')
  
  # menyimpan game
  def do_simpan(self, args):
    print('Game telah disimpan.')
  
  # melanjutkan game yang telah disimpan
  def do_lanjutkan(self, args):
    print('Game telah dilanjutkan.')
  
  # mengakhiri game
  def do_keluar(self, args):
    print('Terima kasih telah bermain!')
    return True
  
  # pergi ke lokasi yang ditentukan
  def do_pergi(self, args):
    if args in ['rumah', 'kantor polisi', 'taman']:
      self.location = args
      print(f'Kamu telah pergi ke {args}.')
    else:
      print('Lokasi tersebut tidak ditemukan.')
  
  # melihat sekeliling
  def do_lihat(self, args):
    if self.location == 'rumah':
      print('''
        Kamu berada di rumah yang sepi. Ada beberapa barang yang tergeletak di atas meja:
        - sebuah surat
        - sebuah pisau dapur
        - sebuah handphone
      ''')
    elif self.location == 'kantor polisi':
      print('''
        Kamu berada di kantor polisi yang ramai. Beberapa petugas sedang sibuk dengan pekerjaan mereka.
        Di sudut ruangan, terlihat seorang tersangka duduk di sebuah kursi dengan wajah datar.
      ''')
    elif self.location == 'taman':
      print('''
        Kamu berada di taman kota yang indah. Ada beberapa orang yang sedang berjalan-jalan atau
        duduk di bangku. Sebuah karung sampah tergeletak di sudut taman.
      ''')
  
  # menginterogasi tuan yang ditentukan
  def do_interogasi(self, args):
    if args == self.pembunuh:
      print(f'Kamu berhasil mengungkap kebenaran! {args} adalah pembunuh yang sebenarnya.')
      print('Selamat, kamu telah menyelesaikan game ini!')
      return True
    else:
      print(f'{args} tidak terlibat dalam kasus ini.')

if __name__ == '__main__':
  game = Game()
  game.cmdloop()
