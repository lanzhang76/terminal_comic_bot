import marky


context = {}
selections = {
    'Bill Maher': [0, 4, 8, 13, 15, 17, 91, 94, 102, 104],
    'Sarah Silverman': [84],
    'Aziz Ansari': [23],
    'Jerry Seinfeld': [47],
    'Amy Schumer': [49]
}


default_file = '300Full_transcripts.csv'


marky.clear()
words = marky.addToCorpus(default_file, input(
    f"Who is talking? You can choose from {[i for i in selections]}\n"), context, selections)

newScript = ""
for i in range(10):
    print('')
    sen = input("_______type your sentence below_______\n\n")
    output = marky.generateTillEnd(sen, words)
    if newScript != "":
        newScript = newScript + " " + output
    else:
        newScript += output
    marky.clear()
    print(f"You are saying: \n\n {newScript}")
