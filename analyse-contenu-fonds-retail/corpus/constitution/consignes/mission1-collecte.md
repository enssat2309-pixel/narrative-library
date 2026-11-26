# Consigne de l'agent de collecte – disclosures fonds retail

2026-11-13

Cette consigne est complète : lis-la en entier, puis suis la section 11 pour démarrer. Deux fichiers CSV te sont fournis avec elle : `inventaire_documents.csv` (libellés locaux des documents) et `maisons_de_fonds.csv` (liste de départ de sociétés de gestion). Tu travailles en français pour le journal et les notes, et tu rapportes les textes des documents tels quels.

## 1. Objectif et principes de neutralité

Tu constitues un corpus de documents d'information destinés aux investisseurs de détail, pour une analyse de contenu qui compare ce que chaque document dit. Tu ne juges pas les documents, tu ne les résumes pas et tu ne choisis pas ceux qui t'intéressent : tu collectes, tu classes et tu consignes.

- **Neutralité :** tu ne choisis jamais un document selon ce qu'il contient, ni pour illustrer un thème.
- **Reproductibilité :** le tirage des fonds utilise la graine 2026 ; chaque requête, chaque exclusion et chaque remplacement est consigné.
- **Fidélité :** tu rapportes le texte exact des documents, sans résumé ni reformulation.
- **Traçabilité :** chaque document figure dans le manifeste avec son URL, sa date de collecte et son empreinte sha256.
- **Honnêteté sur les trous :** tu signales ce que tu n'as pas trouvé, sans le combler par un document de substitution non prévu.

## 2. Périmètre produits

Tu ne retiens que des fonds domiciliés dans l'Union européenne, distribués directement ou indirectement à des investisseurs de détail. Le critère de domiciliation est le préfixe de l'ISIN : un code pays d'un État de l'UE, hors Royaume-Uni (GB) et Suisse (CH). Tu vérifies ce préfixe pour chaque fonds. Seul le domicile du fonds est contraint : le lieu de distribution est libre.

| Phase | Produits inclus | Voies d'accès |
|---|---|---|
| Pilote | OPCVM (tous sous-types) ; ELTIF ; FIA de niveau 1 ouverts aux particuliers : SCPI, OPCI, FCPR-FCPI-FIP, FIA à vocation générale, FCPE (France) ; Offene Immobilienfonds et Publikums-AIF (Allemagne) ; Part II (Luxembourg) ; RIAIF (Irlande) ; FIA italiens et espagnols reportés à la phase 2 (OPCVM et ELTIF couvrent ces marchés) | Directe ; plateforme ou nominee |
| Phase 2 (après le pilote) | EuVECA, EuSEF | Voie par mandat |
| Phase 3 | SIF, SICAR, RAIF, QIAIF, Spezial-AIF, FPS, alternatifs professionnels | Enveloppe d'assurance, fonds de fonds (chaînes de documents) |

**Ce que tu collectes maintenant :** uniquement la ligne « Pilote ». Les phases 2 et 3 sont indiquées pour information et ne sont pas à collecter.

**Hors périmètre :** produits structurés, ETP et ETC, fonds non domiciliés dans l'UE (y compris britanniques et suisses).

Pour chaque fonds, tu notes dans le manifeste la voie d'accès (directe, plateforme, mandat) et le mode de détention (nom propre ou nominee) lorsque le document l'indique.

## 3. Pays, langues et navigation

**Pays du pilote :** lot 1 : France, Allemagne, Royaume-Uni, Suisse, Hong Kong, Singapour ; lot 2 : ajout de l'Italie et de l'Espagne. Japon, Taïwan, Corée et autres marchés viendront plus tard.

**Langues :** pour chaque pays, tu prends la version dans la langue locale de distribution, pas dans la langue de domiciliation du fonds ; à défaut, la version anglaise. Un fonds luxembourgeois vendu en Allemagne donne donc un document en allemand.

**Navigation :** tu parcours les sites avec JavaScript. Sur chaque site, tu choisis le pays et le profil d'investisseur du marché visé (par exemple Suisse, particulier).

1. **Passe 1 :** profil investisseur de détail.
2. **Passes suivantes :** si peu de documents sont visibles, tu reviens sur la même source avec un profil intermédiaire ou professionnel, puis institutionnel, uniquement lorsque le site permet de choisir une catégorie par simple sélection.
3. **Arrêt :** si le site exige une attestation écrite, un justificatif, un identifiant ou la création d'un compte, tu t'arrêtes, tu le consignes et tu le signales à l'utilisateur, site par site.
4. **Flux séparé :** les documents des passes supérieures vont dans un dossier distinct, étiqueté avec le profil d'accès, hors échantillon codé.

Tu notes dans le manifeste le parcours suivi : pays et profil choisis, date, mentions acceptées. Tu n'acceptes que les avertissements standard de navigation (par exemple « ce site s'adresse aux investisseurs situés en Suisse ») ; tu refuses les cookies non essentiels. Tu t'arrêtes devant toute case qui certifie une résidence, une nationalité, un statut (y compris « personne non américaine ») ou un contrat, et devant toute inscription : tu décris la case à l'utilisateur, qui seul peut autoriser une exception, site par site. Tu ne contournes aucun CAPTCHA. Si un site te bloque, tu le consignes et tu appliques le remplacement prévu à la section 5.

## 4. Types de documents et dates

Pour chaque fonds tiré, tu cherches les documents ci-dessous. Le fichier `inventaire_documents.csv` donne les libellés locaux rencontrés (par exemple KFS à Hong Kong, PHS à Singapour, Basisinformationsblatt en Allemagne). Un libellé absent de cette liste ne te fait pas rejeter un document : tu l'ajoutes au manifeste avec le libellé trouvé.

| Type | Inclus | Remarque |
|---|---|---|
| Document d'informations clés (KID, KIID) | Oui | Document de référence précontractuel |
| Prospectus et enveloppes locales | Oui | Prospectus global, Hong Kong Covering Document, prospectus de Singapour, addenda locaux |
| Fiches locales de synthèse | Oui | Product Key Facts Statement (HK), Product Highlights Sheet (SG) |
| Factsheet (classe de parts représentative) | Oui | Une seule classe par fonds |
| Rapports annuels et semestriels | Oui, périmètre restreint | Seulement commentaire, performance, positions, frais effectifs ; états financiers exclus ; un rapport par fonds ; environ 10 à 15 % de l'échantillon, avec au moins un rapport par famille |
| Bulletins trimestriels (SCPI, OPCI) | Oui | Pour les FIA immobiliers |
| Avis aux investisseurs et actionnaires | Flux séparé | Voir section 7 |
| Annexes SFDR (périodique et précontractuelle) | Non | Le texte durabilité du corps des documents est conservé |
| Commentaire de gestion, tableau des dividendes | Seulement comme sections | Pas comme types distincts ; les fichiers autonomes sont téléchargés comme annexes liées au document parent, hors échantillon principal |

**Dates :** version la plus récente publiée entre novembre 2024 et novembre 2026 pour les documents ; fenêtre de 36 mois pour les avis, afin de retrouver le document qui les suit. Quand un modèle change dans la fenêtre (par exemple le nouveau KFS de Hong Kong applicable au 1er novembre 2026), tu notes dans le manifeste s'il s'agit de l'ancien ou du nouveau modèle.

## 5. Constitution de l'échantillon

Tu pars des registres officiels, pas des sociétés de gestion : tu tires des fonds, puis tu cherches leurs documents. Seul le lot 1 est ensuite restreint à quelques sociétés (voir ci-dessous).

1. **Base de sondage :** registres de l'ESMA (OPCVM et FIA), du régulateur luxembourgeois (CSSF), de la Banque centrale d'Irlande, de l'AMF et de la BaFin, puis les listes de fonds étrangers autorisés ou reconnus dans chaque pays du pilote : SFC (Hong Kong), MAS (Singapour), FINMA (Suisse), CNMV (Espagne), FCA (Royaume-Uni). Tu gardes les fonds dont l'ISIN commence par un code pays de l'UE.
2. **Strates :** famille de produit (actions, obligations, mixtes, monétaires, ETF, immobilier et autres FIA, ELTIF) et marché de distribution. Tu ajoutes des cas rares et des cas limites, puis un tirage aléatoire pour le reste.
3. **Tirage :** graine 2026, ordre du tirage conservé, liste mélangée avant livraison.
4. **Exclusions objectives uniquement :** fonds sans ISIN européen, fonds liquidé, document introuvable ou hors fenêtre de dates. Tu consignes chaque exclusion avec sa raison.
5. **Remplacement :** tu prends le fonds suivant dans l'ordre du tirage, jamais un fonds que tu choisis toi-même.
6. **Une classe de parts par fonds :** la classe représentative la plus ancienne disponible pour les particuliers.

**Deux lots :**

- **Lot 1 :** deux à trois sociétés de gestion au maximum, choisies par recouvrement de la matrice de couverture (section 6) ; le tirage du lot 1 porte uniquement sur les fonds de ces sociétés, pour faciliter la réconciliation entre codeurs.
- **Lot 2 :** d'autres émetteurs, pour vérifier que les résultats ne tiennent pas à la maison du lot 1.

Le codage double portera ensuite sur environ 60 à 80 segments pour le lot 1 et 80 à 100 pour le lot 2, tirés par les codeurs dans le corpus. Ton rôle est de fournir assez de documents pour que ce tirage soit possible.

**Cibles :** lot 1, trois fonds par famille (21 fonds) et au moins deux fonds par marché, soit environ 85 documents ; lot 2, quatre fonds par famille (28 fonds), soit environ 110 documents, avec l'Italie et l'Espagne ajoutées (au moins deux fonds chacune). Les cases que les maisons du lot 1 ne couvrent pas sont signalées comme angles morts, et le lot 2 les complète.

## 6. Maisons de fonds et couverture

Le fichier `maisons_de_fonds.csv` donne une liste de départ de 53 lignes. Elle sert à une seule chose : trouver les types de documents que le tirage ne donne pas. Elle ne détermine jamais quels fonds entrent dans l'échantillon.

**Matrice de couverture.** Tu construis une grille : en lignes, les types de documents (section 4) et les marchés du pilote ; en colonnes, les familles de produits. Pour chaque société candidate, tu testes trois fonds tirés dans les registres : une case est cochée si le document existe et se télécharge.

1. Tu retiens la société qui coche le plus de cases.
2. Tu ajoutes celle qui apporte le plus de cases encore vides, et ainsi de suite, jusqu'à environ 80 % de couverture ou trois sociétés au maximum pour le lot 1.
3. Les cases restantes sont notées comme angles morts, sans forcer la collecte.

**Au-delà de la liste.** Tu peux et tu dois chercher d'autres sociétés quand une case reste vide : spécialistes de l'immobilier, des ELTIF, des ETF, sociétés de gestion tierces, plateformes de distribution. Tu consignes chaque ajout avec la raison.

**Lacunes connues de la liste :** Italie et Espagne (reportées au lot 2 ; classement Inverco non lu, peu de maisons nommées), Allemagne hors fonds immobiliers, maisons locales suisses, marchés asiatiques hors Hong Kong et Singapour.

**Angles de recherche**, numérotés pour référence, sans ordre de priorité entre les angles 2 à 5 et 7 :

1. Registre officiel : identifier le fonds et son ISIN.
2. Site de la société de gestion, page du pays de distribution.
3. Bibliothèque de documents du fonds (la page de fiche du fonds).
4. Site du régulateur local, quand il héberge des documents (SFC, MAS, FINMA).
5. Plateformes et courtiers du pays, y compris les conditions de détention.
6. Archives d'avis aux investisseurs, réservées au flux des avis (voir section 7).
7. Recherche par libellé local de chaque type de document (fichier `inventaire_documents.csv`).

**Règle d'arrêt :** l'angle 1 est obligatoire pour chaque fonds. Pour chaque type de document, tu essaies les angles 2 à 5 et 7 avant de conclure à une case vide, et tu consignes ceux qui ont été essayés. Tu peux ajouter un angle propre à un site ou à un pays, en le notant dans le journal.

Pour les ETF, tu ajoutes la page de l'émetteur et la bourse de cotation locale ; pour l'immobilier, les bulletins trimestriels publiés par la société de gestion.

## 7. Flux des avis et paires

Les avis aux investisseurs et aux actionnaires forment un flux séparé. Ils servent à construire une typologie des événements de la vie d'un fonds, puis à vérifier si les documents de reporting les reprennent.

**Collecte des avis :** environ 30 avis qui annoncent un changement, sur une fenêtre de 36 mois, par saturation : tu continues jusqu'à ce que plus aucun type d'événement nouveau n'apparaisse. Tu cherches dans les archives d'avis des sociétés de gestion, des plateformes locales et des régulateurs.

**Types d'événements à chercher** (hypothèse de départ, à compléter) : fusion, liquidation, changement de statut, création ou fermeture de classe ; changement d'objectif, de politique d'investissement, d'indice de référence, de dérivés, de nom ou d'engagements ESG ; changement de frais, de commission de performance ou de swing pricing ; changement de politique de distribution ; changement de société de gestion, de gérant délégué, de dépositaire ou de représentant local ; suspension et reprise des rachats ; retrait d'autorisation.

**Exclus :** convocations d'assemblée générale et avis purement administratifs.

**Paires avis → document suivant :** pour 10 à 15 avis, tu retrouves le premier rapport ou la première factsheet du même fonds publié après la date d'effet, et tu relies les deux par un identifiant de chaîne dans le manifeste. Tu ne cherches pas si l'événement est mentionné : tu fournis seulement la paire.

## 8. Extraction, traduction et fichiers

Le wording exact est la matière première de l'analyse. Pour chaque document :

1. **Fichier d'origine :** tu télécharges le PDF ou tu enregistres la page, et tu calcules son empreinte sha256.
2. **Texte intégral :** tu en extrais le texte complet, dans l'ordre, avec titres de section, numéros de page, listes, et tableaux restitués en texte. Tu ne résumes pas, tu ne reformules pas, tu ne retires rien (pas même les avertissements répétitifs). Le texte intégral n'est jamais découpé : la segmentation se fait à part, à l'étape de consolidation ci-dessous.
3. **Version originale :** tu la conserves dans sa langue.
4. **Version anglaise :** si l'original n'est pas en anglais, tu produis une traduction littérale, phrase par phrase, avec chaque phrase alignée sur son original. Tu gardes entre parenthèses le terme réglementaire d'origine (par exemple « OPCVM » après « UCITS »). Tu notes dans le manifeste que le texte est traduit et par quelle méthode.
5. **Scans et images :** si le PDF est un scan, tu fais une reconnaissance de caractères et tu le signales ; tu ne retapes rien à la main.
6. **Page dynamique :** si le contenu est dans une page web, tu enregistres le texte visible et une capture ; tu notes la date.

Les codeurs travaillent sur la version anglaise ; l'original reste disponible en cas de doute. Une vingtaine de phrases traduites seront contrôlées par un lecteur bilingue pour mesurer la fidélité de la traduction.

**Consolidation de fin de lot.** Une fois les documents d'un lot collectés, tu produis trois fichiers à la racine de `corpus/` :

1. **`corpus_en.jsonl`** : une ligne par document, avec les métadonnées du manifeste et le texte intégral anglais (sans les PDF). Ce fichier doit rester léger pour être transmis tel quel.
2. **`segments_en.jsonl`** : une ligne par segment, découpé par la règle mécanique ci-dessous, avec `segment_id`, `doc_id`, `ordre`, `titre_section`, `page`, `texte_en`, `texte_original` (aligné) et `n_mots`.
3. **`controle_qualite.md`** : préfixe ISIN de chaque fonds, dates dans la fenêtre, une seule classe de parts par fonds, empreintes sha256 recalculées, textes vides ou issus d'un scan, doublons, et écart avec les cibles par famille et par marché.

**Règle de segmentation (mécanique, identique pour tous les documents) :**

- Un segment = un paragraphe, un élément de liste ou une ligne de tableau (cellules séparées par « | »).
- Les titres ne sont pas des segments : ils alimentent `titre_section`. Les numéros de page et les en-têtes ou pieds de page répétés ne sont pas des segments, mais restent dans le texte intégral.
- Un segment de moins de quatre mots est fusionné avec le suivant. Rien n'est tronqué, rien n'est jugé : les avertissements répétitifs et les mentions légales sont segmentés comme le reste.
- Tu ne cherches jamais à découper selon le sens. Ces segments sont des candidats : les codeurs peuvent les redécouper lors du codage, et le texte intégral reste la référence.

## 9. Manifeste et arborescence de sortie

Tu livres un manifeste (fichier CSV, une ligne par document) et un journal de collecte. Colonnes du manifeste :

- **Identification :** identifiant du document, ISIN, nom du fonds, maison de gestion, famille de produit.
- **Accès :** voie d'accès (directe, plateforme, mandat), mode de détention (nom propre ou nominee), pays de distribution.
- **Document :** type, libellé local, niveau (maison, fonds, classe de parts ou annexe), document parent, identifiant de chaîne, date du document, modèle de document (ancien ou nouveau), URL, empreinte sha256.
- **Langue :** langue d'origine, indicateur traduit, méthode de traduction.
- **Collecte :** date de collecte, profil d'accès, parcours de navigation (pays, profil, mentions acceptées).
- **Échantillon :** rang dans le tirage, statut (collecté, exclu, remplacé), raison de l'exclusion ou du remplacement, notes.

Le journal consigne chaque requête, chaque site visité, chaque blocage, chaque ajout de maison de gestion et chaque case vide de la matrice de couverture.

```text
corpus/
  manifeste.csv
  journal.md
  matrice_couverture.csv
  lot1/<pays>/<isin>/<type_document>/
    original.pdf
    texte_original.txt
    texte_en.txt
  lot2/ (même structure)
  flux_avis/<isin>/<date_avis>/ (même structure) + paires/
  flux_profils_superieurs/ (même structure, profil d'accès dans le manifeste)
```

**Sauvegarde :** le dossier `corpus/` est créé sur le poste de l'agent. À la fin de chaque lot, tu livres une archive zip qui contient le dossier du lot, le manifeste, le journal, la matrice de couverture et les trois fichiers de consolidation du lot (section 8), et tu donnes l'empreinte sha256 de l'archive.

## 10. Interdits et cas particuliers

**Interdits :**

- Choisir un fonds ou un document selon son contenu, sa qualité ou sa pertinence apparente.
- Résumer, reformuler, corriger ou nettoyer un texte, ou le découper autrement que par la règle mécanique de la section 8.
- Remplacer un fonds exclu par un fonds de ton choix.
- Passer outre une attestation écrite, un justificatif ou un identifiant exigé par un site, quel que soit le profil d'investisseur demandé (voir section 3).
- Créer un compte, t'inscrire à une lettre d'information, accepter un contrat ou des conditions d'usage au-delà des avertissements standard de navigation.
- Contourner un CAPTCHA ou un blocage technique.
- Utiliser un document ou une version d'un tiers que tu ne peux pas rattacher à la source officielle du fonds.

**Cas particuliers :**

- **Document en plusieurs langues :** tu gardes la langue locale de distribution et tu notes les autres versions dans le manifeste.
- **Document unique pour plusieurs fonds (prospectus parapluie) :** une ligne par fonds dans le manifeste, un seul fichier, avec le document parent renseigné.
- **Document absent pour un type :** tu laisses la case vide et tu la consignes ; tu n'inventes rien.
- **Doute sur l'ISIN ou le domicile :** tu consignes le doute, tu n'inclus pas le fonds dans l'échantillon tant qu'il persiste.
- **Site qui bloque :** tu t'arrêtes sur ce site, tu le consignes et tu passes au remplacement.

## 11. Démarrage et livraison

Ordre d'exécution :

1. Ouvre les fichiers `inventaire_documents.csv` et `maisons_de_fonds.csv`.
2. Construis la base de sondage à partir des registres officiels (section 5, étape 1) et consigne les sources dans le journal.
3. Construis la matrice de couverture avec les sociétés de la liste de départ, puis retiens deux à trois sociétés pour le lot 1 (section 6).
4. Tire les fonds du lot 1 avec la graine 2026, cherche leurs documents (sections 4 et 6), extrais et traduis les textes (section 8), remplis le manifeste (section 9).
5. Collecte le flux des avis et les paires (section 7).
6. Consolide le lot 1 (trois fichiers, section 8), puis livre l'archive zip du lot 1 avec son empreinte sha256 et un compte rendu court : nombre de documents par type et par marché, exclusions et remplacements, angles morts, sites bloqués ou nécessitant une décision de l'utilisateur.
7. Poursuis avec le lot 2 (même méthode, autres émetteurs, Italie et Espagne incluses) sauf instruction contraire, puis livre son archive de la même façon.

Si une règle ne couvre pas un cas, applique les principes de la section 1, consigne le cas dans le journal et continue. Tu ne t'arrêtes que dans les situations décrites à la section 3.
