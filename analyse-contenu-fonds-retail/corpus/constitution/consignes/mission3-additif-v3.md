# Mission 3 – Additif v3 du tirage (17 novembre 2026)

Le contrôle de la v2 a montré que la règle « 5 espaces » excluait surtout des tableaux de coûts, de scénarios et de performance : elle dépendait du contenu. Elle est supprimée (décision D-013).

1. Suppression de l'exclusion « 5 espaces consécutifs ou plus » pour tous les types de documents. Toutes les autres règles de la v2 restent inchangées.
2. Nouveau champ `texte_affichage` : texte original où chaque suite de 5 espaces ou plus est remplacée par « | ». Champs `segment_precedent` et `segment_suivant` pour le contexte. Ces champs ne modifient aucun calcul.
3. Relance complète, deux exécutions identiques.
4. Livrables dans tirage_v3/ et compte rendu comparant v2 et v3.
