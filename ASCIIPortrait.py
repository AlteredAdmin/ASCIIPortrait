from PIL import Image

def image_to_ascii(image_path, output_width=100):
    # Expanded ASCII characters list to represent different brightness levels
    ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " ", "!", "=", "-", "_", "(", ")", "<", ">", "[", "]", "{", "}", "|", "^", "/", "\\"]

    # Load the image
    image = Image.open(image_path)

    # Calculate aspect ratio
    width, height = image.size
    aspect_ratio = height / float(width)
    output_height = int(output_width * aspect_ratio / 2)  # Dividing by 2 because characters are typically about twice as tall as they are wide

    # Resize the image to fit the output dimensions
    image = image.resize((output_width, output_height))
    image = image.convert("L")  # Convert to grayscale

    pixels = list(image.getdata())
    grayscale_chars = [ascii_chars[pixel * len(ascii_chars) // 256] for pixel in pixels]
    ascii_image = [grayscale_chars[index: index + output_width] for index in range(0, len(grayscale_chars), output_width)]

    return "\n".join(["".join(row) for row in ascii_image])

if __name__ == "__main__":
    image_path = input("Enter the image path: ")
    image_path = image_path.strip('"')  # Remove any double quotes
    ascii_result = image_to_ascii(image_path)
    with open("ascii_output.txt", "w") as f:
        f.write(ascii_result)
    print("ASCII representation saved to ascii_output.txt!")
