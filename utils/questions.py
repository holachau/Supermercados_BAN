answers = {
    "qYesNo": {
        "label": 's/n',
        "true": ["s", "S", "y", "Y"],
        "false": ["n", "N"]
    }
}

def qYesNo (label):
    ans = None
    answersYesNo = answers["qYesNo"]["true"].copy()
    answersYesNo.extend(answers["qYesNo"]["false"])
    while ans not in answersYesNo:
        ans = input("¿" + label + " (" + answers["qYesNo"]["label"] + ")? ")
        
    return (True if ans in answers["qYesNo"]["true"] else False)