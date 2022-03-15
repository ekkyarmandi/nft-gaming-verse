import os

def check_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)

def find_all_layers(root_path):
    layers = []
    for root, _, files in os.walk(root_path):
        for file in files:
            if file.endswith("png"):
                layer = {
                    "sequence": int(file.split("_")[0]),
                    "trait_name": "_".join(file.split("_")[1:]).replace(".png",""),
                    "path": root + "/" + file
                }
                layers.append(layer)
    return layers

def create_source(file_name='source.svg'):

    output_path = 'source'
    check_folder(output_path)

    output_path = os.path.join(output_path,file_name)

    with open('./scripts/svg_headers.txt') as f:
        header = f.read()