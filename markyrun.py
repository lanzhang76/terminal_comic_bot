import marky

#           ▌
# ▛▚▀▖▝▀▖▙▀▖▌▗▘▌ ▌
# ▌▐ ▌▞▀▌▌  ▛▚ ▚▄▌
# ▘▝ ▘▝▀▘▘  ▘ ▘▗▄▘
# a Markov Chain comic bot
# by Lan Zhang

context = {}
selections = {
    'Bill Maher': [0, 4, 8, 13, 15, 17, 91, 94, 102, 104],
    'Sarah Silverman': [84],
    'Aziz Ansari': [23],
    'Jerry Seinfeld': [47],
    'Louis C.K.': [82, 83, 85],
    'Kevin Hart': [19, 46],
    'Ali Wong': [132],
    'Amy Schumer': [49]
}


default_file = '300Full_transcripts.csv'


while context == {}:
    marky.clear()
    words = marky.addToCorpus(default_file, input(
        f"Who is talking? You can choose from {[i for i in selections]}\n"), context, selections)
else:
    newScript = ""
    for i in range(10):
        print('')
        sen = (input("_______type below_______\n\n")).strip()
        output = marky.generateTillEnd(sen, words)
        if newScript != "":
            newScript = newScript + " " + output
        else:
            newScript += output
        marky.clear()
        print(" ")
        print(" ▛▚▀▖▝▀▖▙▀▖▌▗▘▌ ▌")
        print(" ▌▐ ▌▞▀▌▌  ▛▚ ▚▄▌")
        print(" ▘▝ ▘▝▀▘▘  ▘ ▘▗▄▘")
        print(
            f"You, in the spirit of {[i for i in context][0]} ,say: \n\n{newScript}")
    print("")
