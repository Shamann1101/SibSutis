from struct import unpack
# import hachoir_parser
from PIL import Image


class PcxFile:
    """
    typedef struct TPaletteStruct
     {
      unsigned char Red
      unsigned char Green
      unsigned char Blue
    """
    def __init__(self, f_path):
        self.f_path = f_path
        self.f_ref = open(f_path, "rb")

        self.id = unpack("B", self.f_ref.read(1))[0]
        self.Version = unpack("B", self.f_ref.read(1))[0]
        self.Coding = unpack("B", self.f_ref.read(1))[0]
        self.BitPerPixel = unpack("B", self.f_ref.read(1))[0]
        self.XMin = unpack("H", self.f_ref.read(2))[0]
        self.YMin = unpack("H", self.f_ref.read(2))[0]
        self.XMax = unpack("H", self.f_ref.read(2))[0]
        self.YMax = unpack("H", self.f_ref.read(2))[0]
        self.HRes = unpack("H", self.f_ref.read(2))[0]
        self.VRes = unpack("H", self.f_ref.read(2))[0]
        self.Palette = unpack("48c", self.f_ref.read(48))[0]
        self.Reserved = unpack("B", self.f_ref.read(1))[0]
        self.Planes = unpack("B", self.f_ref.read(1))[0]
        self.BytePerLine = unpack("H", self.f_ref.read(2))[0]
        self.PaletteInfo = unpack("H", self.f_ref.read(2))[0]
        self.HScreenSize = unpack("H", self.f_ref.read(2))[0]
        self.VScreenSize = unpack("H", self.f_ref.read(2))[0]
        self.Filler = unpack("54c", self.f_ref.read(54))[0]

        # Reading color table
        # self.f_ref.seek(self.dib_size + 14)

    def print_all(self):
        print("id: {}".format(self.id))
        print("Version: {}".format(self.Version))
        print("Coding: {}".format(self.Coding))
        print("BitPerPixel: {}".format(self.BitPerPixel))
        print("XMin: {}".format(self.XMin))
        print("YMin: {}".format(self.YMin))
        print("XMax: {}".format(self.XMax))
        print("YMax: {}".format(self.YMax))
        print("HRes: {}".format(self.HRes))
        print("VRes: {}".format(self.VRes))
        print("Palette: {}".format(self.Palette))
        print("Reserved: {}".format(self.Reserved))
        print("Planes: {}".format(self.Planes))
        print("BytePerLine: {}".format(self.BytePerLine))
        print("PaletteInfo: {}".format(self.PaletteInfo))
        print("HScreenSize: {}".format(self.HScreenSize))
        print("VScreenSize: {}".format(self.VScreenSize))
        print("Filler: {}".format(self.Filler))


def _main():
    file_name = "Carib256.pcx"
    f = PcxFile(file_name)
    f.print_all()

    im = Image.open(file_name)
    print(im.format, im.size, im.mode)


if __name__ == "__main__":
    _main()
