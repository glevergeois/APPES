import pandas as pd
from io import StringIO

data = """
Index\tOrdre\tNom scientifique\tNom commun\tCategorie Liste rouge France\tTendance\tCategorie Liste rouge mondiale\tCategorie\tSous-Categorie\tStatut d'endemisme*
1\tCarnivora\tMustela_lutreola\tVison_d'Europe\tCr\tDowna\tCr\tmammifere\tmammifere_terrestre
2\tCarnivora\tUrsus_arctos\tOurs_brun\tCr\tUppera\tLc\tmammifere\tmammifere_terrestre
3\tChiroptera\tRhinolophus_mehelyi\tRhinolophe_de_Mehely\tCr*\t?\tVu\tmammifere\tmammifere_terrestre
4\tCarnivora\tLynx_lynx\tLynx_boreal\tEn\tStilla\tLc\tmammifere\tmammifere_terrestre
5\tCetartiodactyla\tCapra_pyrenaica\tBouquetin_iberique\tEn\tUppera\tLc\tmammifere\tmammifere_terrestre
6\tChiroptera\tMyotis_dasycneme\tMurin_des_marais\tEn\t?\tNt\tmammifere\tmammifere_terrestre
7\tRodentia\tCricetus_cricetus\tGrand_hamster\tEn\tStilla\tLc\tmammifere\tmammifere_terrestre
8\tCarnivora\tCanis_lupus\tLoup_gris\tVu\tUppera\tLc\tmammifere\tmammifere_terrestre
9\tCetartiodactyla\tOvis_gmelinii\tMouflon_d'Armenie\tVu\tStilla\tVu\tmammifere\tmammifere_terrestre
10\tChiroptera\tMiniopterus_schreibersii\tMinioptere_de_Schreibers\tVu\t?\tNt\tmammifere\tmammifere_terrestre
11\tChiroptera\tMyotis_escalerai\tMurin_d'Escalera\tVu\t?\tNe\tmammifere\tmammifere_terrestre
12\tChiroptera\tMyotis_punicus\tMurin_du_Maghreb\tVu\tDowna\tDd\tmammifere\tmammifere_terrestre
13\tChiroptera\tNyctalus_lasiopterus\tGrande_noctule\tVu\t?\tVu\tmammifere\tmammifere_terrestre
14\tChiroptera\tNyctalus_noctula\tNoctule_commune\tVu\tDowna\tLc\tmammifere\tmammifere_terrestre
15\tChiroptera\tPlecotus_macrobullaris\tOreillard_montagnard\tVu\t?\tLc\tmammifere\tmammifere_terrestre
16\tSoricomorpha\tGalemys_pyrenaicus\tDesman_des_Pyrenees\tVu\tDowna\tVu\tmammifere\tmammifere_terrestre
17\tCarnivora\tMustela_putorius\tPutois_d'Europe\tNt\tDowna\tLc\tmammifere\tmammifere_terrestre
18\tCetartiodactyla\tCapra_ibex\tBouquetin_des_Alpes\tNt\tUppera\tLc\tmammifere\tmammifere_terrestre
19\tChiroptera\tTadarida_teniotis\tMolosse_de_Cestoni\tNt\t?\tLc\tmammifere\tmammifere_terrestre
20\tChiroptera\tEptesicus_serotinus\tSerotine_commune\tNt\t?\tLc\tmammifere\tmammifere_terrestre
21\tChiroptera\tMyotis_bechsteinii\tMurin_de_Bechstein\tNt\t?\tNt\tmammifere\tmammifere_terrestre
22\tChiroptera\tMyotis_blythii\tPetit_murin\tNt\t?\tLc\tmammifere\tmammifere_terrestre
23\tChiroptera\tMyotis_capaccinii\tMurin_de_Capaccini\tNt\t?\tVu\tmammifere\tmammifere_terrestre
24\tChiroptera\tNyctalus_leisleri\tNoctule_de_Leisler\tNt\tDowna\tLc\tmammifere\tmammifere_terrestre
25\tChiroptera\tPipistrellus_nathusii\tPipistrelle_de_Nathusius\tNt\t?\tLc\tmammifere\tmammifere_terrestre
26\tChiroptera\tPipistrellus_pipistrellus\tPipistrelle_commune\tNt\tDowna\tLc\tmammifere\tmammifere_terrestre
27\tLagomorpha\tLepus_corsicanus\tLievre_de_Corse\tNt\tUppera\tVu\tmammifere\tmammifere_terrestre
28\tLagomorpha\tLepus_timidus\tLievre_variable\tNt\tDowna\tLc\tmammifere\tmammifere_terrestre
29\tLagomorpha\tOryctolagus_cuniculus\tLapin_de_garenne\tNt\tDowna\tNt\tmammifere\tmammifere_terrestre
30\tRodentia\tArvicola_sapidus\tCampagnol_amphibie\tNt\tDowna\tVu\tmammifere\tmammifere_terrestre
31\tRodentia\tArvicola_terrestris\tCampagnol_terrestre\tNt\tDowna\tLc\tmammifere\tmammifere_terrestre
32\tSoricomorpha\tCrocidura_leucodon\tCrocidure_leucode\tNt\tDowna\tLc\tmammifere\tmammifere_terrestre
33\tSoricomorpha\tCrocidura_suaveolens\tCrocidure_des_jardins\tNt\tDowna\tLc\tmammifere\tmammifere_terrestre
34\tSoricomorpha\tTalpa_caeca\tTaupe_aveugle\tNt\t?\tLc\tmammifere\tmammifere_terrestre
35\tCarnivora\tVulpes_vulpes\tRenard_roux\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
36\tCarnivora\tFelis_silvestris\tChat_forestier\tLc\tUppera\tLc\tmammifere\tmammifere_terrestre
37\tCarnivora\tLutra_lutra\tLoutre_d'Europe\tLc\tUppera\tNt\tmammifere\tmammifere_terrestre
38\tCarnivora\tMartes_foina\tFouine\tLc\t?\tLc\tmammifere\tmammifere_terrestre
39\tCarnivora\tMartes_martes\tMartre_des_pins\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
40\tCarnivora\tMeles_meles\tBlaireau_europeen\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
41\tCarnivora\tMustela_erminea\tHermine\tLc\t?\tLc\tmammifere\tmammifere_terrestre
42\tCarnivora\tMustela_nivalis\tBelette_d'Europe\tLc\t?\tLc\tmammifere\tmammifere_terrestre
43\tCarnivora\tGenetta_genetta\tGenette_commune\tLc\tUppera\tLc\tmammifere\tmammifere_terrestre
44\tCetartiodactyla\tRupicapra_pyrenaica\tIsard\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
45\tCetartiodactyla\tRupicapra_rupicapra\tChamois\tLc\tUppera\tLc\tmammifere\tmammifere_terrestre
46\tCetartiodactyla\tCapreolus_capreolus\tChevreuil_europeen\tLc\tUppera\tLc\tmammifere\tmammifere_terrestre
47\tCetartiodactyla\tCervus_elaphus\tCerf_elaphe\tLc\tUppera\tLc\tmammifere\tmammifere_terrestre
48\tCetartiodactyla\tSus_scrofa\tSanglier\tLc\tUppera\tLc\tmammifere\tmammifere_terrestre
49\tChiroptera\tRhinolophus_euryale\tRhinolophe_euryale\tLc\t?\tNt\tmammifere\tmammifere_terrestre
50\tChiroptera\tRhinolophus_ferrumequinum\tGrand_rhinolophe\tLc\tUppera\tLc\tmammifere\tmammifere_terrestre
51\tChiroptera\tRhinolophus_hipposideros\tPetit_rhinolophe\tLc\tUppera\tLc\tmammifere\tmammifere_terrestre
52\tChiroptera\tBarbastella_barbastellus\tBarbastelle_d'Europe\tLc\t?\tNt\tmammifere\tmammifere_terrestre
53\tChiroptera\tHypsugo_savii\tVespere_de_Savi\tLc\t?\tLc\tmammifere\tmammifere_terrestre
54\tChiroptera\tMyotis_alcathoe\tMurin_d'Alcathoe\tLc\t?\tDd\tmammifere\tmammifere_terrestre
55\tChiroptera\tMyotis_brandtii\tMurin_de_Brandt\tLc\t?\tLc\tmammifere\tmammifere_terrestre
56\tChiroptera\tMyotis_daubentonii\tMurin_de_Daubenton\tLc\t?\tLc\tmammifere\tmammifere_terrestre
57\tChiroptera\tMyotis_emarginatus\tMurin_à_oreilles_echancrees\tLc\tUppera\tLc\tmammifere\tmammifere_terrestre
58\tChiroptera\tMyotis_myotis\tGrand_murin\tLc\tUppera\tLc\tmammifere\tmammifere_terrestre
59\tChiroptera\tMyotis_mystacinus\tMurin_à_moustaches\tLc\tUppera\tLc\tmammifere\tmammifere_terrestre
60\tChiroptera\tMyotis_nattereri\tMurin_de_Natterer\tLc\t?\tLc\tmammifere\tmammifere_terrestre
61\tChiroptera\tPipistrellus_kuhlii\tPipistrelle_de_Kuhl\tLc\tUppera\tLc\tmammifere\tmammifere_terrestre
62\tChiroptera\tPipistrellus_pygmaeus\tPipistrelle_pygmee\tLc\t?\tLc\tmammifere\tmammifere_terrestre
63\tChiroptera\tPlecotus_auritus\tOreillard_roux\tLc\t?\tLc\tmammifere\tmammifere_terrestre
64\tChiroptera\tPlecotus_austriacus\tOreillard_gris\tLc\t?\tLc\tmammifere\tmammifere_terrestre
65\tErinaceomorpha\tErinaceus_europaeus\tHerisson_d'Europe\tLc\t?\tLc\tmammifere\tmammifere_terrestre
66\tLagomorpha\tLepus_europaeus\tLievre_d'Europe\tLc\t?\tLc\tmammifere\tmammifere_terrestre
67\tRodentia\tCastor_fiber\tCastor_d'Eurasie\tLc\tUppera\tLc\tmammifere\tmammifere_terrestre
68\tRodentia\tArvicola_scherman\tCampagnol_fouisseur\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
69\tRodentia\tChionomys_nivalis\tCampagnol_des_neiges\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
70\tRodentia\tMicrotus_agrestis\tCampagnol_agreste\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
71\tRodentia\tMicrotus_arvalis\tCampagnol_des_champs\tLc\tUppera\tLc\tmammifere\tmammifere_terrestre
72\tRodentia\tMicrotus_duodecimcostatus\tCampagnol_provençal\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
73\tRodentia\tMicrotus_lusitanicus\tCampagnol_basque\tLc\t?\tLc\tmammifere\tmammifere_terrestre
74\tRodentia\tMicrotus_multiplex\tCampagnol_de_Fatio\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
75\tRodentia\tMicrotus_pyrenaicus\tCampagnol_des_Pyrenees\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
76\tRodentia\tMicrotus_savii\tCampagnol_de_Savi\tLc\t?\tLc\tmammifere\tmammifere_terrestre
77\tRodentia\tMicrotus_subterraneus\tCampagnol_souterrain\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
78\tRodentia\tEliomys_quercinus\tLerot\tLc\t?\tNt\tmammifere\tmammifere_terrestre
79\tRodentia\tGlis_glis\tLoir_gris\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
80\tRodentia\tMuscardinus_avellanarius\tMuscardin\tLc\t?\tLc\tmammifere\tmammifere_terrestre
81\tRodentia\tApodemus_flavicollis\tMulot_à_collier\tLc\t?\tLc\tmammifere\tmammifere_terrestre
82\tRodentia\tApodemus_sylvaticus\tMulot_sylvestre\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
83\tRodentia\tClethrionomys_glareolus\tCampagnol_roussâtre\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
84\tRodentia\tMicromys_minutus\tRat_des_moissons\tLc\t?\tLc\tmammifere\tmammifere_terrestre
85\tRodentia\tMus_musculus\tSouris_grise\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
86\tRodentia\tMus_spretus\tSouris_d'Afrique_du_Nord\tLc\tUppera\tLc\tmammifere\tmammifere_terrestre
87\tRodentia\tRattus_rattus\tRat_noir\tLc\tDowna\tLc\tmammifere\tmammifere_terrestre
88\tRodentia\tMarmota_marmota\tMarmotte_des_Alpes\tLc\tUppera\tLc\tmammifere\tmammifere_terrestre
89\tRodentia\tSciurus_vulgaris\tEcureuil_roux\tLc\t?\tLc\tmammifere\tmammifere_terrestre
90\tSoricomorpha\tCrocidura_russula\tCrocidure_musette\tLc\tUppera\tLc\tmammifere\tmammifere_terrestre
91\tSoricomorpha\tNeomys_anomalus\tCrossope_de_Miller\tLc\t?\tLc\tmammifere\tmammifere_terrestre
92\tSoricomorpha\tNeomys_fodiens\tCrossope_aquatique\tLc\tDowna\tLc\tmammifere\tmammifere_terrestre
93\tSoricomorpha\tSorex_coronatus\tMusaraigne_couronnee\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
94\tSoricomorpha\tSorex_minutus\tMusaraigne_pygmee\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
95\tSoricomorpha\tSuncus_etruscus\tPachyure_etrusque\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
96\tSoricomorpha\tTalpa_aquitania\tTaupe_d'Aquitaine\tLc\tStilla\tNe\tmammifere\tmammifere_terrestre
97\tSoricomorpha\tTalpa_europaea\tTaupe_d'Europe\tLc\tStilla\tLc\tmammifere\tmammifere_terrestre
98\tChiroptera\tEptesicus_nilssonii\tSerotine_de_Nilsson\tDd\t?\tLc\tmammifere\tmammifere_terrestre
99\tChiroptera\tVespertilio_murinus\tVespertilion_bicolore\tDd\t?\tLc\tmammifere\tmammifere_terrestre
100\tRodentia\tApodemus_alpicola\tMulot_alpestre\tDd\t?\tLc\tmammifere\tmammifere_terrestre
101\tSoricomorpha\tSorex_alpinus\tMusaraigne_alpine\tDd\t?\tNt\tmammifere\tmammifere_terrestre
102\tSoricomorpha\tSorex_antinorii\tMusaraigne_du_Valais\tDd\t?\tDd\tmammifere\tmammifere_terrestre
103\tSoricomorpha\tSorex_araneus\tMusaraigne_carrelet\tDd\t?\tLc\tmammifere\tmammifere_terrestre
"""

df = pd.read_csv(StringIO(data), sep='\t')

json_data = df.to_json(orient='records', indent=2)
json_data = json_data.replace('\u00e9', 'e')

output_file = 'resultat.json'

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(json_data)
