import os
import pandas as pd

def download_data():
    '''
    This function downloads a .csv file from the "kaggle" web page of your choice, 
    unzips it and moves it to the data folder of the current project directory. 
    It also deletes the .zip file.
    '''
    #Gets the name of the dataset.zip
    url = input(f"Write the URL from dataset you wanto to download: ")
    
    #Parameterizes the user and the file
    csv_file = url.split("/")[-1]
    user = url.split("/")[-2]
    
    #Download, decompress and leaves only the csv
    download = f"kaggle datasets download -d {user}/{csv_file}"
    print("Download file")
    descompress_zip = f"unzip {csv_file}.zip"
    print("Descompressing files")
    remove_zip = f"rm -rf {csv_file}.zip"
    print ("removing .zip")

    for i in [download, descompress_zip, remove_zip]:
        os.system(i)
    
    #Moves the .csv file to data folder.
    move_csv = f"mv {csv_file}.csv data/{csv_file}.csv"
    os.system(move_csv)
    print ("Moving file to data")
    return f"Your file: {csv_file}.csv is in data folder. Enjoy!!"

    
def clean_pokemon_csv_dataframe():
    '''
    Important! This function only works with the previously downloaded dataframe, named "pokemon.csv". 
    This file can be obtained at the following url: "https://www.kaggle.com/abcsds/pokemon", 
    in kaggle. It can be downloaded with the "download_data" function.
    
    Load this file from the "data" folder with the name "pokemon.csv".
    Cleans the "mega" pokemon, cleans the "legendary" pokemon, 
    deletes the "total" and "legendary" columns. Finally, sets as index the number of the pokemon.
    '''
    
    #Loads the DataFrame, to works with it.
    pokemon = pd.read_csv("data/pokemon.csv")
    
    #Identifies the "Mega" pokemon in the "Name" column.
    def identify_megas(x):
        mega = x.split(" ")[0]
        if mega.endswith("Mega"):
           return "Mega"
        else:
          return x
    #Applies the function "identify_megas" to "Name" column. And then, drops the "mega" rows.
    pokemon["Name"] = pokemon["Name"].apply(identify_megas)
    pokemon = pokemon.drop(pokemon[pokemon["Name"] == "Mega"].index)

    #Drops the rows of legendary pokemon. And, then, removes the "Legendary" and "Total" columns
    pokemon = pokemon.drop(pokemon[pokemon["Legendary"] == True].index)
    pokemon = pokemon.drop(pokemon[["Total", "Legendary"]], axis=1)
    
    #Sets the real number of the pokemon at index.
    pokemon = pokemon.set_index("#")

    #Returns the clean DataFrame
    return pokemon



