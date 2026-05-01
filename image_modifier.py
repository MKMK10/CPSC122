##############################################
# Programmer: Maria Kravtsova
# Class: CPSC 122-01, Spring 2026
# Programming Assignment #1
# Submitted: 4/30/2026
#
# I attempted the bonus.
# 
# Description: This program takes a ppm image and applies various modifications to it.
# Then it prints said modified images into new ppm image files.
##############################################
import random



def load_image_data(filename: str) -> list[list[list[int]]]:
    """
    Takes the ppm image and turns it into a 3D list.
    Returns the data taken from the ppm image.
    """
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    clean_lines = []
    for line in lines:
        line = line.strip()
        if line != "" and not line.startswith("#"):
            clean_lines.append(line)
    assert clean_lines[0] == "P3"
    parts = clean_lines[1].split()
    width = int(parts[0])
    height = int(parts[1])
    max_val = int(clean_lines[2])

    pixel_values = []
    for line in clean_lines[3:]:
        nums = line.split()
        for n in nums:
            pixel_values.append(int(n))

    data = []
    index = 0
    for r in range(height):
        row = []
        for c in range(width):
            red = pixel_values[index]
            green = pixel_values[index + 1]
            blue = pixel_values[index + 2]
            row.append([red, green, blue])
            index += 3
        data.append(row)
    return data

def write_image_data(data: list[list[list[int]]], filename: str) -> None:
    """
    Turns the data from the 3D list image into a ppm file.
    """
    height = len(data)
    width = len(data[0])

    file = open(filename, "w")
    file.write("P3\n")
    file.write(str(width) + " " + str(height) + "\n")
    file.write("255\n")
    for row in data:
        for pixel in row:
            file.write(str(pixel[0]) + " " +
                       str(pixel[1]) + " " +
                       str(pixel[2]) + " ")
        file.write("\n")
    file.close()

def apply_modification(data: list[list[list[int]]], mod: str) -> list[list[list[int]]] | None:
    """
    Applies all the modifications required from the assignment, including the bonus.
    Returns the data from each modifier.
    """
    if mod == "vertical_flip":
        return apply_vertical_flip(data)
    elif mod == "horizontal_flip":
        return apply_horizontal_flip(data)
    elif mod == "horizontal_blur":
        return apply_horizontal_blur(data)
    elif mod == "remove_red":
        new_data = []
        for row in data:
            new_row = []
            for pixel in row:
                new_row.append([0, pixel[1], pixel[2]])
            new_data.append(new_row)
        return new_data
    elif mod == "remove_green":
        new_data = []
        for row in data:
            new_row = []
            for pixel in row:
                new_row.append([pixel[0], 0, pixel[2]])
            new_data.append(new_row)
        return new_data
    elif mod == "remove_blue":
        new_data = []
        for row in data:
            new_row = []
            for pixel in row:
                new_row.append([pixel[0], pixel[1], 0])
            new_data.append(new_row)
        return new_data
    elif mod == "negative":
        new_data = []
        for row in data:
            new_row = []
            for pixel in row:
                new_pixel = []
                for val in pixel:
                    new_pixel.append(compute_negative(val))
                new_row.append(new_pixel)
            new_data.append(new_row)
        return new_data
    elif mod == "high_contrast":
        new_data = []
        for row in data:
            new_row = []
            for pixel in row:
                new_pixel = []
                for val in pixel:
                    new_pixel.append(compute_high_contrast(val))
                new_row.append(new_pixel)
            new_data.append(new_row)
        return new_data
    elif mod == "noise":
        new_data = []
        for row in data:
            new_row = []
            for pixel in row:
                new_pixel = []
                for val in pixel:
                    new_pixel.append(compute_random_noise(val))
                new_row.append(new_pixel)
            new_data.append(new_row)
        return new_data
    elif mod == "grayscale":
        new_data = []
        for row in data:
            new_row = []
            for pixel in row:
                new_row.append(compute_pixel_gray_scale(pixel))
            new_data.append(new_row)
        return new_data
    else:
        return None

def apply_vertical_flip(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """
    Flips the image vertically.
    """
    new_data = []
    for i in range(len(data) - 1, -1, -1):
        new_data.append(data[i])
    return new_data

def apply_horizontal_flip(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """
    Flips the image horizontally.
    """
    new_data = []
    for row in data:
        new_row = []
        for i in range(len(row) - 1, -1, -1):
            new_row.append(row[i])
        new_data.append(new_row)
    return new_data

def apply_horizontal_blur(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """
    (BONUS ATTEMPTED HERE)
    Applies a horizontal blur to the image.
    """
    height = len(data)
    width = len(data[0])

    new_data = []
    for r in range(height):
        new_row = []
        for c in range(width):
            total = [0, 0, 0]
            count = 0
            for offset in [-1, 0, 1]:
                nc = c + offset
                if 0 <= nc < width:
                    total[0] += data[r][nc][0]
                    total[1] += data[r][nc][1]
                    total[2] += data[r][nc][2]
                    count += 1
            new_pixel = [
                total[0] // count,
                total[1] // count,
                total[2] // count]
            new_row.append(new_pixel)
        new_data.append(new_row)
    return new_data

def compute_negative(val: int) -> int:
    """
    Returns the negative of the color value.
    """
    return abs(255 - val)

def compute_high_contrast(val: int) -> int:
    """
    Turns the value to either 0 or 255.
    """
    if val > 127:
        return 255
    else:
        return 0

def compute_random_noise(val: int) -> int:
    noise = random.randint(-50, 50)
    new_val = val + noise

    if new_val < 0:
        return 0
    elif new_val > 255:
        return 255
    return new_val

def compute_pixel_gray_scale(pixel: list[int]) -> list[int]:
    """
    Turns the pixel grey.
    """
    avg = (pixel[0] + pixel[1] + pixel[2]) // 3
    return [avg, avg, avg]

def main() -> None:
    filename = input("ppm file name: ")
    base_name = filename.split(".")[0]
    print("The image is loading.")
    data = load_image_data(filename)

    modifications = [
        "vertical_flip",
        "horizontal_flip",
        "remove_red",
        "remove_green",
        "remove_blue",
        "negative",
        "high_contrast",
        "noise",
        "grayscale",
        "horizontal_blur"
    ]
    for mod in modifications:
        print("Applying", mod)
        new_data = apply_modification(data, mod)
        output_name = base_name + "_" + mod + ".ppm"
        write_image_data(new_data, output_name)
        print("Writing", output_name)
    print("All modifications complete.")

main()