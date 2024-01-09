import pandas as pd
from io import StringIO

data = """
Index\tOrdre\tNom scientifique\tNom commun\tCategorie Liste rouge France\tTendance\tCategorie Liste rouge mondiale\tCategorie\tSous-Categorie\tStatut d'endemisme*
714\tDecapoda\tAustropotamobius_torrentium\tÉcrevisse_des_torrents\tCr\tDd\tNULL\tcrustaces\tdecapode
715\tDecapoda\tAstacus_astacus\tÉcrevisse_à_pattes_rouges\tEn\tVu\tNULL\tcrustaces\tdecapode
716\tDecapoda\tGallocaris_inermis\tCrevette_cavernicole\tVu\tNe\tNULL\tcrustaces\tdecapode\tX
717\tDecapoda\tAustropotamobius_pallipes\tÉcrevisse_à_pattes_blanches\tVu\tEn\tNULL\tcrustaces\tdecapode
718\tDecapoda\tAtyaephyra_desmaresti\tCaridine_de_Desmarest\tLc\tNe\tNULL\tcrustaces\tdecapode
"""

df = pd.read_csv(StringIO(data), sep='\t')

json_data = df.to_json(orient='records', indent=2)
json_data = json_data.replace('\u00e9', 'e')

output_file = 'resultat.json'

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(json_data)
