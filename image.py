from PIL import Image
import os

def image_effect(image_path, output_path, effect):
    src_image = Image.open(image_path)

    # jezeli obrazek nie jest w przestrzeni barw rgb konwertujemy do rgb zeby dzialalo
    if src_image.mode != 'RGB':
        src_image = src_image.convert('RGB')

    r, g, b = src_image.split()

    if effect == 'red':
        new_image = Image.merge("RGB", (r, Image.new('L', r.size), Image.new('L', r.size)))
    elif effect == 'green':
        new_image = Image.merge("RGB", (Image.new('L', g.size), g, Image.new('L', g.size)))
    elif effect == 'blue':
        new_image = Image.merge("RGB", (Image.new('L', b.size), Image.new('L', b.size), b))
    elif effect == 'cyan':
        new_image = Image.merge("RGB", (Image.new('L', r.size), g, b))
    elif effect == 'magenta':
        new_image = Image.merge("RGB", (r, Image.new('L', g.size), b))
    elif effect == 'yellow':
        new_image = Image.merge("RGB", (r, g, Image.new('L', b.size)))
    else:
        new_image = Image.merge("RGB", (r, g, b))
        

    new_image.save(output_path)

input_path = os.path.join('media', 'image.png')
output_path = os.path.join('media', 'image_effect.png')

effect = 'original'  # możliwe wartości: red, green, blue, cyan, magenta, yellow

image_effect(input_path, output_path, effect)
