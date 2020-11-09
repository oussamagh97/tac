"""Filter out stopwords for word cloud"""

import sys
import nltk
from nltk.corpus import stopwords

sw = stopwords.words("french")
sw += ["les", "plus", "cette", "fait", "faire", "être", "deux", "comme", "dont", "tout",
       "ils", "bien", "sans", "peut", "tous", "après", "ainsi", "donc", "cet", "sous",
       "celle", "entre", "encore", "toutes", "pendant", "moins", "dire", "cela", "non",
       "faut", "trois", "aussi", "dit", "avoir", "doit", "contre", "depuis", "autres",
       "van", "het", "autre", "jusqu", "Cependant", "certes", "son", "bref", "donc", "or",
        "actuellement", "vers", "autres", "exception","leur", "mais", "puisque", "ailleurs",
        "courant", "minutes", "centimes", "chiffres", "kilowatt-heure", "ferait", "faute",    
        "cherchera", "infiniment", "avantage", "centre", "différence", "moyenne", "classe",
        "lignes", "question", "comparaison", "dernières", "similaires", "façon", "magnifique",
         "favorable", "grande", "proposition", "regrettons", "nous", "vous", "eux", "compagnie",
         "conduire vers", "futur", "passion", "exceptions", "discussion","millions", "milliers", 
          "abonder", "demande", "texte", "suffisant", "Soit", "favorable", "cercle", "ayant",
          "numérique", "personnes", "extraordinaires", "Messieurs", "divers", "uniquement", 
          "soulagement", "nouveau", "parfaitement", "intégralement", "moins", "petite", "raison"
          "jours", "jour", "semaine", "légèrement", "moi-même", "important", "heures", "bonne",
          "mensuel", "trentième", "somme", "matinée", "seulement", "jamais" , "samedi", "francs",
          "article", "certain", "certaine", "certains", "certaines", "consentement", "relative",
          "quelquefois", "un", "une","deux", "trois", "quatres", "cinq", "matin", "minutes", "heures",
          "qualité", "définitif", "filles", "fille", "garcons", "garcon", "ci-aprés", "minimum", "maximum", "proportion",
          "nombre", "l'exécution", "nécessité", "égal", "moitié", "ci-contre", "point", "satisfaction", "rapidement", "plan", "relatif", "jamais","choix","etc",
          "ans","leurs","celui","grand","grande","octobre","alors","rien","part", "suivant","celui","cause","rien","laquelle","raison","toute","chose","devant","date","décembre","beaucoup","alors","rien","chose","lorsque","quelque","grand","année","totalservice","bruxelle","bruxelles"]
sw = set(sw)

def filtering(year):
    path = f"{year}.txt"
    output = open(f"{year}_keywords.txt", "w",encoding='utf-8')

    with open(path,encoding="utf-8") as f:
        text = f.read()
        words = nltk.wordpunct_tokenize(text)
        kept = [w.lower() for w in words if len(
            w) > 2 and w.isalpha() and w.lower() not in sw]
        kept_string = " ".join(kept)
        output.write(kept_string)


if __name__ == '__main__':
    chosen_year = sys.argv[1]
    filtering(chosen_year)