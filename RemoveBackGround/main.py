from rembg import remove

# Input and output paths
input_path = "image.jpeg"
output_path = "output.png"

# Open the input image
with open(input_path, 'rb') as input_file:
    input_data = input_file.read()

# Remove background
output_data = remove(input_data)

# Save the result
with open(output_path, 'wb') as output_file:
    output_file.write(output_data)