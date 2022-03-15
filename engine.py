import json, os, sys

from attr import attr

from scripts import rule
from scripts import svg_writer as svg

import random

def compiler(layers_path,generate_attribute=True,generate_source=True):

    if generate_attribute:
        
        # define the output folder
        output_path = 'output'
        attribute_file_name = 'attributes.json'
        svg.check_folder(output_path)
        
        # generate attributes
        attributes = {}
        for _, _, files in os.walk(layers_path):
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
        
        # create the source.svg file
        svg.create(source_path=layers_path)

def generator(attribute_file):
    
    attribute = json.load(open(attribute_file))

    skin_colors = [
        'WHITE',
        'BLACK',
        'ALBINO'
    ]

    skin_color = random.choice(['WHITE','BLACK','ALBINO'])
    vitiligo = random.choice([True,False])

    attribute = rule.by_skin(skin_color,vitiligo,attribute)

    # for key in attribute:
    #     item = random.choice(attribute[key])
    #     instance.update({key:item})

def exporter():
    pass

if __name__ == "__main__":

    if sys.argv[1] == 'compile':

        compiler(
            'layers',
            generate_attribute=False,
            generate_source=True
        )

    elif sys.argv[1] == 'generate':

        generator('./source/attributes.json')