"""Wspólny preset kolorów dla zdjęć Tamarillo: neutralizacja balansu bieli, ciepły ton, lekkie wyciszenie, podniesione cienie."""
import numpy as np
from PIL import Image, ImageOps

def grade(im):
    a = np.asarray(ImageOps.exif_transpose(im).convert('RGB')).astype(np.float32) / 255.0
    # 1) częściowe wyrównanie balansu bieli (gray world, siła 0.65)
    m = a.reshape(-1, 3).mean(0); g = m.mean()
    a = a * (1 + 0.65 * (g / m - 1))
    # 2) wspólny ciepły ton
    a = a * np.array([1.035, 1.0, 0.95])
    # 3) lekkie wyciszenie nasycenia
    l = (a * [0.299, 0.587, 0.114]).sum(2, keepdims=True)
    a = l + (a - l) * 0.9
    # 4) podniesione cienie, miękkie światła (krzywa)
    a = np.clip(a, 0, 1)
    a = a + 0.07 * (1 - a) ** 3 - 0.03 * a ** 4
    # 5) delikatny kontrast w średnich tonach
    a = 0.5 + (a - 0.5) * 1.04
    return Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))
