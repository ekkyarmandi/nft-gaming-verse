# add local PATH
import os

gtkhome = "C:\\Program Files\\GTK3-Runtime Win64\\bin"
os.environ["PATH"] = gtkhome + ";" + os.environ["PATH"]

# import necessary libraries
from xml.etree import ElementTree as ET
from tqdm import tqdm
import cairosvg
import random
import json
import sys

# import local functions
from scripts import rule
from scripts import svg_writer as svg

# exclude the namespace
ET.register_namespace("", "http://www.w3.org/2000/svg")


def compiler(layers_path, generate_attribute=True, generate_source=True):

    if generate_attribute:

        # define the output folder
        output_path = "source"
        attribute_file_name = "attributes.json"
        svg.check_folder(output_path)

        # generate attributes
        attributes = {}
        for _, _, files in os.walk(layers_path):
            for file in files:
                if file.endswith("png"):
                    file_name, _ = os.path.splitext(file.split("/")[-1])
                    file_name = file_name.split("_")
                    trait_type, trait_name = file_name[1], file_name[-1]
                    try:
                        attributes[trait_type].append(trait_name)
                    except:
                        attributes.update({trait_type: [trait_name]})

        # dump the attributes.json
        json.dump(
            attributes,
            open(os.path.join(output_path, attribute_file_name), "w"),
            indent=4,
        )

        # print out the message
        print(attribute_file_name, "have been created.")

    if generate_source:

        # create the source.svg file
        svg.create(source_path=layers_path)


def generator(number=10, attribute_file="source\\attributes.json", output_path="output\\metadata.json"):

    # define the trait type choosing sequence
    trait_types = [
        "BACKGROUND",
        "SKIN",
        "VITILIGO SKIN",
        "MOUTH",
        "VITILIGO FACE",
        "CLOTHES",
        "HEAD",
        "EYES",
        "EYES PUPIL",
        "FACE",
        "HAIR",
        "ACCESSORIES",
        "GAMING GADGETS",
        "BUBBLE GUM",
    ]

    # define allowed trait types
    allowed_traits = [
        "BACKGROUND",
        "SKIN",
        "VITILIGO SKIN",
        "MOUTH",
        "CLOTHES",
        "HEAD",
        "EYES",
        "FACE",
        "HAIR",
        "ACCESSORIES",
        "GAMING GADGETS",
    ]

    # define the empty variable
    metadata = []
    unique_metadata = []
    number = int(number)
    while len(metadata) < number:

        # read the attributes file
        attributes = json.load(open(attribute_file))

        # random generate the combination
        instance = {}
        for trait_type in trait_types:
            if trait_type in allowed_traits:
                item = rule.choose(attributes, trait_type)
            else:
                item = random.choice(attributes[trait_type])
            attributes = rule.update(trait_type, item, attributes)
            instance = rule.get_rid(trait_type, item, instance)
            instance.update({trait_type: item})

        # collect the instance
        instance_str = ",".join(instance.values())
        if instance_str not in unique_metadata:
            unique_metadata.append(instance_str)
            metadata.append(instance)
            print(len(metadata))

    # dump the metadata
    json.dump(metadata, open(output_path, "w"), indent=4)
    
    # reformat the metadata
    real_metadata = []
    for instance in metadata:
        new_instance = rule.reformat(instance)
        real_metadata.append(new_instance)

    # dump the metadata
    output_path = output_path.replace("metadata", "real_metadata")
    json.dump(real_metadata, open(output_path, "w"), indent=4)


def exporter(metadata_path, file_name="sample"):
    def metadata2list(metadata):
        return [f"{k}_{v}" for k, v in metadata.items() if v != "NOTHING"]

    # read the metadata
    metadata = json.load(open(metadata_path))

    # export the artworks based on metadata
    i = 0
    file_name = "output\\" + str(file_name) + "{}.png"
    for j in tqdm(metadata, desc=f"Exporting {len(metadata)} Gaming Verse", ncols=100):

        # read the svg file
        tree = ET.parse(open("source\\source.svg"))
        root = tree.getroot()

        # apply the metadata
        for element in root.iter():
            if element.tag.split("}")[-1] == "g":
                label = element.get("{http://www.inkscape.org/namespaces/inkscape}label")
                if label in metadata2list(j):
                    style = element.get("style")
                    new_style = style.replace("display:none", "display:inline")
                    element.set("style", new_style)

        # export the ballz
        tree.write("source\\exported.svg", xml_declaration=True)

        # export the svg into png
        cairosvg.svg2png(url="source\\exported.svg", write_to=file_name.format(i + 1))

        # increment i
        i += 1

    # remove the export file
    os.remove("source\\exported.svg")


if __name__ == "__main__":

    if sys.argv[1] == "compile":
        compiler(layers_path="layers", generate_attribute=False, generate_source=True)

    elif sys.argv[1] == "generate":
        number = sys.argv[2]
        generator(number)
        print(number, "metadata have been generated.")

    elif sys.argv[1] == "export":
        try:
            exporter(os.path.join("output", sys.argv[2]), sys.argv[3])
        except:
            exporter(os.path.join("output", "metadata.json"), file_name="sample")

    elif sys.argv[1] == "produce":
        generator(number=sys.argv[2])
        exporter('output\\metadata.json','example')