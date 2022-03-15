import json, os, sys

from scripts import rule
from scripts import svg_writer as svg

import random

def compiler(layers_path,generate_attribute=True,generate_source=True):

    if generate_attribute:
        
        # define the output folder
        output_path = 'source'
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

        # print out the message
        print(attribute_file_name,"have been creat")

    if generate_source:
        
        # create the source.svg file
        svg.create(source_path=layers_path)

def generator(number=10, attribute_file='source\\attributes.json', output_path='output\\matadata.json'):

    # define the trait type choosing sequence
    trait_types = [
        'BACKGROUND',
        'SKIN',
        'VITILIGO SKIN',
        'EYES',
        'MOUTH',
        'CLOTHES',
        'HEAD',
        'FACE',
        'HAIR',
        'ACCESSORIES',
        'GAMING GADGETS'
    ]

    # define the empty variable
    metadata = []
    for i in range(number):

        # read the attributes file
        attributes = json.load(open(attribute_file))

        # random generate the combination
        instance = {}
        for trait_type in trait_types:
            item = random.choice(attributes[trait_type])
            attributes = rule.update(trait_type,item,attributes)
            instance = rule.get_rid(trait_type,item,instance)
            instance.update({trait_type:item})

        # collect the instance
        metadata.append(instance)

    # dump the metadata
    json.dump(metadata,open(output_path,'w'),indent=4)

def exporter():
    pass

if __name__ == "__main__":

    if sys.argv[1] == 'compile':

        compiler(
            'layers',
            generate_attribute=False,
            generate_source=True
        )

    # elif sys.argv[1] == 'generate':

    #     generator('./source/attributes.json')

    # generator(number=10)