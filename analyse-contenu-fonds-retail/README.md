# Analyse de contenu – informations données aux investisseurs de détail dans les fonds de l'UE

## Objet

Construire et valider une méthode pour mesurer **ce que disent les documents d'information des fonds européens destinés aux investisseurs de détail** (KID, KIID, factsheets, prospectus, rapports, fiches locales comme les KFS de Hong Kong et les PHS de Singapour) : ce qui est communiqué, ce qui manque, ce qui varie selon les marchés, les produits et les émetteurs.

Le projet repose sur trois briques :

1. **Le codebook** : une taxonomie de 52 codes en 10 domaines (A à J) et 2 codes résiduels (Z), ancrée dans la réglementation mais organisée autour des besoins de l'investisseur, avec des règles de frontière et des facettes.
2. **Le corpus** : environ 340 documents de fonds domiciliés dans l'UE, collectés de façon neutre (registres officiels, tirage reproductible, graine 2026).
3. **Le pilote** : un codage double indépendant de segments tirés au hasard, mesuré par l'alpha de Krippendorff, pour vérifier que le codebook est assez clair avant de l'appliquer à grande échelle.

## État en bref (26 novembre 2026)

- Codebook v3 en service ; décisions de révision en cours (étape C).
- Corpus des lots 1 et 2 collecté, consolidé et tiré ; pas de nouvelle collecte prévue.
- Tour 1 du pilote codé (alpha 0,97 entre deux bots, revue humaine montrant un accord réel plus faible).
- Prochaine étape : finir l'étape C, puis préparer le tour 2 avec deux codeurs humains.

Détail : [`STATUT.md`](STATUT.md) · Jalons : [`FEUILLE_DE_ROUTE.md`](FEUILLE_DE_ROUTE.md) · Décisions : [`decisions/journal.md`](decisions/journal.md)

## Où trouver quoi

| Dossier | Contenu |
|---|---|
| [`GOUVERNANCE.md`](GOUVERNANCE.md) | Rôles, processus de décision, conventions, règle d'indépendance des codeurs |
| [`INDEX.md`](INDEX.md) | Liste de tous les fichiers de la section, avec leur statut |
| [`decisions/`](decisions/) | Journal et une fiche par décision |
| [`cadrage/`](cadrage/) | Périmètre, produits, pays, inventaire des documents, maisons de fonds |
| [`codebook/`](codebook/) | Versions du codebook (codes, frontières, facettes), candidats, historique |
| [`corpus/`](corpus/) | Comment le corpus a été constitué (consignes, rapports, tirage, lisibilité) et où sont les fichiers lourds |
| [`pilote/`](pilote/) | Protocole, tour 1 (paquet, codages, analyse), tour 2 |
| [`correspondances/`](correspondances/) | Ponts avec les autres sections du dépôt (PRIIPs KID, UCITS KIID, classifications de sociétés de gestion) |
| [`outils/`](outils/) | Scripts réutilisables |
| [`livrables/`](livrables/) | Versions finales destinées à être partagées |

## Fichiers lourds

Les PDF, les archives des lots et le corpus segmenté complet sont dans Dropbox, dossier `Narratives Library/analyse-contenu-fonds-retail/`. Voir [`corpus/references.md`](corpus/references.md).

## Contribuer

Ouvrez une *issue* avec l'étiquette « proposition » (contexte, options, recommandation), puis une *pull request* pour toute modification. Voir [`GOUVERNANCE.md`](GOUVERNANCE.md).
