import json, os
from scripts import svg_writer as svg

def compiler(root,generate_attribute=True,generate_source=True):

    if generate_attribute:
        
        # define the output folder
        output_path = 'output'
        attribute_file_name = 'attributes.json'
        svg.check_folder(output_path)
        
        # generate attributes
        attributes = {}
        for root, _, files in os.walk(root):
            for file in files:
                if file.endswith("png"):
                    file_name, _ = os.path.splitext(file.split("/")[-1])
                    file_name = file_name.split("_")
                    trait_type, trait_name = file_name[1], file_name[-1]
                    try: attributes[trait_type].append(trait_name)
                    except: attributes.update({trait_type:[trait_name]})

        # dump the attributes.json
        json.dump(
            attributes,
            open(os.path.join(output_path,attribute_file_name),"w"),
            indent=4
        )

    if generate_source:
        
        # collecting the layers
        layers = svg.find_all_layers('layers')

        # extract sequences
        sequences = sorted(list(dict.fromkeys([l['sequence'] for l in layers])))

def generator():
    pass

def exporter():
    pass

if __name__ == "__main__":

    compiler('layers',generate_attribute=True)