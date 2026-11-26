# Auto-contrôle avant livraison — mission 3, version 3 (section 7)

Rédigé le 17/11/2026 21:57 (heure d'Europe/Luxembourg).

## 1. Deux exécutions successives

- Exécution 1 : `nice python3 tirage_v3/tirage_script.py /workspace/doc-screener/tirage_v3` (PYTHONHASHSEED=1).
- Exécution 2 : même script, mêmes fichiers d'entrée, PYTHONHASHSEED=777, sortie dans un dossier temporaire hors du projet (`/tmp/tirage_v3_run2`).
- sha256 de tirage_pilote.csv, exécution 1 : `9a250a41140532c7868e0c584cf5005a303017f8e9882aa294a98d0585a26e8e`
- sha256 de tirage_pilote.csv, exécution 2 : `9a250a41140532c7868e0c584cf5005a303017f8e9882aa294a98d0585a26e8e`
- Résultat : identiques ; cadre_documents.csv, segments_perimetre_v2.csv et entonnoir.md identiques octet pour octet : oui. journal_tirage.md ne diffère que par l'heure de production.

## 2. Contrôles

- Aucun segment_id en double : OK (478 lignes, 478 segment_id distincts).
- Aucune unité documentaire tirée deux fois dans une strate : OK (96 unités tirées).
- Aucun document exclu du cadre dans le tirage : OK.
- Aucun segment tiré portant la règle « 5 espaces » : OK ; aucun segment du cadre ne porte plus cette règle : OK.
- Segments de l'unité LOT2-FR0013532363-FR-KID-68889a53-KID tous situés pages 1 à 3 : OK (pages [1, 2]).
- Nouveaux champs : 3 colonnes ajoutées après regle_perimetre_v2 ; `texte_affichage` sans suite de 5 blancs : OK ; texte_original inchangé (les nouveaux champs sont calculés après le tirage).

## 3. Effectifs du tirage principal par strate (cible section 5.1)

| Lot | Strate | Documents principal (cible) | Segments principal (cible) | Documents de réserve (cible 5) | Segments de réserve des docs principaux (cible 3 × docs) |
|---|---|---|---|---|---|
| lot1 | S1 | 10 (10) | 20 (20) | 1 | 30 (30) |
| lot1 | S2 | 7 (10) | 14 (20) | 0 | 21 (21) |
| lot1 | S3 | 9 (10) | 18 (20) | 0 | 27 (27) |
| lot1 | S4 | 9 (10) | 18 (20) | 0 | 27 (27) |
| lot2 | S1 | 12 (12) | 24 (24) | 3 | 36 (36) |
| lot2 | S2 | 12 (12) | 24 (24) | 1 | 36 (36) |
| lot2 | S3 | 12 (12) | 24 (24) | 5 | 36 (36) |
| lot2 | S4 | 12 (12) | 24 (24) | 3 | 36 (36) |

## 4. Explication des écarts

- Écarts en documents du lot 1 identiques à la v1 et à la v2, et acceptés : 14 fonds collectés seulement, avec la règle « un document par fonds et par strate ». S2 perd aussi 5 factsheets réservées aux professionnels et 2 factsheets de paires. Plafond par maison inchangé.
- Segments manquants dans un document : seul LOT2-FR0000934325-FR-Rapport-8b48b254 (lot 2 S4) reste incomplet en réserve (3 segments sur 5). Rien n'a été complété à la main.

## 5. Anomalies

- Aucune anomalie nouvelle (journal, section 8 ; détails dans compte_rendu_v3.md).
