import struct
from struct import unpack
import numpy as np
import urllib.request
from pathlib import Path
from itertools import chain

np.random.seed(42)


def unpack_drawing(file_handle):
    # Skip key_id: 8, countrycode: 2, recognized: 1, timestamp: 4 = 15
    file_handle.read(15)
    (n_strokes,) = unpack("H", file_handle.read(2))

    N = 0
    for i in range(n_strokes):
        (n_points,) = unpack("H", file_handle.read(2))
        N += n_points
        file_handle.read(2 * n_points)

    return N


def unpack_drawings(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield unpack_drawing(f)
            except struct.error:
                break


urllib.request.urlretrieve(
    "https://raw.githubusercontent.com/cs-deep-quickdraw/notebooks/master/100_classes.txt",
    "100_classes.txt",
)

# Create data dir
Path("./data").mkdir(exist_ok=True)

f = open("100_classes.txt", "r")
# And for reading use
classes = [cls.strip() for cls in f.readlines()][:15]
f.close()


def download(classes):
    base = "https://storage.googleapis.com/quickdraw_dataset/full/binary/"
    for i, c in enumerate(classes):
        cls_url = c.replace("_", "%20")
        path = base + cls_url + ".bin"
        print((1 + i) / len(classes), c, path)
        urllib.request.urlretrieve(path, "data/" + c + ".bin")


download(classes)


i_drawings = chain(*[unpack_drawings(f"data/{cls}.bin") for cls in classes])

sizes = [size for size in i_drawings]

print(
    np.mean(sizes),
    np.percentile(sizes, 90),
    np.percentile(sizes, 95),
    np.percentile(sizes, 99),
)
