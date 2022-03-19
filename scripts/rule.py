import re

def update(key,value,attributes):

    def remove(attributes,keyword,trait_type):
        entities = [t for t in attributes[trait_type] if keyword in t]
        for e in entities:
            attributes[trait_type].remove(e)
        if len(attributes[trait_type]) == 0:
            attributes[trait_type] = ["NOTHING"]
        return attributes

    def keep(attributes,keyword,trait_type):
        entities = [t for t in attributes[trait_type] if keyword in t or t == "NOTHING"]
        attributes[trait_type] = entities
        return attributes

    if key == 'SKIN' and value == 'ALBINO':
        attributes = remove(attributes,keyword='(BLACK)',trait_type='EYES')
        attributes = remove(attributes,keyword='(WHITE)',trait_type='EYES')
        attributes = remove(attributes,keyword='(BLACK)',trait_type='FACE')
        attributes = remove(attributes,keyword='(WHITE)',trait_type='FACE')
        attributes = remove(attributes,keyword='(BLACK)',trait_type='MOUTH')
        attributes = remove(attributes,keyword='(WHITE)',trait_type='MOUTH')
        attributes = remove(attributes,keyword='(BLACK)',trait_type='BUBBLE GUM')
        attributes = remove(attributes,keyword='(WHITE)',trait_type='BUBBLE GUM')
        attributes['VITILIGO SKIN'] = ['NOTHING']
    elif key == 'SKIN' and value == 'WHITE':
        attributes = remove(attributes,keyword='(ALBINO)',trait_type='EYES')
        attributes = remove(attributes,keyword='(BLACK)',trait_type='EYES')
        attributes = remove(attributes,keyword='(ALBINO)',trait_type='FACE')
        attributes = remove(attributes,keyword='(BLACK)',trait_type='FACE')
        attributes = remove(attributes,keyword='(ALBINO)',trait_type='MOUTH')
        attributes = remove(attributes,keyword='(BLACK)',trait_type='MOUTH')
        attributes = remove(attributes,keyword='(ALBINO)',trait_type='BUBBLE GUM')
        attributes = remove(attributes,keyword='(BLACK)',trait_type='BUBBLE GUM')
    elif key == 'SKIN' and value == 'BLACK':
        attributes = remove(attributes,keyword='(ALBINO)',trait_type='EYES')
        attributes = remove(attributes,keyword='(WHITE)',trait_type='EYES')
        attributes = remove(attributes,keyword='(ALBINO)',trait_type='FACE')
        attributes = remove(attributes,keyword='(WHITE)',trait_type='FACE')
        attributes = remove(attributes,keyword='(ALBINO)',trait_type='MOUTH')
        attributes = remove(attributes,keyword='(WHITE)',trait_type='MOUTH')
        attributes = remove(attributes,keyword='(ALBINO)',trait_type='BUBBLE GUM')
        attributes = remove(attributes,keyword='(WHITE)',trait_type='BUBBLE GUM')

    if key == "VITILIGO SKIN" and value == "NOTHING":
        attributes['VITILIGO FACE'] = ['NOTHING']

    if key == "MOUTH" and "MOUTH" in attributes['VITILIGO FACE'] and any([x in value for x in ['BRACES','LOLLIPOP','BUBBLEGUM','CIGAR']]):
        attributes['VITILIGO FACE'] = ['MOUTH']
    if key == "MOUTH" and "BUBBLEGUM" not in value:
        attributes['BUBBLE GUM'] = ['NOTHING']
    if key == "MOUTH" and "BUBBLEGUM" in value:
        attributes['HEAD'].remove('LOKI CROWN')
        attributes = remove(attributes,keyword='CYCLOPS LASER GLASSES',trait_type='HEAD')
    elif key == "MOUTH" and any([x in value for x in ['BRACES','LOLLIPOP','CIGAR']]):
        attributes['HEAD'].remove('LOKI CROWN - BUBBLE GUM MOUTH')

    if key == "CLOTHES" and value in ["ASSASSIN'S CREED COSTUME","PIKACHU COSTUME"]:
        attributes['HEAD'] = ['NOTHING']
        attributes['HAIR'] = ['NOTHING']
        attributes['ACCESSORIES'] = ['NOTHING']
        attributes = remove(attributes,keyword='CYCLOPS LASER GLASSES',trait_type='EYES')
        attributes = remove(attributes,keyword='VR GOGGLES',trait_type='EYES')
        attributes = remove(attributes,keyword='AGENT 47',trait_type='FACE')
    elif key == "CLOTHES" and value in ['SQUID GAME JACKET','TOMMY VERCETTI SHIRT']:
        attributes = remove(attributes,keyword='BK BAG',trait_type='ACCESSORIES')
        attributes['ACCESSORIES'].remove('GOLD CHAIN')
        attributes['ACCESSORIES'].remove('SILVER CHAIN')

    if key == "HEAD" and 'LOKI CROWN' in value:
        attributes = remove(attributes,keyword='GAMMER EARRING',trait_type='ACCESSORIES')
        attributes = remove(attributes,keyword='POTARA EARRING',trait_type='ACCESSORIES')
        attributes = remove(attributes,keyword='CYCLOPS LASER GLASSES',trait_type='EYES')
        attributes = remove(attributes,keyword='VR GOGGLES',trait_type='EYES')
    elif key == "HEAD" and "BASEBALL CAP BACK" in value:
        attributes = keep(attributes,keyword='(BASEBALL HAT)',trait_type='HAIR')
        attributes = remove(attributes,keyword='VR GOGGLES',trait_type='EYES')
    elif key == "HEAD" and "HEADPHONES" in value:
        attributes = remove(attributes,keyword='CYCLOPS LASER GLASSES',trait_type='EYES')
        attributes = remove(attributes,keyword='VR GOGGLES',trait_type='EYES')
        attributes = remove(attributes,keyword='GAMMER EARRING',trait_type='ACCESSORIES')
        attributes = remove(attributes,keyword='POTARA EARRING',trait_type='ACCESSORIES')
        attributes = remove(attributes,keyword='(BASEBALL HAT)',trait_type='HAIR')
        if "BASE HAIR" in value:
            attributes = keep(attributes,keyword='BASE',trait_type='HAIR')
        elif "DREADLOCKS" in value:
            attributes = keep(attributes,keyword='DREADLOCKS',trait_type='HAIR')
        elif "PUSHED BACK HAIR" in value:
            attributes = keep(attributes,keyword='PUSHED BACK',trait_type='HAIR')
        elif "TWISTS" in value:
            attributes = keep(attributes,keyword='TWISTS',trait_type='HAIR')
    elif key == "HEAD" and (value in ['LUIGI HAT','MARIO HAT','WATIO HAT'] or 'DRINKING HELMET' in value):
        attributes = remove(attributes,keyword='VR',trait_type='EYES')
        attributes = remove(attributes,keyword='CYCLOPS',trait_type='EYES')
        attributes['HAIR'] = ['NOTHING']
    elif key == "HEAD" and value == "JASON MASK":
        attributes = remove(attributes,keyword='VR',trait_type='EYES')
        attributes = remove(attributes,keyword='CYCLOPS',trait_type='EYES')
        attributes = remove(attributes,keyword='(BASEBALL HAT)',trait_type='HAIR')

    if key == "EYES" and "GLOW" in value:
        attributes = remove(attributes,keyword='GOD OF WAR - BASE EYES',trait_type='FACE')
        attributes['FACE'].remove('GOD OF WAR - SLEEPY EYES')
        attributes['EYES PUPIL'] = ['NOTHING']
    elif key == "EYES" and "SLEEPY" in value:
        attributes = keep(attributes,keyword='SLEEPY',trait_type='EYES PUPIL')
        attributes = remove(attributes,keyword='GOD OF WAR - BASE EYES',trait_type='FACE')
        attributes['FACE'].remove('GOD OF WAR - GLOW EYES')
    elif key == "EYES" and any([x in value for x in ['VR','CYCLOPS']]):
        attributes['FACE'].remove('GOD OF WAR - SLEEPY EYES')
        attributes['FACE'].remove('GOD OF WAR - GLOW EYES')
        attributes['EYES PUPIL'] = ['NOTHING']
    elif key == "EYES" and value == "NOTHING":
        attributes = keep(attributes,keyword='BASE',trait_type='EYES PUPIL')
        attributes = remove(attributes,keyword='GLOW',trait_type='FACE')
        attributes = remove(attributes,keyword='SLEEPY',trait_type='FACE')

    return attributes

def get_rid(key,value,instance):
    if key == "HEAD" and value == "JASON MASK":
        instance['MOUTH'] = 'NOTHING'
    
    return instance

def reformat(metadata):

    def remove_text_in_bracket(text):
        x = re.search('\((.*?)\)',text)
        if x != None:
            w = x.group()
            text = text.replace(w,"").strip()
        return text

    new_metadata = {
        "BACKGROUND": metadata['BACKGROUND'],
        "SKIN": metadata['SKIN'],
        "MOUTH": None,
        "CLOTHES": metadata['CLOTHES'],
        "HEAD": metadata['HEAD'],
        "EYES": None,
        "FACE": None,
        "HAIR": None,
        "ACCESSORIES": metadata['ACCESSORIES'],
        "GAMING GADGETS": metadata['GAMING GADGETS']
    }

    new_metadata['EYES'] = metadata['EYES'] = remove_text_in_bracket(metadata['EYES'])
    new_metadata['FACE'] = metadata['FACE'] = remove_text_in_bracket(metadata['FACE'])
    new_metadata['HAIR'] = metadata['HAIR'] = remove_text_in_bracket(metadata['HAIR'])

    if metadata['VITILIGO SKIN'] == 'BASE':
        new_metadata['SKIN'] = " ".join([metadata['SKIN'],'VITILIGO'])

    if 'LOKI CROWN' in metadata['HEAD']:
        new_metadata['HEAD'] = 'LOKI CROWN'
    elif 'HEADPHONES' in metadata['HEAD']:
        new_metadata['HEAD'] = " ".join(metadata['HEAD'].split(" ")[:2])

    if metadata['MOUTH'] != 'NOTHING':
        new_metadata['MOUTH'] = remove_text_in_bracket(metadata['MOUTH'])
    elif metadata['MOUTH'] == 'NOTHING':
        new_metadata['MOUTH'] = 'BASE'

    if 'GOD OF WAR' in metadata['FACE']:
        new_metadata['FACE'] = 'GOD OF WAR'

    if any([x in metadata['EYES'] for x in ['SLEEPY','GLOW','NOTHING']]):
        if metadata['EYES'] == 'NOTHING':
            new_metadata['EYES'] = metadata['EYES'] = 'BASE'
        if metadata['EYES PUPIL'] != 'NOTHING':
            color = metadata['EYES PUPIL'].split(' ')[1:]
            color = " ".join(color)
            new_metadata['EYES'] = " ".join([metadata['EYES'],color,'PUPIL'])

    return new_metadata