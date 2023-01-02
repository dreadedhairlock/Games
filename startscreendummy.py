import tkinter as tk
from PIL import Image, ImageDraw, ImageEnhance, ImageTk
import random

# membuat gambar acak
image_size = (200, 200)
image = Image.new('L', image_size, color=255)
draw = ImageDraw.Draw(image)

for x in range(image_size[0]):
  for y in range(image_size[1]):
    draw.point((x, y), fill=random.randint(0, 255))

# meningkatkan kontras gambar
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(2)
image = ImageTk.PhotoImage(image)

# membuat window
window = tk.Tk()
window.title('Misteri Pembunuhan')

# membuat label untuk gambar
image_label = tk.Label(image=image)
image_label.pack()

# membuat tombol mulai
start_button = tk.Button(text='Mulai', command=lambda: print('Mulai game baru'))
start_button.pack()

# membuat tombol lanjutkan
continue_button = tk.Button(text='Lanjutkan', command=lambda: print('Lanjutkan game yang tersimpan'))
continue_button.pack()

# membuat tombol simpan
save_button = tk.Button(text='Simpan', command=lambda: print('Simpan game saat ini'))
save_button.pack()

# menjalankan window
window.mainloop()