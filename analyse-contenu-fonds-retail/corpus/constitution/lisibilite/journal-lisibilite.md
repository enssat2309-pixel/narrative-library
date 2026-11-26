# Journal — mission 4, contrôle de lisibilité (17/11/2026)

Produit par lisibilite_script.py le 17/11/2026 22:40 (heure d'Europe/Luxembourg). Aucun accès réseau, aucune traduction, aucun fichier livré modifié.

## Fichiers lus

- `tirage_v3/tirage_pilote.csv` : sha256 `9a250a41140532c7868e0c584cf5005a303017f8e9882aa294a98d0585a26e8e`
- `lisibilite_travail/decisions.csv` : sha256 `827dd2e6a8c182d4b2599068f32ed01dc27de5b4edaa6e810f43cb0142efe359` (décisions prises à la lecture, une par ligne, par lots d'environ 15 segments)

## Décisions de lisibilité

- Chaque segment a été lu (texte_affichage ; texte_original quand la mise en page était douteuse ; segments voisins pour comprendre le découpage). Un script n'a servi qu'à afficher les segments par lots ; il n'a pris aucune décision.
- Ordre appliqué : E1 d'abord ; sinon retenu si R1, R2 ou R3 ; sinon premier motif E2 à E5. En cas de doute : retenu, avec une note de 10 à 20 mots.
- Quand plusieurs critères R s'appliquent, le critère noté est le plus caractéristique du segment (R1 dès qu'une phrase rédigée est présente).
- Interprétation E1 : deux colonnes de texte rédigé juxtaposées sur les mêmes lignes, ou en lignes alternées (colonne de droite renvoyée à la ligne). Un texte rédigé juxtaposé à un tableau libellé-valeur (ou à une liste chiffrée) n'est pas deux textes rédigés : retenu, avec une note de doute.
- Interprétation E4 : les listes de positions ou de titres en portefeuille sont écartées même quand chaque ligne associe un titre et une valeur (exemple explicite de E4) ; une telle liste est retenue si le segment contient aussi une phrase ou un libellé-valeur hors positions.

## Remplacement (section 3)

- Traitement par lot et strate, documents principaux par rang_document croissant, puis segments principaux par rang_segment croissant.
- Segment principal écarté : premier segment de réserve retenu du même document (rangs 3, 4, 5) ; à défaut, file des documents de réserve de la strate (rang_document croissant, puis rangs de segments 1 à 5), segments retenus seulement, chaque segment une seule fois ; un document de réserve entamé est épuisé avant le suivant (file unique parcourue dans l'ordre).
- Les manques du tirage v3 (documents absents au lot 1) ne sont pas comblés : la section 3 ne remplace que des segments écartés.

## Paquets de codage (section 4)

- Pour chaque lot, jeu final trié par segment_id puis `random.Random("2026-codage-<lot>").shuffle(liste)`, avec <lot> exactement comme dans les graines de tirage_script.py : `lot1`, `lot2` (graines « 2026-codage-lot1 » et « 2026-codage-lot2 »). id_codage dans l'ordre du mélange (L1-001…, L2-001…).
- texte_en repris tel quel du tirage (vide si absent). Colonnes exclues : maison, fonds, ISIN, pays, sha256, strate, règle de périmètre, rangs, segment_id.

## Recontrôle (section 6.1)

- 478 lignes triées par segment_id, `random.Random("2026-recontrole-lisibilite").shuffle(liste)`, puis les 40 premières (mélange puis tranche [:40], et non `rng.sample`). Fichier d'entrée aveugle : `lisibilite_travail/recontrole_entree.csv` (segment_id, type_document, langue_origine, titre_section, texte_affichage, texte_original, segment_precedent, segment_suivant), dans l'ordre du tirage.
- Organisation de la relecture à l'aveugle : un relecteur distinct a reçu uniquement `recontrole_entree.csv` et les critères de la mission (sections 2 et 7), sans accès aux décisions, critères, notes, remplacements ni paquets de la première passe. Il a appliqué E1 au sens littéral (mêmes lignes) et noté le premier critère de maintien dans l'ordre R1 > R2 > R3. Ses 40 décisions (`lisibilite_travail/recontrole_decisions.csv`, sha256 `ce7c34a6f368d4c58b9969d4d1c3b6045d7b377123c3c25ea8d9140af8b109be`) sont recopiées à côté des décisions de première passe dans `lisibilite/recontrole_lisibilite.csv`. Résultat : 39 décisions identiques sur 40, 38 critères identiques. Aucune décision de première passe n'a été modifiée.
