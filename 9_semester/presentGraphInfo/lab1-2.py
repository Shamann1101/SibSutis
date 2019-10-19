from struct import pack, unpack
from sys import argv


class BmpFile:
    def __init__(self, f_path):
        self.f_path = f_path
        self.f_ref = open(f_path, "rb")

        # Parsing BMP Header
        self.type = self.f_ref.read(2).decode()
        self.file_size = unpack("I", self.f_ref.read(4))[0]
        self.reserved1 = unpack("H", self.f_ref.read(2))[0]
        self.reserved2 = unpack("H", self.f_ref.read(2))[0]
        self.offset = unpack("I", self.f_ref.read(4))[0]

        # Parsing DIB Header
        self.dib_size = unpack("I", self.f_ref.read(4))[0]
        self.width = unpack("I", self.f_ref.read(4))[0]
        self.height = unpack("I", self.f_ref.read(4))[0]
        self.color_planes = unpack("H", self.f_ref.read(2))[0]
        self.bits_per_pixel = unpack("H", self.f_ref.read(2))[0]
        self.compression_type = unpack("I", self.f_ref.read(4))[0]
        self.raw_image_size = unpack("I", self.f_ref.read(4))[0]
        self.horizontal_resolution = unpack("I", self.f_ref.read(4))[0]
        self.vertical_resolution = unpack("I", self.f_ref.read(4))[0]
        self.n_of_colors = unpack("I", self.f_ref.read(4))[0]
        self.important_colors = unpack("I", self.f_ref.read(4))[0]

        # Reading color table
        self.f_ref.seek(self.dib_size + 14)
        self.palette = self.f_ref.read(self.bits_per_pixel * self.n_of_colors)
        # print("Current position = {}".format(self.f_ref.tell()))
        # Reading raw image data
        self.f_ref.seek(self.offset)
        self.raw_image_data = self.f_ref.read(self.raw_image_size)

    def save_to_file(self, f_path):
        with open(f_path, "wb") as f:
            # Writing BMP Header
            f.write(self.type.encode())
            f.write(pack("I", self.file_size))
            f.write(pack("H", self.reserved1))
            f.write(pack("H", self.reserved2))
            f.write(pack("I", self.offset))

            # Writing DIB Header
            f.write(pack("I", self.dib_size))
            f.write(pack("I", self.width))
            f.write(pack("I", self.height))
            f.write(pack("H", self.color_planes))
            f.write(pack("H", self.bits_per_pixel))
            f.write(pack("I", self.compression_type))
            f.write(pack("I", self.raw_image_size))
            f.write(pack("I", self.horizontal_resolution))
            f.write(pack("I", self.vertical_resolution))
            f.write(pack("I", self.n_of_colors))
            f.write(pack("I", self.important_colors))

            # Writing palette
            f.write(self.palette)

            # Writing raw image data
            f.write(self.raw_image_data)

    def transform_to_grey(self):
        mutable_table = bytearray(self.palette)
        new_palette = []

        palette = list(_divide_chunks(mutable_table, 4))

        for color in palette:
            avg = int((color[0] + color[1] + color[2]) / 3)
            rgb = [avg] * 3 + [0]
            new_palette += rgb

        self.palette = bytes(new_palette)

    def draw_border_around(self, border_width):
        offset = _get_pixel_row_offset(self.width)
        mutable_table = bytearray(self.raw_image_data)
        bitmap_counter = 0

        # print("[DEBUG] Calculated row fffset = {}".format(offset))
        # print("[DEBUG] Len of width * height = {}".format(self.height*self.width))
        # print("[DEBUG] Len of actual pixmap = {}".format(len(mutable_table)))
        for y in range(0, self.height):
            for x in range(0, self.width):
                if y < border_width \
                        or y >= self.height - border_width \
                        or x < border_width \
                        or x >= self.width - border_width:
                    mutable_table[bitmap_counter] = 0
                    bitmap_counter += 1
                else:
                    bitmap_counter += 1
            if offset > 0:
                bitmap_counter += offset
        self.raw_image_data = bytes(mutable_table)

    def print_bmp_header_info(self):
        print("<BMP Header info>")
        print(("Type: {}\n" +
               "File size: {}\n" +
               "Res1: {}\n" +
               "Res2: {}\n" +
               "Offset: {}"
               ).format(self.type, self.file_size, self.reserved1, self.reserved2, self.offset))
        print("</BMP Header info>\n")
        print("<DIB Header info>")
        print(("DIB size: {}\n" +
               "Width: {}\n" +
               "Height: {}\n" +
               "Color Planes: {}\n" +
               "Bits per pixel: {}\n" +
               "Compression Method: {}\n" +
               "Raw image size: {}\n" +
               "Horizontal resolution: {}\n" +
               "Vertical resolution: {}\n" +
               "# of Colors: {}\n" +
               "Important Colors:"
               ).format(self.dib_size, self.width, self.height, self.color_planes, self.bits_per_pixel,
                        self.compression_type, self.raw_image_size, self.horizontal_resolution,
                        self.vertical_resolution, self.n_of_colors, self.important_colors))
        print("</DIB Header info>")


def _get_pixel_row_offset(width):
    offset = 0
    while width % 4 != 0:
        width += 1
        offset += 1

    return offset


def _divide_chunks(l, n):
    # looping till length l 
    for i in range(0, len(l), n):
        yield l[i:i + n]


def _main():
    file_name = "Carib256.bmp"
    if len(argv) > 1:
        file_name = argv[1]
    f = BmpFile(file_name)
    f.print_bmp_header_info()
    f.transform_to_grey()
    f.save_to_file('grey_' + file_name)

    f = BmpFile(file_name)
    f.draw_border_around(15)
    f.save_to_file('border_' + file_name)


if __name__ == "__main__":
    _main()
