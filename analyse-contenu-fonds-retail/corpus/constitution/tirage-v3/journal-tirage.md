# Journal du tirage — mission 3, version 3 (ajustement v3 du 17/11/2026)

Version 3 : seuls changements par rapport à la v2 livrée dans `tirage_v2/` (non modifiée) : (1) suppression, pour tous les types et toutes les strates, de l'exclusion générale « 5 espaces consécutifs ou plus » ; les segments qu'elle décidait passent aux règles suivantes (« moins de 4 mots », « texte identique », sinon « oui » avec leur règle de structure) ; (2) ajout dans tirage_pilote.csv des champs de lecture `texte_affichage`, `segment_precedent` et `segment_suivant` (section 6 bis), sans effet sur aucun calcul. Toutes les autres règles de la v2 sont inchangées (fichier composite, chiffres > moitié, moins de 4 mots, texte identique, périmètre des prospectus et rapports, annexes SFDR, exclusions du cadre, graines, ordre de tri, un document par fonds et par strate, plafond par maison au plus ceil(0,4 × N), cibles et réserves).
Confirmation : la règle « chiffres > moitié » s'applique au texte_original tel quel ; numérateur = chiffres (str.isdigit), dénominateur = caractères non blancs (tout caractère pour lequel str.isspace est faux : espaces, espaces insécables, autres espaces Unicode, tabulations et sauts de ligne ne comptent pas). C'était déjà le calcul de la v1 et de la v2.

Produit par tirage_script.py le 17/11/2026 21:53 (heure d'Europe/Luxembourg). Aucun accès réseau, aucun téléchargement, aucune traduction ; aucun fichier existant modifié ni supprimé. Aucun segment ni document choisi, retiré, remplacé ou réordonné à la main.

## 1. Fichiers lus (empreintes sha256)

- `corpus/lot1_2026-11-15.zip` : `a32fa2717d5b4763098203c297b39ae459714ef39f9565136e2ac9a73d632cbd`
- `corpus/lot2_2026-11-15.zip` : `16b8421c386bdf9d980400da4677c884210ef7febe3c725a634b7b0556135c6e`
- `corpus/manifeste_lot1_2026-11-15_rectifie.csv` : `8406b06b04c9c774c0ee1ea4d014797b7fc98a2e84a8cea60460ee35c3b0e9b1`
- `corpus/lot2/manifeste_lot2_rectifie.csv` : `9ea24b201173f60917c51e3bcb13384e970253036690920b89cc37933190df77`
- `consolidation/manifeste_complete.csv` : `fa3c69f5692fb447e3aa8e6d9e86f9d66501d947eadd2d21042a233a06de4f68`
- `consolidation/segments.jsonl` : `6fc8d29d4ec4035ad25a08f86789bf479034cfe533408ce2f3d1a492bfd49181`
- `consolidation/corpus.jsonl` : `6f11735fa2f079be931ca0c4b73856182d505e728815ec5f10a5e64125e2c52d`

Manifestes lus dans les archives livrées : `manifeste.csv` (lot 1), `lot2/manifeste_lot2.csv` (lot 2), `lot2/annexe_SG/manifeste_annexe_SG.csv` (annexe Singapour), `lot2/echantillon_lot2.csv` (sociétés de gestion du lot 2).

## 2. Valeurs rectifiées le 16/11 utilisées

Les colonnes `langue_origine` et `indicateur_traduit` sont reprises des manifestes rectifiés du 16/11 (journal `corpus/journal_rectifications_2026-11-16.md`) là où elles diffèrent des manifestes livrés le 15/11 : 66 valeurs sur 58 lignes. Le statut de traduction (`statut_en` du cadre) est le `statut_traduction` de la consolidation, identique à l'indicateur rectifié pour toutes les lignes collectées.

| Lot | Ligne du manifeste | Colonne | Valeur livrée | Valeur rectifiée retenue | Statut de la ligne |
|---|---|---|---|---|---|
| lot1 | LOT1-LU0138981039-FR-Prospectus-4e4a5ec4 | langue_origine | en | fr | collecté |
| lot1 | LOT1-LU0138981039-DE-Prospectus-500d5b56 | langue_origine | en | de | collecté |
| lot1 | LOT1-LU2348335964-DE-Prospectus-500d5b56 | langue_origine | en | de | collecté |
| lot1 | AVIS-001 | langue_origine | fr | es | collecté |
| lot1 | AVIS-002 | langue_origine | fr | es | collecté |
| lot1 | AVIS-003 | langue_origine | fr | es | collecté |
| lot1 | AVIS-004 | langue_origine | en | es | collecté |
| lot1 | AVIS-004 | indicateur_traduit | non | non traduit | collecté |
| lot1 | AVIS-005 | langue_origine | fr | es | collecté |
| lot1 | AVIS-006 | langue_origine | fr | es | collecté |
| lot1 | AVIS-007 | langue_origine | fr | es | collecté |
| lot1 | AVIS-008 | langue_origine | fr | es | collecté |
| lot1 | AVIS-009 | langue_origine | en | es | collecté |
| lot1 | AVIS-009 | indicateur_traduit | non | non traduit | collecté |
| lot1 | AVIS-010 | langue_origine | (vide) | es | collecté |
| lot1 | AVIS-011 | langue_origine | (vide) | es | collecté |
| lot1 | AVIS-012 | langue_origine | (vide) | es | collecté |
| lot1 | AVIS-013 | langue_origine | (vide) | es | collecté |
| lot1 | AVIS-014 | langue_origine | (vide) | es | collecté |
| lot1 | AVIS-015 | langue_origine | (vide) | es | collecté |
| lot1 | AVIS-016 | langue_origine | en | es | collecté |
| lot1 | AVIS-016 | indicateur_traduit | non | non traduit | collecté |
| lot1 | AVIS-017 | langue_origine | en | es | collecté |
| lot1 | AVIS-017 | indicateur_traduit | non | non traduit | collecté |
| lot1 | AVIS-018 | langue_origine | en | es | collecté |
| lot1 | AVIS-018 | indicateur_traduit | non | non traduit | collecté |
| lot1 | AVIS-019 | langue_origine | en | es | collecté |
| lot1 | AVIS-019 | indicateur_traduit | non | non traduit | collecté |
| lot1 | AVIS-020 | langue_origine | fr | es | collecté |
| lot1 | AVIS-021 | langue_origine | (vide) | fr | collecté |
| lot1 | AVIS-022 | langue_origine | (vide) | fr | collecté |
| lot1 | AVIS-023 | langue_origine | (vide) | fr | collecté |
| lot1 | AVIS-024 | langue_origine | (vide) | fr | collecté |
| lot1 | AVIS-026 | langue_origine | (vide) | fr | collecté |
| lot1 | AVIS-027 | langue_origine | (vide) | fr | collecté |
| lot1 | AVIS-030 | langue_origine | en | es | collecté |
| lot1 | AVIS-030 | indicateur_traduit | non | non traduit | collecté |
| lot1 | AVIS-038 | langue_origine | fr | es | collecté |
| lot1 | AVIS-039 | langue_origine | fr | es | collecté |
| lot1 | AVIS-040 | langue_origine | en | es | collecté |
| lot1 | AVIS-040 | indicateur_traduit | non | non traduit | collecté |
| lot1 | AVIS-041 | langue_origine | fr | es | collecté |
| lot1 | AVIS-042 | langue_origine | fr | es | collecté |
| lot1 | AVIS-043 | langue_origine | fr | es | collecté |
| lot1 | AVIS-044 | langue_origine | fr | es | collecté |
| lot1 | AVIS-045 | langue_origine | fr | es | collecté |
| lot1 | CH-016-DOC-0a6e2f7b | langue_origine | (vide) | es | collecté |
| lot1 | CH-012-DOC-c628f399 | langue_origine | (vide) | es | collecté |
| lot1 | CH-014-DOC-28541296 | langue_origine | (vide) | es | collecté |
| lot1 | CH-015-DOC-8ed968d7 | langue_origine | (vide) | es | collecté |
| lot1 | CH-013-DOC-57e5fd00 | langue_origine | (vide) | es | collecté |
| lot1 | CH-002-DOC-47b2ebed | langue_origine | (vide) | es | collecté |
| lot1 | CH-003-DOC-13f9e8e8 | langue_origine | (vide) | es | collecté |
| lot1 | CH-001-DOC-7d962702 | langue_origine | (vide) | es | collecté |
| lot1 | CH-005-DOC-5bc5ca24 | langue_origine | (vide) | es | collecté |
| lot1 | CH-024-DOC-4c04fafb | langue_origine | (vide) | fr | collecté |
| lot1 | CH-021-DOC-1178d96c | langue_origine | (vide) | fr | collecté |
| lot1 | CH-025-DOC-0814d4a4 | langue_origine | (vide) | es | collecté |
| lot1 | CH-026-DOC-161f9c06 | langue_origine | (vide) | es | collecté |
| lot1 | CH-027-DOC-6f1cf548 | langue_origine | (vide) | es | collecté |
| lot1 | CH-028-DOC-d631dfc4 | langue_origine | (vide) | es | collecté |
| lot2 | LOT2-DE000A0M98N2-DE-Prospectus-305d50ec | indicateur_traduit | non traduit | oui | collecté |
| lot2 | LOT2-FR0013532363-FR-Rapport-41430957 | indicateur_traduit | non traduit | oui | collecté |
| lot2 | LOT2-DE0009770206-DE-Prospectus-9c9a4bef | indicateur_traduit | non traduit | oui | collecté |
| lot2 | LOT2-FR0007468830-FR-Rapport-00d5c413 | indicateur_traduit | non traduit | oui | collecté |
| lot2 | LOT2-LU0599613147-FR-Prospectus-665694a8 | langue_origine | (vide) | fr | collecté |

## 3. Construction du cadre (sections 4.1, 4.2)

- Unité documentaire = lignes « collecté » d'un même lot partageant le même sha256 ; ligne de référence = plus petit `identifiant_document` (ordre alphabétique) ; `lignes_manifeste` = toutes les lignes du groupe ; `fonds_concernes` = ISIN de ces lignes ; `pays_distribution` = pays de ces lignes. Aucun sha256 n'est partagé entre deux lots. Les lignes « manquant » et « exclu » n'ont pas de fichier et ne forment pas d'unité.
- Segments d'une unité = segments de la ligne de référence dans `segments.jsonl` ; les segments identiques des autres lignes du groupe sont ignorés (comptés une seule fois).
- `tronque` et `reserve_professionnels` : repris de `consolidation/manifeste_complete.csv`. `tronque = oui` : les 4 lignes du rapport Ossiam LU0599613147 (sha256 a83a1a56…, PDF illisible, aucun texte). `reserve_professionnels = oui` : recherche mécanique faite à la consolidation (expressions « réservé aux investisseurs professionnels », « professional investors only », « nur für professionelle Anleger », « únicamente a inversores profesionales »… sur les pages 1-2, la dernière page et les en-têtes/pieds répétés) : 15 lignes, toutes des factsheets. Une unité est exclue si l'une de ses lignes porte le marqueur.
- Annexe Singapour : lot `annexe_SG` de la consolidation. Avis : `type_document = Avis`. Paires : lignes dont `notes` commence par « paire » ou dont `document_parent` est un avis (identifiants CH-xxx-DOC-…, rapports CNMV et factsheets appariés aux avis).
- Strates : S1 = KID, KIID, fiches locales (Fiche_locale = KFS de Hong Kong ; PHS) ; S2 = factsheets ; S3 = prospectus ; S4 = rapports (annuels et semestriels) et bulletins trimestriels. Les avis n'entrent dans aucune strate (« hors strate »).
- `maison_gestion` : valeur du manifeste ; pour la valeur générique « autre émetteur » du lot 2, la société de gestion de l'ISIN est reprise de `lot2/echantillon_lot2.csv` (archive livrée) sous la forme « autre émetteur : <société> », et c'est cette valeur qui compte pour le plafond par maison. Aucune autre normalisation (« BlackRock » et « BlackRock (iShares) », « Fidelity » et « Fidelity International » restent distincts ; aucune de ces paires ne coexiste dans une même strate du cadre).

## 3 bis. Fichiers composites (règle de l'ajustement du 17/11)

Recherche dans tout le corpus (lots 1, 2 et annexe Singapour) des fichiers (même sha256, lignes « collecté ») listés sous plusieurs types de document. Au lieu du type de la ligne de référence, le fichier est découpé par pages d'après les titres du texte (`consolidation/corpus.jsonl`, marqueurs de page « ----- p. N ----- ») : page de titre de KID = « Document d'Informations Clés » (ou équivalent) dans les 15 premières lignes non vides de la page ; début du prospectus = ligne réduite au mot « PROSPECTUS » dans les 15 premières lignes non vides ; un KID couvre sa page de titre jusqu'à la page qui précède le KID suivant ou le prospectus, et appartient à la classe de parts dont l'ISIN figure dans ses pages. Les segments sont répartis selon leur champ `page` ; leurs `segment_id` ne changent pas.
Doc_id des unités créées : doc_id de la ligne de référence (plus petit doc_id du groupe, celui sous lequel les segments figurent dans segments.jsonl), suivi de « -KID » (KID de la classe de parts du manifeste, strate S1) ou « -PROSPECTUS » (strate S3) ; les pages des KID des autres classes forment une unité « -KID-AUTRES-CLASSES », gardée dans cadre_documents.csv pour la traçabilité et exclue du cadre (motif « KID d'une autre classe de parts »).

### LOT2-FR0013532363-FR-KID-68889a53 (lot lot2, sha256 68889a537503d063d59a62a7a3b05ffcfe73b8197549d60b6794fb9ca3c222da)

- Lignes du manifeste : LOT2-FR0013532363-FR-KID-68889a53, LOT2-FR0013532363-FR-Prospectus-68889a53 ; types : KID, Prospectus ; ISIN du manifeste : FR0013532363.
- KID repéré dans le texte : pages 1-3 ; ISIN présents : FR0013532363 ; classe de parts du manifeste.
- KID repéré dans le texte : pages 4-6 ; ISIN présents : FR0014005DN0 ; autre classe de parts.
- KID repéré dans le texte : pages 7-9 ; ISIN présents : FR0013532371 ; autre classe de parts.
- Début du prospectus repéré dans le texte : page 10 (dernière page du fichier : 37).
- Limites annoncées par les notes de LOT2-FR0013532363-FR-KID-68889a53 : plages 1-3, 4-9 ; début annoncé 10.
- Limites annoncées par les notes de LOT2-FR0013532363-FR-Prospectus-68889a53 : plages 1-3 ; début annoncé 10.
- **Limites retenues** : KID de la part du manifeste pages 1-3 ; KID des autres classes pages 4-9 ; prospectus pages 10-37.
- Unité LOT2-FR0013532363-FR-KID-68889a53-KID : type KID, strate S1, pages 1-3, 31 segments, 31 « oui » perimetre_v2, dans le cadre.
- Unité LOT2-FR0013532363-FR-KID-68889a53-KID-AUTRES-CLASSES : type KID, strate S1, pages 4-9, 67 segments, 53 « oui » perimetre_v2, exclue du cadre (KID d'une autre classe de parts).
- Unité LOT2-FR0013532363-FR-KID-68889a53-PROSPECTUS : type Prospectus, strate S3, pages 10-37, 293 segments, 237 « oui » perimetre_v2, dans le cadre.
- Segments du fichier hors des pages retenues : 0.


## 4. Règles de périmètre v2 réellement utilisées (section 4.3)

Le champ `perimetre` n'est pas modifié ; `perimetre_v2` et `regle_perimetre_v2` sont écrits pour chaque segment des unités dans `segments_perimetre_v2.csv` (fichier nouveau). Les règles portent sur les titres de section (`titre_section`), le nom et l'ISIN des fonds du groupe, des marqueurs de structure et des critères de forme ; jamais sur le sens.

Mécanique des titres :
- Un titre est pris en compte quand `titre_section` change d'un segment au suivant ; « haut de page » = premier segment d'une nouvelle page portant un nouveau titre (approximation : l'indicateur de haut de page de la consolidation n'est pas dans segments.jsonl).
- Recollement (4.3) : la segmentation de la consolidation a déjà recollé les lignes de titre consécutives d'un même bloc ; les intitulés coupés restants ont leur fin en tête du premier segment de la section (ex. « State Street SPDR MSCI Europe Communication Services UCITS » + « ETF »). Le titre comparé = titre + les lignes de tête de ce segment qui ont de 1 à 4 mots, sans chiffre, sans ponctuation finale ni double espace (au plus 2 lignes), si le titre ne finit pas par une ponctuation. Pour les compartiments, si le titre recollé ne classe rien, le titre brut est aussi essayé ; « propre » l'emporte sur « autre ». Le texte des segments n'est pas modifié.
- Titre ignoré (état inchangé) s'il a la forme d'un fragment de prose : commence par une minuscule, un tiret ou une puce, ou finit par « ; » ou « , ».
- Fonds d'une unité regroupant plusieurs lignes : une section est « propre au fonds » si son titre contient l'ISIN ou le nom de l'un des fonds du groupe.

Comptes des titres : exploités : 92450, ignorés (fragment de prose) : 37769, recollés : 11913, titre avec mot de frais non retenu comme titre de frais : 1.

Règles appliquées, avec le nombre de segments (tous lots, toutes unités, y compris hors cadre) :

| perimetre_v2 | Règle | Segments |
|---|---|---|
| non | annexe SFDR (texte : « Legal entity identifier ») | 34791 |
| non | annexe SFDR (titre : « Annexe SFDR ») | 33352 |
| non | rapport : liste de positions / titres en portefeuille | 30623 |
| non | rapport : états financiers et notes | 30389 |
| non | annexe SFDR (texte : « Modèle d'informations précontractuelles / périodiques (article 8 ou 9) ») | 28141 |
| non | prospectus : autre compartiment | 19887 |
| oui | rapport : performance | 14215 |
| non | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 12724 |
| oui | prospectus : partie générale | 9186 |
| non | annexe SFDR (titre : « Sustainability indicators (encadré du modèle) ») | 7977 |
| oui | prospectus : partie générale (retour sur un intitulé d'annexe en haut de page) | 7814 |
| oui | prospectus : partie générale (fin d'annexe-liste, titre en haut de page) | 6282 |
| non | annexe SFDR (texte : « Sustainability indicators (encadré du modèle) ») | 5626 |
| oui | rapport : section non classée, gardée (cas non tranché) | 5568 |
| oui | prospectus : autre compartiment → oui, cas non tranché (section propre au fonds non repérée) | 4250 |
| non | annexe SFDR (titre : « Legal entity identifier ») | 3960 |
| non | exclusion générale : chiffres > moitié des caractères non blancs | 3723 |
| oui | type toujours inclus (KID, fiche locale, factsheet, bulletin) | 3440 |
| non | annexe SFDR (titre : « Product name ») | 3243 |
| oui | prospectus : section propre au fonds (nom dans le titre) | 2897 |
| oui | rapport : commentaire de gestion | 2878 |
| oui | rapport : frais effectifs (titre complet) | 2130 |
| oui | prospectus : section propre au fonds (ISIN dans le titre) | 1695 |
| non | rapport : rapport d'audit | 1156 |
| non | annexe SFDR (titre : « Modèle d'informations précontractuelles / périodiques (article 8 ou 9) ») | 763 |
| oui | avis : type non visé par 4.3, gardé (cas non tranché, hors cadre) | 380 |
| non | prospectus : annexe qui est une simple liste (sub-custodian) | 148 |
| non | annexe SFDR (texte : « Product name ») | 114 |
| non | prospectus : annexe qui est une simple liste (directory) | 63 |
| non | annexe SFDR (titre : « Règlement délégué (UE) 2022/1288 ») | 63 |
| non | prospectus : annexe qui est une simple liste (sous-dépositaires) | 48 |
| non | prospectus : annexe qui est une simple liste (unterverwahrer) | 33 |
| non | prospectus : annexe qui est une simple liste (list of funds) | 19 |
| non | prospectus : annexe qui est une simple liste (elenco dei comparti) | 13 |
| non | prospectus : annexe qui est une simple liste (anschriften) | 11 |
| non | exclusion générale : moins de 4 mots | 7 |
| non | prospectus : annexe qui est une simple liste (liste des compartiments) | 5 |

Déclencheurs d'annexe SFDR réellement utilisés (nombre de fois où le marqueur a ouvert une annexe SFDR) :

| Type | Marqueur | Trouvé dans | Ouvertures |
|---|---|---|---|
| Prospectus | Annexe SFDR | titre | 159 |
| Prospectus | Legal entity identifier | texte | 62 |
| Rapport | Legal entity identifier | titre | 30 |
| Prospectus | Modèle d'informations précontractuelles / périodiques (article 8 ou 9) | texte | 26 |
| Rapport | Legal entity identifier | texte | 20 |
| Prospectus | Product name | titre | 18 |
| Rapport | Modèle d'informations précontractuelles / périodiques (article 8 ou 9) | texte | 15 |
| Rapport | Annexe SFDR | titre | 15 |
| Prospectus | Sustainability indicators (encadré du modèle) | titre | 11 |
| Prospectus | Legal entity identifier | titre | 6 |
| Rapport | Product name | titre | 4 |
| Rapport | Product name | texte | 2 |
| Prospectus | Modèle d'informations précontractuelles / périodiques (article 8 ou 9) | titre | 2 |
| Rapport | Sustainability indicators (encadré du modèle) | titre | 2 |
| Prospectus | Sustainability indicators (encadré du modèle) | texte | 1 |
| Rapport | Modèle d'informations précontractuelles / périodiques (article 8 ou 9) | titre | 1 |
| Prospectus | Règlement délégué (UE) 2022/1288 | titre | 1 |

Précisions :
- Prospectus : « oui » partie générale (état initial) et section propre au fonds ; « non » autres compartiments, annexes-listes (sous-dépositaires, adresses, liste des fonds) et annexes SFDR. Retour en partie générale : intitulé d'annexe (« Appendix », « Annexe », « Anhang »…) en haut de page, ou titre en haut de page après une annexe-liste. Contrairement à la consolidation, un titre quelconque en haut de page ne ramène plus en partie générale (cause des « Fondsmerkmale » classés partie générale au milieu d'un autre compartiment).
- Annexes SFDR (prospectus et rapports) : une annexe s'ouvre sur un titre portant un marqueur, ou sur un segment dont le texte porte un marqueur (sauf segment de sommaire : points de conduite « ..... » ou titre « Contents / Sommaire / Inhaltsverzeichnis »). Marqueurs : « Legal entity identifier » et équivalents (titre ou texte) ; « Product name : » et équivalents (titre ou 200 premiers caractères) ; en-tête du modèle « Pre-contractual / Periodic disclosure … Article 8 ou 9 » et équivalents (titre ou texte) ; encadré « Sustainability indicators measure … » et équivalents (titre ou texte) ; « Annexe II / III » (titre seulement, avec un mot du modèle SFDR dans le titre ou au début du segment) ; « 2022/1288 » (titre seulement) ; « Annexe SFDR » (titre commençant par un mot d'annexe suivi de « SFDR », ou par « SFDR »). L'en-tête du modèle n'est reconnu dans le texte qu'en début de ligne ou après une colonne (3 espaces ou plus), pas au milieu d'une phrase. Les renvois de prose (« Anhang II dieses Prospekts », « conformément au règlement délégué (UE) 2022/1288 », « les informations précontractuelles … sont disponibles en annexe ») n'ouvrent donc pas d'annexe : un premier essai qui les comptait classait à tort des parties générales entières en « annexe SFDR » ; ces marqueurs ont été resserrés au vu des seules positions d'ouverture des annexes (titres et débuts de segments déclencheurs), sans consulter les tirages d'essai. Fermeture : prospectus — titre de compartiment, d'annexe-liste ou intitulé d'annexe en haut de page ; rapports — titre d'audit, de positions, d'états financiers ou de commentaire de gestion (un titre de performance ou de frais, fréquent dans le modèle SFDR périodique, ne la ferme pas).
- Rapports : « non » rapport d'audit, listes de positions et de titres en portefeuille, états financiers et notes, annexes SFDR (mêmes marqueurs, appliqués aussi aux rapports : le doute sur une annexe SFDR vaut « non ») ; « oui » commentaire de gestion, frais effectifs, performance. Frais : titre complet — le titre doit contenir un terme de frais non précédé d'une exclusion (« hors », « net of », « after », « ohne », « sin »…) et compter au plus 12 mots ; « Contributions à la performance de l'exercice (hors frais) » n'est donc pas un titre de frais (il est classé performance). Section non classée : « oui » (cas non tranché).
- KID, fiches locales, factsheets, bulletins : « oui » sauf exclusions générales.
- Exclusions générales (tous types), appliquées dans cet ordre aux segments sinon « oui » : chiffres > moitié des caractères non blancs ; moins de 4 mots (`n_mots`) ; texte identique (espaces normalisés) à un segment déjà retenu « oui » plus haut dans la même unité.

Exemples de titres recollés (40 au plus) :

- LOT1-IE0032523478-DE-Prospectus-811887be : « iShares Public Limited Company » → « iShares Public Limited Company Deutscher Konsolidierter Prospekt »
- LOT1-IE0032523478-DE-Prospectus-811887be : « Währung, die sich » → « Währung, die sich von der Basiswährung »
- LOT1-IE0032523478-DE-Prospectus-811887be : « Ladungsfähige Anschrift: 3 rue d’Antin, 75002 Paris, » → « Ladungsfähige Anschrift: 3 rue d’Antin, 75002 Paris, Frankreich »
- LOT1-IE0032523478-DE-Prospectus-811887be : « LT-01103 Vilnius » → « LT-01103 Vilnius Litauen »
- LOT1-IE0032523478-DE-Prospectus-811887be : « 150, Al Matar Street » → « 150, Al Matar Street (Airport Road) »
- LOT1-IE0032523478-DE-Prospectus-811887be : « Investition keine Umweltziele » → « Investition keine Umweltziele oder sozialen Ziele erheblich »
- LOT1-IE0032523478-DE-Prospectus-811887be : « enthält es einen Mindestanteil von 40 % an » → « enthält es einen Mindestanteil von 40 % an nachhaltigen Investitionen »
- LOT1-IE0032523478-DE-Prospectus-811887be : « mit dem Finanzprodukt » → « mit dem Finanzprodukt beworbenen ökologischen oder »
- LOT1-IE0032523478-DE-Prospectus-811887be : « bedeutendsten nachteiligen » → « bedeutendsten nachteiligen Auswirkungen von »
- LOT1-IE0032523478-DE-Prospectus-811887be : « umweltfreundlichen » → « umweltfreundlichen betrieblichen Aktivitäten »
- LOT1-IE0032523478-DE-Prospectus-811887be : « investiert wird, » → « investiert wird, widerspiegeln »
- LOT1-IE0032523478-DE-Prospectus-811887be : « Taxonomiekonformität » → « Taxonomiekonformität umfassen die Kriterien für fossiles Gas die Begrenzung »
- LOT1-IE0032523478-DE-Prospectus-811887be : « sind nachhaltige » → « sind nachhaltige Investitionen mit einem »
- LOT1-IE0032523478-DE-Prospectus-811887be : « denen gemessen wird, » → « denen gemessen wird, ob das Finanzprodukt die »
- LOT1-IE0032523478-DE-Prospectus-811887be : « mit dem Finanzprodukt » → « mit dem Finanzprodukt beworbenen ökologischen oder »
- LOT1-IE0032523478-DE-Prospectus-811887be : « bedeutendsten nachteiligen » → « bedeutendsten nachteiligen Auswirkungen von »
- LOT1-IE0032523478-DE-Prospectus-811887be : « umweltfreundlichen » → « umweltfreundlichen Investitionen der Unternehmen, in die »
- LOT1-IE0032523478-DE-Prospectus-811887be : « investiert wird, » → « investiert wird, widerspiegeln »
- LOT1-IE0032523478-DE-Prospectus-811887be : « Taxonomiekonformität » → « Taxonomiekonformität umfassen die Kriterien für fossiles Gas die Begrenzung »
- LOT1-IE0032523478-DE-Prospectus-811887be : « sind nachhaltige » → « sind nachhaltige Investitionen mit einem »
- LOT1-IE0032523478-DE-Prospectus-811887be : « denen gemessen wird, » → « denen gemessen wird, ob das Finanzprodukt die »
- LOT1-IE0032523478-DE-Prospectus-811887be : « Investition keine Umweltziele » → « Investition keine Umweltziele oder sozialen Ziele erheblich »
- LOT1-IE0032523478-DE-Prospectus-811887be : « enthält es einen Mindestanteil von 30 % an » → « enthält es einen Mindestanteil von 30 % an nachhaltigen Investitionen »
- LOT1-IE0032523478-DE-Prospectus-811887be : « mit dem Finanzprodukt » → « mit dem Finanzprodukt beworbenen ökologischen oder sozialen Merkmale erreicht »
- LOT1-IE0032523478-DE-Prospectus-811887be : « bedeutendsten nachteiligen » → « bedeutendsten nachteiligen Auswirkungen von »
- LOT1-IE0032523478-DE-Prospectus-811887be : « umweltfreundlichen » → « umweltfreundlichen Investitionen der Unternehmen, in die »
- LOT1-IE0032523478-DE-Prospectus-811887be : « investiert wird, » → « investiert wird, widerspiegeln »
- LOT1-IE0032523478-DE-Prospectus-811887be : « Taxonomiekonformität » → « Taxonomiekonformität umfassen die Kriterien für fossiles Gas die Begrenzung »
- LOT1-IE0032523478-DE-Prospectus-811887be : « sind nachhaltige » → « sind nachhaltige Investitionen mit einem »
- LOT1-IE0032523478-DE-Prospectus-811887be : « denen gemessen wird, » → « denen gemessen wird, ob das Finanzprodukt die »
- LOT1-IE0032523478-DE-Prospectus-811887be : « Investition keine Umweltziele » → « Investition keine Umweltziele oder sozialen Ziele erheblich »
- LOT1-IE0032523478-DE-Prospectus-811887be : « mit dem Finanzprodukt » → « mit dem Finanzprodukt beworbenen ökologischen oder sozialen Merkmale erreicht »
- LOT1-IE0032523478-DE-Prospectus-811887be : « bedeutendsten nachteiligen » → « bedeutendsten nachteiligen Auswirkungen von »
- LOT1-IE0032523478-DE-Prospectus-811887be : « Bereichen Umwelt, Soziales » → « Bereichen Umwelt, Soziales und Beschäftigung, Achtung der Menschenrechte und »
- LOT1-IE0032523478-DE-Prospectus-811887be : « Überwachungsprozess » → « Überwachungsprozess UNGC und OECD »
- LOT1-IE0032523478-DE-Prospectus-811887be : « Taxonomiekonformität » → « Taxonomiekonformität umfassen die Kriterien für fossiles Gas die Begrenzung »
- LOT1-IE0032523478-DE-Prospectus-811887be : « Kernenergie » → « Kernenergie Kernenergie »
- LOT1-IE0032523478-DE-Prospectus-811887be : « sind nachhaltige » → « sind nachhaltige Investitionen mit einem Umweltziel, die die Kriterien »
- LOT1-IE0032523478-DE-Prospectus-811887be : « Wirtschaftstätigkeiten gemäß » → « Wirtschaftstätigkeiten gemäß der EU-Taxonomie nicht »
- LOT1-IE0032523478-DE-Prospectus-811887be : « fundregistrationsandlisting » → « fundregistrationsandlisting s@blackrock.com »

Exemples de titres ignorés comme fragments de prose (15 au plus) :

- LOT1-IE0032523478-DE-Prospectus-811887be : « iShares Public Limited Company »
- LOT1-IE0032523478-DE-Prospectus-811887be : « „Wesentliche Anlegerinformationen“ oder „Basisinformationsblatt“: Die wesentlichen Informationen für den Anleger, »
- LOT1-IE0032523478-DE-Prospectus-811887be : « •    Austausch mit Indexanbietern in Bezug auf den Referenzindex; und »
- LOT1-IE0032523478-DE-Prospectus-811887be : « der Basiswährung »
- LOT1-IE0032523478-DE-Prospectus-811887be : « der Basiswährung »
- LOT1-IE0032523478-DE-Prospectus-811887be : « iShares $ Corp Bond »
- LOT1-IE0032523478-DE-Prospectus-811887be : « iShares China Large »
- LOT1-IE0032523478-DE-Prospectus-811887be : « iShares MSCI Taiwan »
- LOT1-IE0032523478-DE-Prospectus-811887be : « Die Liste der Referenzwert-Administratoren, die im Register nach der Benchmark-Verordnung eingetragen sind, »
- LOT1-IE0032523478-DE-Prospectus-811887be : « •    STOXX Limited (für die EURO STOXX-Indizes im Geltungsbereich); und »
- LOT1-IE0032523478-DE-Prospectus-811887be : « •    FTSE International Limited (für die FTSE-Indizes im Geltungsbereich); und »
- LOT1-IE0032523478-DE-Prospectus-811887be : « •   die Gewichtungen der Wertpapiere, aus denen sich der Referenzindex zusammensetzt, dazu führen »
- LOT1-IE0032523478-DE-Prospectus-811887be : « •   ein neuer Index verfügbar ist, der den bestehenden Referenzindex ersetzt; »
- LOT1-IE0032523478-DE-Prospectus-811887be : « •   die Qualität (einschließlich der Richtigkeit und der Verfügbarkeit von Daten) eines bestimmten »
- LOT1-IE0032523478-DE-Prospectus-811887be : « Staatsanleihen, Anleihen mit Staatsbezug und verbriefte Anleihen, variabel verzinsliche Anleihen, »

## 5. Cas non tranchés

Règle : cas non tranché = « oui » et consigné, sauf liste de positions, annexe SFDR, rapport d'audit (doute = « non »). Sections de rapport non classées : « oui » (comptées ci-dessus sous « rapport : section non classée »).

- lot1 — LOT1-LU0297942194-FR-Prospectus-13a405e5 : prospectus parapluie : aucune section propre au fonds repérée, les sections « autre compartiment » passent en « oui » (dans le cadre)
- lot1 — LOT1-LU0297942194-CH-Prospectus-dab44aab : prospectus parapluie : aucune section propre au fonds repérée, les sections « autre compartiment » passent en « oui » (dans le cadre)
- lot1 — LOT1-LU1159239190-DE-Prospectus-3c88f629 : prospectus parapluie : aucune section propre au fonds repérée, les sections « autre compartiment » passent en « oui » (dans le cadre)
- lot1 — LOT1-LU0224105477-FR-Prospectus-9f8a5429 : prospectus parapluie : aucune section propre au fonds repérée, les sections « autre compartiment » passent en « oui » (dans le cadre)
- lot1 — LOT1-LU0224105477-HK-Prospectus-3b3c5fe3 : prospectus parapluie : aucune section propre au fonds repérée, les sections « autre compartiment » passent en « oui » (dans le cadre)
- annexe_SG — LOT2-ANNEXE-SG-LU0224105477-SG-Prospectus-4eb906ef : prospectus parapluie : aucune section propre au fonds repérée, les sections « autre compartiment » passent en « oui » (hors cadre)

## 6. Tirage : paramètres, parcours et écarts à la cible

Paramètres : graine 2026 ; générateur Python `random.Random("2026-<lot>-<strate>")` puis `random.Random("2026-<lot>-<strate>-<doc_id>")` (graine chaîne, déterministe) ; {'lot1': 20, 'lot2': 24} segments par strate ; 2 segments par document ; {'lot1': 10, 'lot2': 12} documents par strate ; 5 documents et 3 segments de réserve ; plafond par maison ceil(0.4 × N).

Interprétations : (a) la liste est triée par doc_id puis mélangée par `shuffle` ; (b) une maison est refusée dès qu'elle a déjà ceil(0,4 × N) unités acceptées (au plus 40 % ; une lecture littérale « pas plus de » autoriserait une unité de plus) ; (c) les conditions de fonds et de maison continuent de s'appliquer aux unités de réserve, qui sont les 5 unités acceptées suivantes, et comptent pour les acceptations suivantes ; (d) dans un document, les segments `perimetre_v2 = oui` sont triés par `ordre` avant le mélange, et un segment est écarté si son `ordre` diffère de 1 de celui d'un segment déjà retenu ; (e) `texte_en` n'est rempli que si `statut_en` vaut « traduit_automatique_aligne » ou « original_anglais » (texte anglais d'origine).


### lot1 — S1 : 29 unités éligibles, plafond par maison 4

- LOT1-LU0297942194-CH-KID-4130ae5b (BlackRock (iShares) ; LU0297942194) : acceptée : tirage principal rang 1
- LOT1-LU0297942194-FR-KID-d3dd9e86 (BlackRock (iShares) ; LU0297942194) : refusée : fonds déjà couvert (LU0297942194)
- LOT1-LU0297942194-DE-KID-bbb589dd (BlackRock (iShares) ; LU0297942194) : refusée : fonds déjà couvert (LU0297942194)
- LOT1-IE00BFMXLY20-DE-KID-1b18b5da (State Street (SPDR) ; IE00BFMXLY20) : acceptée : tirage principal rang 2
- LOT1-LU2348335964-FR-KID-e28ecde5 (Fidelity International ; LU2348335964) : acceptée : tirage principal rang 3
- LOT1-LU0224105477-DE-KID-8ff64de5 (BlackRock (iShares) ; LU0224105477) : acceptée : tirage principal rang 4
- LOT1-LU0138981039-HK-Fiche_locale-90211555 (Fidelity International ; LU0138981039) : acceptée : tirage principal rang 5
- LOT1-LU0297942194-HK-Fiche_locale-15df9cad (BlackRock (iShares) ; LU0297942194) : refusée : fonds déjà couvert (LU0297942194)
- LOT1-LU0224105477-CH-KID-37fd21d0 (BlackRock (iShares) ; LU0224105477) : refusée : fonds déjà couvert (LU0224105477)
- LOT1-FR0012686350-FR-KID-4abc6155 (Fidelity International ; FR0012686350) : acceptée : tirage principal rang 6
- LOT1-IE0032523478-DE-KID-5a9e1e1a (BlackRock (iShares) ; IE0032523478) : acceptée : tirage principal rang 7
- LOT1-LU0064964074-DE-KID-8f532e88 (Fidelity International ; LU0064964074) : acceptée : tirage principal rang 8
- LOT1-LU0138981039-DE-KID-16870321 (Fidelity International ; LU0138981039) : refusée : fonds déjà couvert (LU0138981039)
- LOT1-IE00BKWQ0M75-DE-KID-20cc4a89 (State Street (SPDR) ; IE00BKWQ0M75) : acceptée : tirage principal rang 9
- LOT1-IE00B66F4759-FR-KID-471e2943 (BlackRock (iShares) ; IE00B66F4759) : acceptée : tirage principal rang 10
- LOT1-LU0138981039-CH-KID-d7378742 (Fidelity International ; LU0138981039) : refusée : fonds déjà couvert (LU0138981039)
- LOT1-LU2348335964-CH-KID-4348600e (Fidelity International ; LU2348335964) : refusée : fonds déjà couvert (LU2348335964)
- LOT1-LU0138981039-FR-KID-80ce1c26 (Fidelity International ; LU0138981039) : refusée : fonds déjà couvert (LU0138981039)
- LOT1-LU0224105477-FR-KID-35fcde51 (BlackRock (iShares) ; LU0224105477) : refusée : fonds déjà couvert (LU0224105477)
- LOT1-LU2348335964-DE-KID-b2ebf272 (Fidelity International ; LU2348335964) : refusée : fonds déjà couvert (LU2348335964)
- LOT1-IE00B3X84Y31-DE-KID-60e939de (BlackRock (iShares) ; IE00B3X84Y31) : refusée : maison « BlackRock (iShares) » déjà à 4 unités (plafond 4)
- LOT1-IE00B66F4759-DE-KID-f8a882da (BlackRock (iShares) ; IE00B66F4759) : refusée : fonds déjà couvert (IE00B66F4759)
- LOT1-IE00B3X84Y31-CH-KID-6952624f (BlackRock (iShares) ; IE00B3X84Y31) : refusée : maison « BlackRock (iShares) » déjà à 4 unités (plafond 4)
- LOT1-LU1159239190-DE-KID-0119d56d (State Street (SPDR) ; LU1159239190) : acceptée : réserve rang 11
- LOT1-LU0064964074-FR-KID-ffd643a0 (Fidelity International ; LU0064964074) : refusée : fonds déjà couvert (LU0064964074)
- LOT1-LU1159239190-CH-KID-9e3990a0 (State Street (SPDR) ; LU1159239190) : refusée : fonds déjà couvert (LU1159239190)
- LOT1-LU0064964074-CH-KID-949b09d1 (Fidelity International ; LU0064964074) : refusée : fonds déjà couvert (LU0064964074)
- LOT1-LU0224105477-HK-Fiche_locale-08e9e456 (BlackRock (iShares) ; LU0224105477) : refusée : fonds déjà couvert (LU0224105477)
- LOT1-IE00BKWQ0M75-UK-KID-e7b746d2 (State Street (SPDR) ; IE00BKWQ0M75) : refusée : fonds déjà couvert (IE00BKWQ0M75)

### lot1 — S2 : 13 unités éligibles, plafond par maison 4

- LOT1-IE00BKWQ0M75-UK-Factsheet-0b2522d8 (State Street (SPDR) ; IE00BKWQ0M75) : acceptée : tirage principal rang 1
- LOT1-LU0297942194-FR-Factsheet-0c9e8b88 (BlackRock (iShares) ; LU0297942194) : acceptée : tirage principal rang 2
- LOT1-LU0297942194-DE-Factsheet-599c390e (BlackRock (iShares) ; LU0297942194) : refusée : fonds déjà couvert (LU0297942194)
- LOT1-LU0138981039-DE-Factsheet-503089e9 (Fidelity International ; LU0138981039) : acceptée : tirage principal rang 3
- LOT1-LU0138981039-FR-Factsheet-62a3ddc1 (Fidelity International ; LU0138981039) : refusée : fonds déjà couvert (LU0138981039)
- LOT1-LU0224105477-CH-Factsheet-69a96578 (BlackRock (iShares) ; LU0224105477) : acceptée : tirage principal rang 4
- LOT1-IE0032523478-DE-Factsheet-a942093a (BlackRock (iShares) ; IE0032523478) : acceptée : tirage principal rang 5
- LOT1-IE00B66F4759-DE-Factsheet-13cce8fa (BlackRock (iShares) ; IE00B66F4759) : acceptée : tirage principal rang 6
- LOT1-IE00B66F4759-FR-Factsheet-e5cc407f (BlackRock (iShares) ; IE00B66F4759) : refusée : fonds déjà couvert (IE00B66F4759)
- LOT1-LU0224105477-DE-Factsheet-3f68290b (BlackRock (iShares) ; LU0224105477) : refusée : fonds déjà couvert (LU0224105477)
- LOT1-LU0224105477-FR-Factsheet-69cb39c9 (BlackRock (iShares) ; LU0224105477) : refusée : fonds déjà couvert (LU0224105477)
- LOT1-LU1159239190-CH-Factsheet-35487d39 (State Street (SPDR) ; LU1159239190) : acceptée : tirage principal rang 7
- LOT1-LU0297942194-CH-Factsheet-5e7eb1e5 (BlackRock (iShares) ; LU0297942194) : refusée : fonds déjà couvert (LU0297942194)

### lot1 — S3 : 20 unités éligibles, plafond par maison 4

- LOT1-LU0297942194-CH-Prospectus-dab44aab (BlackRock (iShares) ; LU0297942194) : acceptée : tirage principal rang 1
- LOT1-LU0138981039-FR-Prospectus-4e4a5ec4 (Fidelity International ; LU0138981039) : acceptée : tirage principal rang 2
- LOT1-LU0224105477-FR-Prospectus-9f8a5429 (BlackRock (iShares) ; LU0224105477) : acceptée : tirage principal rang 3
- LOT1-LU0064964074-DE-Prospectus-500d5b56 (Fidelity International ; LU0064964074;LU0138981039;LU2348335964) : refusée : fonds déjà couvert (LU0138981039)
- LOT1-IE0032523478-DE-Prospectus-811887be (BlackRock (iShares) ; IE0032523478;IE00B66F4759) : acceptée : tirage principal rang 4
- LOT1-LU0224105477-DE-Prospectus-a5c19c26 (BlackRock (iShares) ; LU0224105477;LU0297942194) : refusée : fonds déjà couvert (LU0224105477;LU0297942194)
- LOT1-IE00B3X84Y31-CH-Prospectus-8bbfdd0b (BlackRock (iShares) ; IE00B3X84Y31) : acceptée : tirage principal rang 5
- LOT1-IE00B3X84Y31-DE-Prospectus-dfb753f4 (BlackRock (iShares) ; IE00B3X84Y31) : refusée : fonds déjà couvert (IE00B3X84Y31)
- LOT1-IE00BKWQ0M75-DE-Prospectus-e75278cd (State Street (SPDR) ; IE00BKWQ0M75) : acceptée : tirage principal rang 6
- LOT1-FR0012686350-FR-Prospectus-775bab23 (Fidelity International ; FR0012686350) : acceptée : tirage principal rang 7
- LOT1-LU1159239190-DE-Prospectus-3c88f629 (State Street (SPDR) ; LU1159239190) : acceptée : tirage principal rang 8
- LOT1-LU0138981039-HK-Prospectus-4d41c650 (Fidelity International ; LU0138981039) : refusée : fonds déjà couvert (LU0138981039)
- LOT1-LU0297942194-FR-Prospectus-13a405e5 (BlackRock (iShares) ; LU0297942194) : refusée : fonds déjà couvert (LU0297942194)
- LOT1-LU0224105477-HK-Prospectus-3b3c5fe3 (BlackRock (iShares) ; LU0224105477;LU0297942194) : refusée : fonds déjà couvert (LU0224105477;LU0297942194)
- LOT1-IE00BKWQ0M75-UK-Prospectus-6665411a (State Street (SPDR) ; IE00BKWQ0M75) : refusée : fonds déjà couvert (IE00BKWQ0M75)
- LOT1-LU0064964074-CH-Prospectus-240ac0a4 (Fidelity International ; LU0064964074;LU0138981039;LU2348335964) : refusée : fonds déjà couvert (LU0138981039)
- LOT1-LU1159239190-CH-Prospectus-fa5c281f (State Street (SPDR) ; LU1159239190) : refusée : fonds déjà couvert (LU1159239190)
- LOT1-LU2575673467-FR-Prospectus-206bbbf6 (BlackRock (iShares) ; LU2575673467) : refusée : maison « BlackRock (iShares) » déjà à 4 unités (plafond 4)
- LOT1-FR0010241059-FR-Prospectus-1adc73ac (Fidelity International ; FR0010241059) : acceptée : tirage principal rang 9
- LOT1-IE00B66F4759-FR-Prospectus-447da58e (BlackRock (iShares) ; IE00B66F4759) : refusée : fonds déjà couvert (IE00B66F4759)

### lot1 — S4 : 25 unités éligibles, plafond par maison 4

- LOT1-FR0012686350-FR-Rapport-semestriel-4534e5dc (Fidelity International ; FR0012686350) : acceptée : tirage principal rang 1
- LOT1-LU0224105477-FR-Rapport-c403beec (BlackRock (iShares) ; LU0224105477;LU0297942194) : acceptée : tirage principal rang 2
- LOT1-LU0064964074-CH-Rapport-annuel-be094d27 (Fidelity International ; LU0064964074;LU0138981039;LU2348335964) : acceptée : tirage principal rang 3
- LOT1-LU0064964074-DE-Rapport-annuel-39b118c1 (Fidelity International ; LU0064964074;LU0138981039;LU2348335964) : refusée : fonds déjà couvert (LU0064964074;LU0138981039;LU2348335964)
- LOT1-IE00BKWQ0M75-UK-Rapport-semestriel-64ef8f3a (State Street (SPDR) ; IE00BKWQ0M75) : acceptée : tirage principal rang 4
- LOT1-IE00B3X84Y31-CH-Rapport-annuel-d88de70d (BlackRock (iShares) ; IE00B3X84Y31) : acceptée : tirage principal rang 5
- LOT1-FR0010241059-FR-Rapport-53765f21 (Fidelity International ; FR0010241059) : acceptée : tirage principal rang 6
- LOT1-IE00B66F4759-FR-Rapport-annuel-e5a9a63e (BlackRock (iShares) ; IE00B66F4759) : acceptée : tirage principal rang 7
- LOT1-IE0032523478-DE-Rapport-semestriel-2f82086c (BlackRock (iShares) ; IE0032523478) : acceptée : tirage principal rang 8
- LOT1-FR0012686350-FR-Rapport-a5af012e (Fidelity International ; FR0012686350) : refusée : fonds déjà couvert (FR0012686350)
- LOT1-IE00B3X84Y31-CH-Rapport-semestriel-bb45a622 (BlackRock (iShares) ; IE00B3X84Y31) : refusée : fonds déjà couvert (IE00B3X84Y31)
- LOT1-FR0010241059-FR-Rapport-semestriel-3d4fe48f (Fidelity International ; FR0010241059) : refusée : fonds déjà couvert (FR0010241059)
- LOT1-LU0064964074-CH-Rapport-semestriel-0e0819ab (Fidelity International ; LU0064964074;LU0138981039;LU2348335964) : refusée : fonds déjà couvert (LU0064964074;LU0138981039;LU2348335964)
- LOT1-LU1159239190-DE-Rapport-9fca8b91 (State Street (SPDR) ; LU1159239190) : acceptée : tirage principal rang 9
- LOT1-LU0224105477-DE-Rapport-e0b20b5e (BlackRock (iShares) ; LU0224105477;LU0297942194) : refusée : fonds déjà couvert (LU0224105477;LU0297942194)
- LOT1-LU0064964074-DE-Rapport-semestriel-0255e77b (Fidelity International ; LU0064964074) : refusée : fonds déjà couvert (LU0064964074)
- LOT1-LU0224105477-CH-Rapport-annuel-e0fb8e5e (BlackRock (iShares) ; LU0224105477;LU0297942194) : refusée : fonds déjà couvert (LU0224105477;LU0297942194)
- LOT1-IE00B3X84Y31-DE-Rapport-annuel-e20f4164 (BlackRock (iShares) ; IE00B3X84Y31) : refusée : fonds déjà couvert (IE00B3X84Y31)
- LOT1-LU1159239190-CH-Rapport-semestriel-790224f5 (State Street (SPDR) ; LU1159239190) : refusée : fonds déjà couvert (LU1159239190)
- LOT1-LU0224105477-FR-Rapport-semestriel-52391372 (BlackRock (iShares) ; LU0224105477) : refusée : fonds déjà couvert (LU0224105477)
- LOT1-LU1159239190-CH-Rapport-82391e18 (State Street (SPDR) ; LU1159239190) : refusée : fonds déjà couvert (LU1159239190)
- LOT1-LU0138981039-FR-Rapport-annuel-9639d199 (Fidelity International ; LU0138981039) : refusée : fonds déjà couvert (LU0138981039)
- LOT1-IE00BKWQ0M75-DE-Rapport-annuel-0b3f1435 (State Street (SPDR) ; IE00BKWQ0M75) : refusée : fonds déjà couvert (IE00BKWQ0M75)
- LOT1-IE00B66F4759-DE-Rapport-annuel-b7cbe9cb (BlackRock (iShares) ; IE00B66F4759) : refusée : fonds déjà couvert (IE00B66F4759)
- LOT1-IE00B3X84Y31-DE-Rapport-semestriel-6eef4c19 (BlackRock (iShares) ; IE00B3X84Y31) : refusée : fonds déjà couvert (IE00B3X84Y31)

### lot2 — S1 : 34 unités éligibles, plafond par maison 5

- LOT2-FR0000934325-FR-KID-166ac1fe (autre émetteur : LBP AM ; FR0000934325) : acceptée : tirage principal rang 1
- LOT2-FR0010730630-FR-KID-8a0be46d (autre émetteur : OFI INVEST ASSET MANAGEMENT ; FR0010730630) : acceptée : tirage principal rang 2
- LOT2-IE00BZ163L38-ES-KID-fb775f4b (Vanguard ; IE00BZ163L38) : acceptée : tirage principal rang 3
- LOT2-IE00BZ163H91-FR-KID-67f25750 (Vanguard ; IE00BZ163H91) : acceptée : tirage principal rang 4
- LOT2-IE00BZ163L38-UK-KID-092f797c (Vanguard ; IE00BZ163L38) : refusée : fonds déjà couvert (IE00BZ163L38)
- LOT2-IE00BZ163H91-IT-KID-3fcfa440 (Vanguard ; IE00BZ163H91) : refusée : fonds déjà couvert (IE00BZ163H91)
- LOT2-IE00BZ163L38-FR-KID-2b6a90df (Vanguard ; IE00BZ163L38) : refusée : fonds déjà couvert (IE00BZ163L38)
- LOT2-IE00BZ163K21-CH-KID-67c7c3f1 (Vanguard ; IE00BZ163K21) : acceptée : tirage principal rang 5
- LOT2-LU0599613147-IT-KID-0459887a (Natixis Investment Managers ; LU0599613147) : acceptée : tirage principal rang 6
- LOT2-LU0599613147-CH-KID-a6c8c734 (Natixis Investment Managers ; LU0599613147) : refusée : fonds déjà couvert (LU0599613147)
- LOT2-IE00BZ163K21-IT-KID-87675c15 (Vanguard ; IE00BZ163K21) : refusée : fonds déjà couvert (IE00BZ163K21)
- LOT2-LU0599613147-DE-KID-9c8cae19 (Natixis Investment Managers ; LU0599613147) : refusée : fonds déjà couvert (LU0599613147)
- LOT2-ES0165143001-ES-KID-5796ad1e (autre émetteur : MUTUACTIVOS, S.A., S.G.I.I.C. ; ES0165143001) : acceptée : tirage principal rang 7
- LOT2-IE00BZ163H91-DE-KID-fbdb27e4 (Vanguard ; IE00BZ163H91) : refusée : fonds déjà couvert (IE00BZ163H91)
- LOT2-FR0013532363-FR-KID-68889a53-KID (autre émetteur : COLVILLE CAPITAL PARTNERS FRANCE ; FR0013532363) : acceptée : tirage principal rang 8
- LOT2-FR001400S0F2-FR-KID-04981841 (autre émetteur : WORMSER FRERES GESTION ; FR001400S0F2) : acceptée : tirage principal rang 9
- LOT2-IE00BZ163K21-DE-KID-9048e411 (Vanguard ; IE00BZ163K21) : refusée : fonds déjà couvert (IE00BZ163K21)
- LOT2-IE00BZ163L38-IT-KID-28baa902 (Vanguard ; IE00BZ163L38) : refusée : fonds déjà couvert (IE00BZ163L38)
- LOT2-FR0010389254-FR-KID-70035ecf (autre émetteur : CREDIT MUTUEL ASSET MANAGEMENT ; FR0010389254) : acceptée : tirage principal rang 10
- LOT2-IE00BZ163K21-ES-KID-76a7a075 (Vanguard ; IE00BZ163K21) : refusée : fonds déjà couvert (IE00BZ163K21)
- LOT2-IE00BZ163H91-UK-KID-90effbc3 (Vanguard ; IE00BZ163H91) : refusée : fonds déjà couvert (IE00BZ163H91)
- LOT2-IE00BZ163L38-CH-KID-527197e1 (Vanguard ; IE00BZ163L38) : refusée : fonds déjà couvert (IE00BZ163L38)
- LOT2-DE0007483612-DE-KID-4604f8f4 (Deka Immobilien ; DE0007483612) : acceptée : tirage principal rang 11
- LOT2-IE00BZ163H91-CH-KID-b3b30820 (Vanguard ; IE00BZ163H91) : refusée : fonds déjà couvert (IE00BZ163H91)
- LOT2-IE00BZ163H91-ES-KID-72bb91b4 (Vanguard ; IE00BZ163H91) : refusée : fonds déjà couvert (IE00BZ163H91)
- LOT2-FR0007373998-FR-KID-2b9741a2 (autre émetteur : CREDIT MUTUEL ASSET MANAGEMENT ; FR0007373998) : acceptée : tirage principal rang 12
- LOT2-FR0007468830-FR-KID-d675fb0e (autre émetteur : SOCIETE GENERALE GESTION ; FR0007468830) : acceptée : réserve rang 13
- LOT2-DE0009770206-IT-KID-d0f2c299 (autre émetteur : ODDO BHF Asset Management GmbH ; DE0009770206) : acceptée : réserve rang 14
- LOT2-LU0599613147-FR-KID-ca46a51d (Natixis Investment Managers ; LU0599613147) : refusée : fonds déjà couvert (LU0599613147)
- LOT2-IE00BZ163K21-FR-KID-396a10c1 (Vanguard ; IE00BZ163K21) : refusée : fonds déjà couvert (IE00BZ163K21)
- LOT2-DE0009770206-DE-KID-12793293 (autre émetteur : ODDO BHF Asset Management GmbH ; DE0009770206) : refusée : fonds déjà couvert (DE0009770206)
- LOT2-LU0599613147-UK-KID-de03d88a (Natixis Investment Managers ; LU0599613147) : refusée : fonds déjà couvert (LU0599613147)
- LOT2-IE00BZ163L38-DE-KID-c4e7dd6d (Vanguard ; IE00BZ163L38) : refusée : fonds déjà couvert (IE00BZ163L38)
- LOT2-DE000A0M98N2-DE-KID-853c96db (autre émetteur : Catella Real Estate AG ; DE000A0M98N2) : acceptée : réserve rang 15

### lot2 — S2 : 23 unités éligibles, plafond par maison 5

- LOT2-DE0009770206-DE-Factsheet-e6a5d01d (autre émetteur : ODDO BHF Asset Management GmbH ; DE0009770206) : acceptée : tirage principal rang 1
- LOT2-IE00BZ163L38-CH-Factsheet-ca121140 (Vanguard ; IE00BZ163L38) : acceptée : tirage principal rang 2
- LOT2-IE00BZ163L38-DE-Factsheet-e341f86e (Vanguard ; IE00BZ163L38) : refusée : fonds déjà couvert (IE00BZ163L38)
- LOT2-FR001400S0F2-FR-Factsheet-ca3efed4 (autre émetteur : WORMSER FRERES GESTION ; FR001400S0F2) : acceptée : tirage principal rang 3
- LOT2-IE00BZ163K21-CH-Factsheet-b69a423e (Vanguard ; IE00BZ163K21) : acceptée : tirage principal rang 4
- LOT2-IE00BZ163H91-CH-Factsheet-ec0396e1 (Vanguard ; IE00BZ163H91) : acceptée : tirage principal rang 5
- LOT2-IE00BZ163K21-DE-Factsheet-8a8f1d1a (Vanguard ; IE00BZ163K21) : refusée : fonds déjà couvert (IE00BZ163K21)
- LOT2-FR0010730630-FR-Factsheet-746f8c70 (autre émetteur : OFI INVEST ASSET MANAGEMENT ; FR0010730630) : acceptée : tirage principal rang 6
- LOT2-FR0010389254-FR-Factsheet-23f0bc27 (autre émetteur : CREDIT MUTUEL ASSET MANAGEMENT ; FR0010389254) : acceptée : tirage principal rang 7
- LOT2-IE00BZ163K21-FR-Factsheet-66d5536f (Vanguard ; IE00BZ163K21) : refusée : fonds déjà couvert (IE00BZ163K21)
- LOT2-IE00BZ163L38-FR-Factsheet-c80b1017 (Vanguard ; IE00BZ163L38) : refusée : fonds déjà couvert (IE00BZ163L38)
- LOT2-IE00BZ163H91-FR-Factsheet-be3dcffc (Vanguard ; IE00BZ163H91) : refusée : fonds déjà couvert (IE00BZ163H91)
- LOT2-IE00BZ163H91-DE-Factsheet-f8aab691 (Vanguard ; IE00BZ163H91) : refusée : fonds déjà couvert (IE00BZ163H91)
- LOT2-IE00BZ163K21-UK-Factsheet-047af590 (Vanguard ; IE00BZ163K21) : refusée : fonds déjà couvert (IE00BZ163K21)
- LOT2-ES0165143001-ES-Factsheet-129b3735 (autre émetteur : MUTUACTIVOS, S.A., S.G.I.I.C. ; ES0165143001) : acceptée : tirage principal rang 8
- LOT2-FR0013532363-FR-Factsheet-55bad07b (autre émetteur : COLVILLE CAPITAL PARTNERS FRANCE ; FR0013532363) : acceptée : tirage principal rang 9
- LOT2-FR0000934325-FR-Factsheet-607c2d96 (autre émetteur : LBP AM ; FR0000934325) : acceptée : tirage principal rang 10
- LOT2-IE00BZ163H91-UK-Factsheet-0ce88453 (Vanguard ; IE00BZ163H91) : refusée : fonds déjà couvert (IE00BZ163H91)
- LOT2-DE000A0M98N2-DE-Factsheet-6fd11424 (autre émetteur : Catella Real Estate AG ; DE000A0M98N2) : acceptée : tirage principal rang 11
- LOT2-IE00BZ163L38-UK-Factsheet-26fabe6a (Vanguard ; IE00BZ163L38) : refusée : fonds déjà couvert (IE00BZ163L38)
- LOT2-DE0009770206-IT-Factsheet-1a02e55d (autre émetteur : ODDO BHF Asset Management GmbH ; DE0009770206) : refusée : fonds déjà couvert (DE0009770206)
- LOT2-FR0007468830-FR-Factsheet-a5a6a818 (autre émetteur : SOCIETE GENERALE GESTION ; FR0007468830) : acceptée : tirage principal rang 12
- LOT2-LU0599613147-IT-Factsheet-4c6ae5ba (Natixis Investment Managers ; LU0599613147) : acceptée : réserve rang 13

### lot2 — S3 : 26 unités éligibles, plafond par maison 5

- LOT2-FR0000934325-FR-Prospectus-fb186b32 (autre émetteur : LBP AM ; FR0000934325) : acceptée : tirage principal rang 1
- LOT2-LU0599613147-DE-Prospectus-11a04632 (Natixis Investment Managers ; LU0599613147) : acceptée : tirage principal rang 2
- LOT2-LU0599613147-CH-Prospectus-dbdd1e5d (Natixis Investment Managers ; LU0599613147) : refusée : fonds déjà couvert (LU0599613147)
- LOT2-FR0007016712-FR-Prospectus-dfa3f387 (autre émetteur : FINANCIERE DE LA CITE ; FR0007016712) : acceptée : tirage principal rang 3
- LOT2-IE00BZ163H91-ES-Prospectus-02d06502 (Vanguard ; IE00BZ163H91;IE00BZ163K21;IE00BZ163L38) : acceptée : tirage principal rang 4
- LOT2-LU0599613147-FR-Prospectus-665694a8 (Natixis Investment Managers ; LU0599613147) : refusée : fonds déjà couvert (LU0599613147)
- LOT2-FR0013532363-FR-Prospectus-650332b7 (autre émetteur : COLVILLE CAPITAL PARTNERS FRANCE ; FR0013532363) : acceptée : tirage principal rang 5
- LOT2-DE000A0M98N2-DE-Prospectus-305d50ec (autre émetteur : Catella Real Estate AG ; DE000A0M98N2) : acceptée : tirage principal rang 6
- LOT2-FR001400S0F2-FR-Prospectus-c5531513 (autre émetteur : WORMSER FRERES GESTION ; FR001400S0F2) : acceptée : tirage principal rang 7
- LOT2-ES0165143001-ES-Prospectus-5679cc3a (autre émetteur : MUTUACTIVOS, S.A., S.G.I.I.C. ; ES0165143001) : acceptée : tirage principal rang 8
- LOT2-FR00140039R3-FR-Prospectus-1f22cb86 (autre émetteur : CA INDOSUEZ GESTION ; FR00140039R3) : acceptée : tirage principal rang 9
- LOT2-FR0007468830-FR-Prospectus-b503cce8 (autre émetteur : SOCIETE GENERALE GESTION ; FR0007468830) : acceptée : tirage principal rang 10
- LOT2-FR0011422427-FR-Prospectus-a4dd8fc9 (autre émetteur : Société Générale Investment Solutions (France) ; FR0011422427) : acceptée : tirage principal rang 11
- LOT2-FR001400MEI9-FR-Prospectus-d1d0892c (autre émetteur : AURIS GESTION ; FR001400MEI9) : acceptée : tirage principal rang 12
- LOT2-FR0010730630-FR-Prospectus-4b03e02f (autre émetteur : OFI INVEST ASSET MANAGEMENT ; FR0010730630) : acceptée : réserve rang 13
- LOT2-IE00BZ163H91-DE-Prospectus-fae9beff (Vanguard ; IE00BZ163H91) : refusée : fonds déjà couvert (IE00BZ163H91)
- LOT2-FR0013532363-FR-KID-68889a53-PROSPECTUS (autre émetteur : COLVILLE CAPITAL PARTNERS FRANCE ; FR0013532363) : refusée : fonds déjà couvert (FR0013532363)
- LOT2-DE0009770206-IT-Prospectus-0878c7bf (autre émetteur : ODDO BHF Asset Management GmbH ; DE0009770206) : acceptée : réserve rang 14
- LOT2-FR0014010344-FR-Prospectus-341a7920 (autre émetteur : COVEA FINANCE ; FR0014010344) : acceptée : réserve rang 15
- LOT2-FR0011513563-FR-Prospectus-db112f8d (BNP Paribas Asset Management (Easy, BNP Paribas REIM) ; FR0011513563) : acceptée : réserve rang 16
- LOT2-FR0013529864-FR-Prospectus-eaccb443 (autre émetteur : CREDIT MUTUEL ASSET MANAGEMENT ; FR0013529864) : acceptée : réserve rang 17
- LOT2-FR0007373998-FR-Prospectus-e00df39a (autre émetteur : CREDIT MUTUEL ASSET MANAGEMENT ; FR0007373998) : non examinée (principal et réserve complets)
- LOT2-FR001400R7U7-FR-Prospectus-8c916fe6 (BNP Paribas Asset Management (Easy, BNP Paribas REIM) ; FR001400R7U7) : non examinée (principal et réserve complets)
- LOT2-FR0010389254-FR-Prospectus-642e3917 (autre émetteur : CREDIT MUTUEL ASSET MANAGEMENT ; FR0010389254) : non examinée (principal et réserve complets)
- LOT2-DE0009770206-DE-Prospectus-9c9a4bef (autre émetteur : ODDO BHF Asset Management GmbH ; DE0009770206) : non examinée (principal et réserve complets)
- LOT2-LU2423921167-IT-Prospectus-f481d65c (autre émetteur : AZIMUT INVESTMENTS S.A. ; LU2423921167) : non examinée (principal et réserve complets)

### lot2 — S4 : 23 unités éligibles, plafond par maison 5

- LOT2-FR0013532363-FR-Rapport-41430957 (autre émetteur : COLVILLE CAPITAL PARTNERS FRANCE ; FR0013532363) : acceptée : tirage principal rang 1
- LOT2-FR0007016712-FR-Rapport-5470aba3 (autre émetteur : FINANCIERE DE LA CITE ; FR0007016712) : acceptée : tirage principal rang 2
- LOT2-ES0165143001-ES-Rapport-8f788e58 (autre émetteur : MUTUACTIVOS, S.A., S.G.I.I.C. ; ES0165143001) : acceptée : tirage principal rang 3
- LOT2-FR0010730630-FR-Rapport-19070631 (autre émetteur : OFI INVEST ASSET MANAGEMENT ; FR0010730630) : acceptée : tirage principal rang 4
- LOT2-LU0599613147-UK-Rapport-semestriel-17341d68 (Natixis Investment Managers ; LU0599613147) : acceptée : tirage principal rang 5
- LOT2-FR001400MEI9-FR-Rapport-63309046 (autre émetteur : AURIS GESTION ; FR001400MEI9) : acceptée : tirage principal rang 6
- LOT2-LU0599613147-CH-Rapport-266eb15d (Natixis Investment Managers ; LU0599613147) : refusée : fonds déjà couvert (LU0599613147)
- LOT2-DE0009770206-IT-Rapport-b5854258 (autre émetteur : ODDO BHF Asset Management GmbH ; DE0009770206) : acceptée : tirage principal rang 7
- LOT2-DE0007483612-DE-Rapport-07efc82f (Deka Immobilien ; DE0007483612) : acceptée : tirage principal rang 8
- LOT2-IE00BZ163H91-DE-Rapport-969836b2 (Vanguard ; IE00BZ163H91;IE00BZ163K21;IE00BZ163L38) : acceptée : tirage principal rang 9
- LOT2-DE0009770206-DE-Rapport-8ec78c7c (autre émetteur : ODDO BHF Asset Management GmbH ; DE0009770206) : refusée : fonds déjà couvert (DE0009770206)
- LOT2-DE000A0M98N2-DE-Rapport-2e078ef2 (autre émetteur : Catella Real Estate AG ; DE000A0M98N2) : acceptée : tirage principal rang 10
- LOT2-DE0009770206-IT-Rapport-semestriel-cfc8229a (autre émetteur : ODDO BHF Asset Management GmbH ; DE0009770206) : refusée : fonds déjà couvert (DE0009770206)
- LOT2-FR0007468830-FR-Rapport-00d5c413 (autre émetteur : SOCIETE GENERALE GESTION ; FR0007468830) : acceptée : tirage principal rang 11
- LOT2-LU2423921167-IT-Rapport-5f699175 (autre émetteur : AZIMUT INVESTMENTS S.A. ; LU2423921167) : acceptée : tirage principal rang 12
- LOT2-LU0599613147-CH-Rapport-semestriel-79f8b982 (Natixis Investment Managers ; LU0599613147) : refusée : fonds déjà couvert (LU0599613147)
- LOT2-IE00BZ163H91-CH-Rapport-semestriel-d6188094 (Vanguard ; IE00BZ163H91;IE00BZ163K21;IE00BZ163L38) : refusée : fonds déjà couvert (IE00BZ163H91;IE00BZ163K21;IE00BZ163L38)
- LOT2-IE00BZ163H91-DE-Rapport-semestriel-6a21e594 (Vanguard ; IE00BZ163H91;IE00BZ163K21;IE00BZ163L38) : refusée : fonds déjà couvert (IE00BZ163H91;IE00BZ163K21;IE00BZ163L38)
- LOT2-IE00BZ163H91-CH-Rapport-df89a2c8 (Vanguard ; IE00BZ163H91;IE00BZ163K21;IE00BZ163L38) : refusée : fonds déjà couvert (IE00BZ163H91;IE00BZ163K21;IE00BZ163L38)
- LOT2-FR0000934325-FR-Rapport-8b48b254 (autre émetteur : LBP AM ; FR0000934325) : acceptée : réserve rang 13
- LOT2-FR001400S0F2-FR-Rapport-5270c3b7 (autre émetteur : WORMSER FRERES GESTION ; FR001400S0F2) : acceptée : réserve rang 14
- LOT2-DE0009770206-DE-Rapport-semestriel-61f694f8 (autre émetteur : ODDO BHF Asset Management GmbH ; DE0009770206) : refusée : fonds déjà couvert (DE0009770206)
- LOT2-FR0011513563-FR-Bulletin_trimestriel-64308ad4 (BNP Paribas Asset Management (Easy, BNP Paribas REIM) ; FR0011513563) : acceptée : réserve rang 15

### Écarts à la cible

- lot1 — S1 : documents de réserve : cible 5, obtenu 1. Le cadre ne permet pas d'atteindre la cible ; arrêt sans complément manuel.
- lot1 — S2 : documents (tirage principal) : cible 10, obtenu 7. Le cadre ne permet pas d'atteindre la cible ; arrêt sans complément manuel.
- lot1 — S2 : documents de réserve : cible 5, obtenu 0. Le cadre ne permet pas d'atteindre la cible ; arrêt sans complément manuel.
- lot1 — S3 : documents (tirage principal) : cible 10, obtenu 9. Le cadre ne permet pas d'atteindre la cible ; arrêt sans complément manuel.
- lot1 — S3 : documents de réserve : cible 5, obtenu 0. Le cadre ne permet pas d'atteindre la cible ; arrêt sans complément manuel.
- lot1 — S4 : documents (tirage principal) : cible 10, obtenu 9. Le cadre ne permet pas d'atteindre la cible ; arrêt sans complément manuel.
- lot1 — S4 : documents de réserve : cible 5, obtenu 0. Le cadre ne permet pas d'atteindre la cible ; arrêt sans complément manuel.
- lot2 — S1 : documents de réserve : cible 5, obtenu 3. Le cadre ne permet pas d'atteindre la cible ; arrêt sans complément manuel.
- lot2 — S2 : documents de réserve : cible 5, obtenu 1. Le cadre ne permet pas d'atteindre la cible ; arrêt sans complément manuel.
- lot2 — S4 : documents de réserve : cible 5, obtenu 3. Le cadre ne permet pas d'atteindre la cible ; arrêt sans complément manuel.
- lot2 — S4 : segments du document LOT2-FR0000934325-FR-Rapport-8b48b254 (principal + réserve) : cible 5, obtenu 3. Le cadre ne permet pas d'atteindre la cible ; arrêt sans complément manuel.

## 7. Auto-contrôles internes

- aucun segment_id en double : OK — 478 lignes, 478 segment_id distincts
- aucune unité tirée deux fois dans une strate : OK — 96 couples (strate, unité)
- aucun document exclu du cadre dans le tirage : OK 
- tous les segments tirés sont perimetre_v2 = oui dans leur unité : OK 
- segments.jsonl contigu par document : OK — 605916 lignes lues, 328302 lignes de doublons non référence ignorées

| Lot | Strate | Documents principal | Documents réserve | Segments principal (docs principaux) | Segments réserve (docs principaux) | Segments des docs de réserve |
|---|---|---|---|---|---|---|
| lot1 | S1 | 10 | 1 | 20 | 30 | 5 |
| lot1 | S2 | 7 | 0 | 14 | 21 | 0 |
| lot1 | S3 | 9 | 0 | 18 | 27 | 0 |
| lot1 | S4 | 9 | 0 | 18 | 27 | 0 |
| lot2 | S1 | 12 | 3 | 24 | 36 | 15 |
| lot2 | S2 | 12 | 1 | 24 | 36 | 5 |
| lot2 | S3 | 12 | 5 | 24 | 36 | 25 |
| lot2 | S4 | 12 | 3 | 24 | 36 | 13 |

## 6 bis. Champs d'affichage (v3)

- `texte_affichage` : texte_original dont chaque ligne est d'abord débarrassée de ses blancs de début et de fin, puis dont chaque suite de 5 blancs ou plus (hors saut de ligne : espace, espace insécable U+00A0, espaces Unicode tels que U+2007 et U+202F, tabulation) est remplacée par «  |  » (deux espaces, barre verticale, deux espaces). Le retrait des blancs de bord est fait avant le remplacement, pour qu'une colonne en début de ligne ne laisse pas une barre isolée en tête. Les sauts de ligne sont conservés.
- `segment_precedent` / `segment_suivant` : texte_affichage des segments d'ordre immédiatement inférieur et supérieur de la même unité documentaire, quel que soit leur périmètre ; vide s'il n'y en a pas. Pour les unités découpées d'un fichier composite (Colville), « même unité » veut dire l'unité découpée : un voisin situé sur une page d'une autre unité (par exemple le segment de la page 4 pour le dernier segment du KID pages 1-3) est laissé vide.
- Ces champs ne sont lus qu'après le tirage ; ils ne modifient ni texte_original, ni n_mots, ni aucune règle ni le tirage.


## 8. Anomalies

- Aucune.

## 9. Effet de l'ordre des règles (suppression de « 5 espaces »)

Rédigé le 17/11/2026 21:57 (heure d'Europe/Luxembourg) par analyse_v3.py, par comparaison segment par segment de `tirage_v2/segments_perimetre_v2.csv` (lu sans modification) et de `tirage_v3/segments_perimetre_v2.csv` (277614 segments des unités documentaires, mêmes segment_id dans les deux versions).

Segments que la v2 classait « exclusion générale : 5 espaces consécutifs ou plus » : 48119 au total, dont 42844 dans des unités du cadre. Comme la règle « chiffres » est appliquée avant, aucun d'eux ne peut devenir « chiffres » ; ils passent aux règles suivantes : « moins de 4 mots », puis « texte identique », sinon « oui » avec leur règle de structure.

| Nouvelle règle (v3) | Tous segments | Dans le cadre |
|---|---|---|
| rapport : performance | 11868 | 10637 |
| prospectus : partie générale (retour sur un intitulé d'annexe en haut de page) | 6393 | 5504 |
| exclusion générale : texte identique à un segment déjà retenu dans l'unité | 5963 | 5061 |
| rapport : section non classée, gardée (cas non tranché) | 4724 | 4603 |
| prospectus : partie générale | 4349 | 4088 |
| prospectus : autre compartiment → oui, cas non tranché (section propre au fonds non repérée) | 3801 | 2723 |
| prospectus : partie générale (fin d'annexe-liste, titre en haut de page) | 3054 | 2863 |
| rapport : commentaire de gestion | 2374 | 2374 |
| type toujours inclus (KID, fiche locale, factsheet, bulletin) | 2028 | 1658 |
| rapport : frais effectifs (titre complet) | 1574 | 1496 |
| prospectus : section propre au fonds (nom dans le titre) | 1332 | 1303 |
| prospectus : section propre au fonds (ISIN dans le titre) | 533 | 533 |
| avis : type non visé par 4.3, gardé (cas non tranché, hors cadre) | 125 | 0 |
| exclusion générale : moins de 4 mots | 1 | 1 |
| **Total** | 48119 | 42844 |

Par strate (unités du cadre), anciens segments « 5 espaces » devenus « oui » / restés « non » :

| Lot | Strate | Devenus oui | Restés non (texte identique ou moins de 4 mots) |
|---|---|---|---|
| lot1 | S1 | 468 | 0 |
| lot1 | S2 | 148 | 5 |
| lot1 | S3 | 13062 | 1005 |
| lot1 | S4 | 17077 | 3078 |
| lot2 | S1 | 425 | 0 |
| lot2 | S2 | 586 | 3 |
| lot2 | S3 | 3952 | 497 |
| lot2 | S4 | 2064 | 474 |

Effet en chaîne de la règle « texte identique » : 41 autres segments (dont 40 dans le cadre) changent de règle. Ils étaient « oui » en v2 et deviennent « texte identique » en v3, parce qu'un segment plus haut dans l'unité au texte identique, auparavant exclu par « 5 espaces », est maintenant retenu. Aucun autre changement de règle.

| Règle v2 | Règle v3 | Segments | Dans le cadre |
|---|---|---|---|
| prospectus : partie générale (fin d'annexe-liste, titre en haut de page) | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 9 | 9 |
| rapport : performance | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 8 | 8 |
| prospectus : partie générale | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 5 | 5 |
| prospectus : section propre au fonds (nom dans le titre) | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 5 | 5 |
| rapport : frais effectifs (titre complet) | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 5 | 5 |
| prospectus : partie générale (retour sur un intitulé d'annexe en haut de page) | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 4 | 4 |
| rapport : commentaire de gestion | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 2 | 2 |
| type toujours inclus (KID, fiche locale, factsheet, bulletin) | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 2 | 2 |
| prospectus : autre compartiment → oui, cas non tranché (section propre au fonds non repérée) | exclusion générale : texte identique à un segment déjà retenu dans l'unité | 1 | 0 |
