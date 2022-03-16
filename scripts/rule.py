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

    if key == 'SKIN' and value == 'ALBINO':
        attributes['EYES'].remove('GLOW (BLACK)')
        attributes['EYES'].remove('GLOW (WHITE)')
        attributes['EYES'].remove('GLOW LIGHT GREEN (BLACK)')
        attributes['EYES'].remove('GLOW LIGHT GREEN (WHITE)')
        attributes['EYES'].remove('GLOW TURQUOISE (BLACK)')
        attributes['EYES'].remove('GLOW TURQUOISE (WHITE)')
        attributes['EYES'].remove('SLEEPY (BLACK)')
        attributes['EYES'].remove('SLEEPY (WHITE)')
        attributes['FACE'].remove('AGENT 47 (BLACK)')
        attributes['FACE'].remove('AGENT 47 (WHITE)')
        attributes['FACE'].remove('GOD OF WAR - BASE EYES (BLACK)')
        attributes['FACE'].remove('GOD OF WAR - BASE EYES (WHITE)')
        attributes['FACE'].remove('PAINT ALLOY (BLACK)')
        attributes['FACE'].remove('PAINT ALLOY (WHITE)')
        attributes['MOUTH'].remove('BRACES (BLACK)')
        attributes['MOUTH'].remove('BRACES (WHITE)')
        attributes['MOUTH'].remove('LOLLIPOP (BLACK)')
        attributes['MOUTH'].remove('LOLLIPOP (WHITE)')
        attributes['MOUTH'].remove('BUBBLEGUM (BLACK)')
        attributes['MOUTH'].remove('BUBBLEGUM (WHITE)')
        attributes['MOUTH'].remove('CIGAR (BLACK)')
        attributes['MOUTH'].remove('CIGAR (WHITE)')
        attributes['VITILIGO SKIN'] = ['NOTHING']
    elif key == 'SKIN' and value == 'WHITE':
        attributes['EYES'].remove('GLOW (ALBINO)')
        attributes['EYES'].remove('GLOW (BLACK)')
        attributes['EYES'].remove('GLOW LIGHT GREEN (ALBINO)')
        attributes['EYES'].remove('GLOW LIGHT GREEN (BLACK)')
        attributes['EYES'].remove('GLOW TURQUOISE (ALBINO)')
        attributes['EYES'].remove('GLOW TURQUOISE (BLACK)')
        attributes['EYES'].remove('SLEEPY (ALBINO)')
        attributes['EYES'].remove('SLEEPY (BLACK)')
        attributes['FACE'].remove('AGENT 47 (ALBINO)')
        attributes['FACE'].remove('AGENT 47 (BLACK)')
        attributes['FACE'].remove('GOD OF WAR - BASE EYES (ALBINO)')
        attributes['FACE'].remove('GOD OF WAR - BASE EYES (BLACK)')
        attributes['FACE'].remove('PAINT ALLOY (ALBINO)')
        attributes['FACE'].remove('PAINT ALLOY (BLACK)')
        attributes['MOUTH'].remove('BRACES (ALBINO)')
        attributes['MOUTH'].remove('BRACES (BLACK)')
        attributes['MOUTH'].remove('LOLLIPOP (ALBINO)')
        attributes['MOUTH'].remove('LOLLIPOP (BLACK)')
        attributes['MOUTH'].remove('BUBBLEGUM (ALBINO)')
        attributes['MOUTH'].remove('BUBBLEGUM (BLACK)')
        attributes['MOUTH'].remove('CIGAR (ALBINO)')
        attributes['MOUTH'].remove('CIGAR (BLACK)')
    elif key == 'SKIN' and value == 'BLACK':
        attributes['EYES'].remove('GLOW (ALBINO)')
        attributes['EYES'].remove('GLOW (WHITE)')
        attributes['EYES'].remove('GLOW LIGHT GREEN (ALBINO)')
        attributes['EYES'].remove('GLOW LIGHT GREEN (WHITE)')
        attributes['EYES'].remove('GLOW TURQUOISE (ALBINO)')
        attributes['EYES'].remove('GLOW TURQUOISE (WHITE)')
        attributes['EYES'].remove('SLEEPY (ALBINO)')
        attributes['EYES'].remove('SLEEPY (WHITE)')
        attributes['FACE'].remove('AGENT 47 (ALBINO)')
        attributes['FACE'].remove('AGENT 47 (WHITE)')
        attributes['FACE'].remove('GOD OF WAR - BASE EYES (ALBINO)')
        attributes['FACE'].remove('GOD OF WAR - BASE EYES (WHITE)')
        attributes['FACE'].remove('PAINT ALLOY (ALBINO)')
        attributes['FACE'].remove('PAINT ALLOY (WHITE)')
        attributes['MOUTH'].remove('BRACES (ALBINO)')
        attributes['MOUTH'].remove('BRACES (WHITE)')
        attributes['MOUTH'].remove('LOLLIPOP (ALBINO)')
        attributes['MOUTH'].remove('LOLLIPOP (WHITE)')
        attributes['MOUTH'].remove('BUBBLEGUM (ALBINO)')
        attributes['MOUTH'].remove('BUBBLEGUM (WHITE)')
        attributes['MOUTH'].remove('CIGAR (ALBINO)')
        attributes['MOUTH'].remove('CIGAR (WHITE)')

    if key == "VITILIGO SKIN" and value == "NOTHING":
        attributes['VITILIGO FACE'] = ['NOTHING']

    if key == "MOUTH" and "MOUTH" in attributes['VITILIGO FACE'] and any([x in value for x in ['BRACES','LOLLIPOP','BUBBLEGUM','CIGAR']]):
        attributes['VITILIGO FACE'] = ['MOUTH']
    if key == "MOUTH" and "BUBBLEGUM" in value:
        attributes['HEAD'].remove('LOKI CROWN')
    elif key == "MOUTH" and any([x in value for x in ['BRACES','LOLLIPOP','CIGAR']]):
        attributes['HEAD'].remove('LOKI CROWN - BUBBLE GUM MOUTH')

    if key == "CLOTHES" and value in ["ASSASSIN'S CREED COSTUME","PIKACHU COSTUME"]:
        attributes['HEAD'] = ['NOTHING']
        attributes['HAIR'] = ['NOTHING']
        attributes['ACCESSORIES'] = ['NOTHING']
        attributes['EYES'].remove('CYCLOPS LASER GLASSES BLUE')
        attributes['EYES'].remove('CYCLOPS LASER GLASSES GREEN')
        attributes['EYES'].remove('CYCLOPS LASER GLASSES PINK')
        attributes['EYES'].remove('CYCLOPS LASER GLASSES TURQUOISE')
        attributes['EYES'].remove('CYCLOPS LASER GLASSES VIOLET')
        attributes['EYES'].remove('CYCLOPS LASER GLASSES YELLOW')
        attributes['EYES'].remove('CYCLOPS LASER GLASSES')
        attributes['EYES'].remove('VR GOGGLES BLACK')
        attributes['EYES'].remove('VR GOGGLES BROWN')
        attributes['EYES'].remove('VR GOGGLES LIGHT GREY')
        attributes['EYES'].remove('VR GOGGLES MULTICOLOR 01')
        attributes['EYES'].remove('VR GOGGLES MULTICOLOR 02')
        attributes['EYES'].remove('VR GOGGLES MULTICOLOR 03')
        attributes['EYES'].remove('VR GOGGLES MULTICOLOR 04')
        attributes['EYES'].remove('VR GOGGLES WHITE')
    elif key == "CLOTHES" and value in ['SQUID GAME JACKET','TOMMY VERCETTI SHIRT']:
        attributes['ACCESSORIES'].remove('BK BAG BLACK')
        attributes['ACCESSORIES'].remove('BK BAG BLUE')
        attributes['ACCESSORIES'].remove('BK BAG LIGHT GREEN')
        attributes['ACCESSORIES'].remove('BK BAG LIGHT GREY')
        attributes['ACCESSORIES'].remove('BK BAG LIME GREEN')
        attributes['ACCESSORIES'].remove('BK BAG ORANGE')
        attributes['ACCESSORIES'].remove('BK BAG PURPLE')
        attributes['ACCESSORIES'].remove('BK BAG RED')
        attributes['ACCESSORIES'].remove('BK BAG SKY BLUE')
        attributes['ACCESSORIES'].remove('BK BAG YELLOW')
        attributes['ACCESSORIES'].remove('GOLD CHAIN')
        attributes['ACCESSORIES'].remove('SILVER CHAIN')

    if key == "HEAD" and 'LOKI CROWN' in value:
        attributes['ACCESSORIES'].remove('GAMMER EARRING GOLD')
        attributes['ACCESSORIES'].remove('GAMMER EARRING SILVER')
        attributes['ACCESSORIES'].remove('POTARA EARRING BLUE')
        attributes['ACCESSORIES'].remove('POTARA EARRING GREEN')
        attributes['ACCESSORIES'].remove('POTARA EARRING ORANGE')
        attributes['ACCESSORIES'].remove('POTARA EARRING PURPLE')
        attributes['ACCESSORIES'].remove('POTARA EARRING RED')
        attributes['ACCESSORIES'].remove('POTARA EARRING YELLOW')

    return attributes

def get_rid(key,value,instance):
    if key == "HEAD" and value == "JASON MASK":
        instance['MOUTH'] = 'NOTHING'
    
    return instance