"""Problem of the week: Picking Boxes"""

__author__ = "Ayaan Adrito"

def main():

    ORIG_LENGTH = 4
    ORIG_WIDTH = 3
    ORIG_HEIGHT = 5
    MAX_VOLUME = 4000000

    length = ORIG_LENGTH
    width = ORIG_WIDTH
    height = ORIG_HEIGHT

    first_box = False
    stefan_dimensions = []
    lali_dimensions = []

    # Calculate Stefan's box dimensions
    while first_box == False:

        if 1000 > length + width + height > 100:
            stefan_dimensions = [length, width, height, length * width * height]
            first_box = True
        
        length += ORIG_LENGTH
        width += ORIG_WIDTH
        height += ORIG_HEIGHT

    length = ORIG_LENGTH
    width = ORIG_WIDTH
    height = ORIG_HEIGHT
    first_box = False

    # Calculate Lalis's dimensions
    while first_box == False:

        if length * width * height < MAX_VOLUME:
            lali_dimensions = [length, width, height, length * width * height]
        else:
            first_box = True
        
        length += ORIG_LENGTH
        width += ORIG_WIDTH
        height += ORIG_HEIGHT

    print(stefan_dimensions)
    print(lali_dimensions)

if __name__ == "__main__":
    main()