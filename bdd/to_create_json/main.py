import pandas as pd
from io import StringIO

data = """Index\tOrdre\tNom scientifique\tNom commun\tCategorie Liste rouge France\tTendance\tCategorie Liste rouge mondiale\tCategorie\tSous-Categorie\tStatut d'endemisme*
2231\tSquatinidae\tSquatina_squatina\tAnge_de_mer_commun\tCr\t?\tCr\trequins\tNULL\tNULL
2232\tCentrophoridae\tCentrophorus_granulosus\tRequin-chagrin\tEn\t?\tVu\trequins\tNULL\tNULL
2233\tCentrophoridae\tCentrophorus_squamosus\tSquale-chagrin_de_l'Atlantique\tEn\t?\tVu\trequins\tNULL\tNULL
2234\tLamnidae\tLamna_nasus\tRequin-taupe_commun\tEn\t?\tVu\trequins\tNULL\tNULL
2235\tSqualidae\tSqualus_acanthias\tAiguillat_commun\tEn\t?\tVu\trequins\tNULL\tNULL
2236\tCetorhinidae\tCetorhinus_maximus\tRequin-pelerin\tVu\t?\tVu\trequins\tNULL\tNULL
2237\tCarcharhinidae\tPrionace_glauca\tRequin_peau_bleue\tNt\tStilla\tNt\trequins\tNULL\tNULL
2238\tEtmopteridae\tCentroscyllium_fabricii\tAiguillat_noire\tNt\t?\tLc\trequins\tNULL\tNULL
2239\tScyliorhinidae\tGaleus_melastomus\tChien_espagnol\tLc\tStilla\tLc\trequins\tNULL\tNULL
2240\tScyliorhinidae\tScyliorhinus_canicula\tPetite_roussette\tLc\tStilla\tLc\trequins\tNULL\tNULL
2241\tScyliorhinidae\tScyliorhinus_stellaris\tGrande_roussette\tLc\tStilla\tNt\trequins\tNULL\tNULL
2242\tAlopiidae\tAlopias_vulpinus\tRequin-renard_commun\tDd\t?\tVu\trequins\tNULL\tNULL
2243\tCarcharhinidae\tCarcharhinus_brachyurus\tRequin_cuivre\tDd\t?\tNt\trequins\tNULL\tNULL
2244\tCarcharhinidae\tCarcharhinus_brevipinna\tRequin-tisserand\tDd\t?\tNt\trequins\tNULL\tNULL
2245\tCarcharhinidae\tCarcharhinus_limbatus\tRequin_borde\tDd\t?\tNt\trequins\tNULL\tNULL
2246\tCarcharhinidae\tCarcharhinus_plumbeus\tRequin_gris\tDd\t?\tVu\trequins\tNULL\tNULL
2247\tCentrophoridae\tDeania_calcea\tSquale-savate\tDd\t?\tLc\trequins\tNULL\tNULL
2248\tChlamydoselachidae\tChlamydoselachus_anguineus\tRequin-lezard\tDd\t?\tNt\trequins\tNULL\tNULL
2249\tDalatiidae\tCentroscymnus_coelolepis\tPailona_commun\tDd\t?\tNt\trequins\tNULL\tNULL
2250\tDalatiidae\tDalatias_licha\tSquale-liche\tDd\t?\tNt\trequins\tNULL\tNULL
2251\tDalatiidae\tScymnodon_ringens\tSquale-grogneur_commun\tDd\t?\tDd\trequins\tNULL\tNULL
2252\tDalatiidae\tSqualiolus_laticaudus\tSquale_nain\tDd\t?\tLc\trequins\tNULL\tNULL
2253\tEchinorhinidae\tEchinorhinus_brucus\tSquale_boucle\tDd\t?\tDd\trequins\tNULL\tNULL
2254\tEtmopteridae\tEtmopterus_princeps\tSagre_rude\tDd\t?\tDd\trequins\tNULL\tNULL
2255\tEtmopteridae\tEtmopterus_spinax\tSagre_commun\tDd\t?\tLc\trequins\tNULL\tNULL
2256\tHexanchidae\tHeptranchias_perlo\tPerlon\tDd\t?\tNt\trequins\tNULL\tNULL
2257\tHexanchidae\tHexanchus_griseus\tGriset\tDd\t?\tNt\trequins\tNULL\tNULL
2258\tLamnidae\tCarcharodon_carcharias\tGrand_requin_blanc\tDd\t?\tVu\trequins\tNULL\tNULL
2259\tMitsukurinidae\tMitsukurina_owstoni\tRequin-lutin\tDd\t?\tLc\trequins\tNULL\tNULL
2260\tOdontaspididae\tCarcharias_taurus\tRequin-taureau\tDd\t?\tVu\trequins\tNULL\tNULL
2261\tOdontaspididae\tOdontaspis_ferox\tRequin-feroce\tDd\t?\tVu\trequins\tNULL\tNULL
2262\tOxynotidae\tOxynotus_centrina\tCentrine_commune\tDd\t?\tVu\trequins\tNULL\tNULL
2263\tOxynotidae\tOxynotus_paradoxus\tHumantin\tDd\t?\tDd\trequins\tNULL\tNULL
2264\tPseudotriakidae\tPseudotriakis_microdon\tRequin_à_longue_dorsale\tDd\t?\tDd\trequins\tNULL\tNULL
2265\tScyliorhinidae\tApristurus_melanoasper\tHolbiche_noire\tDd\t?\tDd\trequins\tNULL\tNULL
2266\tSomniosidae\tCentroselachus_crepidater\tPailona_à_long_nez\tDd\t?\tLc\trequins\tNULL\tNULL
2267\tSomniosidae\tSomniosus_microcephalus\tLaimargue_du_Groenland\tDd\t?\tNt\trequins\tNULL\tNULL
2268\tSomniosidae\tSomniosus_rostratus\tLaimargue_de_Mediterranee\tDd\t?\tDd\trequins\tNULL\tNULL
2269\tSomniosidae\tZameus_squamulosus\tSquale-grogneur_veloute\tDd\t?\tDd\trequins\tNULL\tNULL
2270\tSphyrnidae\tSphyrna_lewini\tRequin-marteau_halicorne\tDd\t?\tEn\trequins\tNULL\tNULL
2271\tSphyrnidae\tSphyrna_mokarran\tGrand_requin-marteau\tDd\t?\tEn\trequins\tNULL\tNULL
2272\tSphyrnidae\tSphyrna_zygaena\tRequin-marteau_commun\tDd\t?\tVu\trequins\tNULL\tNULL
2273\tSqualidae\tSqualus_blainville\tAiguillat-coq\tDd\t?\tDd\trequins\tNULL\tNULL
2274\tSqualidae\tSqualus_uyato\tPetit_squale-chagrin\tDd\t?\tDd\trequins\tNULL\tNULL
2275\tSquatinidae\tSquatina_aculeata\tAnge_de_mer_epineux\tDd\t?\tCr\trequins\tNULL\tNULL
2276\tSquatinidae\tSquatina_oculata\tAnge_de_mer_ocelle\tDd\t?\tCr\trequins\tNULL\tNULL
2277\tTriakidae\tGaleorhinus_galeus\tRequin_hâ\tDd\t?\tVu\trequins\tNULL\tNULL
2278\tTriakidae\tMustelus_asterias\tÉmissole_tachetee\tDd\t?\tLc\trequins\tNULL\tNULL
2279\tTriakidae\tMustelus_mustelus\tÉmissole_lisse\tDd\t?\tVu\trequins\tNULL\tNULL
2280\tTriakidae\tMustelus_punctulatus\tÉmissole_pointillee\tDd\t?\tDd\trequins\tNULL\tNULL"""

lines = data.split('\n')

for index, line in enumerate(lines):
    tab_count = line.count('\t')
    if tab_count != 9:
        print(f"Index {index + 4}: {tab_count} occurrences de '\\t'")

df = pd.read_csv(StringIO(data), sep='\t')

json_data = df.to_json(orient='records', indent=2)
json_data = json_data.replace('\u00e9', 'e')

output_file = 'resultat.json'

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(json_data)
