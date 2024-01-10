import pandas as pd
from io import StringIO

data = """
Index\tOrdre\tNom scientifique\tNom commun\tCategorie Liste rouge France\tTendance\tCategorie Liste rouge mondiale\tCategorie\tSous-Categorie\tStatut d'endemisme*

"""

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
