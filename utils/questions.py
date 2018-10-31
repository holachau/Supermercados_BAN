answers = {
    "qYesNo": {
        "true": ["s", "S", "y", "Y"],
        "false": ["n", "N"]
    }
}

def qYesNo (label):
    ans = None
    answersYesNo = answers["qYesNo"]["true"]
    answersYesNo.extend(answers["qYesNo"]["false"])
    while ans not in answersYesNo:
        ans = input("¿" + label + " (s/n)? ")

    print(answers["qYesNo"]["true"])
    return True if ans in answers["qYesNo"]["true"] else False

print(qYesNo("Desea continuar"))
