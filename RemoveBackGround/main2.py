from rembg import remove

input_path = "image.jpeg"
output_path = "output.png"

with open(input_path, 'rb') as i: # rb read binary
    with open(output_path, 'wb') as o: #wb write binary
        input = i.read()
        output = remove(input)
        o.write(output)

