from os import mkdir
from time import time
from PIL import Image
from math import sqrt
from statistics import mean
from pathlib import Path


def calculate_distance(start, target):
    x = abs(target[0] - start[0])
    y = abs(target[1] - start[1])
    z = abs(target[2] - start[2])

    return sqrt(x ** 2 + y ** 2 + z ** 2)

def calculate_taxicab_distance(start, target):
    x = abs(target[0] - start[0])
    y = abs(target[1] - start[1])
    z = abs(target[2] - start[2])

    return x + y + z


def get_pixels(img_path):
    img = Image.open(img_path)

    pixels = img.getdata()
    return img, set(pixels)

def reduce(pixels, colors, taxicab=False):
    centroids = {i:i for i in colors} # color: position
    old_centroids = {i:None for i in colors} # color: position
    iters = 0

    while old_centroids != centroids:
        old_centroids = centroids.copy() # color: position
        centroid_points = {i:[] for i in colors} # color: points

        for i in pixels:
            if taxicab:
                belonging_centroid = min(centroids, key=lambda x: calculate_distance(centroids[x], i))
            else:
                belonging_centroid = min(centroids, key=lambda x: calculate_taxicab_distance(centroids[x], i))
            centroid_points[belonging_centroid].append(i)
        
        for i in centroid_points:
            if not centroid_points[i]:
                centroids[i] = i
                continue

            mean_x = int(mean([j[0] for j in centroid_points[i]]))
            mean_y = int(mean([j[1] for j in centroid_points[i]]))
            mean_z = int(mean([j[2] for j in centroid_points[i]]))
            
            centroids[i] = (mean_x, mean_y, mean_z)
        
        iters += 1

    replace_dict = {i:i for i in colors} # dictionary specifying what color to replace with
    for i in centroid_points:
        for j in centroid_points[i]:
            replace_dict[j] = i
    return replace_dict, iters

def create_img(img, centroids):
    size = img.size
    pixs = img.load()
    for i in range(size[0]):
        for j in range(size[1]):
            pixs[i, j] = centroids[pixs[i, j]]
    
    return img

def convert(path, colors, type): # type - 1 = euclidean, 2 = taxicab
    start_time = time()
    path = Path(path)
    base_path = str(path.parent.absolute()) + "\\"
    img_name = path.name
    name = path.stem # without extension
    
    img, pixels_set = get_pixels(base_path + img_name)

    if type == 1:
        save_path = f"converted_images/{name}/converted_euc_{img_name}"
        centroid_data, iters = reduce(pixels_set, colors)
    elif type == 2:
        save_path = f"converted_images/{name}/converted_tax_{img_name}"
        centroid_data, iters = reduce(pixels_set, colors, True)
    else:
        print("Wrong type")
        return

    new_img = create_img(img, centroid_data)

    new_img.save(save_path)

    return {"iter_cnt": iters, "time_elapsed": int(time() - start_time)}

def convert_to_rgbs(hexs):
    rgbs = []
    for i in hexs:
        hex = i.lstrip("#")

        r = int(hex[0:2], 16)
        g = int(hex[2:4], 16)
        b = int(hex[4:6], 16)

        rgbs.append((r, g, b))

    return rgbs

def main():
    img_name = input("Enter image name: ")
    colors = input("Enter hex colors separated by commas: ").replace(" ", "").split(",")

    colors_rgb = convert_to_rgbs(colors)

    name = Path(f"source_images/{img_name}").stem
    
    mkdir(f"converted_images/{name}")

    euc_det = convert(f"source_images/{img_name}", colors_rgb, 1)
    tax_det = convert(f"source_images/{img_name}", colors_rgb, 2)

    text_colors_hex = ""
    for i in colors:
        if i[0] != "#":
            i = "#" + i
        
        text_colors_hex += f" - {i}\n"

    text_colors_rgb = ""
    for i in colors_rgb:      
        i = ", ".join(str(j) for j in i)  
        text_colors_rgb += f" - {i}\n"

    text = f"Name: {img_name}\n\n"
    text += f"Colors used (RGB):\n{text_colors_rgb}\n"
    text += f"Colors used (Hex):\n{text_colors_hex}\n"
    text += f"Euclidean:\n - number of iterations: {euc_det['iter_cnt']}\n - time elapsed: {euc_det['time_elapsed']} seconds\n\n"
    text += f"Taxicab:\n - number of iterations: {tax_det['iter_cnt']}\n - time elapsed: {tax_det['time_elapsed']} seconds"

    with open(f"converted_images/{name}/details.txt", "w+") as f:
        f.write(text)

if __name__ == "__main__":
    main()