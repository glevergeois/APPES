import pandas as pd
from io import StringIO

data = """
Index\tOrdre\tNom scientifique\tNom commun\tCategorie Liste rouge France\tTendance\tCategorie Liste rouge mondiale\tStatut d'endemisme*
1\tSalmoniformes\tCoregonus_bezola\tBezoule\tEx\t?\tEx\tX
2\tSalmoniformes\tCoregonus_fera\tCoregone_fera\tEx\t?\tEx
3\tSalmoniformes\tCoregonus_hiemalis\tCoregone_gravenche\tEx\t?\tEx
4\tAcipenseriformes\tAcipenser_oxyrinchus\tEsturgeon_noir\tRe\t?\tNt
5\tCyprinodontiformes\tAphanius_iberus\tAphanius_d'Espagne\tRe\t?\tEn
6\tCyprinodontiformes\tValencia_hispanica\tCyprinodonte_de_Valence\tRe\t?\tCr
7\tAcipenseriformes\tAcipenser_sturio\tEsturgeon_europeen\tCr\t?\tCr
8\tClupeiformes\tAlosa_alosa\tGrande_alose\tCr\t?\tLc
9\tAnguilliformes\tAnguilla_anguilla\tAnguille_europeenne\tCr\tDowna\tCr
10\tScorpaeniformes\tCottus_petiti\tChabot_du_Lez\tCr\tDowna\tVu\tX
11\tCypriniformes\tBarbatula_leoparda\tLoche_leopard\tEn\t?\tNe\tX
12\tCypriniformes\tMisgurnus_fossilis\tLoche_d'etang\tEn\t?\tLc
13\tPetromyzontiformes\tPetromyzon_marinus\tLamproie_marine\tEn\tDowna\tLc
14\tSalmoniformes\tSalvelinus_alpinus\tOmble_chevalier\tEn\tDowna\tLc
15\tCypriniformes\tSqualius_laietanus\tChevesne_catalan\tEn\tDowna\tLc
16\tPerciformes\tZingel_asper\tApron_du_Rhône\tEn\t?\tCr
17\tEsociformes\tEsox_aquitanicus\tBrochet_aquitain\tVu\t?\tNe\tX
18\tEsociformes\tEsox_lucius\tBrochet_commun\tVu\tDowna\tLc
19\tPetromyzontiformes\tLampetra_fluviatilis\tLamproie_de_rivière\tVu\tDowna\tLc
20\tGadiformes\tLota_lota\tLote_de_rivière\tVu\tDowna\tLc
21\tSalmoniformes\tThymallus_thymallus\tOmbre_commun\tVu\tDowna\tLc
22\tClupeiformes\tAlosa_agone\tAlose_feinte_mediterraneenne\tNt\tStilla\tLc
23\tClupeiformes\tAlosa_fallax\tAlose_feinte_atlantique\tNt\tDowna\tLc
24\tCyprinodontiformes\tAphanius_fasciatus\tAphanius_de_Corse\tNt\t?\tLc
25\tCypriniformes\tBarbus_meridionalis\tBarbeau_meridional\tNt\t?\tNt
26\tCypriniformes\tCobitis_taenia\tLoche_epineuse\tNt\t?\tLc
27\tScorpaeniformes\tCottus_aturi\tChabot_du_Bearn\tNt\t?\tLc
28\tScorpaeniformes\tCottus_hispaniolensis\tChabot_des_Pyrenees\tNt\t?\tLc
29\tScorpaeniformes\tCottus_rhenanus\tChabot_de_Rhenanie\tNt\t?\tLc
30\tCypriniformes\tGobio_lozanoi\tGoujon_de_l'Adour\tNt\t?\tLc
31\tCypriniformes\tLeuciscus_bearnensis\tVandoise_du_Bearn\tNt\tDowna\tLc\tX
32\tCypriniformes\tLeuciscus_burdigalensis\tVandoise_rostree\tNt\tDowna\tLc\tX
33\tOsmeriformes\tOsmerus_eperlanus\tEperlan_europeen\tNt\t?\tLc
34\tCypriniformes\tParachondrostoma_toxostoma\tToxostome\tNt\tDowna\tVu
35\tCypriniformes\tPhoxinus_bigerri\tVairon_basque\tNt\t?\tLc
36\tGasterosteiformes\tPungitius_vulgaris\tEpinochette_du_Poitou\tNt\t?\tNe\tX
37\tSalmoniformes\tSalmo_salar\tSaumon_atlantique\tNt\tDowna\tLc
38\tCypriniformes\tAbramis_brama\tBrème_commune\tLc\tDowna\tLc
39\tCypriniformes\tAlburnoides_bipunctatus\tSpirlin\tLc\tUppera\tNe
40\tCypriniformes\tAlburnus_alburnus\tAblette\tLc\tDowna\tLc
41\tAtheriniformes\tAtherina_boyeri\tAtherine\tLc\tStilla\tLc
42\tCypriniformes\tBarbatula_barbatula\tLoche_franche\tLc\tStilla\tLc
43\tCypriniformes\tBarbatula_quignardi\tLoche_du_Languedoc\tLc\tStilla\tLc
44\tCypriniformes\tBarbus_barbus\tBarbeau_fluviatile\tLc\tStilla\tLc
45\tCypriniformes\tBlicca_bjoerkna\tBrème_bordelière\tLc\tDowna\tLc
46\tMugiliformes\tChelon_ramada\tMulet_porc\tLc\tUppera\tLc
47\tCypriniformes\tChondrostoma_nasus_hotu\tLc\tDowna\tLc
48\tScorpaeniformes\tCottus_gobio\tChabot_commun\tLc\t?\tLc
49\tScorpaeniformes\tCottus_perifretum\tChabot_fluviatile\tLc\tUppera\tLc
50\tCypriniformes\tCyprinus_carpio\tCarpe_commune\tLc\t?\tVu
51\tGasterosteiformes\tGasterosteus_aculeatus\tEpinoche\tLc\tDowna\tLc
52\tCypriniformes\tGobio_gobio\tGoujon_commun\tLc\tStilla\tLc
"""

df = pd.read_csv(StringIO(data), sep='\t')

json_data = df.to_json(orient='records', indent=2)
json_data = json_data.replace('\u00e9', 'e')

output_file = 'resultat.json'

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(json_data)
