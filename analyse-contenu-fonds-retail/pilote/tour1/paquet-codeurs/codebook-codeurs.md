# Codebook du pilote – version 3 (pour les codeurs)

Ce document est la seule référence pour coder. Il contient : la liste des 52 codes (section 1), les 23 règles de frontière entre codes voisins (section 2) et les facettes (section 3). Les exemples sont des formulations types, rédigées pour illustrer : ils ne viennent pas des segments à coder.

## 1. Les codes


### A – Le produit et le document

**A1 – Identification.** Ce qui désigne le produit lui-même.

- Inclut : Nom, ISIN, classe de parts, devise, capitalisation/distribution, date de lancement.
- Exclut : Conditions d'accès de la classe (→ G3). Type de document (→ A3).
- Exemple : « Fonds X, classe de parts C, EUR, capitalisation. »
- Règles de frontière : 13, 14, 21

**A2 – Acteurs.** Les entités nommées et leur rôle.

- Inclut : Société de gestion, dépositaire, initiateur, distributeur, autorité de contrôle.
- Exclut : Mécanismes de contrôle ou de supervision (→ A5).
- Exemple : « Société de gestion : X. Dépositaire : Y. »
- Règles de frontière : 15

**A3 – Nature et statut du document.** Ce qui désigne le document et non le produit.

- Inclut : Type (KID, KIID, factsheet), « communication publicitaire », date de mise à jour, langue.
- Exclut : Caractéristiques du produit (→ A1).
- Exemple : « Ce document est une communication publicitaire. »
- Règles de frontière : 13

**A4 – Événements et modifications du produit.** Faits datés qui changent le produit.

- Inclut : Fusion, changement de politique, de société de gestion, de frais, liquidation décidée.
- Exclut : Durée de vie prévue au contrat (→ B7).
- Exemple : « Le fonds a été fusionné avec X le 1er mars. »
- Règles de frontière : 11

**A5 – Gouvernance et conflits d'intérêts.** Mécanismes de contrôle, de supervision et de gestion des conflits.

- Inclut : Conseil indépendant, politique de rémunération du personnel, gestion des conflits, comité de valorisation.
- Exclut : Rémunération du distributeur (→ F3). Noms des acteurs (→ A2).
- Exemple : « Un conseil indépendant supervise la gestion et les conflits d'intérêts. »
- Règles de frontière : 15, 16


### B – Ce que fait le produit

**B1 – Objectif.** Ce que le produit cherche à atteindre, décrit de façon neutre.

- Inclut : Objectif de gestion, indice de référence visé, type de rendement recherché.
- Exclut : Phrase qui défend le produit (→ I3). Moyens mis en œuvre (→ B2, B3).
- Exemple : « Le fonds vise une croissance du capital à long terme. »
- Règles de frontière : —

**B2 – Politique et univers.** Ce que le fonds peut détenir.

- Inclut : Classes d'actifs, zones, secteurs, notations, limites d'investissement propres au fonds.
- Exclut : Technique de mise en œuvre (→ B5). Manière de choisir (→ B3).
- Exemple : « Investit au moins 70 % en actions européennes de grandes capitalisations. »
- Règles de frontière : 9, 10

**B3 – Processus et style.** Comment le gérant choisit et gère.

- Inclut : Analyse fondamentale, style value/growth, gestion active ou passive, règles d'allocation.
- Exclut : Ce qui peut être détenu (→ B2).
- Exemple : « Sélection de titres par analyse fondamentale, approche value. »
- Règles de frontière : 9

**B4 – Rôle de l'indice.** Place de l'indice dans la gestion.

- Inclut : Réplication (physique, synthétique), référence de comparaison, univers dérivé de l'indice.
- Exclut : Chiffres de performance de l'indice (→ E2).
- Exemple : « Réplication physique de l'indice MSCI World. »
- Règles de frontière : 10

**B5 – Instruments et techniques.** Moyens utilisés pour mettre en œuvre la stratégie.

- Inclut : Dérivés, couverture de change, levier, prêts de titres, mises en pension.
- Exclut : Actif détenu pour l'exposition (→ B2).
- Exemple : « Peut utiliser des dérivés pour se couvrir ou pour du levier. »
- Règles de frontière : 10

**B6 – Mécanique contractuelle et prestations d'assurance.** Formule de paiement et conditions contractuelles.

- Inclut : Barrières, plafonds, coupons, remboursement anticipé, garanties, prestations en cas de décès.
- Exclut : Date d'échéance et prorogation (→ B7).
- Exemple : « Remboursement : 100 % du capital + 60 % de la hausse de l'indice, plafonnée à 40 %. »
- Règles de frontière : 12

**B7 – Cycle de vie et fin de produit.** Durée de vie prévue au contrat et fin du produit.

- Inclut : Durée, prorogation, période d'investissement, échéance, liquidation, fusion prévue.
- Exclut : Durée de détention conseillée (→ G2). Fait daté (→ A4).
- Exemple : « Le fonds a une durée de 8 ans, prorogeable deux fois d'un an. »
- Règles de frontière : 11, 12

**B8 – Valorisation et calcul de la VL.** Comment la valeur est établie.

- Inclut : Méthode de valorisation, fréquence de calcul, experts indépendants, traitement des actifs non cotés.
- Exclut : Publication et fréquence de la VL pour l'investisseur (→ G3).
- Exemple : « La valeur liquidative est calculée par un expert indépendant, chaque trimestre. »
- Règles de frontière : —


### C – Le portefeuille

**C1 – Composition observée.** Contenu du portefeuille à une date.

- Inclut : Répartition par actif, secteur, pays, principales lignes, au jj/mm.
- Exclut : Règles permanentes de composition (→ B2).
- Exemple : « Au 30/09, 62 % actions, 30 % obligations. »
- Règles de frontière : —

**C2 – Mouvements de gestion.** Opérations de gestion sur la période.

- Inclut : Achats, ventes, arbitrages, changements d'allocation du trimestre.
- Exclut : Explication de la performance (→ E3).
- Exemple : « Nous avons allégé les valeurs technologiques au profit de la santé. »
- Règles de frontière : —


### D – Les risques

**D1 – Indicateur synthétique.** Échelle de risque du document.

- Inclut : SRI (1-7), SRRI, explication de la classe de risque.
- Exclut : Message général gain/perte sans échelle (→ E4).
- Exemple : « Nous avons classé ce produit dans la classe de risque 4 sur 7. »
- Règles de frontière : —

**D2 – Risque de marché.** Dépendance à l'évolution des marchés.

- Inclut : Actions, taux, change, matières premières, volatilité.
- Exclut : Perte de capital et protection (→ D6).
- Exemple : « La valeur du fonds dépend de l'évolution des marchés actions. »
- Règles de frontière : 5

**D3 – Risque de crédit et de contrepartie.** Défaut d'entités sous-jacentes ou de contreparties.

- Inclut : Crédit des émetteurs détenus, contrepartie d'un swap, d'un prêt de titres.
- Exclut : Défaillance de l'initiateur ou de l'émetteur du produit (→ D7).
- Exemple : « La contrepartie du swap peut ne pas honorer ses engagements. »
- Règles de frontière : 6

**D4 – Risque de liquidité.** Risque énoncé de ne pas pouvoir vendre ou racheter.

- Inclut : Difficulté de vendre en période de tension, absence de marché secondaire, sans seuil ni durée.
- Exclut : Préavis, plafonds, suspension chiffrés (→ G4).
- Exemple : « Le fonds peut être difficile à vendre en cas de tensions de marché. »
- Règles de frontière : 2

**D5 – Risque opérationnel, juridique, fiscal.** Risques liés au fonctionnement, au droit ou à la fiscalité.

- Inclut : Erreur de gestion, défaillance du dépositaire, changement de loi, changement fiscal.
- Exclut : Description du traitement fiscal (→ G5).
- Exemple : « Un changement de législation fiscale pourrait affecter le rendement. »
- Règles de frontière : 7

**D6 – Perte en capital et protection.** Possibilité de perdre et niveau de protection.

- Inclut : Capital non garanti, garantie partielle, absence de protection.
- Exclut : Compromis rendement/risque général (→ E4).
- Exemple : « Vous pouvez perdre tout ou partie de votre capital. »
- Règles de frontière : 5

**D7 – Défaillance de l'initiateur.** Risque que l'entité qui fabrique ou garantit le produit fasse défaut.

- Inclut : Risque de l'émetteur d'une note, de l'assureur, du garant.
- Exclut : Contreparties et émetteurs sous-jacents (→ D3).
- Exemple : « L'émetteur de cette note peut faire défaut et vous perdriez votre investissement. »
- Règles de frontière : 6

**D8 – Mesures statistiques de risque.** Mesures observées sur le passé.

- Inclut : Volatilité, VaR, pire baisse, durée de récupération, ratio de Sharpe.
- Exclut : Scénarios projetés (→ E1).
- Exemple : « Perte maximale historique : 22 %, récupérée en 14 mois. »
- Règles de frontière : 4


### E – La performance et les revenus

**E1 – Scénarios.** Projections chiffrées de performance.

- Inclut : Scénarios de tensions, défavorable, intermédiaire, favorable.
- Exclut : Mesures du passé (→ D8).
- Exemple : « Scénario de tensions : vous pourriez perdre 41 % après 1 an. »
- Règles de frontière : 4

**E2 – Performance passée.** Chiffres de rendement passé.

- Inclut : Performances annuelles, cumulées, de l'indice, graphiques de périodes passées.
- Exclut : Cause de la performance (→ E3).
- Exemple : « Le fonds a gagné 8 % en 2025. »
- Règles de frontière : 17, 23

**E3 – Explication et attribution.** Pourquoi la performance a eu lieu.

- Inclut : Contributions positives et négatives, facteurs de la période.
- Exclut : Mouvements de gestion (→ C2).
- Exemple : « Porté par la technologie. »
- Règles de frontière : 17

**E4 – Compromis gain/perte générique.** Message général sur le lien rendement/risque.

- Inclut : « plus de rendement potentiel, plus de risque ».
- Exclut : Échelle de risque (→ D1). Perte de capital (→ D6).
- Exemple : « Un rendement potentiel plus élevé s'accompagne d'un risque plus élevé. »
- Règles de frontière : 5

**E5 – Notations, classements, distinctions.** Appréciations par un tiers.

- Inclut : Notes Morningstar, classements, prix, y compris notes de durabilité (avec marqueur durabilité).
- Exclut : Label ou classification déclarés par le produit (→ H1).
- Exemple : « Note Morningstar : 4 étoiles. »
- Règles de frontière : 17

**E6 – Revenus et distributions.** Politique, fréquence, taux, origine et dates des revenus distribués aux investisseurs (règle ou montants observés).

- Inclut : Politique de distribution ou de capitalisation ; fréquence ; taux ou montant distribué ; origine (revenu ou capital) ; dates de paiement ; historique des dividendes.
- Exclut : Type de part comme simple identifiant de classe (→ A1) ; fiscalité des distributions (→ G5) ; rendement total passé (→ E2).
- Exemple : « Le fonds distribue chaque année au moins 85 % du revenu net. »
- Règles de frontière : 21, 22, 23


### F – Les coûts

**F1 – Structure des frais.** Type et niveau de chaque frais.

- Inclut : Frais d'entrée, de sortie, courants, de transaction, commission de performance.
- Exclut : Impact global (→ F2). Rémunération du distributeur (→ F3).
- Exemple : « Frais courants : 1,2 % par an. »
- Règles de frontière : 8

**F2 – Incidence des coûts.** Impact global des coûts sur le rendement.

- Inclut : Réduction du rendement en % ou en euros selon la durée de détention.
- Exclut : Niveau de chaque frais (→ F1).
- Exemple : « Après 5 ans, l'incidence des coûts est de 2,1 % par an, soit 840 €. »
- Règles de frontière : 8

**F3 – Coûts de distribution.** Rémunération du distributeur ou de l'intermédiaire.

- Inclut : Rétrocessions, commissions de placement, avantages.
- Exclut : Gestion des conflits d'intérêts (→ A5).
- Exemple : « Nous versons à votre conseiller une rétrocession de 0,5 % par an. »
- Règles de frontière : 8, 16


### G – L'investisseur et ses conditions

**G1 – Investisseur visé.** Profil de la personne pour qui le produit est conçu.

- Inclut : Connaissances, capacité à supporter une perte, objectif, restriction par type d'investisseur.
- Exclut : Place dans un portefeuille (→ I4).
- Exemple : « Pour des investisseurs capables de supporter une perte. »
- Règles de frontière : 1, 14

**G2 – Horizon.** Durée de détention conseillée.

- Inclut : Période de détention recommandée (RHP).
- Exclut : Durée de vie du produit (→ B7). Conséquences d'une sortie anticipée (→ G4).
- Exemple : « Période de détention recommandée : 5 ans. »
- Règles de frontière : 3, 11

**G3 – Souscription et rachat.** Conditions normales pour entrer et sortir.

- Inclut : Minimum, fréquence de souscription, publication de la VL, délai de règlement.
- Exclut : Plafonds, préavis, suspension (→ G4). Appels de capital (→ G6).
- Exemple : « Souscription minimale initiale : 100 000 €. »
- Règles de frontière : 14

**G4 – Sortie anticipée et liquidité réelle.** Conditions pratiques et limites de sortie.

- Inclut : Préavis, plafonds de rachat, suspension, pénalités, outils de gestion de la liquidité, avec seuil ou durée.
- Exclut : Risque général sans seuil ni durée (→ D4).
- Exemple : « Le gestionnaire peut plafonner les rachats à 10 % de l'actif par trimestre. »
- Règles de frontière : 2, 3

**G5 – Fiscalité.** Traitement fiscal pour l'investisseur.

- Inclut : Imposition des plus-values, enveloppe fiscale, dépendance à la situation personnelle.
- Exclut : Risque de changement fiscal (→ D5).
- Exemple : « Les plus-values sont imposées au taux de 30 %. »
- Règles de frontière : 7, 22

**G6 – Engagement de capital et appels de fonds.** Obligations de verser le capital par tranches.

- Inclut : Montant engagé, calendrier d'appels, conséquences d'un défaut de versement.
- Exclut : Souscription simple (→ G3).
- Exemple : « Le capital est appelé en plusieurs tranches sur 3 ans. »
- Règles de frontière : —


### H – La durabilité

**H1 – Classification, labels, engagements.** Ce que le produit déclare sur sa durabilité.

- Inclut : Article 8 ou 9 SFDR, labels, part minimale d'investissements durables (engagement).
- Exclut : Note d'un tiers (→ E5). Résultat mesuré (→ H3).
- Exemple : « Produit classé article 8 SFDR. Au moins 20 % d'investissements durables. »
- Règles de frontière : 18

**H2 – Méthodes extra-financières.** Comment la durabilité est intégrée.

- Inclut : Exclusions, notations ESG, engagement actionnarial, vote.
- Exclut : Engagement chiffré (→ H1). Résultat (→ H3).
- Exemple : « Exclut les producteurs de charbon thermique. »
- Règles de frontière : 18

**H3 – Indicateurs et résultats.** Résultats mesurés de durabilité.

- Inclut : Empreinte carbone, part alignée effective, PAI.
- Exclut : Seuil promis (→ H1).
- Exemple : « Empreinte carbone : 85 tCO2/M€ au 31/12. »
- Règles de frontière : 18


### I – Le discours de marché et commercial

**I1 – Revue de marché.** Regard sur la période écoulée, sans parler du produit.

- Inclut : Mouvements de marché, événements macroéconomiques passés.
- Exclut : Phrase qui défend le produit (→ I3).
- Exemple : « Les marchés actions ont progressé de 5 % ce trimestre. »
- Règles de frontière : 19

**I2 – Perspectives.** Regard sur l'avenir du marché.

- Inclut : Anticipations, scénarios macro, convictions de marché.
- Exclut : Scénarios chiffrés du produit (→ E1).
- Exemple : « Nous anticipons une baisse des taux d'ici fin d'année. »
- Règles de frontière : 19

**I3 – Argumentaire de vente.** Phrase qui cherche à convaincre sur le produit.

- Inclut : Atouts, opportunités, positionnement favorable.
- Exclut : Description neutre (→ B1). Revue de marché (→ I1).
- Exemple : « Le fonds est bien placé pour profiter de ce contexte. »
- Règles de frontière : 19

**I4 – Rôle dans le portefeuille.** Place du produit dans un portefeuille.

- Inclut : Diversifieur, satellite, socle, corrélation avec d'autres classes d'actifs.
- Exclut : Profil de l'investisseur (→ G1).
- Exemple : « Peut servir de socle d'un portefeuille diversifié. »
- Règles de frontière : 1


### J – Mentions transversales

**J1 – Avertissements génériques.** Formules standard attachées aux chiffres ou au document.

- Inclut : « les performances passées ne préjugent pas des performances futures », mise en garde générale, alerte de complexité.
- Exclut : Avertissement propre au produit (→ code de risque D).
- Exemple : « Les performances passées ne préjugent pas des performances futures. »
- Règles de frontière : 20

**J2 – Renvois.** Indications vers d'autres documents ou sources d'information.

- Inclut : Prospectus, site internet, rapports, suivi et reporting investisseur.
- Exclut : Source d'un chiffre (→ J5).
- Exemple : « Pour plus d'informations, consultez le prospectus. »
- Règles de frontière : 20

**J3 – Réclamations.** Comment contester ou signaler.

- Inclut : Procédure de réclamation, médiateur, contacts.
- Exclut : Contact général de la société (→ A2).
- Exemple : « Pour toute réclamation, contactez le service clientèle. »
- Règles de frontière : —

**J4 – Restrictions de commercialisation.** Qui ne peut pas acheter le produit, où.

- Inclut : Pays autorisés, interdiction aux personnes américaines, restrictions réglementaires.
- Exclut : Restriction par type d'investisseur (→ G1).
- Exemple : « Ce fonds n'est pas disponible aux personnes américaines. »
- Règles de frontière : —

**J5 – Sources et méthodes.** Origine et méthode des chiffres.

- Inclut : Source de données, date d'arrêté, méthode de calcul.
- Exclut : Renvoi vers un document (→ J2).
- Exemple : « Source : Morningstar, données au 30/09. »
- Règles de frontière : 20


### Z – Codes résiduels

**Z1 – Résiduel.** Segment lisible et informatif qui ne rentre dans aucun code.

- Inclut : Toute information utile à l'investisseur non classable ailleurs.
- Exclut : Mobilier de page ou contenu sans information (→ Z2).
- Exemple : —
- Règles de frontière : —

**Z2 – Hors périmètre.** Contenu sans lien avec l'information à l'investisseur.

- Inclut : Numéros de page, mentions techniques, éléments de mise en page.
- Exclut : Tout contenu informatif (→ code correspondant ou Z1).
- Exemple : « Page 2 sur 3. »
- Règles de frontière : —

## 2. Règles de frontière

Quand un segment hésite entre deux codes voisins, la règle ci-dessous décide.

| N° | Codes | Règle |
|---|---|---|
| 1 | G1 / I4 | Profil de la personne → G1. Place du produit dans un portefeuille → I4. |
| 2 | D4 / G4 | Risque énoncé sans seuil ni durée → D4. Conditions pratiques de sortie, ou segment avec seuil ou durée → G4. |
| 3 | G2 / G4 | Durée recommandée → G2. Conséquences d'une sortie anticipée → G4. Si les deux sont présents : code principal et code secondaire (pas de découpage dans ce pilote). |
| 4 | D8 / E1 | Mesure observée sur le passé → D8. Projection chiffrée → E1. |
| 5 | D2 / D6 / E4 | Dépendance au marché → D2. Perte de capital et protection → D6. Compromis rendement/risque général → E4. |
| 6 | D3 / D7 | Entité qui fabrique ou garantit le produit → D7. Entités sous-jacentes et contreparties → D3. |
| 7 | D5 / G5 | Risque de changement fiscal → D5. Description du traitement fiscal → G5. |
| 8 | F1 / F2 / F3 | Type et niveau du frais → F1. Impact global → F2. Rémunération du distributeur → F3 (marqueur gouvernance = oui si un conflit est décrit). |
| 9 | B2 / B3 | Ce que le fonds peut détenir → B2. Manière de sélectionner et de gérer → B3. |
| 10 | B2 / B5 / B4 | Actif détenu pour l'exposition → B2. Technique ou instrument → B5. Indice et réplication → B4. |
| 11 | B7 / G2 / A4 | Durée de vie au contrat → B7. Durée de détention conseillée → G2. Fait daté → A4. |
| 12 | B6 / B7 | Formule de paiement, barrières, plafonds, coupons → B6. Échéance, prorogation, liquidation → B7. |
| 13 | A1 / A3 | Ce qui désigne le produit → A1. Ce qui désigne le document → A3. |
| 14 | A1 / G3 / G1 | Identifiants et attributs de classe → A1. Conditions d'accès → G3. Restriction selon le type d'investisseur → G1. |
| 15 | A2 / A5 | Noms et rôles → A2. Mécanismes de contrôle, supervision, rémunération du personnel → A5. |
| 16 | A5 / F3 | Montant ou rémunération du distributeur → F3. Gestion des conflits d'intérêts → A5. |
| 17 | E2 / E3 / E5 | Chiffre de performance → E2. Cause → E3. Note ou classement par un tiers → E5. |
| 18 | H1 / H2 / H3 | Classification, label, engagement futur → H1. Méthode → H2. Résultat mesuré → H3. |
| 19 | I1 / I2 / I3 | Avis sur le marché passé → I1, à venir → I2. Phrase qui défend le produit → I3. |
| 20 | J1 / J2 / J5 | Formule standard → J1. Avertissement propre au produit → son code de risque. Renvoi → J2. Source ou méthode de calcul → J5. |
| 21 | E6 / A1 | Le type de part (capitalisation ou distribution) cité comme identifiant de classe → A1. La règle de distribution (fréquence, source, calcul) → E6. |
| 22 | E6 / G5 | Le fait de distribuer, la fréquence et le montant → E6. Le traitement fiscal des distributions → G5. |
| 23 | E6 / E2 | Un taux de distribution ou un montant versé → E6. Une performance totale passée → E2. |

## 3. Facettes

Chaque segment reçoit, en plus de son code principal, quatre facettes. Elles décrivent le segment, indépendamment du code.

**Temporalité**

- `regle` : ce qui est prévu de façon permanente ou générale (politique, conditions, méthode, frais applicables).
- `observe` : un fait ou un chiffre constaté à une date ou sur une période passée (performance 2025, composition au 30/09, dividende versé).
- `projete` : une projection, une anticipation ou un scénario sur l'avenir.
- `sans_objet` : aucune de ces trois (par exemple une identification ou un renvoi).

**Fonction**

- `informer` : décrit ou donne un fait, de façon neutre.
- `avertir` : met en garde, signale un risque, une limite ou une condition défavorable.
- `promouvoir` : cherche à convaincre ou présente le produit favorablement.
- `orienter` : renvoie vers un document, un contact, une démarche (où trouver, comment agir).

**Marqueur durabilité** : `oui` si le segment parle de durabilité, d'ESG, de climat, de SFDR ou d'un label durable, quel que soit son code ; sinon `non`.

**Marqueur gouvernance** : `oui` si le segment décrit un conflit d'intérêts ou une rémunération susceptible d'en créer un, quel que soit son code ; sinon `non`.
