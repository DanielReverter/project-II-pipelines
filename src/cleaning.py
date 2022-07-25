import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

# This file has all the cleaning functions that are used in the project


def strip(name):
    '''
    This function takes a string and returns the same string without any spaces or linebreaks at the beginning and end
    '''
    return name.strip()

def age(birth_year):
    '''
    This function takes someones birth year and returns their current age at the end of 2022
    '''
    return 2022-birth_year

def china(df):
    '''
    This funtion changes my dataframe so that every chinese/vietnamese name is written "Name" + "Surname" instead of "Surname" + "Name
    '''
    for i in range(len(df["name"])):
        if df["federation"][i]=="China " or df["federation"][i]=="Viet Nam ":
            names_list = df["name"][i].split(" ")
            ordered_name = names_list[-1]
            for n in range(len(names_list)-1):
                ordered_name += " "
                ordered_name += names_list[n]
            df["name"][i] = ordered_name

def scrapping():
    '''
    This function scrapes the name, rapid rating and blitz rating for all the top players according to chess.com/ratings and returns this data in the form af a dataframe
    '''
    rapid = []
    blitz = []
    names = []
    for i in range(1,7):
        url = f"https://www.chess.com/ratings?page={i}"
        html = requests.get(url)
        soup = BeautifulSoup(html.content, "html.parser")
        names_temp = soup.select("a.master-players-rating-username")
        names_temp = [name.get_text().strip() for name in names_temp]
        names.extend(names_temp)
        ranks = soup.select("div.master-players-rating-player-rank")
        ranks = [int(rank.get_text().strip()) for rank in ranks]
        i = 0
        for rank in ranks:
            if i%3 == 1:
                rapid.append(rank)
            i += 1
        i=0
        for rank in ranks:
            if i%3 == 2:
                blitz.append(rank)
            i += 1
    fide = {
        "name":names,
        "rapid": rapid,
        "blitz":blitz
    }
    return pd.DataFrame(fide)

def replace_names(df):
    '''
    This function replaces some names in the priginal dataframe so they match the scrapped dataframe names
    '''
    names_dict = {"Maxime Vachier Lagrave":"Maxime Vachier-Lagrave", "Jan Krzysztof Duda":"Jan-Krzysztof Duda", \
              "Sam Shankland":"Samuel Shankland", "Santosh Gujrathi Vidit":"Vidit Santosh Gujrathi", \
              "Erigaisi Arjun":"Arjun Erigaisi", "AR Saleh Salem":"Saleh Salem", "Samuel Sevian":"Sam Sevian", \
              "Li Chao b":"Li Chao", "Jorden Van Foreest":"Jorden van Foreest", \
              "M. Amin Tabatabaei":"Mohammad Amin Tabatabaei", "Narayanan.S.L":"Narayanan Sunilduth Lyna", \
              "Gawain C Jones":"Gawain Jones", "David W L Howell":"David Howell", "Luke J McShane":"Luke McShane", \
              "Liviu Dieter Nisipeanu":"Liviu-Dieter Nisipeanu", "Aleksandr Riazantsev":"Alexander Riazantsev", \
              "Erwin L'Ami":"Erwin l'Ami", "Samvel Ter Sahakyan":"Samvel Ter-Sahakyan", \
              "Loek Van Wely":"Loek van Wely", "S.P. Sethuraman":"S P Sethuraman", \
              "Murali Karthikeyan":"Karthikeyan Murali", "Volodymyr Onyshchuk":"Vladimir Onischuk", \
              "Nigel D Short":"Nigel Short", "Chithambaram VR Aravindh":"Aravindh Chithambaram"}
    return df.replace({"name":names_dict})