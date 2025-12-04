import PyPDF2
import re
import json


# VARIABLES D'ENTRÉE
semestre_court = "A22" # exemple : "P16" ou "A16"


# variables dérivées
semestre_mi_long = semestre_court.replace("A", "A20").replace("P", "P20") # "A16" -> "A2016"
file_name = f"data-raw/conseil_perfectionnement_complet_{semestre_mi_long}.pdf"
semestre = semestre_court.replace("A", "Automne 20").replace("P", "Printemps 20") # "A16" -> "Automne 2016"
output_file_name = f"data-clean/output_{semestre_court}.json"

print("Fichier : ", file_name)

# ouverture du fichier pdf
pdfFileObj = open(file_name, 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
print("pages : ", len(pdfReader.pages))


# données de toutes des uvs du semestre
all_uvs_data = {}

# on parcourt l'ensemble des pages
for i in range(len(pdfReader.pages)):

    # affiche une barre de progression
    print("\r", i, "/", len(pdfReader.pages), end="")

    pageObj = pdfReader.pages[i]
    text = pageObj.extract_text()
    text = text.replace("\n ", " ")

    # on ignore ces pages là (existe en cas de commentaire trop long sur une uv)
    if not text.startswith(semestre):
        continue
    
    uv_data = {}

    # code de l'uv
    uv_full_title = re.search(f"{semestre}(.*)Rapport du responsable", text, re.DOTALL)
    if uv_full_title:
        uv_full_title = uv_full_title.group(1).strip()
        uv_data["code"] = uv_full_title.split(":", 1)[0].strip()
        uv_data["title"] = uv_full_title.split(":", 1)[1].strip().replace("\n", "")

    # prof
    prof = re.search("Rapport du responsable de l'enseignement : (.*)\n", text)
    uv_data["prof"] = prof.group(1).strip() if prof else None

    # nb inscrits, taux de réussite
    stats = re.search("(\d+) inscrits, (\d+) absent\(s\), (\d+) étudiants reçus à l'uv \(Réussite : (.*)%\) ", text)
    if stats:
        uv_data["nb_inscrits"] = int(stats.group(1))
        uv_data["nb_absents"] = int(stats.group(2))
        uv_data["nb_recus"] = int(stats.group(3))
        uv_data["taux_reussite"] = float(stats.group(4))


    questions = {}
    questions_raw = re.search("Question 1.*Page", text, re.DOTALL)
    questions_raw = questions_raw.group().split("Question")
    for i in range(1,len(questions_raw)):
        q_notes = re.findall(" (\d+.*)%", questions_raw[i])
        q_notes = [float(i) for i in q_notes]
        questions[i] = {"++": q_notes[0], "+": q_notes[1], "-": q_notes[2], "--": q_notes[3]}
    uv_data["questions"] = questions

    all_uvs_data[uv_data["code"]] = uv_data 

# store all_uvs_data in a json file
with open(output_file_name, "w") as f:
    json.dump(all_uvs_data, f, indent=4)