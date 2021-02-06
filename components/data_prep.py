from sync import *
from components.utils import sql_to_dataframe

# generate clean dataframe containing objects from LDES
all = sql_to_dataframe()

def total_count():
    """counts all objects in the db"""
    return len(all)

# generate dataframe per institutions
df = pd.DataFrame(all)

is_stam = df["MaterieelDing.beheerder"] == "http://www.wikidata.org/entity/Q980285"
df_stam = df[is_stam]
len_stam = df[is_stam].count()
is_dmg = df["MaterieelDing.beheerder"] == "http://www.wikidata.org/entity/Q1809071"
df_dmg = df[is_dmg]
len_dmg = df[is_dmg].count()

# counter "registratie"
def counter_reg():
    cnt_stam_title = df_stam["MensgemaaktObject.titel"].count()
    cnt_stam_id = df_stam["Object.identificator"].count()
    cnt_stam_beschrijving = df_stam["Entiteit.beschrijving"].count()
    cnt_stam_objectnaam = df_stam["Entiteit.classificatie"].count()
    cnt_stam_materiaal = df_stam["MensgemaaktObject.materiaal"].count()
    cnt_stam_dimension = df_stam["MensgemaaktObject.dimensie"].count()
    cnt_stam_collection = df_stam["MensgemaaktObject.maaktDeelUitVan"].count()
    cnt_stam_creator = df_stam["MaterieelDing.productie"].count()
    cnt_stam_location = df_stam["MensgemaaktObject.locatie"].count()
    cnt_stam_exhibition = df_stam["Entiteit.maaktDeelUitVan"].count()
    cnt_stam_producer = df_stam["Entiteit.wordtNaarVerwezenDoor"].count()

    cnt_dmg_title = df_dmg["MensgemaaktObject.titel"].count()
    cnt_dmg_id = df_dmg["Object.identificator"].count()
    cnt_dmg_beschrijving = df_dmg["Entiteit.beschrijving"].count()
    cnt_dmg_objectnaam = df_dmg["Entiteit.classificatie"].count()
    cnt_dmg_materiaal = df_dmg["MensgemaaktObject.materiaal"].count()
    cnt_dmg_dimension = df_dmg["MensgemaaktObject.dimensie"].count()
    cnt_dmg_collection = df_dmg["MensgemaaktObject.maaktDeelUitVan"].count()
    cnt_dmg_creator = df_dmg["MaterieelDing.productie"].count()
    cnt_dmg_location = df_dmg["MensgemaaktObject.locatie"].count()
    cnt_dmg_exhibition = df_dmg["Entiteit.maaktDeelUitVan"].count()
    cnt_dmg_producer = df_dmg["Entiteit.wordtNaarVerwezenDoor"].count()

    cnt_all = pd.DataFrame({"STAM": [cnt_stam_title, cnt_stam_id, cnt_stam_beschrijving,
                                     cnt_stam_objectnaam, cnt_stam_materiaal, cnt_stam_dimension,
                                     cnt_stam_collection, cnt_stam_creator, cnt_stam_location,
                                     cnt_stam_exhibition, cnt_stam_producer],
                            "DMG": [cnt_dmg_title, cnt_dmg_id, cnt_dmg_beschrijving,
                                    cnt_dmg_objectnaam, cnt_dmg_materiaal, cnt_dmg_dimension,
                                    cnt_dmg_collection, cnt_dmg_creator, cnt_dmg_location,
                                    cnt_dmg_exhibition, cnt_dmg_producer]},
                           index=["title", "id", "description", "object type", "material", "dimension(s)",
                                  "part of (collection)", "creator", "location", "exhibition history",
                                  "production information (producer)"])

    cnt_all["STAM_P"] = (cnt_all["STAM"]/count_list[0][0]) * 100
    cnt_all["DMG_P"] = (cnt_all["DMG"]/count_list[1][0]) * 100
    return cnt_all


