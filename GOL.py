import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Ukuran grid
N = 100

# Inisialisasi grid dengan nilai random
grid = np.random.randint(0, 2, (N, N))

# Fungsi untuk menghitung jumlah tetangga yang hidup
def count_neighbours(grid, i, j):
    count = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            if i+x >= 0 and i+x < N and j+y >= 0 and j+y < N:
                count += grid[i+x][j+y]
    return count

# Fungsi untuk melakukan update grid
def update(frame_number, img, grid):
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            count = count_neighbours(grid, i, j)
            if grid[i][j] == 1:
                if count < 2 or count > 3:
                    new_grid[i][j] = 0
            else:
                if count == 3:
                    new_grid[i][j] = 1
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img

# Konfigurasi plot
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')

# Animasi
ani = animation.FuncAnimation(fig, update, fargs=(img, grid), frames=100, interval=50)
plt.show()
