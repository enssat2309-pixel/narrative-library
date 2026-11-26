# Protocole du pilote de codage – tour 1

> Statut : archivé. Ce protocole régit le tour 1 (17-19 novembre 2026). Le tour 2 suit les décisions D-016 à D-018 (découpage en unités, 2 × 2 étiquettes, codeurs humains via Dropbox). Copie du document Claude « Protocole du pilote de codage – disclosures fonds retail » (révision 4).

## 1. Objet du pilote

Le pilote vérifie une seule chose : **le codebook v3 est-il assez clair pour que deux codeurs indépendants classent les mêmes segments de la même façon ?** Il ne décrit pas encore ce que contiennent les documents. La fiabilité se mesure avec l'alpha de Krippendorff sur le code principal.

## 2. Rôles au tour 1

| Acteur | Rôle | Ne voit jamais | Livrable |
|---|---|---|---|
| Bot de collecte | Collecte, extraction, segmentation, tirage, contrôle de lisibilité, paquet de codage | Le codebook | `segments_a_coder_lot1.csv` et `_lot2.csv`, `correspondance.csv` |
| Codeur A (Opus) | Code chaque segment (code principal, secondaires, facettes) | La collecte, le codeur B, les analyses | `codage_A_lot1.csv`, compte rendu |
| Codeur B (Sonnet) | Idem | La collecte, le codeur A, les analyses | `codage_B_lot1.csv`, compte rendu |
| Claude (analyste) | Consignes, alpha, analyse des désaccords, révisions proposées ; ne code pas | — | Rapport de pilote |
| Arbitre | Lance les sessions, transmet les fichiers, tranche, contrôle, décide | — | Arbitrages |

## 3. Matériau

- Tour 1 : lot 1, 63 segments (KID et fiches locales 20, factsheets 14, prospectus 13, rapports 16), en allemand, français et anglais.
- Tour 2 prévu : lot 2, 96 segments (24 par type de document), en cinq langues.
- Segments tirés en deux temps, graine 2026, textes uniques, un document par fonds et par strate, plafond par maison ; tri de lisibilité sur critères de forme.
- Limites : lot 1 sous la cible (63 sur 80), Singapour et Hong Kong absents, rubriques en deux colonnes des KID du lot 1 un peu sous-représentées.

## 4. Déroulement

1. Deux sessions neuves sur deux modèles différents, avec la consigne, le codebook et le paquet.
2. Codage et comptes rendus.
3. Analyse : alpha global, par type de document et par domaine ; matrice des confusions ; désaccords.
4. Contrôle humain sur des segments où les bots sont d'accord.
5. Arbitrage et révisions du codebook.
6. Tour 2 avec le codebook révisé.

## 5. Règles de codage du tour 1

Un code principal par segment (proposition qui occupe le plus de texte), jusqu'à deux secondaires, pas de découpage ; quatre facettes ; codage sur l'original ; règles de frontière du codebook. Détail : `tour1/paquet-codeurs/consigne-codeurs.md`.

## 6. Critères de décision

| Alpha (code principal) | Décision |
|---|---|
| 0,80 ou plus | Codebook fiable : passage au grand corpus |
| 0,67 à 0,80 | Utilisable avec prudence : révision des codes faibles |
| Moins de 0,67 | Refonte des domaines en cause |

Contrôle humain satisfaisant si l'arbitre est d'accord avec le code commun des bots sur au moins 80 % des segments contrôlés.
