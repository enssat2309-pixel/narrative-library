# Entonnoir du cadre de tirage — mission 3, version 3 (ajustement v3 du 17/11/2026)

Effectifs à chaque étape, par lot et par strate. Unités documentaires = fichiers uniques (sha256) parmi les lignes « collecté » du manifeste ; les segments sont comptés une seule fois par unité (segments de la ligne de référence). « Règle appliquée » = première règle qui décide du segment ; « déclenchements bruts » = nombre de segments qui remplissent chaque critère d'exclusion générale, même si une autre règle a décidé avant (non exclusifs).


## lot1 — S1 (Fiche_locale, KID)

| Étape | Effectif |
|---|---|
| Lignes « collecté » du manifeste | 29 |
| Unités documentaires (sha256 uniques) | 29 |
| Exclues du cadre (total, un document peut avoir plusieurs motifs) | 0 |
| Unités dans le cadre | 29 |
| Unités dans le cadre avec ≥ 2 segments perimetre_v2 « oui » (éligibles au temps 1) | 29 |
| Segments totaux (toutes unités) | 816 |
| Segments perimetre (ancien) « oui » (toutes unités) | 816 |
| Segments perimetre_v2 « oui » (toutes unités) | 802 |
| Segments totaux (unités dans le cadre) | 816 |
| Segments perimetre (ancien) « oui » (unités dans le cadre) | 816 |
| Segments perimetre_v2 « oui » (unités dans le cadre) | 802 |

Segments par règle appliquée (toutes unités de la strate) :

| perimetre_v2 | Règle appliquée | Segments |
|---|---|---|
| oui | type toujours inclus (KID, fiche locale, factsheet, bulletin) | 802 |
| non | exclusion générale : chiffres > moitié des caractères non blancs | 10 |
| non | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 4 |

Déclenchements bruts des exclusions générales (non exclusifs) :

| Critère | Segments |
|---|---|
| exclusion générale : chiffres > moitié des caractères non blancs | 10 |
| exclusion générale : moins de 4 mots | 0 |

## lot1 — S2 (Factsheet)

| Étape | Effectif |
|---|---|
| Lignes « collecté » du manifeste | 20 |
| Unités documentaires (sha256 uniques) | 20 |
| Exclues du cadre — mention de réserve aux professionnels (reserve_professionnels = oui) | 5 |
| Exclues du cadre — paire d'avis (flux séparé) | 2 |
| Exclues du cadre (total, un document peut avoir plusieurs motifs) | 7 |
| Unités dans le cadre | 13 |
| Unités dans le cadre avec ≥ 2 segments perimetre_v2 « oui » (éligibles au temps 1) | 13 |
| Segments totaux (toutes unités) | 430 |
| Segments perimetre (ancien) « oui » (toutes unités) | 430 |
| Segments perimetre_v2 « oui » (toutes unités) | 380 |
| Segments totaux (unités dans le cadre) | 241 |
| Segments perimetre (ancien) « oui » (unités dans le cadre) | 241 |
| Segments perimetre_v2 « oui » (unités dans le cadre) | 212 |

Segments par règle appliquée (toutes unités de la strate) :

| perimetre_v2 | Règle appliquée | Segments |
|---|---|---|
| oui | type toujours inclus (KID, fiche locale, factsheet, bulletin) | 380 |
| non | exclusion générale : chiffres > moitié des caractères non blancs | 40 |
| non | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 10 |

Déclenchements bruts des exclusions générales (non exclusifs) :

| Critère | Segments |
|---|---|
| exclusion générale : chiffres > moitié des caractères non blancs | 40 |
| exclusion générale : moins de 4 mots | 0 |

## lot1 — S3 (Prospectus)

| Étape | Effectif |
|---|---|
| Lignes « collecté » du manifeste | 27 |
| Unités documentaires (sha256 uniques) | 20 |
| Exclues du cadre (total, un document peut avoir plusieurs motifs) | 0 |
| Unités dans le cadre | 20 |
| Unités dans le cadre avec ≥ 2 segments perimetre_v2 « oui » (éligibles au temps 1) | 20 |
| Segments totaux (toutes unités) | 84134 |
| Segments perimetre (ancien) « oui » (toutes unités) | 75029 |
| Segments perimetre_v2 « oui » (toutes unités) | 17606 |
| Segments totaux (unités dans le cadre) | 84134 |
| Segments perimetre (ancien) « oui » (unités dans le cadre) | 75029 |
| Segments perimetre_v2 « oui » (unités dans le cadre) | 17606 |

Segments par règle appliquée (toutes unités de la strate) :

| perimetre_v2 | Règle appliquée | Segments |
|---|---|---|
| non | annexe SFDR (titre : « Annexe SFDR ») | 24370 |
| non | annexe SFDR (texte : « Legal entity identifier ») | 22367 |
| non | prospectus : autre compartiment | 10892 |
| oui | prospectus : partie générale (retour sur un intitulé d'annexe en haut de page) | 5708 |
| non | annexe SFDR (texte : « Sustainability indicators (encadré du modèle) ») | 5626 |
| oui | prospectus : partie générale | 5272 |
| oui | prospectus : partie générale (fin d'annexe-liste, titre en haut de page) | 3425 |
| oui | prospectus : autre compartiment → oui, cas non tranché (section propre au fonds non repérée) | 3066 |
| non | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 1218 |
| non | annexe SFDR (titre : « Product name ») | 704 |
| non | annexe SFDR (titre : « Sustainability indicators (encadré du modèle) ») | 592 |
| non | annexe SFDR (titre : « Legal entity identifier ») | 434 |
| oui | prospectus : section propre au fonds (nom dans le titre) | 135 |
| non | prospectus : annexe qui est une simple liste (sub-custodian) | 125 |
| non | annexe SFDR (texte : « Modèle d'informations précontractuelles / périodiques (article 8 ou 9) ») | 89 |
| non | prospectus : annexe qui est une simple liste (sous-dépositaires) | 48 |
| non | prospectus : annexe qui est une simple liste (unterverwahrer) | 33 |
| non | prospectus : annexe qui est une simple liste (anschriften) | 11 |
| non | exclusion générale : chiffres > moitié des caractères non blancs | 6 |
| non | prospectus : annexe qui est une simple liste (directory) | 6 |
| non | prospectus : annexe qui est une simple liste (liste des compartiments) | 5 |
| non | prospectus : annexe qui est une simple liste (list of funds) | 2 |

Déclenchements bruts des exclusions générales (non exclusifs) :

| Critère | Segments |
|---|---|
| exclusion générale : chiffres > moitié des caractères non blancs | 10 |
| exclusion générale : moins de 4 mots | 2 |

## lot1 — S4 (Rapport)

| Étape | Effectif |
|---|---|
| Lignes « collecté » du manifeste | 48 |
| Unités documentaires (sha256 uniques) | 38 |
| Exclues du cadre — paire d'avis (flux séparé) | 13 |
| Exclues du cadre (total, un document peut avoir plusieurs motifs) | 13 |
| Unités dans le cadre | 25 |
| Unités dans le cadre avec ≥ 2 segments perimetre_v2 « oui » (éligibles au temps 1) | 25 |
| Segments totaux (toutes unités) | 122332 |
| Segments perimetre (ancien) « oui » (toutes unités) | 95026 |
| Segments perimetre_v2 « oui » (toutes unités) | 21704 |
| Segments totaux (unités dans le cadre) | 119393 |
| Segments perimetre (ancien) « oui » (unités dans le cadre) | 92164 |
| Segments perimetre_v2 « oui » (unités dans le cadre) | 19256 |

Segments par règle appliquée (toutes unités de la strate) :

| perimetre_v2 | Règle appliquée | Segments |
|---|---|---|
| non | rapport : états financiers et notes | 26769 |
| non | annexe SFDR (texte : « Modèle d'informations précontractuelles / périodiques (article 8 ou 9) ») | 24410 |
| non | rapport : liste de positions / titres en portefeuille | 22122 |
| oui | rapport : performance | 12793 |
| non | annexe SFDR (texte : « Legal entity identifier ») | 11325 |
| non | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 7480 |
| oui | rapport : section non classée, gardée (cas non tranché) | 5132 |
| non | exclusion générale : chiffres > moitié des caractères non blancs | 3441 |
| non | annexe SFDR (titre : « Legal entity identifier ») | 3381 |
| oui | rapport : commentaire de gestion | 2469 |
| oui | rapport : frais effectifs (titre complet) | 1310 |
| non | rapport : rapport d'audit | 696 |
| non | annexe SFDR (titre : « Modèle d'informations précontractuelles / périodiques (article 8 ou 9) ») | 447 |
| non | annexe SFDR (titre : « Annexe SFDR ») | 346 |
| non | annexe SFDR (titre : « Product name ») | 209 |
| non | exclusion générale : moins de 4 mots | 2 |

Déclenchements bruts des exclusions générales (non exclusifs) :

| Critère | Segments |
|---|---|
| exclusion générale : chiffres > moitié des caractères non blancs | 7283 |
| exclusion générale : moins de 4 mots | 2 |

## lot1 — hors strate (Avis)

| Étape | Effectif |
|---|---|
| Lignes « collecté » du manifeste | 45 |
| Unités documentaires (sha256 uniques) | 45 |
| Exclues du cadre — avis (flux séparé) | 45 |
| Exclues du cadre (total, un document peut avoir plusieurs motifs) | 45 |
| Unités dans le cadre | 0 |
| Unités dans le cadre avec ≥ 2 segments perimetre_v2 « oui » (éligibles au temps 1) | 0 |
| Segments totaux (toutes unités) | 419 |
| Segments perimetre (ancien) « oui » (toutes unités) | 419 |
| Segments perimetre_v2 « oui » (toutes unités) | 380 |
| Segments totaux (unités dans le cadre) | 0 |
| Segments perimetre (ancien) « oui » (unités dans le cadre) | 0 |
| Segments perimetre_v2 « oui » (unités dans le cadre) | 0 |

Segments par règle appliquée (toutes unités de la strate) :

| perimetre_v2 | Règle appliquée | Segments |
|---|---|---|
| oui | avis : type non visé par 4.3, gardé (cas non tranché, hors cadre) | 380 |
| non | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 25 |
| non | exclusion générale : chiffres > moitié des caractères non blancs | 12 |
| non | exclusion générale : moins de 4 mots | 2 |

Déclenchements bruts des exclusions générales (non exclusifs) :

| Critère | Segments |
|---|---|
| exclusion générale : chiffres > moitié des caractères non blancs | 12 |
| exclusion générale : moins de 4 mots | 9 |

## lot2 — S1 (KID)

| Étape | Effectif |
|---|---|
| Lignes « collecté » du manifeste | 37 |
| Unités documentaires (sha256 uniques) | 35 |
| Exclues du cadre — KID d'une autre classe de parts | 1 |
| Exclues du cadre (total, un document peut avoir plusieurs motifs) | 1 |
| Unités dans le cadre | 34 |
| Unités dans le cadre avec ≥ 2 segments perimetre_v2 « oui » (éligibles au temps 1) | 34 |
| Segments totaux (toutes unités) | 929 |
| Segments perimetre (ancien) « oui » (toutes unités) | 929 |
| Segments perimetre_v2 « oui » (toutes unités) | 909 |
| Segments totaux (unités dans le cadre) | 862 |
| Segments perimetre (ancien) « oui » (unités dans le cadre) | 862 |
| Segments perimetre_v2 « oui » (unités dans le cadre) | 856 |

Segments par règle appliquée (toutes unités de la strate) :

| perimetre_v2 | Règle appliquée | Segments |
|---|---|---|
| oui | type toujours inclus (KID, fiche locale, factsheet, bulletin) | 909 |
| non | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 15 |
| non | exclusion générale : chiffres > moitié des caractères non blancs | 5 |

Déclenchements bruts des exclusions générales (non exclusifs) :

| Critère | Segments |
|---|---|
| exclusion générale : chiffres > moitié des caractères non blancs | 5 |
| exclusion générale : moins de 4 mots | 0 |

## lot2 — S2 (Factsheet)

| Étape | Effectif |
|---|---|
| Lignes « collecté » du manifeste | 33 |
| Unités documentaires (sha256 uniques) | 32 |
| Exclues du cadre — mention de réserve aux professionnels (reserve_professionnels = oui) | 9 |
| Exclues du cadre (total, un document peut avoir plusieurs motifs) | 9 |
| Unités dans le cadre | 23 |
| Unités dans le cadre avec ≥ 2 segments perimetre_v2 « oui » (éligibles au temps 1) | 23 |
| Segments totaux (toutes unités) | 1250 |
| Segments perimetre (ancien) « oui » (toutes unités) | 1250 |
| Segments perimetre_v2 « oui » (toutes unités) | 1172 |
| Segments totaux (unités dans le cadre) | 991 |
| Segments perimetre (ancien) « oui » (unités dans le cadre) | 991 |
| Segments perimetre_v2 « oui » (unités dans le cadre) | 925 |

Segments par règle appliquée (toutes unités de la strate) :

| perimetre_v2 | Règle appliquée | Segments |
|---|---|---|
| oui | type toujours inclus (KID, fiche locale, factsheet, bulletin) | 1172 |
| non | exclusion générale : chiffres > moitié des caractères non blancs | 49 |
| non | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 28 |
| non | exclusion générale : moins de 4 mots | 1 |

Déclenchements bruts des exclusions générales (non exclusifs) :

| Critère | Segments |
|---|---|
| exclusion générale : chiffres > moitié des caractères non blancs | 49 |
| exclusion générale : moins de 4 mots | 1 |

## lot2 — S3 (Prospectus)

| Étape | Effectif |
|---|---|
| Lignes « collecté » du manifeste | 42 |
| Unités documentaires (sha256 uniques) | 26 |
| Exclues du cadre (total, un document peut avoir plusieurs motifs) | 0 |
| Unités dans le cadre | 26 |
| Unités dans le cadre avec ≥ 2 segments perimetre_v2 « oui » (éligibles au temps 1) | 26 |
| Segments totaux (toutes unités) | 28280 |
| Segments perimetre (ancien) « oui » (toutes unités) | 27603 |
| Segments perimetre_v2 « oui » (toutes unités) | 11799 |
| Segments totaux (unités dans le cadre) | 28280 |
| Segments perimetre (ancien) « oui » (unités dans le cadre) | 27603 |
| Segments perimetre_v2 « oui » (unités dans le cadre) | 11799 |

Segments par règle appliquée (toutes unités de la strate) :

| perimetre_v2 | Règle appliquée | Segments |
|---|---|---|
| non | prospectus : autre compartiment | 7483 |
| oui | prospectus : partie générale | 3599 |
| oui | prospectus : section propre au fonds (nom dans le titre) | 2729 |
| oui | prospectus : partie générale (fin d'annexe-liste, titre en haut de page) | 2653 |
| non | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 2436 |
| non | annexe SFDR (titre : « Product name ») | 2330 |
| non | annexe SFDR (titre : « Annexe SFDR ») | 1736 |
| oui | prospectus : section propre au fonds (ISIN dans le titre) | 1695 |
| oui | prospectus : partie générale (retour sur un intitulé d'annexe en haut de page) | 1123 |
| non | annexe SFDR (texte : « Modèle d'informations précontractuelles / périodiques (article 8 ou 9) ») | 876 |
| non | annexe SFDR (titre : « Sustainability indicators (encadré du modèle) ») | 511 |
| non | annexe SFDR (texte : « Legal entity identifier ») | 476 |
| non | annexe SFDR (titre : « Modèle d'informations précontractuelles / périodiques (article 8 ou 9) ») | 316 |
| non | annexe SFDR (titre : « Legal entity identifier ») | 145 |
| non | annexe SFDR (titre : « Règlement délégué (UE) 2022/1288 ») | 63 |
| non | prospectus : annexe qui est une simple liste (directory) | 57 |
| non | prospectus : annexe qui est une simple liste (sub-custodian) | 23 |
| non | exclusion générale : chiffres > moitié des caractères non blancs | 15 |
| non | prospectus : annexe qui est une simple liste (elenco dei comparti) | 13 |
| non | exclusion générale : moins de 4 mots | 1 |

Déclenchements bruts des exclusions générales (non exclusifs) :

| Critère | Segments |
|---|---|
| exclusion générale : chiffres > moitié des caractères non blancs | 16 |
| exclusion générale : moins de 4 mots | 9 |

## lot2 — S4 (Bulletin_trimestriel, Rapport)

| Étape | Effectif |
|---|---|
| Lignes « collecté » du manifeste | 60 |
| Unités documentaires (sha256 uniques) | 25 |
| Exclues du cadre — fichier tronqué ou texte absent (tronque = oui) | 1 |
| Exclues du cadre (total, un document peut avoir plusieurs motifs) | 1 |
| Unités dans le cadre | 24 |
| Unités dans le cadre avec ≥ 2 segments perimetre_v2 « oui » (éligibles au temps 1) | 23 |
| Segments totaux (toutes unités) | 20370 |
| Segments perimetre (ancien) « oui » (toutes unités) | 11809 |
| Segments perimetre_v2 « oui » (toutes unités) | 3124 |
| Segments totaux (unités dans le cadre) | 20370 |
| Segments perimetre (ancien) « oui » (unités dans le cadre) | 11809 |
| Segments perimetre_v2 « oui » (unités dans le cadre) | 3124 |

Segments par règle appliquée (toutes unités de la strate) :

| perimetre_v2 | Règle appliquée | Segments |
|---|---|---|
| non | rapport : liste de positions / titres en portefeuille | 8501 |
| non | rapport : états financiers et notes | 3620 |
| non | annexe SFDR (texte : « Modèle d'informations précontractuelles / périodiques (article 8 ou 9) ») | 2066 |
| oui | rapport : performance | 1422 |
| non | annexe SFDR (titre : « Sustainability indicators (encadré du modèle) ») | 1052 |
| oui | rapport : frais effectifs (titre complet) | 820 |
| non | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 671 |
| non | annexe SFDR (texte : « Legal entity identifier ») | 623 |
| non | rapport : rapport d'audit | 460 |
| oui | rapport : section non classée, gardée (cas non tranché) | 436 |
| oui | rapport : commentaire de gestion | 409 |
| non | exclusion générale : chiffres > moitié des caractères non blancs | 130 |
| non | annexe SFDR (texte : « Product name ») | 114 |
| oui | type toujours inclus (KID, fiche locale, factsheet, bulletin) | 37 |
| non | annexe SFDR (titre : « Annexe SFDR ») | 8 |
| non | exclusion générale : moins de 4 mots | 1 |

Déclenchements bruts des exclusions générales (non exclusifs) :

| Critère | Segments |
|---|---|
| exclusion générale : chiffres > moitié des caractères non blancs | 946 |
| exclusion générale : moins de 4 mots | 13 |

## annexe_SG — S1 (KID)

| Étape | Effectif |
|---|---|
| Lignes « collecté » du manifeste | 5 |
| Unités documentaires (sha256 uniques) | 5 |
| Exclues du cadre — annexe Singapour (annexe_SG) | 5 |
| Exclues du cadre (total, un document peut avoir plusieurs motifs) | 5 |
| Unités dans le cadre | 0 |
| Unités dans le cadre avec ≥ 2 segments perimetre_v2 « oui » (éligibles au temps 1) | 0 |
| Segments totaux (toutes unités) | 140 |
| Segments perimetre (ancien) « oui » (toutes unités) | 140 |
| Segments perimetre_v2 « oui » (toutes unités) | 140 |
| Segments totaux (unités dans le cadre) | 0 |
| Segments perimetre (ancien) « oui » (unités dans le cadre) | 0 |
| Segments perimetre_v2 « oui » (unités dans le cadre) | 0 |

Segments par règle appliquée (toutes unités de la strate) :

| perimetre_v2 | Règle appliquée | Segments |
|---|---|---|
| oui | type toujours inclus (KID, fiche locale, factsheet, bulletin) | 140 |

Déclenchements bruts des exclusions générales (non exclusifs) :

| Critère | Segments |
|---|---|
| exclusion générale : chiffres > moitié des caractères non blancs | 0 |
| exclusion générale : moins de 4 mots | 0 |

## annexe_SG — S3 (Prospectus)

| Étape | Effectif |
|---|---|
| Lignes « collecté » du manifeste | 5 |
| Unités documentaires (sha256 uniques) | 2 |
| Exclues du cadre — annexe Singapour (annexe_SG) | 2 |
| Exclues du cadre (total, un document peut avoir plusieurs motifs) | 2 |
| Unités dans le cadre | 0 |
| Unités dans le cadre avec ≥ 2 segments perimetre_v2 « oui » (éligibles au temps 1) | 0 |
| Segments totaux (toutes unités) | 18514 |
| Segments perimetre (ancien) « oui » (toutes unités) | 17459 |
| Segments perimetre_v2 « oui » (toutes unités) | 2719 |
| Segments totaux (unités dans le cadre) | 0 |
| Segments perimetre (ancien) « oui » (unités dans le cadre) | 0 |
| Segments perimetre_v2 « oui » (unités dans le cadre) | 0 |

Segments par règle appliquée (toutes unités de la strate) :

| perimetre_v2 | Règle appliquée | Segments |
|---|---|---|
| non | annexe SFDR (titre : « Annexe SFDR ») | 6892 |
| non | annexe SFDR (titre : « Sustainability indicators (encadré du modèle) ») | 5822 |
| non | prospectus : autre compartiment | 1512 |
| oui | prospectus : autre compartiment → oui, cas non tranché (section propre au fonds non repérée) | 1184 |
| oui | prospectus : partie générale (retour sur un intitulé d'annexe en haut de page) | 983 |
| non | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 837 |
| non | annexe SFDR (texte : « Modèle d'informations précontractuelles / périodiques (article 8 ou 9) ») | 700 |
| oui | prospectus : partie générale | 315 |
| oui | prospectus : partie générale (fin d'annexe-liste, titre en haut de page) | 204 |
| oui | prospectus : section propre au fonds (nom dans le titre) | 33 |
| non | prospectus : annexe qui est une simple liste (list of funds) | 17 |
| non | exclusion générale : chiffres > moitié des caractères non blancs | 15 |

Déclenchements bruts des exclusions générales (non exclusifs) :

| Critère | Segments |
|---|---|
| exclusion générale : chiffres > moitié des caractères non blancs | 15 |
| exclusion générale : moins de 4 mots | 0 |
