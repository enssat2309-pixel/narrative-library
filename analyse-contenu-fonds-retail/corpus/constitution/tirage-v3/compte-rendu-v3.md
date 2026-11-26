# Compte rendu — tirage v3 (ajustement du 17/11/2026)

Rédigé le 17/11/2026 21:57 (heure d'Europe/Luxembourg). Seuls changements par rapport à la v2 : suppression de la règle « 5 espaces consécutifs ou plus » ; ajout des champs `texte_affichage`, `segment_precedent` et `segment_suivant` (lecture seulement). Deux exécutions ont donné des sorties identiques (voir autocontrole.md).

## 1. Segments perimetre_v2 « oui » dans le cadre, v2 → v3

| Lot | Strate | Segments oui v2 | Segments oui v3 | Écart | Unités éligibles (≥ 2 oui) v2 → v3 |
|---|---|---|---|---|---|
| lot1 | S1 (KID, KIID, fiches locales, KFS, PHS) | 334 | 802 | +468 | 29 → 29 |
| lot1 | S2 (factsheets) | 66 | 212 | +146 | 13 → 13 |
| lot1 | S3 (prospectus) | 4550 | 17606 | +13056 | 20 → 20 |
| lot1 | S4 (rapports et bulletins) | 2190 | 19256 | +17066 | 25 → 25 |
| lot2 | S1 (KID, KIID, fiches locales, KFS, PHS) | 431 | 856 | +425 | 31 → 34 |
| lot2 | S2 (factsheets) | 339 | 925 | +586 | 23 → 23 |
| lot2 | S3 (prospectus) | 7864 | 11799 | +3935 | 26 → 26 |
| lot2 | S4 (rapports et bulletins) | 1064 | 3124 | +2060 | 21 → 23 |
| **Total** | | 16838 | 54580 | +37742 | |

## 2. Écarts à la cible, v2 → v3

Cible du tirage principal : 10 documents et 20 segments par strate (lot 1), 12 documents et 24 segments (lot 2). Réserve : 5 documents par strate, 3 segments de réserve par document principal.

| Lot | Strate | Documents principal v2 / v3 (écart) | Segments principal v2 / v3 (écart) | Documents de réserve v2 / v3 | Segments de réserve des docs principaux v2 / v3 | Documents principaux communs v2-v3 | Segments principaux communs v2-v3 |
|---|---|---|---|---|---|---|---|
| lot1 | S1 | 10 / 10 (0 / 0) | 20 / 20 (0 / 0) | 1 / 1 | 30 / 30 (cible 30 / 30) | 10 | 1 |
| lot1 | S2 | 7 / 7 (-3 / -3) | 13 / 14 (-7 / -6) | 0 / 0 | 7 / 21 (cible 21 / 21) | 7 | 3 |
| lot1 | S3 | 9 / 9 (-1 / -1) | 18 / 18 (-2 / -2) | 0 / 0 | 27 / 27 (cible 27 / 27) | 9 | 0 |
| lot1 | S4 | 9 / 9 (-1 / -1) | 18 / 18 (-2 / -2) | 0 / 0 | 27 / 27 (cible 27 / 27) | 9 | 1 |
| lot2 | S1 | 12 / 12 (0 / 0) | 24 / 24 (0 / 0) | 3 / 3 | 36 / 36 (cible 36 / 36) | 9 | 1 |
| lot2 | S2 | 12 / 12 (0 / 0) | 24 / 24 (0 / 0) | 1 / 1 | 31 / 36 (cible 36 / 36) | 12 | 1 |
| lot2 | S3 | 12 / 12 (0 / 0) | 24 / 24 (0 / 0) | 5 / 5 | 36 / 36 (cible 36 / 36) | 12 | 0 |
| lot2 | S4 | 12 / 12 (0 / 0) | 24 / 24 (0 / 0) | 3 / 3 | 32 / 36 (cible 36 / 36) | 8 | 1 |

Les écarts en documents du lot 1 sont inchangés : ils viennent du nombre de fonds collectés, avec un document par fonds et par strate, et ont déjà été acceptés. Les documents principaux changent seulement en lot 2 S1 et S4, où des unités deviennent éligibles (au moins 2 segments « oui »). Ailleurs, les documents sont les mêmes, mais les segments tirés changent presque tous, parce que la liste des segments « oui » à mélanger a changé.

## 3. Segments du tirage principal par règle de périmètre (v3, 166 segments)

| Règle | v3 | v2 |
|---|---|---|
| type toujours inclus (KID, fiche locale, factsheet, bulletin) | 82 | 83 |
| prospectus : partie générale | 15 | 14 |
| rapport : performance | 15 | 14 |
| rapport : section non classée, gardée (cas non tranché) | 13 | 11 |
| prospectus : section propre au fonds (ISIN dans le titre) | 9 | 10 |
| rapport : commentaire de gestion | 7 | 8 |
| rapport : frais effectifs (titre complet) | 7 | 7 |
| prospectus : section propre au fonds (nom dans le titre) | 6 | 6 |
| prospectus : partie générale (fin d'annexe-liste, titre en haut de page) | 5 | 5 |
| prospectus : partie générale (retour sur un intitulé d'annexe en haut de page) | 5 | 3 |
| prospectus : autre compartiment → oui, cas non tranché (section propre au fonds non repérée) | 2 | 4 |

## 4. Segments principaux avec une suite de 5 espaces ou plus

97 segments principaux sur 166 ont, dans `texte_original`, une suite de 5 blancs ou plus. On compte comme blancs l'espace, l'espace insécable, les autres espaces Unicode et la tabulation, mais pas le saut de ligne. Par strate : lot1 S1 : 9 ; lot1 S2 : 9 ; lot1 S3 : 13 ; lot1 S4 : 10 ; lot2 S1 : 12 ; lot2 S2 : 20 ; lot2 S3 : 10 ; lot2 S4 : 14. Sur l'ensemble des 478 lignes (réserves comprises), 249 segments sont concernés. Pour eux, `texte_affichage` remplace ces suites par «  |  ».

## 5. Effet de l'ordre des règles

Sur les segments que la v2 excluait par « 5 espaces », 48119 au total (42844 dans le cadre), 11868 ont maintenant la règle « rapport : performance », 6393 ont maintenant la règle « prospectus : partie générale (retour sur un intitulé d'annexe en haut de page) », 5963 ont maintenant la règle « exclusion générale : texte identique à un segment déjà retenu dans l'unité », 4724 ont maintenant la règle « rapport : section non classée, gardée (cas non tranché) ». Les autres règles sont détaillées dans journal_tirage.md, section 9. Par ricochet, 41 segments qui étaient « oui » en v2 deviennent « texte identique ».

## 6. Anomalies

- Aucune anomalie bloquante. Aucune strate n'a été complétée à la main. Les écarts à la cible restants sont listés au point 2 et dans le journal (section 6).
- En lot 2 S4, le document LOT2-FR0000934325-FR-Rapport-8b48b254 n'a toujours que 3 segments, sur les 5 visés avec la réserve (2 en v2). Les autres manques de segments de la v2 (factsheets du lot 1 et du lot 2) sont comblés.
- 5963 anciens segments « 5 espaces » deviennent des doublons (« texte identique »). Ils restent exclus.
- 97 des 166 segments principaux contiennent une suite de 5 blancs ou plus (texte en colonnes). C'est l'effet attendu de la suppression de la règle ; `texte_affichage` les rend lisibles sans changer `texte_original`.
- `segment_precedent` est vide sur 13 lignes et `segment_suivant` sur 12. Dans tous les cas, c'est le premier ou le dernier segment du document. Aucun voisin n'a été coupé par la limite des unités Colville.
