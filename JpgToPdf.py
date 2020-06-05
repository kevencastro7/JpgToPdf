import img2pdf
import os


if __name__ == "__main__":
    for i in range(41, 51):
        dir = "C:/Users/Keven/Documents/kaguya_sama/Volume 06/"
        fn = "[NKMA] Kaguya-sama wa Kokurasetai {}".format(i)
        dirname = dir + fn
        imgs = []
        with open("{}.pdf".format(dirname), "wb") as f:
            for fname in os.listdir(dirname):
                if not fname.endswith(".jpg"):
                    continue
                path = os.path.join(dirname, fname)
                print(fname)
                if os.path.isdir(path):
                    continue
                imgs.append(path)
            f.write(img2pdf.convert(imgs))
