# Compte rendu — contrôle de lisibilité et paquet de codage (mission 4, 17/11/2026)

Rédigé le 17/11/2026 22:40 (heure d'Europe/Luxembourg).

Entrée unique : `tirage_v3/tirage_pilote.csv` (478 lignes, sha256 `9a250a41140532c7868e0c584cf5005a303017f8e9882aa294a98d0585a26e8e`), non modifié. Chaque ligne a été lue et décidée selon la forme seule (section 2) ; aucune décision n'a été prise par un filtre automatique.

## 1. Effectifs par lot et par strate

| Lot | Strate | Segments principaux tirés | Principaux écartés (E1/E2/E3/E4/E5) | Remplacés (même document / document de réserve) | Non remplacés | Effectif final | Cible | Manque |
|---|---|---|---|---|---|---|---|---|
| lot1 | S1 (KID, KIID, fiches locales, KFS, PHS) | 20 | 3 (1/2/0/0/0) | 3 (3 / 0) | 0 | 20 | 20 | 0 |
| lot1 | S2 (factsheets) | 14 | 2 (1/1/0/0/0) | 2 (2 / 0) | 0 | 14 | 20 | 6 |
| lot1 | S3 (prospectus) | 18 | 9 (9/0/0/0/0) | 4 (4 / 0) | 5 | 13 | 20 | 7 |
| lot1 | S4 (rapports et bulletins) | 18 | 8 (3/0/2/3/0) | 6 (6 / 0) | 2 | 16 | 20 | 4 |
| lot2 | S1 (KID, KIID, fiches locales, KFS, PHS) | 24 | 3 (3/0/0/0/0) | 3 (3 / 0) | 0 | 24 | 24 | 0 |
| lot2 | S2 (factsheets) | 24 | 7 (2/4/0/1/0) | 7 (7 / 0) | 0 | 24 | 24 | 0 |
| lot2 | S3 (prospectus) | 24 | 3 (2/1/0/0/0) | 3 (3 / 0) | 0 | 24 | 24 | 0 |
| lot2 | S4 (rapports et bulletins) | 24 | 5 (0/4/1/0/0) | 5 (5 / 0) | 0 | 24 | 24 | 0 |
| **Total** | | 166 | 40 | 33 | 7 | 159 | 176 | 17 |

Le manque comprend les écarts déjà présents au tirage v3 (lot 1 : documents en nombre insuffisant, acceptés) et les segments écartés qui n'ont pu être remplacés faute de réserve. Rien n'a été complété au-delà des règles de remplacement.

## 2. Détail des remplacements

| Lot | Strate | Segment écarté (motif) | Doc. principal (rang) | Remplaçant | Origine (rang doc., rang seg.) |
|---|---|---|---|---|---|
| lot1 | S1 | LOT1-LU2348335964-FR-KID-e28ecde5-000008 (E1) | 3 | LOT1-LU2348335964-FR-KID-e28ecde5-000016 | même document (3, 3) |
| lot1 | S1 | LOT1-LU0064964074-DE-KID-8f532e88-000020 (E2) | 8 | LOT1-LU0064964074-DE-KID-8f532e88-000017 | même document (8, 4) |
| lot1 | S1 | LOT1-IE00BKWQ0M75-DE-KID-20cc4a89-000031 (E2) | 9 | LOT1-IE00BKWQ0M75-DE-KID-20cc4a89-000023 | même document (9, 4) |
| lot1 | S2 | LOT1-LU0138981039-DE-Factsheet-503089e9-000018 (E2) | 3 | LOT1-LU0138981039-DE-Factsheet-503089e9-000026 | même document (3, 3) |
| lot1 | S2 | LOT1-LU1159239190-CH-Factsheet-35487d39-000019 (E1) | 7 | LOT1-LU1159239190-CH-Factsheet-35487d39-000007 | même document (7, 3) |
| lot1 | S3 | LOT1-LU0224105477-FR-Prospectus-9f8a5429-000645 (E1) | 3 | LOT1-LU0224105477-FR-Prospectus-9f8a5429-001920 | même document (3, 4) |
| lot1 | S3 | LOT1-IE00BKWQ0M75-DE-Prospectus-e75278cd-000173 (E1) | 6 | LOT1-IE00BKWQ0M75-DE-Prospectus-e75278cd-000026 | même document (6, 4) |
| lot1 | S3 | LOT1-LU1159239190-DE-Prospectus-3c88f629-000476 (E1) | 8 | LOT1-LU1159239190-DE-Prospectus-3c88f629-000741 | même document (8, 4) |
| lot1 | S3 | LOT1-LU1159239190-DE-Prospectus-3c88f629-000772 (E1) | 8 | LOT1-LU1159239190-DE-Prospectus-3c88f629-000905 | même document (8, 5) |
| lot1 | S4 | LOT1-FR0012686350-FR-Rapport-semestriel-4534e5dc-000021 (E1) | 1 | LOT1-FR0012686350-FR-Rapport-semestriel-4534e5dc-000001 | même document (1, 3) |
| lot1 | S4 | LOT1-FR0012686350-FR-Rapport-semestriel-4534e5dc-000009 (E1) | 1 | LOT1-FR0012686350-FR-Rapport-semestriel-4534e5dc-000024 | même document (1, 4) |
| lot1 | S4 | LOT1-IE00BKWQ0M75-UK-Rapport-semestriel-64ef8f3a-000007 (E3) | 4 | LOT1-IE00BKWQ0M75-UK-Rapport-semestriel-64ef8f3a-000060 | même document (4, 3) |
| lot1 | S4 | LOT1-FR0010241059-FR-Rapport-53765f21-000298 (E1) | 6 | LOT1-FR0010241059-FR-Rapport-53765f21-000040 | même document (6, 3) |
| lot1 | S4 | LOT1-IE0032523478-DE-Rapport-semestriel-2f82086c-000004 (E3) | 8 | LOT1-IE0032523478-DE-Rapport-semestriel-2f82086c-003853 | même document (8, 3) |
| lot1 | S4 | LOT1-IE0032523478-DE-Rapport-semestriel-2f82086c-003869 (E4) | 8 | LOT1-IE0032523478-DE-Rapport-semestriel-2f82086c-003878 | même document (8, 4) |
| lot2 | S1 | LOT2-IE00BZ163L38-ES-KID-fb775f4b-000006 (E1) | 3 | LOT2-IE00BZ163L38-ES-KID-fb775f4b-000016 | même document (3, 3) |
| lot2 | S1 | LOT2-IE00BZ163H91-FR-KID-67f25750-000012 (E1) | 4 | LOT2-IE00BZ163H91-FR-KID-67f25750-000017 | même document (4, 4) |
| lot2 | S1 | LOT2-FR0013532363-FR-KID-68889a53-000011 (E1) | 8 | LOT2-FR0013532363-FR-KID-68889a53-000017 | même document (8, 3) |
| lot2 | S2 | LOT2-DE0009770206-DE-Factsheet-e6a5d01d-000018 (E4) | 1 | LOT2-DE0009770206-DE-Factsheet-e6a5d01d-000050 | même document (1, 3) |
| lot2 | S2 | LOT2-IE00BZ163L38-CH-Factsheet-ca121140-000010 (E2) | 2 | LOT2-IE00BZ163L38-CH-Factsheet-ca121140-000016 | même document (2, 3) |
| lot2 | S2 | LOT2-FR001400S0F2-FR-Factsheet-ca3efed4-000011 (E1) | 3 | LOT2-FR001400S0F2-FR-Factsheet-ca3efed4-000004 | même document (3, 3) |
| lot2 | S2 | LOT2-FR0010389254-FR-Factsheet-23f0bc27-000016 (E2) | 7 | LOT2-FR0010389254-FR-Factsheet-23f0bc27-000051 | même document (7, 3) |
| lot2 | S2 | LOT2-FR0010389254-FR-Factsheet-23f0bc27-000030 (E2) | 7 | LOT2-FR0010389254-FR-Factsheet-23f0bc27-000063 | même document (7, 5) |
| lot2 | S2 | LOT2-ES0165143001-ES-Factsheet-129b3735-000011 (E2) | 8 | LOT2-ES0165143001-ES-Factsheet-129b3735-000006 | même document (8, 4) |
| lot2 | S2 | LOT2-FR0007468830-FR-Factsheet-a5a6a818-000015 (E1) | 12 | LOT2-FR0007468830-FR-Factsheet-a5a6a818-000002 | même document (12, 3) |
| lot2 | S3 | LOT2-DE000A0M98N2-DE-Prospectus-305d50ec-000259 (E1) | 6 | LOT2-DE000A0M98N2-DE-Prospectus-305d50ec-000021 | même document (6, 3) |
| lot2 | S3 | LOT2-FR0011422427-FR-Prospectus-a4dd8fc9-000236 (E1) | 11 | LOT2-FR0011422427-FR-Prospectus-a4dd8fc9-000196 | même document (11, 3) |
| lot2 | S3 | LOT2-FR001400MEI9-FR-Prospectus-d1d0892c-000220 (E2) | 12 | LOT2-FR001400MEI9-FR-Prospectus-d1d0892c-000230 | même document (12, 3) |
| lot2 | S4 | LOT2-FR0007016712-FR-Rapport-5470aba3-000349 (E2) | 2 | LOT2-FR0007016712-FR-Rapport-5470aba3-000110 | même document (2, 3) |
| lot2 | S4 | LOT2-ES0165143001-ES-Rapport-8f788e58-000021 (E2) | 3 | LOT2-ES0165143001-ES-Rapport-8f788e58-000337 | même document (3, 3) |
| lot2 | S4 | LOT2-FR0010730630-FR-Rapport-19070631-000010 (E2) | 4 | LOT2-FR0010730630-FR-Rapport-19070631-000012 | même document (4, 3) |
| lot2 | S4 | LOT2-DE0009770206-IT-Rapport-b5854258-000012 (E3) | 7 | LOT2-DE0009770206-IT-Rapport-b5854258-000364 | même document (7, 3) |
| lot2 | S4 | LOT2-DE0007483612-DE-Rapport-07efc82f-000160 (E2) | 8 | LOT2-DE0007483612-DE-Rapport-07efc82f-000009 | même document (8, 3) |

Segments principaux écartés non remplacés :

- lot1 S3 : LOT1-LU0297942194-CH-Prospectus-dab44aab-000171 (document de rang 1) — réserves du document et de la strate épuisées ; manque consigné.
- lot1 S3 : LOT1-LU0138981039-FR-Prospectus-4e4a5ec4-000017 (document de rang 2) — réserves du document et de la strate épuisées ; manque consigné.
- lot1 S3 : LOT1-LU0138981039-FR-Prospectus-4e4a5ec4-000026 (document de rang 2) — réserves du document et de la strate épuisées ; manque consigné.
- lot1 S3 : LOT1-LU0224105477-FR-Prospectus-9f8a5429-001276 (document de rang 3) — réserves du document et de la strate épuisées ; manque consigné.
- lot1 S3 : LOT1-IE00BKWQ0M75-DE-Prospectus-e75278cd-000177 (document de rang 6) — réserves du document et de la strate épuisées ; manque consigné.
- lot1 S4 : LOT1-LU0224105477-FR-Rapport-c403beec-002842 (document de rang 2) — réserves du document et de la strate épuisées ; manque consigné.
- lot1 S4 : LOT1-LU0224105477-FR-Rapport-c403beec-004089 (document de rang 2) — réserves du document et de la strate épuisées ; manque consigné.

## 3. Taux d'écart par strate et par motif (toutes les lignes évaluées, réserves comprises)

| Lot | Strate | Lignes évaluées | Écartées | Taux | E1 | E2 | E3 | E4 | E5 |
|---|---|---|---|---|---|---|---|---|---|
| lot1 | S1 | 55 | 16 | 29.1 % | 9 (16.4 %) | 7 (12.7 %) | 0 (0.0 %) | 0 (0.0 %) | 0 (0.0 %) |
| lot1 | S2 | 35 | 3 | 8.6 % | 2 (5.7 %) | 1 (2.9 %) | 0 (0.0 %) | 0 (0.0 %) | 0 (0.0 %) |
| lot1 | S3 | 45 | 20 | 44.4 % | 19 (42.2 %) | 0 (0.0 %) | 1 (2.2 %) | 0 (0.0 %) | 0 (0.0 %) |
| lot1 | S4 | 45 | 14 | 31.1 % | 6 (13.3 %) | 0 (0.0 %) | 2 (4.4 %) | 6 (13.3 %) | 0 (0.0 %) |
| lot2 | S1 | 75 | 6 | 8.0 % | 5 (6.7 %) | 1 (1.3 %) | 0 (0.0 %) | 0 (0.0 %) | 0 (0.0 %) |
| lot2 | S2 | 65 | 17 | 26.2 % | 5 (7.7 %) | 11 (16.9 %) | 0 (0.0 %) | 1 (1.5 %) | 0 (0.0 %) |
| lot2 | S3 | 85 | 6 | 7.1 % | 3 (3.5 %) | 2 (2.4 %) | 1 (1.2 %) | 0 (0.0 %) | 0 (0.0 %) |
| lot2 | S4 | 73 | 13 | 17.8 % | 1 (1.4 %) | 7 (9.6 %) | 1 (1.4 %) | 4 (5.5 %) | 0 (0.0 %) |
| **Total** | | 478 | 95 | 19.9 % | 50 (10.5 %) | 29 (6.1 %) | 5 (1.0 %) | 11 (2.3 %) | 0 (0.0 %) |

Critères des segments retenus : R1 (phrase) 296, R2 (libellé et valeur) 69, R3 (identification) 18.

## 4. Cas douteux (41, tous retenus)

| segment_id | Lot | Strate | Critère | Note |
|---|---|---|---|---|
| LOT1-LU0138981039-HK-Fiche_locale-90211555-000046 | lot1 | S1 | R1 | Fragment coupé au début (suite du titre), mais plus de cinq mots lisibles ; retenu par prudence. |
| LOT1-IE00BKWQ0M75-UK-Factsheet-0b2522d8-000004 | lot1 | S2 | R2 | Texte rédigé à gauche juxtaposé à un tableau libellé-valeur à droite ; pas deux textes rédigés, retenu. |
| LOT1-IE00BKWQ0M75-UK-Factsheet-0b2522d8-000009 | lot1 | S2 | R2 | Deux tableaux juxtaposés (performances et positions) ; lignes libellé-valeur lisibles, retenu par prudence. |
| LOT1-LU0297942194-FR-Factsheet-0c9e8b88-000010 | lot1 | S2 | R1 | Liste de positions, mais contient une phrase et un total libellé ; retenu selon l'ordre des critères. |
| LOT1-LU0297942194-FR-Factsheet-0c9e8b88-000002 | lot1 | S2 | R2 | Texte rédigé à gauche juxtaposé à des caractéristiques libellé-valeur à droite ; pas deux textes rédigés, retenu. |
| LOT1-LU0224105477-CH-Factsheet-69a96578-000004 | lot1 | S2 | R2 | Texte rédigé à gauche juxtaposé à des caractéristiques libellé-valeur à droite ; pas deux textes rédigés, retenu. |
| LOT1-IE0032523478-DE-Factsheet-a942093a-000002 | lot1 | S2 | R2 | Texte rédigé à gauche juxtaposé à des caractéristiques libellé-valeur à droite ; pas deux textes rédigés, retenu. |
| LOT1-IE00B66F4759-DE-Factsheet-13cce8fa-000003 | lot1 | S2 | R1 | Début de phrase coupé (suite du titre), fin complète, plus de cinq mots ; retenu par prudence. |
| LOT1-LU1159239190-CH-Factsheet-35487d39-000009 | lot1 | S2 | R2 | Deux tableaux juxtaposés (performances et ratios) ; lignes libellé-valeur lisibles, retenu par prudence. |
| LOT1-LU1159239190-CH-Factsheet-35487d39-000014 | lot1 | S2 | R2 | Texte rédigé à gauche juxtaposé à un tableau sectoriel libellé-valeur à droite ; retenu par prudence. |
| LOT1-LU0297942194-CH-Prospectus-dab44aab-002076 | lot1 | S3 | R2 | Liste pays et dépositaire sur deux paires de colonnes ; lecture libellé-valeur possible, retenu par prudence. |
| LOT1-LU0224105477-FR-Prospectus-9f8a5429-001920 | lot1 | S3 | R2 | Deux lignes de barème juxtaposées, valeurs rattachées au libellé « Catégorie C » ; retenu par prudence. |
| LOT1-FR0012686350-FR-Rapport-semestriel-4534e5dc-000018 | lot1 | S4 | R1 | Deux bouts de phrases sans lien apparent, dont un de plus de cinq mots ; retenu par prudence. |
| LOT1-LU0064964074-CH-Rapport-annuel-be094d27-000060 | lot1 | S4 | R2 | Restes de graphique ; un indice est suivi d'une valeur, lecture libellé-valeur possible ; retenu par prudence. |
| LOT1-LU0064964074-CH-Rapport-annuel-be094d27-000576 | lot1 | S4 | R1 | Texte rédigé à gauche juxtaposé à une liste de positions chiffrée à droite ; pas deux textes rédigés, retenu. |
| LOT1-FR0010241059-FR-Rapport-53765f21-000040 | lot1 | S4 | R1 | Texte rédigé à gauche juxtaposé à un tableau de mouvements chiffré à droite ; pas deux textes rédigés, retenu. |
| LOT1-LU1159239190-DE-Rapport-9fca8b91-001489 | lot1 | S4 | R1 | Ligne de tableau à gauche juxtaposée à un commentaire rédigé à droite ; pas deux textes rédigés, retenu. |
| LOT2-DE000A0M98N2-DE-KID-853c96db-000030 | lot2 | S1 | R1 | Titre de section formulé en question ; R1 couvre les questions compréhensibles, retenu. |
| LOT2-DE0009770206-DE-Factsheet-e6a5d01d-000050 | lot2 | S2 | R1 | Nom de société puis début de phrase coupé de plus de cinq mots ; retenu par prudence. |
| LOT2-IE00BZ163L38-CH-Factsheet-ca121140-000008 | lot2 | S2 | R3 | Ligne de codes de cotation sans libellés (ticker, SEDOL) ; identifie la cotation, retenu par prudence. |
| LOT2-FR001400S0F2-FR-Factsheet-ca3efed4-000008 | lot2 | S2 | R2 | Surtout des noms de titres en colonnes, mais contient des mentions libellé-valeur (note ESG) ; retenu. |
| LOT2-IE00BZ163K21-CH-Factsheet-b69a423e-000017 | lot2 | S2 | R2 | Valeurs rattachées au libellé « Vergleichsindex », mais périodes des colonnes absentes du segment ; retenu par prudence. |
| LOT2-IE00BZ163K21-CH-Factsheet-b69a423e-000021 | lot2 | S2 | R2 | Valeurs rattachées aux libellés fonds et indice, mais années des colonnes absentes du segment ; retenu par prudence. |
| LOT2-IE00BZ163H91-CH-Factsheet-ec0396e1-000017 | lot2 | S2 | R2 | Valeurs rattachées au libellé « Vergleichsindex », mais périodes des colonnes absentes du segment ; retenu par prudence. |
| LOT2-FR0013532363-FR-Factsheet-55bad07b-000038 | lot2 | S2 | R1 | En-têtes de colonnes mêlés à une seule phrase rédigée (élément de liste) ; pas deux textes, retenu. |
| LOT2-FR0013532363-FR-Factsheet-55bad07b-000005 | lot2 | S2 | R2 | Restes de graphique et indicateurs de risque désordonnés ; valeurs rattachables au fonds et aux libellés, retenu par prudence. |
| LOT2-DE000A0M98N2-DE-Factsheet-6fd11424-000016 | lot2 | S2 | R1 | Slogan en capitales aux mots coupés par des espaces parasites ; énoncé reconstituable, retenu par prudence. |
| LOT2-FR0007468830-FR-Factsheet-a5a6a818-000002 | lot2 | S2 | R2 | Données clés libellé-valeur juxtaposées à un texte d'objectif rédigé ; pas deux textes rédigés, retenu. |
| LOT2-LU0599613147-IT-Factsheet-4c6ae5ba-000004 | lot2 | S2 | R1 | Phrase rédigée juxtaposée à un tableau de données libellé-valeur ; pas deux textes rédigés, retenu. |
| LOT2-IE00BZ163H91-ES-Prospectus-02d06502-004511 | lot2 | S3 | R1 | Élément numéroté d'une liste d'annexe, proche d'un intitulé ; élément de liste rédigé, retenu par prudence. |
| LOT2-DE000A0M98N2-DE-Prospectus-305d50ec-000436 | lot2 | S3 | R1 | Fragment coupé aux deux bouts mais plus de cinq mots d'un tenant, plus un mot isolé ; retenu par prudence. |
| LOT2-DE000A0M98N2-DE-Prospectus-305d50ec-000465 | lot2 | S3 | R1 | Élément de liste coupé par un intitulé de paragraphe intercalé ; un seul texte rédigé, retenu par prudence. |
| LOT2-DE0009770206-IT-Prospectus-0878c7bf-000462 | lot2 | S3 | R1 | Ligne numérotée proche d'un intitulé de section ; peut être un élément de liste, retenu par prudence. |
| LOT2-FR0013532363-FR-Rapport-41430957-000098 | lot2 | S4 | R1 | Deux éléments de liste de deux mots ; éléments de liste, pas un fragment coupé, retenu par prudence. |
| LOT2-FR0007016712-FR-Rapport-5470aba3-000274 | lot2 | S4 | R2 | Valeurs « Néant » rattachées au libellé « Passif », colonnes absentes du segment ; retenu par prudence. |
| LOT2-ES0165143001-ES-Rapport-8f788e58-000177 | lot2 | S4 | R3 | Titre courant d'état financier, mais il nomme le fonds ; R3 prime sur E3, retenu. |
| LOT2-DE0009770206-IT-Rapport-b5854258-000050 | lot2 | S4 | R3 | Restes de graphique aux lettres doublées ; le nom de la part reste reconnaissable, retenu par prudence. |
| LOT2-DE000A0M98N2-DE-Rapport-2e078ef2-000129 | lot2 | S4 | R2 | Valeurs rattachées au libellé « über 10 Jahre », en-têtes de colonnes absents du segment ; retenu par prudence. |
| LOT2-FR0000934325-FR-Rapport-8b48b254-000002 | lot2 | S4 | R1 | Valeur de classification seule, son libellé est dans le titre de section ; groupe nominal compréhensible, retenu. |
| LOT2-FR0011513563-FR-Bulletin_trimestriel-64308ad4-000030 | lot2 | S4 | R2 | Tableau de frais libellé-valeur à gauche juxtaposé à un commentaire rédigé à droite ; pas deux textes rédigés, retenu. |
| LOT2-FR0011513563-FR-Bulletin_trimestriel-64308ad4-000025 | lot2 | S4 | R1 | Texte rédigé à gauche juxtaposé à une ventilation par pays libellé-valeur à droite ; pas deux textes rédigés, retenu. |

## 5. Auto-contrôle (section 6)

### 5.1 Constance du tri

Échantillon : 40 lignes tirées parmi les 478 triées par segment_id, générateur `random.Random("2026-recontrole-lisibilite")`, mélange `rng.shuffle` de la liste triée (même méthode que tirage_script.py) puis les 40 premières lignes du mélange. Réévaluation à l'aveugle (sans la première décision) à partir de `lisibilite_travail/recontrole_entree.csv`.

Organisation : la réévaluation a été faite par un relecteur distinct, qui n'a vu que `recontrole_entree.csv` (texte du segment, voisins, type, langue, titre) et les critères de la mission, sans aucune décision, critère ni note de la première passe. Il a appliqué E1 au sens littéral (colonnes sur les mêmes lignes seulement) et, quand plusieurs conditions de maintien étaient remplies, a noté la première dans l'ordre R1 > R2 > R3. Ses décisions sont dans `recontrole_lisibilite.csv`, à côté de celles de la première passe. Aucune décision de première passe, aucun remplacement ni aucun paquet n'a été modifié à la suite de la relecture.

- Décisions identiques (retenu / écarté) : **39 sur 40**.
- Critères identiques : **38 sur 40**.

| segment_id | Première passe | Relecture | Explication |
|---|---|---|---|
| LOT1-LU1159239190-DE-KID-0119d56d-000007 | écarté (E1) | retenu (R1) | Lecture étendue de E1 en première passe (colonnes en lignes alternées, colonne de droite renvoyée à la ligne) ; la relecture applique E1 au sens littéral (mêmes lignes seulement) et retient la phrase reconstituable. |
| LOT1-IE00BKWQ0M75-UK-Factsheet-0b2522d8-000009 | retenu (R2) | retenu (R1) | Même décision (retenu) ; seul le critère diffère : la première passe note le critère le plus caractéristique (tableaux libellé-valeur), la relecture note le premier critère rempli dans l'ordre R1 > R2 > R3 (une phrase de note de bas de page est présente). |

### 5.2 Contrôles de cohérence

- aucun segment_id utilisé deux fois (jeu final et remplacements) : OK — 159 segments dans le jeu final, 159 distincts ; 33 remplaçants distincts
- aucun segment écarté dans les paquets de codage : OK — 0 écarté(s) trouvé(s)
- lignes des paquets = effectifs finaux du compte rendu : OK — lot1 : 63 lignes, effectif final 63 ; lot2 : 96 lignes, effectif final 96
- chaque id_codage figure dans correspondance.csv : OK — 159 id_codage, 159 lignes de correspondance
- controle_lisibilite.csv couvre les 478 lignes du tirage : OK — 478 lignes
- aucune colonne interdite dans les paquets : OK — colonnes : id_codage, type_document, langue_origine, titre_section, texte_affichage, segment_precedent, segment_suivant, texte_original, texte_en, statut_en
- textes des paquets identiques au tirage (aucune modification) : OK
- recontrole_entree.csv sans décision, critère ni note : OK — 40 lignes, colonnes : segment_id, type_document, langue_origine, titre_section, texte_affichage, texte_original, segment_precedent, segment_suivant

## 6. Anomalies

- **Lecture étendue de E1.** En première passe, E1 couvre aussi les colonnes en lignes alternées (colonne de droite renvoyée à la ligne, lisible dans `texte_original`), et pas seulement deux colonnes sur les mêmes lignes. Le recontrôle montre que cette lecture fait diverger une décision sur 40 (LOT1-LU1159239190-DE-KID-0119d56d-000007, écarté en première passe, retenu en lecture littérale). Les 50 décisions E1 de la première passe sont maintenues telles quelles ; si la lecture littérale est préférée, les segments E1 en lignes alternées seraient à revoir, ce qui modifierait les remplacements.
- **Notation du critère de maintien.** La première passe note le critère le plus caractéristique ; la relecture note le premier dans l'ordre R1 > R2 > R3. Cela explique l'écart de critère sans écart de décision (une ligne sur 40). La répartition R1 / R2 / R3 du point 3 dépend donc de cette convention.
- **Manques au lot 1, S3 et S4.** Ces deux strates n'ont aucun document de réserve (tirage v3) : 5 segments principaux écartés en S3 et 2 en S4 n'ont pu être remplacés une fois les réserves de leur document épuisées. Avec les manques déjà présents au tirage (S2 : 6, S3 : 2, S4 : 2), le lot 1 compte 63 segments sur 80. Rien n'a été complété.
- **Cas douteux.** 41 segments retenus avec une note ; la plupart sont des textes rédigés juxtaposés à un tableau libellé-valeur ou à une liste chiffrée, que la première passe ne classe pas en E1 (une seule colonne rédigée).
- Aucune autre anomalie : contrôles de cohérence tous conformes, fichiers livrés inchangés.
