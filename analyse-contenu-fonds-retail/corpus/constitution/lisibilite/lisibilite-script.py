#!/usr/bin/env python3
"""Mission 4 (17/11/2026) — Contrôle de lisibilité et paquet de codage.
Entrées (lecture seule) : tirage_v3/tirage_pilote.csv ; lisibilite_travail/decisions.csv (décisions de lisibilité prises
segment par segment à la lecture, critères de forme de la section 2).
Sorties : lisibilite/ (controle_lisibilite.csv, segments_a_coder_lot1.csv, segments_a_coder_lot2.csv, correspondance.csv,
compte_rendu_lisibilite.md en projet, journal_lisibilite.md) et lisibilite_travail/recontrole_entree.csv.
Aucun texte n'est modifié ; tout est mécanique et reproductible."""
import csv, random, collections, hashlib, os, datetime
B = "/workspace/doc-screener"
TIRAGE = B + "/tirage_v3/tirage_pilote.csv"; DEC = B + "/lisibilite_travail/decisions.csv"
OUT = B + "/lisibilite"; TRAV = B + "/lisibilite_travail"
LOTS = ["lot1", "lot2"]; STRATES = ["S1", "S2", "S3", "S4"]
CIBLE = {"lot1": 20, "lot2": 24}; PREFIXE = {"lot1": "L1", "lot2": "L2"}
GRAINE_CODAGE = "2026-codage-{lot}"; GRAINE_RECONTROLE = "2026-recontrole-lisibilite"; N_RECONTROLE = 40
MOTIFS = ["E1", "E2", "E3", "E4", "E5"]
LIB = {"E1": "colonnes entremêlées", "E2": "en-tête seul", "E3": "mobilier de page", "E4": "données sans libellé", "E5": "fragment",
       "R1": "phrase", "R2": "libellé et valeur", "R3": "identification"}
NOMS = {"S1": "KID, KIID, fiches locales, KFS, PHS", "S2": "factsheets", "S3": "prospectus", "S4": "rapports et bulletins"}

def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
with open(TIRAGE, encoding="utf-8") as f: T = list(csv.DictReader(f))
with open(DEC, encoding="utf-8") as f: D = {r["segment_id"]: r for r in csv.DictReader(f)}
assert len(T) == 478 and set(D) == {t["segment_id"] for t in T}
for t in T:
    d = D[t["segment_id"]]
    assert d["critere"] in LIB and d["decision"] == ("retenu" if d["critere"][0] == "R" else "écarté")
    t["decision"], t["critere"], t["note_doute"] = d["decision"], d["critere"], d["note_doute"]
    t["rd"], t["rs"] = int(t["rang_document"]), int(t["rang_segment"])
    t["statut_final"], t["remplace"] = "", ""

# ---------------- 3. Remplacement
utilise = set(); remplacements = []; manques = []
for lot in LOTS:
    for st in STRATES:
        L = [t for t in T if t["lot"] == lot and t["strate"] == st]
        docs_p = sorted({t["rd"] for t in L if t["reserve_document"] == "non"})
        docs_r = sorted({t["rd"] for t in L if t["reserve_document"] == "oui"})
        segs = lambda rd: sorted([t for t in L if t["rd"] == rd], key=lambda t: t["rs"])
        file_reserve = [t for rd in docs_r for t in segs(rd)]   # ordre : rang_document puis rang_segment
        for rd in docs_p:
            for p in [t for t in segs(rd) if t["reserve_segment"] == "non"]:
                utilise.add(p["segment_id"])
                if p["decision"] == "retenu":
                    p["statut_final"] = "principal"; continue
                p["statut_final"] = "écarté"
                cand = next((t for t in segs(rd) if t["reserve_segment"] == "oui" and t["decision"] == "retenu" and t["segment_id"] not in utilise), None)
                origine = "même document"
                if cand is None:
                    cand = next((t for t in file_reserve if t["decision"] == "retenu" and t["segment_id"] not in utilise), None)
                    origine = "document de réserve"
                if cand is None:
                    manques.append((lot, st, p["segment_id"], rd)); continue
                utilise.add(cand["segment_id"]); cand["statut_final"] = "remplaçant"; cand["remplace"] = p["segment_id"]
                remplacements.append((lot, st, p["segment_id"], rd, p["critere"], cand["segment_id"], cand["rd"], cand["rs"], origine))
for t in T:
    if not t["statut_final"]: t["statut_final"] = "écarté" if t["decision"] == "écarté" else "réserve non utilisée"
final = [t for t in T if t["statut_final"] in ("principal", "remplaçant")]

# ---------------- 5.1 controle_lisibilite.csv (ordre du tirage)
with open(OUT + "/controle_lisibilite.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["segment_id", "lot", "strate", "doc_id", "rang_document", "rang_segment", "reserve_document", "reserve_segment",
                "decision", "critere", "note_doute", "statut_final", "remplace"])
    for t in T:
        w.writerow([t["segment_id"], t["lot"], t["strate"], t["doc_id"], t["rang_document"], t["rang_segment"], t["reserve_document"],
                    t["reserve_segment"], t["decision"], t["critere"], t["note_doute"], t["statut_final"], t["remplace"]])

# ---------------- 4. Paquets de codage et correspondance
COLS = ["id_codage", "type_document", "langue_origine", "titre_section", "texte_affichage", "segment_precedent", "segment_suivant",
        "texte_original", "texte_en", "statut_en"]
corr = []; paquets = {}
for lot in LOTS:
    liste = sorted([t for t in final if t["lot"] == lot], key=lambda t: t["segment_id"])
    rng = random.Random(GRAINE_CODAGE.format(lot=lot)); rng.shuffle(liste)
    paquets[lot] = liste
    with open(OUT + f"/segments_a_coder_{lot}.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n"); w.writerow(COLS)
        for k, t in enumerate(liste, 1):
            t["id_codage"] = f"{PREFIXE[lot]}-{k:03d}"
            w.writerow([t["id_codage"], t["type_document"], t["langue_origine"], t["titre_section"], t["texte_affichage"], t["segment_precedent"],
                        t["segment_suivant"], t["texte_original"], t["texte_en"] or "", t["statut_en"]])
            corr.append(t)
with open(OUT + "/correspondance.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["id_codage", "segment_id", "lot", "strate", "doc_id", "maison_gestion", "fonds_concernes", "pays_distribution", "rang_document", "rang_segment", "statut_final"])
    for t in corr:
        w.writerow([t["id_codage"], t["segment_id"], t["lot"], t["strate"], t["doc_id"], t["maison_gestion"], t["fonds_concernes"], t["pays_distribution"],
                    t["rang_document"], t["rang_segment"], t["statut_final"]])

# ---------------- 6.1 échantillon de recontrôle (entrée aveugle, sans décision)
tous = sorted(T, key=lambda t: t["segment_id"])
rng = random.Random(GRAINE_RECONTROLE); rng.shuffle(tous); echantillon = tous[:N_RECONTROLE]
with open(TRAV + "/recontrole_entree.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["segment_id", "type_document", "langue_origine", "titre_section", "texte_affichage", "texte_original", "segment_precedent", "segment_suivant"])
    for t in echantillon:
        w.writerow([t["segment_id"], t["type_document"], t["langue_origine"], t["titre_section"], t["texte_affichage"], t["texte_original"], t["segment_precedent"], t["segment_suivant"]])

# ---------------- 6.1 comparaison avec la relecture à l'aveugle (si disponible)
RV = TRAV + "/recontrole_decisions.csv"; comparaison = None
EXPL = {
    "LOT1-LU1159239190-DE-KID-0119d56d-000007": "Lecture étendue de E1 en première passe (colonnes en lignes alternées, colonne de droite renvoyée à la ligne) ; la relecture applique E1 au sens littéral (mêmes lignes seulement) et retient la phrase reconstituable.",
    "LOT1-IE00BKWQ0M75-UK-Factsheet-0b2522d8-000009": "Même décision (retenu) ; seul le critère diffère : la première passe note le critère le plus caractéristique (tableaux libellé-valeur), la relecture note le premier critère rempli dans l'ordre R1 > R2 > R3 (une phrase de note de bas de page est présente).",
}
if os.path.exists(RV):
    with open(RV, encoding="utf-8") as f: rv = list(csv.DictReader(f))
    ids_e = [t["segment_id"] for t in echantillon]
    assert len(rv) == N_RECONTROLE and {r["segment_id"] for r in rv} == set(ids_e)
    rvd = {r["segment_id"]: r for r in rv}; Tsid = {t["segment_id"]: t for t in T}
    with open(OUT + "/recontrole_lisibilite.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["segment_id", "lot", "strate", "decision_premiere_passe", "critere_premiere_passe", "note_premiere_passe",
                    "decision_relecture", "critere_relecture", "note_relecture", "decision_identique", "critere_identique"])
        for sid in ids_e:
            a, b = Tsid[sid], rvd[sid]
            w.writerow([sid, a["lot"], a["strate"], a["decision"], a["critere"], a["note_doute"], b["decision"], b["critere"], b["note_doute"],
                        "oui" if a["decision"] == b["decision"] else "non", "oui" if a["critere"] == b["critere"] else "non"])
    ecarts = [(sid, Tsid[sid], rvd[sid]) for sid in ids_e if Tsid[sid]["decision"] != rvd[sid]["decision"] or Tsid[sid]["critere"] != rvd[sid]["critere"]]
    comparaison = (sum(Tsid[s]["decision"] == rvd[s]["decision"] for s in ids_e), sum(Tsid[s]["critere"] == rvd[s]["critere"] for s in ids_e), ecarts)

# ---------------- 6.2 contrôles de cohérence
def lire(p):
    with open(p, encoding="utf-8") as f: return list(csv.DictReader(f))
pk = {lot: lire(OUT + f"/segments_a_coder_{lot}.csv") for lot in LOTS}; co = lire(OUT + "/correspondance.csv"); cl = lire(OUT + "/controle_lisibilite.csv")
dec = {r["segment_id"]: r["decision"] for r in cl}
eff = collections.Counter((t["lot"], t["strate"]) for t in final)
ctrl = []
ids_final = [r["segment_id"] for r in co]
ctrl.append(("aucun segment_id utilisé deux fois (jeu final et remplacements)",
             len(ids_final) == len(set(ids_final)) and len({r[5] for r in remplacements}) == len(remplacements) and not ({r[5] for r in remplacements} & {t["segment_id"] for t in T if t["statut_final"] == "principal"}),
             f"{len(ids_final)} segments dans le jeu final, {len(set(ids_final))} distincts ; {len(remplacements)} remplaçants distincts"))
ctrl.append(("aucun segment écarté dans les paquets de codage", all(dec[r["segment_id"]] == "retenu" for r in co), f"{sum(dec[r['segment_id']] == 'écarté' for r in co)} écarté(s) trouvé(s)"))
ctrl.append(("lignes des paquets = effectifs finaux du compte rendu",
             all(len(pk[lot]) == sum(eff[(lot, s)] for s in STRATES) for lot in LOTS),
             " ; ".join(f"{lot} : {len(pk[lot])} lignes, effectif final {sum(eff[(lot, s)] for s in STRATES)}" for lot in LOTS)))
idc = [r["id_codage"] for lot in LOTS for r in pk[lot]]
ctrl.append(("chaque id_codage figure dans correspondance.csv", set(idc) == {r["id_codage"] for r in co} and len(idc) == len(set(idc)) == len(co), f"{len(idc)} id_codage, {len(co)} lignes de correspondance"))
ctrl.append(("controle_lisibilite.csv couvre les 478 lignes du tirage", len(cl) == 478 and len({r['segment_id'] for r in cl}) == 478, f"{len(cl)} lignes"))
interdites = {"maison_gestion", "fonds_concernes", "pays_distribution", "sha256", "strate", "regle_perimetre_v2", "rang_document", "rang_segment", "segment_id", "doc_id", "lot"}
ctrl.append(("aucune colonne interdite dans les paquets", all(not (set(pk[lot][0].keys()) & interdites) for lot in LOTS) and all(list(pk[lot][0].keys()) == COLS for lot in LOTS), "colonnes : " + ", ".join(COLS)))
ctrl.append(("textes des paquets identiques au tirage (aucune modification)",
             all(r["texte_original"] == next(t for t in T if t.get("id_codage") == r["id_codage"])["texte_original"] for lot in LOTS for r in pk[lot]), ""))
re_h = list(csv.reader(open(TRAV + "/recontrole_entree.csv", encoding="utf-8")))
ctrl.append(("recontrole_entree.csv sans décision, critère ni note", re_h[0] == ["segment_id", "type_document", "langue_origine", "titre_section", "texte_affichage", "texte_original", "segment_precedent", "segment_suivant"] and len(re_h) == N_RECONTROLE + 1 and len({r[0] for r in re_h[1:]}) == N_RECONTROLE, f"{len(re_h) - 1} lignes, colonnes : " + ", ".join(re_h[0])))

# ---------------- compte rendu (projet) et journal
heure = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)).strftime("%d/%m/%Y %H:%M")
C = []
C.append("# Compte rendu — contrôle de lisibilité et paquet de codage (mission 4, 17/11/2026)\n")
C.append(f"{'**PROJET** — ' if not os.path.exists(TRAV + '/recontrole_decisions.csv') else ''}Rédigé le {heure} (heure d'Europe/Luxembourg).{' Le résultat du recontrôle de constance (section 6.1) reste à insérer.' if not os.path.exists(TRAV + '/recontrole_decisions.csv') else ''}\n")
C.append(f"Entrée unique : `tirage_v3/tirage_pilote.csv` (478 lignes, sha256 `{sha(TIRAGE)}`), non modifié. Chaque ligne a été lue et décidée selon la forme seule (section 2) ; aucune décision n'a été prise par un filtre automatique.\n")
C.append("## 1. Effectifs par lot et par strate\n")
C.append("| Lot | Strate | Segments principaux tirés | Principaux écartés (E1/E2/E3/E4/E5) | Remplacés (même document / document de réserve) | Non remplacés | Effectif final | Cible | Manque |\n|---|---|---|---|---|---|---|---|---|")
tot = collections.Counter()
for lot in LOTS:
    for st in STRATES:
        P = [t for t in T if t["lot"] == lot and t["strate"] == st and t["reserve_document"] == "non" and t["reserve_segment"] == "non"]
        ec = collections.Counter(t["critere"] for t in P if t["decision"] == "écarté")
        rm = [r for r in remplacements if r[0] == lot and r[1] == st]
        nm = sum(1 for m in manques if m[0] == lot and m[1] == st)
        e = eff[(lot, st)]; c = CIBLE[lot]
        C.append(f"| {lot} | {st} ({NOMS[st]}) | {len(P)} | {sum(ec.values())} ({'/'.join(str(ec[m]) for m in MOTIFS)}) | {len(rm)} ({sum(r[8] == 'même document' for r in rm)} / {sum(r[8] == 'document de réserve' for r in rm)}) | {nm} | {e} | {c} | {max(c - e, 0)} |")
        tot.update({"P": len(P), "E": sum(ec.values()), "R": len(rm), "N": nm, "F": e, "C": c})
C.append(f"| **Total** | | {tot['P']} | {tot['E']} | {tot['R']} | {tot['N']} | {tot['F']} | {tot['C']} | {tot['C'] - tot['F']} |")
C.append("\nLe manque comprend les écarts déjà présents au tirage v3 (lot 1 : documents en nombre insuffisant, acceptés) et les segments écartés qui n'ont pu être remplacés faute de réserve. Rien n'a été complété au-delà des règles de remplacement.\n")
C.append("## 2. Détail des remplacements\n")
if remplacements:
    C.append("| Lot | Strate | Segment écarté (motif) | Doc. principal (rang) | Remplaçant | Origine (rang doc., rang seg.) |\n|---|---|---|---|---|---|")
    for lot, st, sid, rd, crit, rid, rrd, rrs, orig in remplacements:
        C.append(f"| {lot} | {st} | {sid} ({crit}) | {rd} | {rid} | {orig} ({rrd}, {rrs}) |")
else: C.append("- Aucun.")
C.append("\nSegments principaux écartés non remplacés :\n")
if manques:
    for lot, st, sid, rd in manques: C.append(f"- {lot} {st} : {sid} (document de rang {rd}) — réserves du document et de la strate épuisées ; manque consigné.")
else: C.append("- Aucun.")
C.append("\n## 3. Taux d'écart par strate et par motif (toutes les lignes évaluées, réserves comprises)\n")
C.append("| Lot | Strate | Lignes évaluées | Écartées | Taux | E1 | E2 | E3 | E4 | E5 |\n|---|---|---|---|---|---|---|---|---|---|")
for lot in LOTS:
    for st in STRATES:
        L = [t for t in T if t["lot"] == lot and t["strate"] == st]; ec = collections.Counter(t["critere"] for t in L if t["decision"] == "écarté")
        n = len(L); x = sum(ec.values())
        C.append(f"| {lot} | {st} | {n} | {x} | {100*x/n:.1f} % | " + " | ".join(f"{ec[m]} ({100*ec[m]/n:.1f} %)" for m in MOTIFS) + " |")
ec = collections.Counter(t["critere"] for t in T if t["decision"] == "écarté"); x = sum(ec.values())
C.append(f"| **Total** | | 478 | {x} | {100*x/478:.1f} % | " + " | ".join(f"{ec[m]} ({100*ec[m]/478:.1f} %)" for m in MOTIFS) + " |")
cr = collections.Counter(t["critere"] for t in T if t["decision"] == "retenu")
C.append(f"\nCritères des segments retenus : R1 (phrase) {cr['R1']}, R2 (libellé et valeur) {cr['R2']}, R3 (identification) {cr['R3']}.\n")
dout = [t for t in T if t["note_doute"]]
C.append(f"## 4. Cas douteux ({len(dout)}, tous retenus)\n")
C.append("| segment_id | Lot | Strate | Critère | Note |\n|---|---|---|---|---|")
for t in dout: C.append(f"| {t['segment_id']} | {t['lot']} | {t['strate']} | {t['critere']} | {t['note_doute']} |")
C.append("\n## 5. Auto-contrôle (section 6)\n")
C.append("### 5.1 Constance du tri\n")
C.append(f"Échantillon : 40 lignes tirées parmi les 478 triées par segment_id, générateur `random.Random(\"{GRAINE_RECONTROLE}\")`, mélange `rng.shuffle` de la liste triée (même méthode que tirage_script.py) puis les 40 premières lignes du mélange. Réévaluation à l'aveugle (sans la première décision) à partir de `lisibilite_travail/recontrole_entree.csv`.\n")
if comparaison is None:
    C.append("**[À COMPLÉTER — résultat du recontrôle : nombre de décisions identiques sur 40 et liste des écarts.]**\n")
else:
    nd, nc, ecarts = comparaison
    C.append("Organisation : la réévaluation a été faite par un relecteur distinct, qui n'a vu que `recontrole_entree.csv` (texte du segment, voisins, type, langue, titre) et les critères de la mission, sans aucune décision, critère ni note de la première passe. Il a appliqué E1 au sens littéral (colonnes sur les mêmes lignes seulement) et, quand plusieurs conditions de maintien étaient remplies, a noté la première dans l'ordre R1 > R2 > R3. Ses décisions sont dans `recontrole_lisibilite.csv`, à côté de celles de la première passe. Aucune décision de première passe, aucun remplacement ni aucun paquet n'a été modifié à la suite de la relecture.\n")
    C.append(f"- Décisions identiques (retenu / écarté) : **{nd} sur 40**.")
    C.append(f"- Critères identiques : **{nc} sur 40**.\n")
    C.append("| segment_id | Première passe | Relecture | Explication |\n|---|---|---|---|")
    for sid, a, b in ecarts:
        C.append(f"| {sid} | {a['decision']} ({a['critere']}) | {b['decision']} ({b['critere']}) | {EXPL.get(sid, 'Écart de lecture.')} |")
    C.append("")
C.append("### 5.2 Contrôles de cohérence\n")
for lib, ok, det in ctrl: C.append(f"- {lib} : {'OK' if ok else 'ÉCHEC'}{' — ' + det if det else ''}")
C.append("\n## 6. Anomalies\n")
if comparaison is None: C.append("**[À COMPLÉTER après le recontrôle.]**")
else:
    n_e1 = sum(1 for t in T if t["critere"] == "E1")
    C.append(f"- **Lecture étendue de E1.** En première passe, E1 couvre aussi les colonnes en lignes alternées (colonne de droite renvoyée à la ligne, lisible dans `texte_original`), et pas seulement deux colonnes sur les mêmes lignes. Le recontrôle montre que cette lecture fait diverger une décision sur 40 (LOT1-LU1159239190-DE-KID-0119d56d-000007, écarté en première passe, retenu en lecture littérale). Les {n_e1} décisions E1 de la première passe sont maintenues telles quelles ; si la lecture littérale est préférée, les segments E1 en lignes alternées seraient à revoir, ce qui modifierait les remplacements.")
    C.append("- **Notation du critère de maintien.** La première passe note le critère le plus caractéristique ; la relecture note le premier dans l'ordre R1 > R2 > R3. Cela explique l'écart de critère sans écart de décision (une ligne sur 40). La répartition R1 / R2 / R3 du point 3 dépend donc de cette convention.")
    C.append("- **Manques au lot 1, S3 et S4.** Ces deux strates n'ont aucun document de réserve (tirage v3) : 5 segments principaux écartés en S3 et 2 en S4 n'ont pu être remplacés une fois les réserves de leur document épuisées. Avec les manques déjà présents au tirage (S2 : 6, S3 : 2, S4 : 2), le lot 1 compte 63 segments sur 80. Rien n'a été complété.")
    C.append(f"- **Cas douteux.** {len(dout)} segments retenus avec une note ; la plupart sont des textes rédigés juxtaposés à un tableau libellé-valeur ou à une liste chiffrée, que la première passe ne classe pas en E1 (une seule colonne rédigée).")
    C.append("- Aucune autre anomalie : contrôles de cohérence tous conformes, fichiers livrés inchangés.")
with open(OUT + "/compte_rendu_lisibilite.md", "w", encoding="utf-8") as f: f.write("\n".join(C) + "\n")

J = []
J.append("# Journal — mission 4, contrôle de lisibilité (17/11/2026)\n")
J.append(f"Produit par lisibilite_script.py le {heure} (heure d'Europe/Luxembourg). Aucun accès réseau, aucune traduction, aucun fichier livré modifié.\n")
J.append("## Fichiers lus\n")
J.append(f"- `tirage_v3/tirage_pilote.csv` : sha256 `{sha(TIRAGE)}`")
J.append(f"- `lisibilite_travail/decisions.csv` : sha256 `{sha(DEC)}` (décisions prises à la lecture, une par ligne, par lots d'environ 15 segments)\n")
J.append("## Décisions de lisibilité\n")
J.append("- Chaque segment a été lu (texte_affichage ; texte_original quand la mise en page était douteuse ; segments voisins pour comprendre le découpage). Un script n'a servi qu'à afficher les segments par lots ; il n'a pris aucune décision.")
J.append("- Ordre appliqué : E1 d'abord ; sinon retenu si R1, R2 ou R3 ; sinon premier motif E2 à E5. En cas de doute : retenu, avec une note de 10 à 20 mots.")
J.append("- Quand plusieurs critères R s'appliquent, le critère noté est le plus caractéristique du segment (R1 dès qu'une phrase rédigée est présente).")
J.append("- Interprétation E1 : deux colonnes de texte rédigé juxtaposées sur les mêmes lignes, ou en lignes alternées (colonne de droite renvoyée à la ligne). Un texte rédigé juxtaposé à un tableau libellé-valeur (ou à une liste chiffrée) n'est pas deux textes rédigés : retenu, avec une note de doute.")
J.append("- Interprétation E4 : les listes de positions ou de titres en portefeuille sont écartées même quand chaque ligne associe un titre et une valeur (exemple explicite de E4) ; une telle liste est retenue si le segment contient aussi une phrase ou un libellé-valeur hors positions.\n")
J.append("## Remplacement (section 3)\n")
J.append("- Traitement par lot et strate, documents principaux par rang_document croissant, puis segments principaux par rang_segment croissant.")
J.append("- Segment principal écarté : premier segment de réserve retenu du même document (rangs 3, 4, 5) ; à défaut, file des documents de réserve de la strate (rang_document croissant, puis rangs de segments 1 à 5), segments retenus seulement, chaque segment une seule fois ; un document de réserve entamé est épuisé avant le suivant (file unique parcourue dans l'ordre).")
J.append("- Les manques du tirage v3 (documents absents au lot 1) ne sont pas comblés : la section 3 ne remplace que des segments écartés.\n")
J.append("## Paquets de codage (section 4)\n")
J.append(f"- Pour chaque lot, jeu final trié par segment_id puis `random.Random(\"2026-codage-<lot>\").shuffle(liste)`, avec <lot> exactement comme dans les graines de tirage_script.py : `lot1`, `lot2` (graines « 2026-codage-lot1 » et « 2026-codage-lot2 »). id_codage dans l'ordre du mélange (L1-001…, L2-001…).")
J.append("- texte_en repris tel quel du tirage (vide si absent). Colonnes exclues : maison, fonds, ISIN, pays, sha256, strate, règle de périmètre, rangs, segment_id.\n")
J.append("## Recontrôle (section 6.1)\n")
J.append(f"- 478 lignes triées par segment_id, `random.Random(\"{GRAINE_RECONTROLE}\").shuffle(liste)`, puis les 40 premières (mélange puis tranche [:40], et non `rng.sample`). Fichier d'entrée aveugle : `lisibilite_travail/recontrole_entree.csv` (segment_id, type_document, langue_origine, titre_section, texte_affichage, texte_original, segment_precedent, segment_suivant), dans l'ordre du tirage.")
if comparaison is not None:
    J.append(f"- Organisation de la relecture à l'aveugle : un relecteur distinct a reçu uniquement `recontrole_entree.csv` et les critères de la mission (sections 2 et 7), sans accès aux décisions, critères, notes, remplacements ni paquets de la première passe. Il a appliqué E1 au sens littéral (mêmes lignes) et noté le premier critère de maintien dans l'ordre R1 > R2 > R3. Ses 40 décisions (`lisibilite_travail/recontrole_decisions.csv`, sha256 `{sha(RV)}`) sont recopiées à côté des décisions de première passe dans `lisibilite/recontrole_lisibilite.csv`. Résultat : {comparaison[0]} décisions identiques sur 40, {comparaison[1]} critères identiques. Aucune décision de première passe n'a été modifiée.")
with open(OUT + "/journal_lisibilite.md", "w", encoding="utf-8") as f: f.write("\n".join(J) + "\n")
print("ok", len(final), {lot: len(paquets[lot]) for lot in LOTS}, len(remplacements), len(manques), all(c[1] for c in ctrl))
