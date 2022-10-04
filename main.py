# import numpy as np

# a = np.array([1, 2, 3])
# a1 = np.array([4]) + a
# print(a1)
#
# a = np.array([1, 2, 3])
# print(a.shape)
# a1 = np.array([[[[5], [2]], [[1], [3]], [[2], [8]]],
#                [[[2], [4]], [[7], [5]], [[1], [9]]],
#                [[[3], [6]], [[8], [6]], [[2], [0]]],
#                [[[4], [2]], [[9], [7]], [[3], [8]]]])
# # (4,3,2,1)
# print(a1.shape)
#
# sum = 0
# for i in range(a1.shape[0]):
#     for j in range(a1.shape[1]):
#         for n in range(a1.shape[2]):
#             for k in range(a1.shape[3]):
#                 sum += a1[i][j][n][k]
# print(sum)

from img2cmap import ImageConverter
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

converter = ImageConverter('imgs/pron.jpg')
cmap = converter.generate_cmap(n_colors=5, palette_name="south_beach_sunset", random_state=42)

import matplotlib.pyplot as plt

colors = cmap.colors

with plt.style.context("dark_background"):
    for i, color in enumerate(colors):
        plt.plot(range(10), [_+i+1 for _ in range(10)], color=color, linewidth=4)

plt.show()