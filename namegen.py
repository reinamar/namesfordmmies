import random

consonant = "bcdfghjklmnpqrstvwxyz"

vowel = "aeiou"

finLength = random.randint(2,4)

length = 0

class syllable:
    def __init__(self, con, vow):
        self.con = con
        self.vow = vow

    def syl(self):
        print(self.con + self.vow, end='')


s1 = syllable(random.choice(consonant.upper()), random.choice(vowel))
s2 = syllable(random.choice(consonant), random.choice(vowel))
s3 = syllable(random.choice(consonant), random.choice(vowel))
s4 = syllable(random.choice(consonant), random.choice(vowel))
s5 = syllable(random.choice(consonant), random.choice(vowel))
s6 = syllable(random.choice(consonant), random.choice(vowel))


while length < finLength:
    if length == 0:
        s1.syl()
        length += 1
    elif length == 1:
        s2.syl()
        length += 1
    elif length == 2:
        s3.syl()
        length += 1
    elif length == 3:
        s4.syl()
        length += 1
    elif length == 4:
        s5.syl()
        length += 1
    else:
        s5.syl()
        length += 1
        print("\nfin")

print()
