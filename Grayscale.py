from PIL import Image

print("Simple Grayscale Converter")
print("Step 1: Put your image file in the same folder as this script.")
print("Step 2: Change 'input_image' and 'output_image' variables below with your filenames.")
print("Step 3: Run the script to create a grayscale image.\n")

input_image = "example.jpg"
output_image = "grayscale.jpg"

image = Image.open(input_image)
grayscale = image.convert("L")
grayscale.save(output_image)

print(f"Done! Grayscale image saved as {output_image}")

