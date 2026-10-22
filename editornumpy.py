import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
img = Image.open("imagem_numpy.jpg")
imagem = np.array(img)
plt.imshow(imagem)
plt.axis("off")
plt.grid()
h, w, _ = imagem.shape
recorte = imagem[int(h * 0.1) : int(h * 0.6), int(w * 0.2) : int(w * 0.8)]
espelhada = imagem[:, ::-1]
canais_alterados = imagem.copy()
canais_alterados[:, :, 2] = 0  
escura = np.clip(imagem * 0.5, 0, 255).astype(np.uint8)
mascara = (imagem[:, :, 0] > 180).astype(np.uint8) * 255
fig, axes = plt.subplots(1, 5, figsize=(20, 4))
# Original
axes[0].imshow(imagem)
axes[0].set_title("Original")
axes[0].axis("off")
# 1. Recorte
axes[1].imshow(recorte)
axes[1].set_title("1. Recorte")
axes[1].axis("off")
# 2. Espelhada
axes[2].imshow(espelhada)
axes[2].set_title("2. Espelhada")
axes[2].axis("off")
# 3. Canais Alterados
axes[3].imshow(canais_alterados)
axes[3].set_title("3. Sem Canal Azul")
axes[3].axis("off")
# 4. Operação Vetorizada (Escura)
axes[4].imshow(escura)
axes[4].set_title("4. Escura (50%)")
axes[4].axis("off")
plt.tight_layout()
plt.savefig("mini_editor_numpy.png", bbox_inches="tight")
plt.close()