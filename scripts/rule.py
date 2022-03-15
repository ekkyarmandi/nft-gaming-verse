import random

def update(key,value,attributes):

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

    if key == "EYES" and any([x in value for x in ["VR","CYCLOPS"]]):
        attributes['FACE'] = ['NOTHING']

    if key == "CLOTHES" and value in ["ASSASSIN'S CREED COSTUME","PIKACHU COSTUME"]:
        attributes['ACCESSORIES'] = ['NOTHING']
        attributes['FACE'] = ['NOTHING']
        attributes['HEAD'] = ['NOTHING']

    if key == "HEAD" and value in ["LUIGI HAT","MARIO HAT","WATIO HAT"]:
        attributes['HAIR'] = ['NOTHING']
    elif key == "HEAD" and value == "JASON MASK":
        attributes['HAIR'] = ['NOTHING']
        attributes['MOUTH'] = ['NOTHING']
    elif key == "HEAD" and value == "DRINKING SODA HELMET":
        attributes['HAIR'] = ['NOTHING']

    return attributes

def get_rid(key,value,instance):
    if key == "HEAD" and value == "JASON MASK":
        instance['MOUTH'] = 'NOTHING'
    return instance