import random
import string
import re
nigger = """
matrix bachelor ceiling innocent divide lumber foster again fantasy into despair surface
color toy upgrade nature ice clay ridge cannon physical sea spray action
earn elegant grit invite isolate half tattoo setup pottery clap keep rabbit
produce scheme mimic twist suspect vote then salad voyage deal monkey magnet
melody beauty casual detail endless shaft dose sun budget teach curious group
riot same garbage wool cart visa guilt robust ripple winner melt theme
shrimp naive pull limit arctic point chaos flip range divorce stable wisdom
exercise tomorrow door stereo beauty mask news badge menu orbit surprise sell
mandate tower raise art middle bomb loud recycle junior spoil elephant horse
stadium success capable leader distance shaft anger mandate coyote true cause practice
decade scatter gadget certain control scene pitch answer degree shop dose damp
private anxiety bleak inform hover wear drive chest stumble face wrong dwarf
fine glimpse fault advance egg ugly drive crazy adult future rule
jungle dinosaur farm loyal manage emotion smooth people lava fun limb absurd liberty sustain vanish then bitter venture million escape guard bright spare rich
say hint orchard bread robot stay liberty primary shed avoid fruit cupboard core canoe pig lava dose relief design real model improve short gasp
celery opinion vault memory aware pause absorb afraid humor only wet market hill calm gown judge stable hello saddle theory deputy muffin access convince
owner simple immune auction update cargo holiday loyal private rose tide purchase hello trigger meat matter enhance burst timber minute lava clump hedgehog parade
hamster pyramid noodle either smooth acoustic mandate oblige virus message silly quiz law discover portion soul dynamic smoke essence defense pen mention resemble lake
total history tide squeeze hybrid control stay antenna clock pride decorate rule woman wrong medal useful accuse wrestle army verb recipe smile universe people 
"""
seed_words = [word.replace("\n", " ") for word in nigger.split(" ")]

def generate_alphanum_random_string():
    length = random.randint(15, 21)
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string

def generateSeedAlikeStr(found: bool):
    # string = f"{random.choice(seed_words)} {random.choice(seed_words)} {random.choice(seed_words)}..."
    # if len(string) < 52:
    #     return string
    # else:
    #     string = f"{random.choice(seed_words)} {random.choice(seed_words)}..."
    #     return string
    if not found:
        return f"{random.choice(seed_words)} {random.choice(seed_words)} {random.choice(seed_words)} {random.choice(seed_words)} {random.choice(seed_words)} {random.choice(seed_words)} {random.choice(seed_words)}..."
    else:
        return f"{random.choice(seed_words)} {random.choice(seed_words)} {random.choice(seed_words)}..."
def unhtml(str: str):
    out = str.replace('<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#4fc93e;">', "")
    out = out.replace("</span></p></body></html>", "")
    out = out.replace('<html><head/><body><p><span style=" font-size:16pt; font-weight:600; color:#000000;">', '')
    out = out.replace('<html><head/><body><p><span style=" font-size:16pt; font-weight:600;">0.00$</span></p></body></html>', '')
    out = out.replace('<html><head/><body><p><span style=" font-size:16pt; font-weight:600;">', '')
    out = out.replace("$", "")
    return out