import argparse

from PIL import Image



def main():
    im1 = Image.open("C:\\Users\\Steven\\Documents\\PI\\vision\\PI-vision\\Images\\dataset2\\23.jpg")
    im1.save("C:\\Users\\Steven\\Documents\\PI\\vision\\PI-vision\\Images\\dataset2\\23.png")

if __name__ == '__main__':
    main()
