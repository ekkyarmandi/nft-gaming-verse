import random

def update(key,value,attributes):

    def remove_vr(attributes):
        try:
            attributes['EYES'].remove('CYCLOPS LASER GLASSES')
            attributes['EYES'].remove('VR GOGGLES BROWN')
            attributes['EYES'].remove('VR GOGGLES LIGHT GREY')
            attributes['EYES'].remove('VR GOGGLES MULTICOLOR 01')
            attributes['EYES'].remove('VR GOGGLES MULTICOLOR 02')
            attributes['EYES'].remove('VR GOGGLES MULTICOLOR 03')
            attributes['EYES'].remove('VR GOGGLES MULTICOLOR 04')
            attributes['EYES'].remove('VR GOGGLES MULTICOLOR 05')
            attributes['EYES'].remove('VR GOGGLES MULTICOLOR 06')
            attributes['EYES'].remove('VR GOGGLES')
        except: pass
        return attributes

    if key == 'SKIN' and value == 'ALBINO BASE':
        attributes['MOUTH'] = ['NOTHING']
        attributes['EYES'].remove('GLOW TEAL')
        attributes['EYES'].remove('GLOW')
        attributes['EYES'].remove('SLEEPY')
        attributes['VITILIGO SKIN'].remove('BASE')
    elif key == 'SKIN' and value == 'BASE':
        attributes['MOUTH'].remove('BRACES BLACK')
        attributes['MOUTH'].remove('BUBBLEGUM BLACK')
    elif key == 'SKIN' and value == 'BLACK BASE':
        attributes['EYES'].remove('GLOW TEAL')
        attributes['EYES'].remove('GLOW')
        attributes['EYES'].remove('SLEEPY')
        attributes['MOUTH'].remove('BRACES')
        attributes['MOUTH'].remove('BUBBLEGUM')
        attributes['MOUTH'].remove('CIGAR')
        attributes['MOUTH'].remove('LOLLIPOP')

    if key == "VITILIGO SKIN" and value == "BASE":
        attributes = remove_vr(attributes)
        attributes['MOUTH'] = ['NOTHING']

    if key == "EYES" and any([x in value for x in ["VR","CYCLOPS"]]):
        attributes['FACE'] = ['NOTHING']

    if key == "CLOTHES" and value in ["ASSASSIN'S CREED COSTUME","PIKACHU COSTUME"]:
        attributes['ACCESSORIES'] = ['NOTHING']
        attributes['FACE'] = ['NOTHING']
        attributes['HEAD'] = ['NOTHING']
        attributes['HAIR'] = ['NOTHING']
        attributes = remove_vr(attributes)

    if key == "HEAD" and value != "NOTHING":
        attributes = remove_vr(attributes)
    if key == "HEAD" and value in ["LUIGI HAT","MARIO HAT","WATIO HAT"]:
        attributes['HAIR'] = ['NOTHING']
    elif key == "HEAD" and value == "JASON MASK":
        attributes['MOUTH'] = ['NOTHING']
    elif key == "HEAD" and value == "DRINKING SODA HELMET":
        attributes['HAIR'] = ['NOTHING']

    return attributes

def get_rid(key,value,instance):
    if key == "HEAD" and value == "JASON MASK":
        instance['MOUTH'] = 'NOTHING'
    
    return instance