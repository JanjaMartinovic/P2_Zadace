'''Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba Nakon toga napisati regex za provjeru eduId koji mora biti formata iprezimeX@sum.ba gdje je i prvo slovo imena + prezime. X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo iprezime@sum.ba). Od korisnika zatražiti unos maila i eduid te ispisati uspješnost. Istražiti greedy i non-greedy quantifiers.'''

import re

regex = "^[a-z]+\.[a-z]+@fpmoz.sum.ba$"

regex1 = "^[a-z]{1}[a-z]+([0-9]*)?@sum.ba$"

while 1:
    unos = input("Mail: ")
    unos1 = input("eduId: ")
    rezultat = re.search(regex, unos)
    rezultat1 = re.search(regex1, unos1)
    if rezultat and rezultat1:
        break
    else:
        print("Unos koji ste unijeli je pogrešan!") 

print("Ispravan unos!") 
