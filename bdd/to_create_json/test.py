contenu_complet = """Salmoniformes Coregonus bezola Bezoule X EX ? EX
Salmoniformes Coregonus fera Corégone fera EX ? EX
Salmoniformes Coregonus hiemalis Corégone gravenche EX ? EX
Acipenseriformes Acipenser oxyrinchus Esturgeon noir RE ? NT
Cyprinodontiformes Aphanius iberus Aphanius d'Espagne RE ? EN
Cyprinodontiformes Valencia hispanica Cyprinodonte de Valence RE ? CR
Acipenseriformes Acipenser sturio Esturgeon européen CR ? CR
Clupeiformes Alosa alosa Grande alose CR ? LC
Anguilliformes Anguilla anguilla Anguille européenne CR  CR
Scorpaeniformes Cottus petiti Chabot du Lez X CR  VU
Cypriniformes Barbatula leoparda Loche léopard X EN ? NE
Cypriniformes Misgurnus fossilis Loche d'étang EN ? LC
Petromyzontiformes Petromyzon marinus Lamproie marine EN  LC
Salmoniformes Salvelinus alpinus Omble chevalier EN  LC
Cypriniformes Squalius laietanus Chevesne catalan EN  LC
Perciformes Zingel asper Apron du Rhône EN ? CR
Esociformes Esox aquitanicus Brochet aquitain X VU ? NE
Esociformes Esox lucius Brochet commun VU  LC
Petromyzontiformes Lampetra fluviatilis Lamproie de rivière VU  LC
Gadiformes Lota lota Lote de rivière VU  LC
Salmoniformes Thymallus thymallus Ombre commun VU  LC
Clupeiformes Alosa agone Alose feinte méditerranéenne NT  LC
Clupeiformes Alosa fallax Alose feinte atlantique NT  LC
Cyprinodontiformes Aphanius fasciatus Aphanius de Corse NT ? LC
Cypriniformes Barbus meridionalis Barbeau méridional NT ? NT
Cypriniformes Cobitis taenia Loche épineuse NT ? LC
Scorpaeniformes Cottus aturi Chabot du Béarn NT ? LC
Scorpaeniformes Cottus hispaniolensis Chabot des Pyrénées NT ? LC
Scorpaeniformes Cottus rhenanus Chabot de Rhénanie NT ? LC
Cypriniformes Gobio lozanoi Goujon de l'Adour NT ? LC
Cypriniformes Leuciscus bearnensis Vandoise du Béarn X NT  LC
Cypriniformes Leuciscus burdigalensis Vandoise rostrée X NT  LC
Osmeriformes Osmerus eperlanus Eperlan européen NT ? LC
Cypriniformes Parachondrostoma toxostoma Toxostome NT  VU
Cypriniformes Phoxinus bigerri Vairon basque NT ? LC
Gasterosteiformes Pungitius vulgaris Epinochette du Poitou X NT ? NE
Salmoniformes Salmo salar Saumon atlantique NT  LC
Cypriniformes Abramis brama Brème commune LC  LC
Cypriniformes Alburnoides bipunctatus Spirlin LC  NE
Cypriniformes Alburnus alburnus Ablette LC  LC
Atheriniformes Atherina boyeri Athérine LC  LC
Cypriniformes Barbatula barbatula Loche franche LC  LC
Cypriniformes Barbatula quignardi Loche du Languedoc LC  LC
Cypriniformes Barbus barbus Barbeau fluviatile LC  LC
Cypriniformes Blicca bjoerkna Brème bordelière LC  LC
Mugiliformes Chelon ramada Mulet porc LC  LC
Cypriniformes Chondrostoma nasus hotu LC  LC
Scorpaeniformes Cottus gobio Chabot commun LC ? LC
Scorpaeniformes Cottus perifretum Chabot fluviatile LC  LC
Cypriniformes Cyprinus carpio Carpe commune LC ? VU
Gasterosteiformes Gasterosteus aculeatus Epinoche LC  LC
Cypriniformes Gobio gobio Goujon commun LC  LC"""
contenu_complet = contenu_complet.replace('é', 'e').replace('\u00c3\u00a9', 'e').replace('EX', 'Ex').replace('RE', 'Re').replace('CR', 'Cr').replace('EN', 'En').replace('VU', 'Vu').replace('NT', 'Nt').replace('LC', 'Lc').replace('DD', 'Dd').replace('NA', 'Na').replace('NE', 'Ne').replace('', 'Downa').replace('', 'Uppera').replace('', 'Stilla')
print(contenu_complet)

def add_X(texte):
    lignes = texte.split('\n')  # Divise le texte en lignes

    for index, ligne in enumerate(lignes, start=1):
        mots = ligne.split()
        nouveaux_mots = [str(index)]
        count = 0

        for mot in mots:
            if mot.lower() == 'de':
                nouveaux_mots.append('_de_')
                count += 1
            elif mot.lower() == 'du':
                nouveaux_mots.append('_du_')
                count += 1
            elif mot.lower() == 'des':
                nouveaux_mots.append('_des_')
                count += 1
            elif (not mot[0].isupper() and not nouveaux_mots[-1][-1].isupper() and 
                not mot.endswith('?') and not mot.startswith("'")):
                nouveaux_mots[-1] += '_' + mot
            elif (mot[0].isupper() and nouveaux_mots[-1].endswith('_')):
                nouveaux_mots[-1] += mot
            else:
                nouveaux_mots.append("\\t" + mot)

        print(nouveaux_mots)
        if len(nouveaux_mots) >= 1:
            if nouveaux_mots[(4 + int(count))] == '\\tX':
                nouveaux_mots.pop(4 +int(count))
                nouveaux_mots.append('\\tX')

        lignes[index-1] = ' '.join(nouveaux_mots)
        
    resultat = '\n'.join(lignes)
    resultat = resultat.replace('__', '_').replace(' ', '')

    return resultat

added_x = add_X(contenu_complet)
output_file = 'test.txt'


with open(output_file, 'w', encoding='utf-8') as file:
    file.write(added_x)
