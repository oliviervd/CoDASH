from components.sync import *
import pandas as pd
from components.utils import sql_to_json
import sqlite3

# generate clean dataframe containing objects from LDES
all = sql_to_json()


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
    cnt_stam_prov = df_stam['MaterieelDing.isOvergedragenBijVerwerving'].count()

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
    cnt_dmg_prov = df_dmg['MaterieelDing.isOvergedragenBijVerwerving'].count()

    cnt_all = pd.DataFrame({"STAM": [cnt_stam_title, cnt_stam_id, cnt_stam_beschrijving,
                                     cnt_stam_objectnaam, cnt_stam_materiaal, cnt_stam_dimension,
                                     cnt_stam_collection, cnt_stam_creator, cnt_stam_location,
                                     cnt_stam_exhibition, cnt_stam_producer, cnt_stam_prov],
                            "DMG": [cnt_dmg_title, cnt_dmg_id, cnt_dmg_beschrijving,
                                    cnt_dmg_objectnaam, cnt_dmg_materiaal, cnt_dmg_dimension,
                                    cnt_dmg_collection, cnt_dmg_creator, cnt_dmg_location,
                                    cnt_dmg_exhibition, cnt_dmg_producer, cnt_dmg_prov]},
                           index=["title", "id", "description", "object type", "material", "dimension(s)",
                                  "part of (collection)", "creator", "location", "exhibition history",
                                  "production information (producer)", "provenance"])

    cnt_all["STAM_P"] = (cnt_all["STAM"] / count_list[0][0]) * 100
    cnt_all["DMG_P"] = (cnt_all["DMG"] / count_list[1][0]) * 100
    return cnt_all


def fetch_count_history():
    connection = sqlite3.connect("data/tracker.db")
    df_cnt_hist = pd.read_sql_query("SELECT * from totalcount", connection)
    df_cnt_hist["date"] = pd.to_datetime(df_cnt_hist["date"], yearfirst=True)
    df_cnt_hist = df_cnt_hist.set_index("date")
    df_cnt_hist.sort_index(ascending=True, inplace=True)
    df_cnt_hist["totalcount"] = df_cnt_hist["totalcount"].astype(str).astype(int)

    return df_cnt_hist


def fetch_prov_info():
    prov_id, prov_method, prov_inst, prov_ds, prov_de = [], [], [], [], []
    for i in range(0, len(all)):
        prov_ds.append(all[i]['MaterieelDing.isOvergedragenBijVerwerving']["Gebeurtenis.tijd"]["Periode.begin"])
        prov_de.append(all[i]['MaterieelDing.isOvergedragenBijVerwerving']["Gebeurtenis.tijd"]["Periode.einde"])
        prov_method.append(all[i]['MaterieelDing.isOvergedragenBijVerwerving']["Activiteit.gebruikteTechniek"])
        prov_id.append(all[i]['Object.identificator']['Identificator.identificator'])
        prov_inst.append(all[i]['MaterieelDing.beheerder'])

    df_prov = pd.DataFrame()
    df_prov["id"] = prov_id
    df_prov["method"] = prov_method
    df_prov["start"] = prov_ds
    df_prov["end"] = prov_de
    df_prov["inst"] = prov_inst

    return df_prov

def fetch_creation_info():
    pass


def fetch_material_info():
    pass