[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)](https://jupyter.org/)
[![Canva](https://img.shields.io/badge/Canva-00C4CC?style=for-the-badge&logo=canva&logoColor=white)](https://www.canva.com/)

# Analyse des résultats académiques de l'UTC

Mini-projet d'analyse des résultats académiques de l'Université de Technologie de Compiègne (UTC).

Réalisé en quelques jours, par simple curiosité, puis publié sur le réseau social de l'université. 

Excellente réception auprès des étudiants.

Juillet 2024.

## Contexte

Pour chaque semestre, les résultats académiques de l'UTC sont compilés dans un fichier pdf disponible sur l'intranet de l'université. Ce fichier contient une page par cours, avec les résultats compilés (nombre d'inscrits, taux de réussite, nombre d'absent), l'évaluation du cours par les étudiants (clarté du cours, qualité des supports pédagogiques, etc), et parfois des commentaires libres des professeurs. 

Voici un exemple de page de résultats pour un cours donné :

![](./assets/pdf-exemple-SY02.png)

Néanmoins, aucune statistique n'est publiée sur ces données : taux de réussite moyen d'un cours sur plusieurs semestres, évolution des taux de réussite dans le temps, etc. 

Notre objectif va donc être de réaliser nous-mêmes ces statistiques, à partir des fichiers pdf disponibles.

## Méthodologie

1. Chaque fichier pdf est téléchargé manuellement (un par semestre entre 2007 et 2024) dans le dossier `data-raw/`, chacun contenant environ 300 pages, pour un total de 35 fichiers. Total : 700Mo. S'il y avait eu plus de fichiers, une automatisation du téléchargement aurait été envisagée, mais ici cela n'en valait pas la peine.
2. Une première étape d'extraction a été réalisée manuellement, dans `1 - extraction.ipynb`, pour comprendre la structure des fichiers pdf et essayer différentes outils. Méthode retenue : extraction avec la libraire `PyPDF2`, puis stockage des données extraites au format .json.
3. Automatisation de l'extraction dans `2 - extraction auto.py`, générant un fichier .json par semestre dans le dossier `data-clean/`.
4. Analyse des données extraites dans `3 - analyse.ipynb`, avec visualisations.
5. Réalisation de visuels intéressants à partir des données analysées, avec Canva.
6. Publication des visuels sur le réseau social étudiant de l'université



## Organisation du dépôt 

- `assets` : images du readme 
- `data-raw` : fichiers pdf originaux téléchargés depuis l'intranet de l'UTC. En raison de leur taille importante, et pour des raisons de confidentialité, ils ne sont pas synchronisés avec le dépôt GitHub.
- `data-clean` : données extraites au format .json, prêtes à être analysées. Même remarque que pour `data-raw`.
- `outputs` : visuels et tableaux réalisés à partir des données analysées.
- `1 - extraction.ipynb` : notebook contenant les premiers essais d'extraction des données depuis les fichiers pdf bruts, en vue de l'automatisation.
- `2 - extraction auto.py` : script python d'extraction automatisée des données pour un fichier pdf donné.
- `3 - analyse.ipynb` : notebook d'analyse des données extraites, avec visualisations.

## Résultats

Certaines tendances intéressantes ou résultats marquants ont été mis en avant, comme par exemple :
- Le taux de réussite entre 2007 et 2024 semble suivre une tendance légèrement à la hausse, passant d'environ 88% entre 2007 et 2012, à plus de 90% depuis 2016. Est-ce dû à une amélioration de la qualité de l'enseignement, ou à un relâchement des exigences ?
- Avec 96% de réussite, le Printemps 2020 est le semestre le mieux réussi de l'histoire de l'UTC. Nous remercierons le COVID-19 pour cette performance inédite : notations assouplies, examens par QCM en ligne, etc.
- Certains cours, réputés parmi les plus difficiles de l'UTC, affichent un taux de réussite moyen inférieur à 70% sur plusieurs années, tombant ponctuellement à 40-50% certains semestres. Il s'agit souvent de cours fondamentaux en mathématiques ou en physique, comme SY02 (Méthodes statistiques pour l'ingénieur) ou MQ01 (Éléments de Résistance des Matériaux).
- Certaines irrégularités amusantes ont été relevées, comme un taux de réussite supérieur à 100% pour le cours QPO01 à l'automne 2015, manifestement car un élève noté absent a tout de même validé le cours.

Plusieurs visuels ont alors été réalisés avec Canva :

![](./assets/visuels_compilés.png)

Ces visuels ont alors été partagés avec les étudiants de l'UTC qui ont beaucoup apprécié l'initiative, comme en témoignent les nombreuses réactions. 

Voici le post Facebook réalisé pour l'occasion :

![](./assets/post_fb2.png)  

## Prochaines étapes

- Mettre à jour le projet avec des données récentes
- Automatiser entièrement les tâches : téléchargement des pdf, extraction, analyse, génération des visuels
- Publier les résultats sur un site web dynamique
- Bonus : utiliser les notes attribués aux cours par les élèves pour faire des analyses croisées (corrélation entre la qualité perçue et le taux de réussite, etc)