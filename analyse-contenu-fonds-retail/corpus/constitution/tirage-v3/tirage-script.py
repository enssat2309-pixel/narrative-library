#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mission 3 (17/11/2026) — Cadre de tirage et tirage en deux temps des segments du pilote — VERSION 3
(ajustement v3 du 17/11/2026 : suppression de l'exclusion générale « 5 espaces consécutifs ou plus » ; ajout des champs
d'affichage texte_affichage, segment_precedent, segment_suivant ; toutes les autres règles de la v2 sont inchangées).

Reconstruit tout à partir des fichiers déjà livrés (aucun accès réseau, aucune traduction,
aucun fichier existant modifié) :
  - corpus/lot1_2026-11-15.zip, corpus/lot2_2026-11-15.zip (manifestes livrés, échantillon lot 2) ;
  - corpus/manifeste_lot1_2026-11-15_rectifie.csv, corpus/lot2/manifeste_lot2_rectifie.csv
    (rectifications du 16/11 : langue_origine, indicateur de traduction) ;
  - consolidation/manifeste_complete.csv (tronque, reserve_professionnels, statut_traduction, lot) ;
  - consolidation/segments.jsonl (lu en flux, jamais chargé en entier) ;
  - consolidation/corpus.jsonl (lu en flux, seulement pour repérer les limites de pages des fichiers composites).
Écrit uniquement dans le dossier de sortie (par défaut /workspace/doc-screener/tirage_v3).
Usage : nice python3 tirage_script.py [dossier_de_sortie]
"""
# ======================= PARAMÈTRES (section 5.1 — ne pas modifier) =======================
GRAINE = 2026
LOTS = ["lot1", "lot2"]                       # tirage séparé par lot
STRATES = {                                   # strates par type de document (type_document du manifeste)
    "S1": ["KID", "KIID", "Fiche_locale", "KFS", "PHS"],     # KID et fiches locales
    "S2": ["Factsheet"],                                      # factsheets
    "S3": ["Prospectus"],                                     # prospectus
    "S4": ["Rapport", "Bulletin_trimestriel"],                # rapports annuels/semestriels, bulletins trimestriels
}
SEGMENTS_PAR_STRATE = {"lot1": 20, "lot2": 24}
SEGMENTS_PAR_DOCUMENT = 2
DOCUMENTS_PAR_STRATE = {lot: n // SEGMENTS_PAR_DOCUMENT for lot, n in SEGMENTS_PAR_STRATE.items()}  # 10 et 12
DOCUMENTS_DE_RESERVE = 5
SEGMENTS_DE_RESERVE = 3
PART_MAX_MAISON = 0.4                          # plafond : ceil(0,4 × nombre de documents à tirer)
MIN_SEGMENTS_OUI = 2                           # une unité doit avoir au moins 2 segments perimetre_v2 = oui
def graine_strate(lot, strate): return f"{GRAINE}-{lot}-{strate}"
def graine_document(lot, strate, doc_id): return f"{GRAINE}-{lot}-{strate}-{doc_id}"
# Interprétation retenue (consignée dans journal_tirage.md) : une maison est refusée dès qu'elle a déjà
# ceil(0,4 × N) unités acceptées dans la strate (au plus 40 % des documents à tirer).
# ==========================================================================================

import csv, io, json, math, os, random, re, sys, hashlib, unicodedata, zipfile, collections, datetime

BASE = "/workspace/doc-screener"
OUT = sys.argv[1] if len(sys.argv) > 1 else BASE + "/tirage_v3"
CORPUS = BASE + "/consolidation/corpus.jsonl"
SEG = BASE + "/consolidation/segments.jsonl"
MAN_COMPLET = BASE + "/consolidation/manifeste_complete.csv"
ZIP_LOT1 = BASE + "/corpus/lot1_2026-11-15.zip"
ZIP_LOT2 = BASE + "/corpus/lot2_2026-11-15.zip"
RECT = {"lot1": BASE + "/corpus/manifeste_lot1_2026-11-15_rectifie.csv",
        "lot2": BASE + "/corpus/lot2/manifeste_lot2_rectifie.csv"}
os.makedirs(OUT, exist_ok=True)

def sha256_fichier(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 22), b""): h.update(b)
    return h.hexdigest()

JOURNAL = []          # lignes du journal (Markdown)
ANOMALIES = []
NON_TRANCHES = []
def J(s=""): JOURNAL.append(s)

# ------------------------------------------------------------------ 1. Manifestes
def lire_csv_zip(zp, nom):
    with zipfile.ZipFile(zp) as z:
        return list(csv.DictReader(io.TextIOWrapper(z.open(nom), encoding="utf-8")))
livres = {"lot1": lire_csv_zip(ZIP_LOT1, "manifeste.csv"),
          "lot2": lire_csv_zip(ZIP_LOT2, "lot2/manifeste_lot2.csv"),
          "annexe_SG": lire_csv_zip(ZIP_LOT2, "lot2/annexe_SG/manifeste_annexe_SG.csv")}
echantillon_lot2 = lire_csv_zip(ZIP_LOT2, "lot2/echantillon_lot2.csv")
societe_par_isin = {r["isin"].strip(): r["societe_gestion"].strip() for r in echantillon_lot2 if r["isin"].strip()}
rectifie = {}
for lot, p in RECT.items():
    for r in csv.DictReader(open(p, encoding="utf-8")): rectifie[r["identifiant_document"]] = r
complet = {r["identifiant_document"]: r for r in csv.DictReader(open(MAN_COMPLET, encoding="utf-8"))}

lignes = []   # (lot, ligne fusionnée)
diff_rect = []
for lot in ["lot1", "lot2", "annexe_SG"]:
    for r in livres[lot]:
        did = r["identifiant_document"]
        c = complet.get(did)
        if c is None or c["lot"] != lot:
            ANOMALIES.append(f"{did} : ligne du manifeste livré absente de manifeste_complete.csv (ou lot différent)"); continue
        if c["empreinte_sha256"] != r["empreinte_sha256"]:
            ANOMALIES.append(f"{did} : sha256 différent entre manifeste livré et manifeste_complete.csv")
        x = dict(r); x["lot"] = lot
        for k in ["reserve_professionnels", "mention_reserve", "tronque", "statut_traduction", "langue_retenue_segments", "n_segments", "statut_traitement"]:
            x[k] = c[k]
        rr = rectifie.get(did)
        if rr is not None:
            for k in ["langue_origine", "indicateur_traduit"]:
                if rr[k] != r[k]:
                    diff_rect.append((lot, did, k, r[k], rr[k], r["statut"]))
                    x[k] = rr[k]
        lignes.append(x)

def est_paire(x):
    return x["notes"].strip().lower().startswith("paire") or x["document_parent"].strip().upper().startswith("AVIS-")

def strate_de(t):
    for s, ts in STRATES.items():
        if t in ts: return s
    return "hors strate"

# ------------------------------------------------------------------ 2. Unités documentaires (4.1)
groupes = collections.OrderedDict()
for x in lignes:
    if x["statut"] != "collecté": continue
    groupes.setdefault((x["lot"], x["empreinte_sha256"]), []).append(x)
unites = {}   # doc_id de l'unité -> dict (pour une unité ordinaire : doc_id de la ligne de référence)
COMPOSITES = {}   # doc_id de référence d'un fichier listé sous plusieurs types -> infos
for (lot, sha), g in groupes.items():
    g = sorted(g, key=lambda x: x["identifiant_document"])
    ref = g[0]
    types = sorted({x["type_document"] for x in g})
    if len(types) > 1: COMPOSITES[ref["identifiant_document"]] = {"lot": lot, "sha256": sha, "types": types, "lignes": [x["identifiant_document"] for x in g],
                                                                 "isin": ref["isin"].strip().upper(), "notes": {x["identifiant_document"]: x["notes"] for x in g}}
    maisons = sorted({x["maison_gestion"] for x in g})
    if len(maisons) > 1: ANOMALIES.append(f"{ref['identifiant_document']} : maisons différentes dans le groupe {maisons} (maison de la ligne de référence retenue)")
    m = ref["maison_gestion"].strip()
    if m == "autre émetteur":
        soc = societe_par_isin.get(ref["isin"].strip(), "")
        maison = f"autre émetteur : {soc}" if soc else "autre émetteur (société non renseignée)"
    else:
        maison = m or "(non renseignée)"
    langs = sorted({x["langue_origine"] for x in g})
    lo = ref["langue_origine"].strip()
    if not lo:
        lo = ref["langue_retenue_segments"].strip()
        if lo: ANOMALIES.append(f"{ref['identifiant_document']} : langue_origine vide dans le manifeste rectifié, langue retenue pour les segments (« {lo} ») reprise")
    motifs = []
    if any(x["tronque"] == "oui" for x in g) or ref["n_segments"] in ("", "0"): motifs.append("fichier tronqué ou texte absent (tronque = oui)")
    if any(x["reserve_professionnels"] == "oui" for x in g): motifs.append("mention de réserve aux professionnels (reserve_professionnels = oui)")
    if lot == "annexe_SG": motifs.append("annexe Singapour (annexe_SG)")
    if ref["type_document"] == "Avis": motifs.append("avis (flux séparé)")
    if any(est_paire(x) for x in g): motifs.append("paire d'avis (flux séparé)")
    unites[ref["identifiant_document"]] = {
        "doc_id": ref["identifiant_document"], "sha256": sha, "lot": lot,
        "strate": strate_de(ref["type_document"]), "type_document": ref["type_document"],
        "fonds_concernes": sorted({x["isin"].strip() for x in g if x["isin"].strip()}),
        "noms": sorted({(x["isin"].strip().upper(), x["nom_fonds"], x["maison_gestion"]) for x in g}),
        "maison_gestion": maison,
        "pays_distribution": sorted({x["pays_distribution"].strip() for x in g if x["pays_distribution"].strip()}),
        "langue_origine": lo, "statut_en": ref["statut_traduction"],
        "lignes_manifeste": [x["identifiant_document"] for x in g],
        "motifs": motifs, "mention_reserve": ref["mention_reserve"],
        "n_seg": 0, "n_old_oui": 0, "n_v2_oui": 0, "oui": [], "source": ref["identifiant_document"], "pages": "",
    }

# ------------------------------------------------------------------ 2 bis. Fichiers composites (ajustement v2, règle « fichier composite »)
KID_TITRE = re.compile(r"document d.informations? cl[ée]s|key information document|basisinformationsblatt|documento contenente le informazioni chiave|documento de datos fundamentales", re.I)
PROSP_TITRE = re.compile(r"^\s*(prospectus|prospekt|verkaufsprospekt|prospetto|folleto)(\s+complet)?\s*$", re.I)
ISIN_RX = re.compile(r"\b[A-Z]{2}[A-Z0-9]{9}\d\b")
PAGE_RX = re.compile(r"^----- p\. (\d+) -----\s*$")
LIGNES_TETE = 15
def limites_composite(texte, isin):
    """Repère, d'après les titres du texte, les pages de chaque KID (titre « Document d'Informations Clés »… dans les
    15 premières lignes non vides d'une page) et la première page du prospectus (ligne réduite au mot « PROSPECTUS »
    dans les 15 premières lignes non vides). Un KID va de sa page de titre à la page qui précède le KID suivant ou le
    prospectus ; il appartient à la classe de parts dont l'ISIN apparaît dans ses pages. Rend (liste de blocs, page_prospectus, page_max)."""
    pages = collections.OrderedDict(); p = None
    for l in texte.split("\n"):
        m = PAGE_RX.match(l)
        if m: p = int(m.group(1)); pages[p] = []; continue
        if p is not None: pages[p].append(l)
    debuts_kid = []; p_prosp = None
    for p, ls in pages.items():
        tete = [l for l in ls if l.strip()][:LIGNES_TETE]
        if p_prosp is None and any(PROSP_TITRE.match(l) for l in tete): p_prosp = p
        elif p_prosp is None and any(KID_TITRE.search(l) for l in tete): debuts_kid.append(p)
    pmax = max(pages) if pages else 0
    blocs = []
    for i, d in enumerate(debuts_kid):
        f = (debuts_kid[i + 1] - 1) if i + 1 < len(debuts_kid) else ((p_prosp - 1) if p_prosp else pmax)
        isins = sorted({x for q in range(d, f + 1) for l in pages.get(q, []) for x in ISIN_RX.findall(l)})
        blocs.append((d, f, isins, isin in isins))
    return blocs, p_prosp, pmax
def limites_notes(notes):
    """Limites annoncées par les notes du manifeste (pour comparaison uniquement)."""
    plages = re.findall(r"pages? (\d+)\s*[-–à]\s*(\d+)", notes); debut = re.findall(r"(?:à partir de|commence à) la page (\d+)", notes)
    return [(int(a), int(b)) for a, b in plages], [int(x) for x in debut]
if COMPOSITES:
    with open(CORPUS, encoding="utf-8") as f:
        for line in f:
            i = line.find('"doc_id": "') + 11; did = line[i:line.index('"', i)]
            if did in COMPOSITES:
                COMPOSITES[did]["texte"] = json.loads(line)["texte_original"] or ""
for ref_id, c in COMPOSITES.items():
    base = unites.pop(ref_id)
    blocs, p_prosp, pmax = limites_composite(c.get("texte", ""), c["isin"])
    c["blocs"] = blocs; c["p_prosp"] = p_prosp; c["pmax"] = pmax
    c["notes_limites"] = {k: limites_notes(v) for k, v in c["notes"].items()}
    propres = [b for b in blocs if b[3]]
    if not propres or p_prosp is None:
        ANOMALIES.append(f"{ref_id} : fichier composite dont les limites de pages n'ont pas pu être repérées dans le texte ; unité laissée sans découpage, exclue du cadre")
        base["motifs"].append("fichier composite non découpable (limites de pages non repérées)"); unites[ref_id] = base; continue
    kid_p = set(); autres_p = set()
    for d, f_, isins, propre in blocs:
        (kid_p if propre else autres_p).update(range(d, f_ + 1))
    prosp_p = set(range(p_prosp, pmax + 1))
    def plages(ps):
        ps = sorted(ps); out = []
        for q in ps:
            if out and q == out[-1][1] + 1: out[-1][1] = q
            else: out.append([q, q])
        return ", ".join(f"{a}-{b}" if a != b else f"{a}" for a, b in out)
    c["retenu"] = {"KID": plages(kid_p), "autres": plages(autres_p), "PROSPECTUS": plages(prosp_p)}
    for suffixe, typ, ps, motif_sup in [("-KID", "KID", kid_p, None), ("-KID-AUTRES-CLASSES", "KID", autres_p, "KID d'une autre classe de parts"), ("-PROSPECTUS", "Prospectus", prosp_p, None)]:
        if not ps: continue
        u = dict(base); u["motifs"] = list(base["motifs"]) + ([motif_sup] if motif_sup else []); u["oui"] = []
        u["doc_id"] = ref_id + suffixe; u["type_document"] = typ; u["strate"] = strate_de(typ); u["pages"] = plages(ps); u["page_set"] = ps
        u["source"] = ref_id; u["composite"] = True
        unites[u["doc_id"]] = u
    c["unites"] = [ref_id + s_ for s_ in ("-KID", "-KID-AUTRES-CLASSES", "-PROSPECTUS") if ref_id + s_ in unites]
SOURCES = {}   # doc_id présent dans segments.jsonl -> liste des unités qui en reçoivent les segments
for did, u in unites.items(): SOURCES.setdefault(u["source"], []).append(did)

# ------------------------------------------------------------------ 3. Règles de périmètre v2 (4.3)
def norm(s):
    s = unicodedata.normalize("NFKD", s.lower()); s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9€$£]+", " ", s).strip()
# Listes reprises de scripts/perimetre.py (consolidation du 15/11), corrigées là où la mission 3 l'exige.
GEN = set("fund fonds funds ucits etf plc sicav fcp fi the a of de des du la le les et and nr acc dist class classe sub teilfonds compartiment compartment portfolio fondo comparto sa s a icav".split())
SUFFIX = re.compile(r"\s*(\(?suite\)?|\(continued\)|continued|\(fortsetzung\)|fortsetzung|\(forts\.?\)|\(segue\)|\(continuaci[oó]n\)|\(cont\.?\))\s*$", re.I)
NOUN = re.compile(r"\b(fund|fonds|portfolio|etf|teilfonds|sub-fund|compartiment|comparto|fondo)\s*$", re.I)
PRODNAME = re.compile(r"(nom du produit|product name|produktname|name des produkts|nome del prodotto|denominazione del prodotto|nombre del producto)\s*:?\s*(.{4,120})", re.I)
SUPPL = re.compile(r"^(supplement|nachtrag|supplément|supplemento|suplemento|annex|annexe|anhang|allegato|anexo|appendix)\b.{0,10}\d*\s*[:\-–]?\s*(.{4,100})$", re.I)
LISTE = re.compile(r"(sub-?custodian|sous-d[ée]positaires|unterverwahrer|sub-?depositari|subcustodi|^directory|adresses|anschriften|indirizzi|direcciones|list of (sub-?)?funds|liste des (compartiments|fonds|sous)|elenco dei (comparti|fondi)|lista de (fondos|subfondos))", re.I)
ANNEXHEAD = re.compile(r"^(appendix|annex|annexe|anhang|allegato|anexo)\b", re.I)
FIN = re.compile(r"(?<!audit of the )(nettoverm[oö]gens|statement of (net assets|operations|changes|financial position|comprehensive income|cash flows|total return)|balance sheet|income statement|profit and loss|notes to the (financial statements|accounts)|financial statements|[ée]tats? financiers|[ée]tat (du patrimoine|des op[ée]rations|de l.actif net|des variations|de situation)|[ée]tats? des variations|^bilan\b|compte de r[ée]sultat|annexes? (aux|des) comptes|notes? (aux|annexes aux) (comptes|[ée]tats)|comptes annuels|ertrags- und aufwandsrechnung|entwicklung des (fonds|netto|sonder)?verm[oö]gens|^bilanz|gewinn- und verlustrechnung|erl[äa]uterungen|anhang (zum|zu den)|jahresabschluss|situazione patrimoniale|sezione reddituale|nota integrativa|prospetti contabili|balance de situaci[oó]n|^balance\b|cuenta de p[ée]rdidas|^memoria\b|estado de (cambios|flujos)|^notes\b)", re.I)
COMM = re.compile(r"(report of the (directors|board|investment manager|manager)|investment manager.?s report|manager.?s report|management report|rapport (de|du) gestion|rapport d.activit|rapport de la soci[ée]t[ée] de gestion|commentaire|t[äa]tigkeitsbericht|bericht (des|der|zum) |relazione (sulla gestione|degli amministratori|di gestione)|informe de gesti[oó]n|market (review|commentary|overview)|investment (review|report|policy|commentary)|politique d.investissement|orientation des placements|anlagepolitik|anlageziel|fund review|chairman|lettre aux porteurs|vision general|visi[oó]n general|pol[ií]tica de inversi[oó]n)", re.I)
PERF = re.compile(r"(performance|wertentwicklung|rendement|rendimento|rentabilidad|evoluci[oó]n del valor)", re.I)
# Correction v2 : « portfolio » suivi de « management » (Portfoliomanagementtechniken, portfolio manager) n'est pas une liste de positions.
POS = re.compile(r"(portfolio(?!\s*-?\s*manag)|portefeuille|portafoglio|verm[oö]gens[üu]bersicht|schedule of investments|statement of investments|portfolio of investments|portfolio statement|portfolio holdings|holdings|inventaire|composition (de l.actif|du portefeuille)|portefeuille[- ]titres|verm[oö]gensaufstellung|wertpapierbestand|elenco (analitico|dei titoli)|cartera|top (ten|10)|principali (titoli|posizioni)|changes in (the )?(composition|portfolio))", re.I)
FEES = re.compile(r"(total expense ratio|\bter\b|ongoing charges|\bfrais\b|laufende kosten|kostenquote|verwaltungsverg[üu]tung|commissioni|spese correnti|\bgastos\b|comisiones|comisi[oó]n|expense ratio|transaction costs|co[uû]ts de transaction)", re.I)
# Correction v2 (titre complet) : un terme de frais précédé d'une exclusion (« hors frais », « net of fees »…) ne fait pas un titre de frais.
FEES_NEG = re.compile(r"\b(hors|excl\w*|excluding|net of|after|before|ohne|nach|vor|sin|senza|netto|avant|apr[eè]s|d[ée]duction faite)\b\W+(\w+\W+){0,2}?(frais|fees|charges|costs|kosten|gastos|comisiones|commissioni|spese|ter)\b", re.I)
FEES_MAX_MOTS = 12
AUDIT = re.compile(r"(audit report|report on the audit|auditor|r[ée]viseur d.entreprises|rapport (du|des) commissaire|bestätigungsvermerk|pr[üu]fungsvermerk|vermerk des unabh|relazione della societ[aà] di revisione|informe de auditor)", re.I)
DOCTITLE = re.compile(r"(^(rapport (annuel|semestriel)|annual report|semi-?annual report|interim report|unaudited semi|jahresbericht|halbjahresbericht|relazione (annuale|semestrale)|informe (anual|semestral))\b|\[\d+\]\s*$)", re.I)
FUNCW = set("the to in of for on by with you your a an der die das des den dem du de la le les et und del della dei per il lo gli el los las y e que von zu im am aux au sur pour par en is are how what when which wie was".split())
EXTRA_OK = set("appendix annex annexe anhang allegato anexo supplement nachtrag supplement supplemento suplemento suite continued fortsetzung forts segue continuacion cont name produkts produktname product nom produit prodotto nombre producto des du del of the".split())
# Marqueurs d'annexe SFDR (exemples de la mission, étendus aux équivalents dans les langues du corpus).
# Chaque marqueur : (libellé, expression, où il est cherché). « titre » = titre de section (recollé) ;
# « texte » = n'importe où dans le segment ; « debut » = 200 premiers caractères du segment.
# Les marqueurs trop fréquents dans la prose (renvois « Annexe II du présent prospectus », « règlement délégué (UE) 2022/1288 »)
# ne sont cherchés que dans les titres, et « Annexe II / III » exige un mot du modèle SFDR à proximité.
MODELE = r"(template|mod[eè]le|vorlage|modello|plantilla|pre-?contractual|pr[ée]contractuel|vorvertraglich|precontrattual|precontractual|periodic|p[ée]riodique|2019\s*/\s*2088|2022\s*/\s*1288)"
SFDR = [(lab, re.compile(p, re.I), ou) for lab, p, ou in [
    ("Legal entity identifier", r"legal entity identifier|identifiant d.entit[ée] juridique|unternehmenskennung|identificativo della persona giuridica|identificador de entidad jur[ií]dica", ("titre", "texte")),
    ("Product name", r"\b(product\s+name|nom du produit|d[ée]nomination du produit|name des produkts|produktname|nome del prodotto|denominazione del prodotto|nombre del producto)\s*:", ("titre", "debut")),
    ("Modèle d'informations précontractuelles / périodiques (article 8 ou 9)", r"(?:^|\n|(?<=[ ]{3}))\W{0,3}(?:sfdr[- ]?\w*\W{0,3})?(?:template\s+|mod[eè]le\s+d.|vorlage\s*[–-]\s*|modello\s+di\s+|plantilla\s+de\s+)?(pre-?contractual disclosure|informations pr[ée]contractuelles|vorvertragliche informationen|informativa precontrattuale|informaci[oó]n precontractual|periodic disclosure|informations p[ée]riodiques|regelm[äa](ß|ss)ige informationen|informativa periodica|informaci[oó]n peri[oó]dica).{0,120}?\b(article|artikel|articolo|art[ií]culo)\s+[89]\b", ("titre", "texte")),
    ("Sustainability indicators (encadré du modèle)", r"(sustainability indicators|indicateurs de durabilit[ée]|nachhaltigkeitsindikatoren|indicatori di sostenibilit[aà]|indicadores de sostenibilidad)\s+(measure|mesurent|messen|misurano|miden)", ("titre", "texte")),
    ("Annexe II / Annexe III (modèle SFDR)", r"\b(annex|annexe|anhang|allegato|anexo)\s+(ii|iii)\b", ("titre+modele",)),
    ("Règlement délégué (UE) 2022/1288", r"2022\s*/\s*1288", ("titre",)),
    ("Annexe SFDR", r"^\W*((annexes?|annex|anhang|anh[äa]nge|appendix|appendices|allegato|anexo)\b.{0,40}\bSFDR\b|SFDR\b)", ("titre",)),
]]
# Préfiltre (accélération seulement, sans effet sur le résultat) : mots-clés obligatoires des marqueurs cherchés dans le texte.
PREFILTRE = re.compile(r"identifier|identifiant|kennung|identificativo|identificador|name|nom|denomina|nombre|disclosure|contractuel|vertraglich|contrattual|contractual|p[ée]riodi|peri[oó]di|regelm|indicat|nachhaltigkeitsindikator", re.I)
SOMMAIRE = re.compile(r"\.{5,}|(…\s*){3,}|_{5,}")
TITRE_SOMMAIRE = re.compile(r"^(contents|table of contents|sommaire|table des mati[eè]res|inhaltsverzeichnis|inhalt|indice|[ií]ndice)\b", re.I)
COURT = {"KID", "KIID", "Factsheet", "Fiche_locale", "KFS", "PHS", "Bulletin_trimestriel"}

def titlecase(c):
    w = [x for x in re.findall(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ'’&\-]*", c) if len(x) >= 4]
    return bool(w) and all(x[0].isupper() for x in w)

class Fonds:
    """Repris de perimetre.py (classe Doc) : repère un titre de compartiment propre / autre."""
    def __init__(s, isin, nom, maison):
        parts = re.split(r"\s+-\s+", nom); s.isin = isin
        s.own = set(norm(parts[-1]).split()) - GEN
        s.umb = (set(norm(" ".join(parts[:-1]) + " " + maison).split()) | GEN | EXTRA_OK | {"ishares", "fidelity", "blackrock", "vanguard", "state", "street", "spdr", "ssga", "funds", "lux", "luxembourg"}) - s.own
    def comp_kind(s, c):
        if s.isin and s.isin in c.upper(): return "propre (ISIN)"
        toks = set(norm(c).split())
        if len(s.own) >= 2 and s.own <= toks and all(t in s.umb or t.isdigit() for t in toks - s.own): return "propre (nom)"
        m = PRODNAME.search(c)
        if m:
            name = re.split(r"\s{2,}|identifiant|legal entity|unternehmenskennung|identificativo|identificador|\(the", m.group(2), flags=re.I)[0]
            nt = set(norm(name).split())
            if s.own and s.own <= nt: return "propre (nom)"
            return "autre" if (nt - GEN - EXTRA_OK) else None
        c2 = SUFFIX.sub("", c).strip(); m2 = SUPPL.match(c2)
        if m2: c2 = m2.group(2).strip()
        if re.match(r"^\d+[.)]\s", c2): return None
        if not NOUN.search(c2) or LISTE.search(c2): return None
        w = norm(c2).split()
        if len(w) < 3 or (set(w) & FUNCW) or not (titlecase(c2) or c2.isupper()): return None
        if not (set(w) - GEN - EXTRA_OK): return None
        return "autre"

def comp_unite(fonds, c):
    ks = [f.comp_kind(c) for f in fonds]
    for k in ks:
        if k and k.startswith("propre"): return k
    return "autre" if "autre" in ks else None

def nmots(s): return len(re.findall(r"\S*\w\S*", s))
CONT_MAX_MOTS = 4; CONT_MAX_LIGNES = 2
def recoller(titre, texte):
    """4.3 : recolle au titre les lignes de titre qui le prolongent en tête du premier segment de la section
    (intitulé coupé par la mise en page). Ligne recollée : 1 à 4 mots, sans chiffre, sans ponctuation finale,
    sans double espace ; au plus 2 lignes ; titre lui-même sans ponctuation finale."""
    if not titre or re.search(r"[.:;!?]\s*$", titre): return titre, 0
    t = titre; n = 0
    for l in texte.split("\n")[:CONT_MAX_LIGNES]:
        c = l.strip()
        if not c or not (1 <= nmots(c) <= CONT_MAX_MOTS) or re.search(r"\d", c) or re.search(r"[.:;,!?]$", c) or "  " in c: break
        t = t + " " + c; n += 1
    return t, n

def fragment_prose(c):
    c = c.strip()
    return (not c) or c[0].islower() or c[0] in "-–—•·✓▪*►>" or c.endswith((";", ","))

def sfdr_titre(titre, texte):
    for lab, rx, ou in SFDR:
        if ("titre" in ou or "titre+modele" in ou) and rx.search(titre):
            if "titre+modele" in ou and not re.search(MODELE, titre + " " + texte[:300], re.I): continue
            return lab, "titre"
    return None, None

def sfdr_motif(titre, texte):
    """Déclenchement par le texte du segment (titre utilisé seulement pour reconnaître un sommaire)."""
    if not texte or not PREFILTRE.search(texte): return None, None
    if SOMMAIRE.search(texte) or (titre and TITRE_SOMMAIRE.search(titre)): return None, None   # sommaire : pas de déclenchement par le texte
    for lab, rx, ou in SFDR:
        if ("texte" in ou and rx.search(texte)) or ("debut" in ou and rx.search(texte[:200])): return lab, "texte"
    return None, None

CHIFFRE = re.compile(r"\d")
# v3 : l'exclusion « 5 espaces consécutifs ou plus » est supprimée. La règle « chiffres » compte les caractères non blancs
# du texte tel quel (str.isspace : espaces, espaces insécables et autres espaces Unicode exclus du dénominateur).
def exclusions_generales(texte, n_mots):
    nb = [ch for ch in texte if not ch.isspace()]
    r = []
    if nb and sum(1 for ch in nb if ch.isdigit()) > 0.5 * len(nb): r.append("chiffres")
    if n_mots < 4: r.append("court")
    return r
LIB_EXCL = {"chiffres": "exclusion générale : chiffres > moitié des caractères non blancs",
            "court": "exclusion générale : moins de 4 mots",
            "doublon": "exclusion générale : texte identique à un segment déjà retenu dans l'unité"}

compteur_titres = collections.Counter(); exemples_recolles = []; exemples_ignores = []
compteur_sfdr = collections.Counter()   # (type, motif, titre/texte)

def classer_document(u, segs):
    """segs : liste de dicts (ordre, segment_id, titre, page, texte, n_mots, perimetre). Rend [(v2, règle)]."""
    t = u["type_document"]; res = []
    fonds = [Fonds(i, n, m) for i, n, m in u["noms"]]
    if t in COURT:
        base = [("oui", "type toujours inclus (KID, fiche locale, factsheet, bulletin)")] * len(segs)
    elif t == "Avis":
        base = [("oui", "avis : type non visé par 4.3, gardé (cas non tranché, hors cadre)")] * len(segs)
    else:
        prosp = (t == "Prospectus")
        state = ("oui", "prospectus : partie générale") if prosp else ("oui", "rapport : section non classée, gardée (cas non tranché)")
        prev_titre = object(); prev_page = object(); vu_propre = False; base = []
        for s in segs:
            titre = s["titre"] or ""
            nouveau = (s["titre"] != prev_titre)
            haut = nouveau and (s["page"] != prev_page)
            prev_titre = s["titre"]; prev_page = s["page"]
            new = None
            if nouveau and titre:
                c, n = recoller(titre, s["texte"])
                if n:
                    compteur_titres["recollés"] += 1
                    if len(exemples_recolles) < 40: exemples_recolles.append((u["doc_id"], titre, c))
                if fragment_prose(titre):
                    compteur_titres["ignorés (fragment de prose)"] += 1
                    if len(exemples_ignores) < 15: exemples_ignores.append((u["doc_id"], titre))
                else:
                    compteur_titres["exploités"] += 1
                    lab, ou = sfdr_titre(c, s["texte"])
                    if lab:
                        new = ("non", f"annexe SFDR (titre : « {lab} »)"); compteur_sfdr[(t, lab, "titre")] += 1
                    elif prosp:
                        k = comp_unite(fonds, c)
                        if k is None and c != titre: k = comp_unite(fonds, titre)
                        elif k == "autre" and c != titre:
                            k2 = comp_unite(fonds, titre)
                            if k2 and k2.startswith("propre"): k = k2
                        if k and k.startswith("propre"): new = ("oui", "prospectus : section propre au fonds (" + k.split("(")[1].rstrip(")") + " dans le titre)"); vu_propre = True
                        elif k == "autre": new = ("non", "prospectus : autre compartiment")
                        elif LISTE.search(c) and len(c) <= 70:
                            new = ("non", "prospectus : annexe qui est une simple liste (" + LISTE.search(c).group(0).lower() + ")")
                        elif haut and ANNEXHEAD.search(c) and state[1] != "prospectus : partie générale" and not SUFFIX.search(c):
                            new = ("oui", "prospectus : partie générale (retour sur un intitulé d'annexe en haut de page)")
                        elif haut and state[1].startswith("prospectus : annexe qui est une simple liste") and not SUFFIX.search(c):
                            new = ("oui", "prospectus : partie générale (fin d'annexe-liste, titre en haut de page)")
                    else:
                        if DOCTITLE.search(c): pass
                        elif AUDIT.search(c): new = ("non", "rapport : rapport d'audit")
                        elif POS.search(c): new = ("non", "rapport : liste de positions / titres en portefeuille")
                        elif FIN.search(c): new = ("non", "rapport : états financiers et notes")
                        elif COMM.search(c): new = ("oui", "rapport : commentaire de gestion")
                        elif state[1].startswith("annexe SFDR"): pass   # dans une annexe SFDR, un titre de frais ou de performance ne la ferme pas
                        elif FEES.search(c) and not FEES_NEG.search(c) and nmots(c) <= FEES_MAX_MOTS: new = ("oui", "rapport : frais effectifs (titre complet)")
                        elif PERF.search(c): new = ("oui", "rapport : performance")
                        elif FEES.search(c): compteur_titres["titre avec mot de frais non retenu comme titre de frais"] += 1
            if new is None and not (state[1].startswith("annexe SFDR")):
                lab, ou = sfdr_motif(titre, s["texte"])
                if lab:
                    new = ("non", f"annexe SFDR (texte : « {lab} »)"); compteur_sfdr[(t, lab, "texte")] += 1
            if new: state = new
            base.append(state)
        if prosp and not vu_propre and any(r[1] == "prospectus : autre compartiment" for r in base):
            base = [("oui", "prospectus : autre compartiment → oui, cas non tranché (section propre au fonds non repérée)") if r[1] == "prospectus : autre compartiment" else r for r in base]
            NON_TRANCHES.append((u["lot"], u["doc_id"], "prospectus parapluie : aucune section propre au fonds repérée, les sections « autre compartiment » passent en « oui »"))
    # exclusions générales, dans l'ordre des segments
    retenus = set()
    for s, (v, r) in zip(segs, base):
        ex = exclusions_generales(s["texte"], s["n_mots"])
        key = " ".join(s["texte"].split())
        if v == "oui":
            if ex: v, r = "non", LIB_EXCL[ex[0]]
            elif key in retenus: v, r = "non", LIB_EXCL["doublon"]
            else: retenus.add(key)
        res.append((v, r, ex))
    return res

# ------------------------------------------------------------------ 4. Passe 1 sur segments.jsonl (en flux)
os.nice(0)
fp = open(os.path.join(OUT, "segments_perimetre_v2.csv"), "w", encoding="utf-8", newline="")
wp = csv.writer(fp); wp.writerow(["segment_id", "doc_id", "lot", "strate", "ordre", "perimetre", "regle_perimetre", "perimetre_v2", "regle_perimetre_v2"])
regles = collections.Counter()      # (lot, strate, règle) -> n (règle appliquée)
declench = collections.Counter()    # (lot, strate, critère) -> n (déclenchements bruts, non exclusifs)
vus_docs = set(); cur = None; buf = []; n_lignes = 0; n_ignores = 0; ordre_ok = True
hors_pages = collections.Counter()
def finir():
    global buf
    if cur is None: return
    for did in SOURCES[cur]:
        u = unites[did]
        sous = [s for s in buf if s["page"] in u["page_set"]] if u.get("composite") else buf
        res = classer_document(u, sous)
        for s, (v, r, ex) in zip(sous, res):
            u["n_seg"] += 1
            if s["perimetre"] == "oui": u["n_old_oui"] += 1
            if v == "oui": u["n_v2_oui"] += 1; u["oui"].append((s["ordre"], s["segment_id"]))
            regles[(u["lot"], u["strate"], v, r)] += 1
            for e in ex: declench[(u["lot"], u["strate"], e)] += 1
            wp.writerow([s["segment_id"], did, u["lot"], u["strate"], s["ordre"], s["perimetre"], s["regle"], v, r])
    if any(unites[d].get("composite") for d in SOURCES[cur]):
        toutes = set().union(*[unites[d]["page_set"] for d in SOURCES[cur]])
        for s in buf:
            if s["page"] not in toutes: hors_pages[cur] += 1
    buf = []
with open(SEG, encoding="utf-8") as f:
    for line in f:
        n_lignes += 1
        i = line.find('"doc_id": "') + 11; did = line[i:line.index('"', i)]
        if did not in SOURCES: n_ignores += 1; continue
        d = json.loads(line)
        if did != cur:
            finir()
            if did in vus_docs: ordre_ok = False; ANOMALIES.append(f"{did} : segments non contigus dans segments.jsonl")
            vus_docs.add(did); cur = did
        buf.append({"segment_id": d["segment_id"], "ordre": d["ordre"], "titre": d["titre_section"], "page": d["page"],
                    "texte": d["texte_original"] or "", "n_mots": d["n_mots"], "perimetre": d["perimetre"], "regle": d["regle_perimetre"]})
    finir()
fp.close()
for did, u in unites.items():
    if u["n_seg"] == 0 and not u["motifs"]:
        u["motifs"].append("fichier tronqué ou texte absent (aucun segment)")
    u["oui"].sort()
    u["exclu"] = "oui" if u["motifs"] else "non"

# ------------------------------------------------------------------ 5. Cadre documentaire (4.4)
with open(os.path.join(OUT, "cadre_documents.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["doc_id", "sha256", "lot", "strate", "type_document", "fonds_concernes", "maison_gestion", "pays_distribution", "langue_origine", "statut_en",
                "n_segments_total", "n_segments_perimetre_v2_oui", "exclu_du_cadre", "motif_exclusion_cadre", "lignes_manifeste", "n_segments_perimetre_oui_ancien"])
    for did in sorted(unites, key=lambda k: (unites[k]["lot"], unites[k]["strate"], k)):
        u = unites[did]
        w.writerow([did, u["sha256"], u["lot"], u["strate"], u["type_document"], ";".join(u["fonds_concernes"]), u["maison_gestion"], ";".join(u["pays_distribution"]),
                    u["langue_origine"], u["statut_en"], u["n_seg"], u["n_v2_oui"], u["exclu"], " ; ".join(u["motifs"]), ";".join(u["lignes_manifeste"]), u["n_old_oui"]])

# ------------------------------------------------------------------ 6. Tirage en deux temps (5.2, 5.3)
tirage_docs = []      # (lot, strate, rang_document, reserve_document, doc_id)
tirage_segs = []      # (lot, strate, rang_document, reserve_document, doc_id, rang_segment, reserve_segment, segment_id, ordre)
ecarts = []; parcours = {}
for lot in LOTS:
    N = DOCUMENTS_PAR_STRATE[lot]; plafond = math.ceil(PART_MAX_MAISON * N)
    for strate in STRATES:
        cand = sorted(did for did, u in unites.items() if u["lot"] == lot and u["strate"] == strate and u["exclu"] == "non" and u["n_v2_oui"] >= MIN_SEGMENTS_OUI)
        rng = random.Random(graine_strate(lot, strate)); rng.shuffle(cand)
        acc = []; fonds_couverts = set(); par_maison = collections.Counter(); trace = []
        for did in cand:
            if len(acc) >= N + DOCUMENTS_DE_RESERVE: trace.append((did, "non examinée (principal et réserve complets)")); continue
            u = unites[did]
            if set(u["fonds_concernes"]) & fonds_couverts: trace.append((did, "refusée : fonds déjà couvert (" + ";".join(sorted(set(u["fonds_concernes"]) & fonds_couverts)) + ")")); continue
            if par_maison[u["maison_gestion"]] >= plafond: trace.append((did, f"refusée : maison « {u['maison_gestion']} » déjà à {par_maison[u['maison_gestion']]} unités (plafond {plafond})")); continue
            acc.append(did); fonds_couverts |= set(u["fonds_concernes"]); par_maison[u["maison_gestion"]] += 1
            trace.append((did, "acceptée : " + ("tirage principal" if len(acc) <= N else "réserve") + f" rang {len(acc)}"))
        parcours[(lot, strate)] = (cand, trace, plafond)
        n_pr = min(len(acc), N); n_res = max(0, len(acc) - N)
        if n_pr < N: ecarts.append((lot, strate, "documents (tirage principal)", N, n_pr))
        if n_res < DOCUMENTS_DE_RESERVE: ecarts.append((lot, strate, "documents de réserve", DOCUMENTS_DE_RESERVE, n_res))
        for rang, did in enumerate(acc, 1):
            res_doc = "non" if rang <= N else "oui"
            tirage_docs.append((lot, strate, rang, res_doc, did))
            segs = list(unites[did]["oui"])  # triés par ordre
            r2 = random.Random(graine_document(lot, strate, did)); r2.shuffle(segs)
            retenus = []
            for o, sid in segs:
                if any(abs(o - o2) == 1 for o2, _ in retenus): continue
                retenus.append((o, sid))
                if len(retenus) >= SEGMENTS_PAR_DOCUMENT + SEGMENTS_DE_RESERVE: break
            if len(retenus) < SEGMENTS_PAR_DOCUMENT: ecarts.append((lot, strate, f"segments du document {did} (tirage principal)", SEGMENTS_PAR_DOCUMENT, len(retenus)))
            if len(retenus) < SEGMENTS_PAR_DOCUMENT + SEGMENTS_DE_RESERVE: ecarts.append((lot, strate, f"segments du document {did} (principal + réserve)", SEGMENTS_PAR_DOCUMENT + SEGMENTS_DE_RESERVE, len(retenus)))
            for k, (o, sid) in enumerate(retenus, 1):
                tirage_segs.append((lot, strate, rang, res_doc, did, k, "non" if k <= SEGMENTS_PAR_DOCUMENT else "oui", sid, o))

# ------------------------------------------------------------------ 7. Passe 2 : champs des segments tirés
# Champs d'affichage (v3) : segments tirés + voisins d'ordre -1 / +1 dans la même unité (sans effet sur aucun calcul)
voulus = {t[7] for t in tirage_segs}
docs_voulus = {unites[t[4]]["source"] for t in tirage_segs}; champs = {}
voisins_voulus = collections.defaultdict(set)   # doc source -> ordres voulus
for t in tirage_segs: voisins_voulus[unites[t[4]]["source"]].update({t[8] - 1, t[8] + 1})
par_ordre = {}   # (doc source, ordre) -> (page, texte_original)
with open(SEG, encoding="utf-8") as f:
    for line in f:
        i = line.find('"doc_id": "') + 11; did = line[i:line.index('"', i)]
        if did not in docs_voulus: continue
        d = json.loads(line)
        if d["segment_id"] in voulus: champs[d["segment_id"]] = d
        if d["ordre"] in voisins_voulus[did]: par_ordre[(did, d["ordre"])] = (d["page"], d["texte_original"] or "")
ESP_AFF = re.compile(r"[^\S\r\n]{5,}")   # 5 blancs ou plus hors saut de ligne : espace, espace insécable U+00A0, U+2007, U+202F, autres espaces Unicode, tabulation
def texte_affichage(t):
    """Lecture seulement : chaque ligne est débarrassée de ses blancs de début et de fin, puis chaque suite de 5 blancs ou plus est remplacée par «  |  »."""
    return "\n".join(ESP_AFF.sub("  |  ", l.strip()) for l in (t or "").split("\n"))
def voisin(u, o):
    v = par_ordre.get((u["source"], o))
    if v is None: return ""
    if u.get("composite") and v[0] not in u["page_set"]: return ""   # unité découpée : le voisin doit appartenir à la même unité
    return texte_affichage(v[1])
regle_seg = {}
with open(os.path.join(OUT, "segments_perimetre_v2.csv"), encoding="utf-8") as f:
    for r in csv.DictReader(f):
        if r["segment_id"] in voulus: regle_seg[r["segment_id"]] = r["regle_perimetre_v2"]
COLS = ["lot", "strate", "rang_document", "reserve_document", "doc_id", "sha256", "fonds_concernes", "maison_gestion", "pays_distribution", "type_document", "langue_origine",
        "rang_segment", "reserve_segment", "segment_id", "titre_section", "page", "n_mots", "texte_original", "texte_en", "statut_en", "regle_perimetre_v2",
        "texte_affichage", "segment_precedent", "segment_suivant"]
with open(os.path.join(OUT, "tirage_pilote.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n"); w.writerow(COLS)
    for lot, strate, rang, resd, did, k, ress, sid, o in sorted(tirage_segs, key=lambda t: (t[0], t[1], t[2], t[5])):
        u = unites[did]; d = champs[sid]
        te = d["texte_en"] if d["statut_en"] in ("traduit_automatique_aligne", "original_anglais") and d["texte_en"] else ""
        w.writerow([lot, strate, rang, resd, did, u["sha256"], ";".join(u["fonds_concernes"]), u["maison_gestion"], ";".join(u["pays_distribution"]), u["type_document"],
                    u["langue_origine"], k, ress, sid, d["titre_section"] or "", d["page"] if d["page"] is not None else "", d["n_mots"], d["texte_original"], te, d["statut_en"], regle_seg[sid],
                    texte_affichage(d["texte_original"]), voisin(u, o - 1), voisin(u, o + 1)])
        if d["langue_origine"] and u["langue_origine"] and d["langue_origine"] != u["langue_origine"]:
            ANOMALIES.append(f"{sid} : langue du segment (« {d['langue_origine']} », langue détectée retenue à la consolidation) ≠ langue du manifeste rectifié (« {u['langue_origine']} ») ; la colonne langue_origine reprend le manifeste rectifié")

# ------------------------------------------------------------------ 8. Auto-contrôles internes (section 7)
ids = [t[7] for t in tirage_segs]
ctrl = []
ctrl.append(("aucun segment_id en double", len(ids) == len(set(ids)), f"{len(ids)} lignes, {len(set(ids))} segment_id distincts"))
dd = collections.Counter((t[0], t[1], t[4]) for t in tirage_docs)
ctrl.append(("aucune unité tirée deux fois dans une strate", all(v == 1 for v in dd.values()), f"{len(dd)} couples (strate, unité)"))
ctrl.append(("aucun document exclu du cadre dans le tirage", all(unites[t[4]]["exclu"] == "non" for t in tirage_docs), ""))
ctrl.append(("tous les segments tirés sont perimetre_v2 = oui dans leur unité", all(t[7] in {sid for _, sid in unites[t[4]]["oui"]} for t in tirage_segs), ""))
ctrl.append(("segments.jsonl contigu par document", ordre_ok, f"{n_lignes} lignes lues, {n_ignores} lignes de doublons non référence ignorées"))

# ------------------------------------------------------------------ 9. Entonnoir
E = []
E.append("# Entonnoir du cadre de tirage — mission 3, version 3 (ajustement v3 du 17/11/2026)\n")
E.append("Effectifs à chaque étape, par lot et par strate. Unités documentaires = fichiers uniques (sha256) parmi les lignes « collecté » du manifeste ; les segments sont comptés une seule fois par unité (segments de la ligne de référence). « Règle appliquée » = première règle qui décide du segment ; « déclenchements bruts » = nombre de segments qui remplissent chaque critère d'exclusion générale, même si une autre règle a décidé avant (non exclusifs).\n")
groupes_es = sorted({(u["lot"], u["strate"]) for u in unites.values()}, key=lambda k: (["lot1", "lot2", "annexe_SG"].index(k[0]), k[1]))
for lot, strate in groupes_es:
    us = [u for u in unites.values() if u["lot"] == lot and u["strate"] == strate]
    nl = sum(len(u["lignes_manifeste"]) for u in us)
    E.append(f"\n## {lot} — {strate} ({', '.join(sorted({u['type_document'] for u in us}))})\n")
    E.append("| Étape | Effectif |\n|---|---|")
    E.append(f"| Lignes « collecté » du manifeste | {nl} |")
    E.append(f"| Unités documentaires (sha256 uniques) | {len(us)} |")
    mc = collections.Counter(m for u in us for m in u["motifs"])
    for m, v in sorted(mc.items()): E.append(f"| Exclues du cadre — {m} | {v} |")
    E.append(f"| Exclues du cadre (total, un document peut avoir plusieurs motifs) | {sum(1 for u in us if u['exclu']=='oui')} |")
    E.append(f"| Unités dans le cadre | {sum(1 for u in us if u['exclu']=='non')} |")
    E.append(f"| Unités dans le cadre avec ≥ {MIN_SEGMENTS_OUI} segments perimetre_v2 « oui » (éligibles au temps 1) | {sum(1 for u in us if u['exclu']=='non' and u['n_v2_oui']>=MIN_SEGMENTS_OUI)} |")
    E.append(f"| Segments totaux (toutes unités) | {sum(u['n_seg'] for u in us)} |")
    E.append(f"| Segments perimetre (ancien) « oui » (toutes unités) | {sum(u['n_old_oui'] for u in us)} |")
    E.append(f"| Segments perimetre_v2 « oui » (toutes unités) | {sum(u['n_v2_oui'] for u in us)} |")
    E.append(f"| Segments totaux (unités dans le cadre) | {sum(u['n_seg'] for u in us if u['exclu']=='non')} |")
    E.append(f"| Segments perimetre (ancien) « oui » (unités dans le cadre) | {sum(u['n_old_oui'] for u in us if u['exclu']=='non')} |")
    E.append(f"| Segments perimetre_v2 « oui » (unités dans le cadre) | {sum(u['n_v2_oui'] for u in us if u['exclu']=='non')} |")
    E.append("\nSegments par règle appliquée (toutes unités de la strate) :\n\n| perimetre_v2 | Règle appliquée | Segments |\n|---|---|---|")
    for (l2, s2, v, r), n in sorted(regles.items(), key=lambda kv: (-kv[1], kv[0])):
        if l2 == lot and s2 == strate: E.append(f"| {v} | {r} | {n} |")
    E.append("\nDéclenchements bruts des exclusions générales (non exclusifs) :\n\n| Critère | Segments |\n|---|---|")
    for e in ["chiffres", "court"]: E.append(f"| {LIB_EXCL[e]} | {declench[(lot, strate, e)]} |")
open(os.path.join(OUT, "entonnoir.md"), "w", encoding="utf-8").write("\n".join(E) + "\n")

# ------------------------------------------------------------------ 10. Journal
heure = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)).strftime("%d/%m/%Y %H:%M")
J("# Journal du tirage — mission 3, version 3 (ajustement v3 du 17/11/2026)\n")
J("Version 3 : seuls changements par rapport à la v2 livrée dans `tirage_v2/` (non modifiée) : (1) suppression, pour tous les types et toutes les strates, de l'exclusion générale « 5 espaces consécutifs ou plus » ; les segments qu'elle décidait passent aux règles suivantes (« moins de 4 mots », « texte identique », sinon « oui » avec leur règle de structure) ; (2) ajout dans tirage_pilote.csv des champs de lecture `texte_affichage`, `segment_precedent` et `segment_suivant` (section 6 bis), sans effet sur aucun calcul. Toutes les autres règles de la v2 sont inchangées (fichier composite, chiffres > moitié, moins de 4 mots, texte identique, périmètre des prospectus et rapports, annexes SFDR, exclusions du cadre, graines, ordre de tri, un document par fonds et par strate, plafond par maison au plus ceil(0,4 × N), cibles et réserves).")
J("Confirmation : la règle « chiffres > moitié » s'applique au texte_original tel quel ; numérateur = chiffres (str.isdigit), dénominateur = caractères non blancs (tout caractère pour lequel str.isspace est faux : espaces, espaces insécables, autres espaces Unicode, tabulations et sauts de ligne ne comptent pas). C'était déjà le calcul de la v1 et de la v2.\n")
J(f"Produit par tirage_script.py le {heure} (heure d'Europe/Luxembourg). Aucun accès réseau, aucun téléchargement, aucune traduction ; aucun fichier existant modifié ni supprimé. Aucun segment ni document choisi, retiré, remplacé ou réordonné à la main.\n")
J("## 1. Fichiers lus (empreintes sha256)\n")
for p in [ZIP_LOT1, ZIP_LOT2, RECT["lot1"], RECT["lot2"], MAN_COMPLET, SEG, CORPUS]:
    J(f"- `{os.path.relpath(p, BASE)}` : `{sha256_fichier(p)}`")
J("\nManifestes lus dans les archives livrées : `manifeste.csv` (lot 1), `lot2/manifeste_lot2.csv` (lot 2), `lot2/annexe_SG/manifeste_annexe_SG.csv` (annexe Singapour), `lot2/echantillon_lot2.csv` (sociétés de gestion du lot 2).\n")
J("## 2. Valeurs rectifiées le 16/11 utilisées\n")
J(f"Les colonnes `langue_origine` et `indicateur_traduit` sont reprises des manifestes rectifiés du 16/11 (journal `corpus/journal_rectifications_2026-11-16.md`) là où elles diffèrent des manifestes livrés le 15/11 : {len(diff_rect)} valeurs sur {len({d[1] for d in diff_rect})} lignes. Le statut de traduction (`statut_en` du cadre) est le `statut_traduction` de la consolidation, identique à l'indicateur rectifié pour toutes les lignes collectées.\n")
J("| Lot | Ligne du manifeste | Colonne | Valeur livrée | Valeur rectifiée retenue | Statut de la ligne |\n|---|---|---|---|---|---|")
for lot, did, k, a, b, st in diff_rect: J(f"| {lot} | {did} | {k} | {a or '(vide)'} | {b or '(vide)'} | {st} |")
J("\n## 3. Construction du cadre (sections 4.1, 4.2)\n")
J("- Unité documentaire = lignes « collecté » d'un même lot partageant le même sha256 ; ligne de référence = plus petit `identifiant_document` (ordre alphabétique) ; `lignes_manifeste` = toutes les lignes du groupe ; `fonds_concernes` = ISIN de ces lignes ; `pays_distribution` = pays de ces lignes. Aucun sha256 n'est partagé entre deux lots. Les lignes « manquant » et « exclu » n'ont pas de fichier et ne forment pas d'unité.")
J("- Segments d'une unité = segments de la ligne de référence dans `segments.jsonl` ; les segments identiques des autres lignes du groupe sont ignorés (comptés une seule fois).")
J("- `tronque` et `reserve_professionnels` : repris de `consolidation/manifeste_complete.csv`. `tronque = oui` : les 4 lignes du rapport Ossiam LU0599613147 (sha256 a83a1a56…, PDF illisible, aucun texte). `reserve_professionnels = oui` : recherche mécanique faite à la consolidation (expressions « réservé aux investisseurs professionnels », « professional investors only », « nur für professionelle Anleger », « únicamente a inversores profesionales »… sur les pages 1-2, la dernière page et les en-têtes/pieds répétés) : 15 lignes, toutes des factsheets. Une unité est exclue si l'une de ses lignes porte le marqueur.")
J("- Annexe Singapour : lot `annexe_SG` de la consolidation. Avis : `type_document = Avis`. Paires : lignes dont `notes` commence par « paire » ou dont `document_parent` est un avis (identifiants CH-xxx-DOC-…, rapports CNMV et factsheets appariés aux avis).")
J("- Strates : S1 = KID, KIID, fiches locales (Fiche_locale = KFS de Hong Kong ; PHS) ; S2 = factsheets ; S3 = prospectus ; S4 = rapports (annuels et semestriels) et bulletins trimestriels. Les avis n'entrent dans aucune strate (« hors strate »).")
J("- `maison_gestion` : valeur du manifeste ; pour la valeur générique « autre émetteur » du lot 2, la société de gestion de l'ISIN est reprise de `lot2/echantillon_lot2.csv` (archive livrée) sous la forme « autre émetteur : <société> », et c'est cette valeur qui compte pour le plafond par maison. Aucune autre normalisation (« BlackRock » et « BlackRock (iShares) », « Fidelity » et « Fidelity International » restent distincts ; aucune de ces paires ne coexiste dans une même strate du cadre).")
J("\n## 3 bis. Fichiers composites (règle de l'ajustement du 17/11)\n")
J("Recherche dans tout le corpus (lots 1, 2 et annexe Singapour) des fichiers (même sha256, lignes « collecté ») listés sous plusieurs types de document. Au lieu du type de la ligne de référence, le fichier est découpé par pages d'après les titres du texte (`consolidation/corpus.jsonl`, marqueurs de page « ----- p. N ----- ») : page de titre de KID = « Document d'Informations Clés » (ou équivalent) dans les 15 premières lignes non vides de la page ; début du prospectus = ligne réduite au mot « PROSPECTUS » dans les 15 premières lignes non vides ; un KID couvre sa page de titre jusqu'à la page qui précède le KID suivant ou le prospectus, et appartient à la classe de parts dont l'ISIN figure dans ses pages. Les segments sont répartis selon leur champ `page` ; leurs `segment_id` ne changent pas.")
J("Doc_id des unités créées : doc_id de la ligne de référence (plus petit doc_id du groupe, celui sous lequel les segments figurent dans segments.jsonl), suivi de « -KID » (KID de la classe de parts du manifeste, strate S1) ou « -PROSPECTUS » (strate S3) ; les pages des KID des autres classes forment une unité « -KID-AUTRES-CLASSES », gardée dans cadre_documents.csv pour la traçabilité et exclue du cadre (motif « KID d'une autre classe de parts »).\n")
if not COMPOSITES: J("- Aucun fichier composite.")
for ref_id, c in COMPOSITES.items():
    J(f"### {ref_id} (lot {c['lot']}, sha256 {c['sha256']})\n")
    J(f"- Lignes du manifeste : {', '.join(c['lignes'])} ; types : {', '.join(c['types'])} ; ISIN du manifeste : {c['isin']}.")
    for d, f_, isins, propre in c.get("blocs", []):
        J(f"- KID repéré dans le texte : pages {d}-{f_} ; ISIN présents : {', '.join(isins) or '(aucun)'} ; {'classe de parts du manifeste' if propre else 'autre classe de parts'}.")
    J(f"- Début du prospectus repéré dans le texte : page {c.get('p_prosp')} (dernière page du fichier : {c.get('pmax')}).")
    for k, (pl, deb) in c.get("notes_limites", {}).items():
        J(f"- Limites annoncées par les notes de {k} : plages {', '.join(f'{a}-{b}' for a, b in pl) or '(aucune)'} ; début annoncé {', '.join(map(str, deb)) or '(aucun)'}.")
    if "retenu" in c:
        J(f"- **Limites retenues** : KID de la part du manifeste pages {c['retenu']['KID']} ; KID des autres classes pages {c['retenu']['autres'] or '(aucune)'} ; prospectus pages {c['retenu']['PROSPECTUS']}.")
    for did in c.get("unites", []):
        u = unites[did]; J(f"- Unité {did} : type {u['type_document']}, strate {u['strate']}, pages {u['pages']}, {u['n_seg']} segments, {u['n_v2_oui']} « oui » perimetre_v2, {'exclue du cadre (' + ' ; '.join(u['motifs']) + ')' if u['exclu'] == 'oui' else 'dans le cadre'}.")
    J(f"- Segments du fichier hors des pages retenues : {hors_pages.get(ref_id, 0)}.\n")

J("\n## 4. Règles de périmètre v2 réellement utilisées (section 4.3)\n")
J("Le champ `perimetre` n'est pas modifié ; `perimetre_v2` et `regle_perimetre_v2` sont écrits pour chaque segment des unités dans `segments_perimetre_v2.csv` (fichier nouveau). Les règles portent sur les titres de section (`titre_section`), le nom et l'ISIN des fonds du groupe, des marqueurs de structure et des critères de forme ; jamais sur le sens.\n")
J("Mécanique des titres :")
J("- Un titre est pris en compte quand `titre_section` change d'un segment au suivant ; « haut de page » = premier segment d'une nouvelle page portant un nouveau titre (approximation : l'indicateur de haut de page de la consolidation n'est pas dans segments.jsonl).")
J(f"- Recollement (4.3) : la segmentation de la consolidation a déjà recollé les lignes de titre consécutives d'un même bloc ; les intitulés coupés restants ont leur fin en tête du premier segment de la section (ex. « State Street SPDR MSCI Europe Communication Services UCITS » + « ETF »). Le titre comparé = titre + les lignes de tête de ce segment qui ont de 1 à {CONT_MAX_MOTS} mots, sans chiffre, sans ponctuation finale ni double espace (au plus {CONT_MAX_LIGNES} lignes), si le titre ne finit pas par une ponctuation. Pour les compartiments, si le titre recollé ne classe rien, le titre brut est aussi essayé ; « propre » l'emporte sur « autre ». Le texte des segments n'est pas modifié.")
J("- Titre ignoré (état inchangé) s'il a la forme d'un fragment de prose : commence par une minuscule, un tiret ou une puce, ou finit par « ; » ou « , ».")
J("- Fonds d'une unité regroupant plusieurs lignes : une section est « propre au fonds » si son titre contient l'ISIN ou le nom de l'un des fonds du groupe.\n")
J("Comptes des titres : " + ", ".join(f"{k} : {v}" for k, v in sorted(compteur_titres.items())) + ".\n")
J("Règles appliquées, avec le nombre de segments (tous lots, toutes unités, y compris hors cadre) :\n")
J("| perimetre_v2 | Règle | Segments |\n|---|---|---|")
tot = collections.Counter()
for (l, s, v, r), n in regles.items(): tot[(v, r)] += n
for (v, r), n in sorted(tot.items(), key=lambda kv: -kv[1]): J(f"| {v} | {r} | {n} |")
J("\nDéclencheurs d'annexe SFDR réellement utilisés (nombre de fois où le marqueur a ouvert une annexe SFDR) :\n")
J("| Type | Marqueur | Trouvé dans | Ouvertures |\n|---|---|---|---|")
for (t, lab, ou), n in sorted(compteur_sfdr.items(), key=lambda kv: -kv[1]): J(f"| {t} | {lab} | {ou} | {n} |")
J("\nPrécisions :")
J("- Prospectus : « oui » partie générale (état initial) et section propre au fonds ; « non » autres compartiments, annexes-listes (sous-dépositaires, adresses, liste des fonds) et annexes SFDR. Retour en partie générale : intitulé d'annexe (« Appendix », « Annexe », « Anhang »…) en haut de page, ou titre en haut de page après une annexe-liste. Contrairement à la consolidation, un titre quelconque en haut de page ne ramène plus en partie générale (cause des « Fondsmerkmale » classés partie générale au milieu d'un autre compartiment).")
J("- Annexes SFDR (prospectus et rapports) : une annexe s'ouvre sur un titre portant un marqueur, ou sur un segment dont le texte porte un marqueur (sauf segment de sommaire : points de conduite « ..... » ou titre « Contents / Sommaire / Inhaltsverzeichnis »). Marqueurs : « Legal entity identifier » et équivalents (titre ou texte) ; « Product name : » et équivalents (titre ou 200 premiers caractères) ; en-tête du modèle « Pre-contractual / Periodic disclosure … Article 8 ou 9 » et équivalents (titre ou texte) ; encadré « Sustainability indicators measure … » et équivalents (titre ou texte) ; « Annexe II / III » (titre seulement, avec un mot du modèle SFDR dans le titre ou au début du segment) ; « 2022/1288 » (titre seulement) ; « Annexe SFDR » (titre commençant par un mot d'annexe suivi de « SFDR », ou par « SFDR »). L'en-tête du modèle n'est reconnu dans le texte qu'en début de ligne ou après une colonne (3 espaces ou plus), pas au milieu d'une phrase. Les renvois de prose (« Anhang II dieses Prospekts », « conformément au règlement délégué (UE) 2022/1288 », « les informations précontractuelles … sont disponibles en annexe ») n'ouvrent donc pas d'annexe : un premier essai qui les comptait classait à tort des parties générales entières en « annexe SFDR » ; ces marqueurs ont été resserrés au vu des seules positions d'ouverture des annexes (titres et débuts de segments déclencheurs), sans consulter les tirages d'essai. Fermeture : prospectus — titre de compartiment, d'annexe-liste ou intitulé d'annexe en haut de page ; rapports — titre d'audit, de positions, d'états financiers ou de commentaire de gestion (un titre de performance ou de frais, fréquent dans le modèle SFDR périodique, ne la ferme pas).")
J("- Rapports : « non » rapport d'audit, listes de positions et de titres en portefeuille, états financiers et notes, annexes SFDR (mêmes marqueurs, appliqués aussi aux rapports : le doute sur une annexe SFDR vaut « non ») ; « oui » commentaire de gestion, frais effectifs, performance. Frais : titre complet — le titre doit contenir un terme de frais non précédé d'une exclusion (« hors », « net of », « after », « ohne », « sin »…) et compter au plus 12 mots ; « Contributions à la performance de l'exercice (hors frais) » n'est donc pas un titre de frais (il est classé performance). Section non classée : « oui » (cas non tranché).")
J("- KID, fiches locales, factsheets, bulletins : « oui » sauf exclusions générales.")
J("- Exclusions générales (tous types), appliquées dans cet ordre aux segments sinon « oui » : chiffres > moitié des caractères non blancs ; moins de 4 mots (`n_mots`) ; texte identique (espaces normalisés) à un segment déjà retenu « oui » plus haut dans la même unité.")
J("\nExemples de titres recollés (40 au plus) :\n")
for did, a, b in exemples_recolles: J(f"- {did} : « {a} » → « {b} »")
J("\nExemples de titres ignorés comme fragments de prose (15 au plus) :\n")
for did, a in exemples_ignores: J(f"- {did} : « {a[:120]} »")
J("\n## 5. Cas non tranchés\n")
J("Règle : cas non tranché = « oui » et consigné, sauf liste de positions, annexe SFDR, rapport d'audit (doute = « non »). Sections de rapport non classées : « oui » (comptées ci-dessus sous « rapport : section non classée »).\n")
for lot, did, m in NON_TRANCHES: J(f"- {lot} — {did} : {m} ({'dans le cadre' if unites[did]['exclu']=='non' else 'hors cadre'})")
J("\n## 6. Tirage : paramètres, parcours et écarts à la cible\n")
J(f"Paramètres : graine {GRAINE} ; générateur Python `random.Random(\"{GRAINE}-<lot>-<strate>\")` puis `random.Random(\"{GRAINE}-<lot>-<strate>-<doc_id>\")` (graine chaîne, déterministe) ; {SEGMENTS_PAR_STRATE} segments par strate ; {SEGMENTS_PAR_DOCUMENT} segments par document ; {DOCUMENTS_PAR_STRATE} documents par strate ; {DOCUMENTS_DE_RESERVE} documents et {SEGMENTS_DE_RESERVE} segments de réserve ; plafond par maison ceil({PART_MAX_MAISON} × N).\n")
J("Interprétations : (a) la liste est triée par doc_id puis mélangée par `shuffle` ; (b) une maison est refusée dès qu'elle a déjà ceil(0,4 × N) unités acceptées (au plus 40 % ; une lecture littérale « pas plus de » autoriserait une unité de plus) ; (c) les conditions de fonds et de maison continuent de s'appliquer aux unités de réserve, qui sont les 5 unités acceptées suivantes, et comptent pour les acceptations suivantes ; (d) dans un document, les segments `perimetre_v2 = oui` sont triés par `ordre` avant le mélange, et un segment est écarté si son `ordre` diffère de 1 de celui d'un segment déjà retenu ; (e) `texte_en` n'est rempli que si `statut_en` vaut « traduit_automatique_aligne » ou « original_anglais » (texte anglais d'origine).\n")
for (lot, strate), (cand, trace, plafond) in parcours.items():
    J(f"\n### {lot} — {strate} : {len(cand)} unités éligibles, plafond par maison {plafond}\n")
    for did, m in trace: J(f"- {did} ({unites[did]['maison_gestion']} ; {';'.join(unites[did]['fonds_concernes'])}) : {m}")
J("\n### Écarts à la cible\n")
if not ecarts: J("- Aucun.")
for lot, strate, quoi, cible, obtenu in ecarts: J(f"- {lot} — {strate} : {quoi} : cible {cible}, obtenu {obtenu}. Le cadre ne permet pas d'atteindre la cible ; arrêt sans complément manuel.")
J("\n## 7. Auto-contrôles internes\n")
for nom, ok, det in ctrl: J(f"- {nom} : {'OK' if ok else 'ÉCHEC'} {('— ' + det) if det else ''}")
cnt = collections.Counter((t[0], t[1], t[3]) for t in tirage_docs); cs = collections.Counter((t[0], t[1], t[3], t[6]) for t in tirage_segs)
J("\n| Lot | Strate | Documents principal | Documents réserve | Segments principal (docs principaux) | Segments réserve (docs principaux) | Segments des docs de réserve |\n|---|---|---|---|---|---|---|")
for lot in LOTS:
    for strate in STRATES:
        J(f"| {lot} | {strate} | {cnt[(lot,strate,'non')]} | {cnt[(lot,strate,'oui')]} | {cs[(lot,strate,'non','non')]} | {cs[(lot,strate,'non','oui')]} | {cs[(lot,strate,'oui','non')]+cs[(lot,strate,'oui','oui')]} |")
J("\n## 6 bis. Champs d'affichage (v3)\n")
J("- `texte_affichage` : texte_original dont chaque ligne est d'abord débarrassée de ses blancs de début et de fin, puis dont chaque suite de 5 blancs ou plus (hors saut de ligne : espace, espace insécable U+00A0, espaces Unicode tels que U+2007 et U+202F, tabulation) est remplacée par «  |  » (deux espaces, barre verticale, deux espaces). Le retrait des blancs de bord est fait avant le remplacement, pour qu'une colonne en début de ligne ne laisse pas une barre isolée en tête. Les sauts de ligne sont conservés.")
J("- `segment_precedent` / `segment_suivant` : texte_affichage des segments d'ordre immédiatement inférieur et supérieur de la même unité documentaire, quel que soit leur périmètre ; vide s'il n'y en a pas. Pour les unités découpées d'un fichier composite (Colville), « même unité » veut dire l'unité découpée : un voisin situé sur une page d'une autre unité (par exemple le segment de la page 4 pour le dernier segment du KID pages 1-3) est laissé vide.")
J("- Ces champs ne sont lus qu'après le tirage ; ils ne modifient ni texte_original, ni n_mots, ni aucune règle ni le tirage.\n")
J("\n## 8. Anomalies\n")
if not ANOMALIES: J("- Aucune.")
for a in ANOMALIES: J(f"- {a}")
open(os.path.join(OUT, "journal_tirage.md"), "w", encoding="utf-8").write("\n".join(JOURNAL) + "\n")
print("ok", len(tirage_segs), "lignes ;", "sha256 tirage_pilote.csv", sha256_fichier(os.path.join(OUT, "tirage_pilote.csv")))
