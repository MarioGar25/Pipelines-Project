import requests

def get_evol_trigger(url): 
    '''
    calls an API about the previously loaded API and puts all pokemon in a list.

    '''
    #call API
    file_list = requests.get(url).json()
    
    #get the pokemon species
    ev = file_list.get("pokemon_species")

    #return list with pokemon
    return [l.get("name") for l in ev]

def compare_and_add_to_DataFrame(level_up, trade, item, shed, others, data):
    '''
    Enters the lists obtained in the previous function, and a DataFrame
    compares the list of evolutionary methods with a 
    column of the dataframe, if it matches, 
    it returns the name of the evolutionary method.
    '''

    if data.lower() in level_up:
        return "Level_up"
    elif data.lower() in trade:
        return "Trade"
    elif data.lower() in item:
        return "Item"
    elif data.lower() in shed:
        return "Shed"
    elif data.lower() in others:
        return "Others"
    else: 
        return "Base"

def get_game(url):

    '''
    calls an API and gets the games of Pokemon.
    
    '''
    #call API
    game_list = requests.get(url).json()

    ##gets the value of version groups
    version_game = game_list.get("version_groups")

    #returns list of list with all games for each generetion
    return [game.get("name") for game in version_game]

def take_region(url):

    '''
    introduces an url from API(regions) and returns a list with the regions of Pokemon
    '''

    all_regions = []

    #calls the API
    region = requests.get(url).json()
    #gets the value of results
    regions = region.get("results")
    
    #adds the values to a list
    for r in regions:
        total_regions = r.get("name")
        all_regions.append(total_regions)

    #returns       
    return all_regions

def get_region(data, regions):

    '''
    compare region with generation
    
    '''
    if data == 1:
        return regions[0]
    elif data == 2:
        return regions[1]
    elif data == 3:
        return regions[2]
    elif data == 4: 
        return regions[3]
    elif data == 5:
        return regions[4]
    elif data ==6:
        return regions[5]
