import base64
import json
import os
from math import ceil

def check_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)

def encode(image_path):
    '''
    Encode an image into base64.
    :param image_path: str -> Path for the image
    :return prettyfy_b64: str -> Encoded base64 image
    '''
    with open(image_path, "rb") as img_file:
        b64 = base64.b64encode(img_file.read()).decode('utf-8')
        max_column = ceil(len(b64)/76) + 1
        rows = [i*76 for i in range(0,max_column)] 
        rows[-1] = len(b64)
        prettify_b64 = []
        for j in range(len(rows)-1):
            a,b = rows[j],rows[j+1]
            prettify_b64.append(b64[a:b])
        return "\n".join(prettify_b64)

def encode_image(data,size):
    '''
    Creating group tag for XML document.
    :param data: dict -> Trait information based on the image file from source_images
    :param size: tupple -> SVG Document size
    :return layer: XML group tag for the image
    '''
    layer = f'''  <g
    inkscape:groupmode="layer"
    id="layer{data['index']}"
    style="display:none"
    inkscape:label="{data['trait_name']}">
    <image
        width="{size[0]}"
        height="{size[1]}"
        preserveAspectRatio="none"
        xlink:href="data:image/png;base64,{encode(data['image_path'])}\n"
        id="image{data['index']}"
        x="0"
        y="0" />
    </g>
    '''
    return layer

def find_all_layers(source_path):

    # find all layers from source_path
    layers = []
    for root, _, files in os.walk(source_path):
        for file in files:
            if file.endswith("png"):
                layer = {
                    "sequence": int(file.split("_")[0]),
                    "trait_name": "_".join(file.split("_")[1:]).replace(".png",""),
                    "path": root + "/" + file
                }
                layers.append(layer)

    # return the layer sequences
    sequences = sorted(list(dict.fromkeys([l['sequence'] for l in layers])))

    return layers, sequences

def create(file_name='source.svg',source_path=None):

    # define the output folder
    output_path = 'source'
    check_folder(output_path)

    # define the output file destination
    file_name = os.path.join(output_path,file_name)

    # prepare the layers
    layers, sequences = find_all_layers(source_path)

    # read the header file
    config = json.load(open('./source/config.json'))
    width = str(config['Width Dimension (px)'])
    height = str(config['Height Dimension (px)'])
    with open('./scripts/svg_headers.txt') as f:
        header = f.read()
        header = header.replace('<width>',width)
        header = header.replace('<height>',height)

    # create a blank svg file
    with open(file_name, 'w') as f:

        # write document header
        f.write(header)

        # insert encoded images
        i = 1
        for seq in sequences:
            for layer in layers:
                if layer['sequence'] == seq:
                    detail = {
                        "index": i,
                        "trait_name": layer['trait_name'],
                        "image_path": layer['path']
                    }
                    img_tag = encode_image(detail,size=(width,height))
                    f.write(img_tag.rstrip()+"\n")
                    i += 1

        # close document tag
        f.write('</svg>')

    # print out the message
    print(file_name,"have been created.")

if __name__ == '__main__':

    create(source_path='layers')