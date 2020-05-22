# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


#takes in damage list and returns the list as floats
def updated_damages(damages):
    decimal_damage = []
    for damage in damages:
        if damage == 'Damages not recorded':
            decimal_damage.append('Damages not recorded')
        #if m or b is in the string, remove it
        #convert the remaining string into a float number
        #then multiply by million or billion respectively
        if 'M' in damage:
            decimal_damage.append(float(damage[:-1]) * 1000000)
        if 'B' in damage:
            decimal_damage.append(float(damage[:-1]) * 1000000000)
    return decimal_damage

fixed_damages = updated_damages(damages)


# function takes in all data lists above and creates a dictionary
# of each hurricane where the keys are the hurricane names
def hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {
            'Name' : names[i],
            'Month' : months[i],
            'Year' : years[i],
            'Max Sustained Wind': max_sustained_winds[i],
            'Areas Affected' : areas_affected[i],
            'Damage': fixed_damages[i],
            'Deaths': deaths[i]
        }
    return hurricanes

hurricanes = hurricane_dict(names, months, years, max_sustained_winds, areas_affected, fixed_damages, deaths)


# function iterates through a dictionary
# setting the current year to the keys of the new dict by_year
# and setting the current hurricane to the values of each year 
# returns by_year dictionary
def hurr_by_year(hurricane_dictionary):
    by_year = {}
    for hurricane in hurricane_dictionary:
        current_year = hurricane_dictionary[hurricane]['Year']
        current_hurr = hurricane_dictionary[hurricane]
        if current_year in by_year:
            by_year[current_year].append(current_hurr)
        else:
            by_year[current_year] = [current_hurr]
    return by_year

hurricanes_by_year = hurr_by_year(hurricanes)



# function takes in a dictionary, creates a locations dictionary
# whose keys are the places in areas_affected and values are
# number of times they come up in the dictionary
# iterate over dictionary -> iterate over key 'areas affected' -> create keys of locations and add values based upon frequency
def area_freq(hurricane_dictionary):
    locations ={}
    for hurricane in hurricane_dictionary:
        for areas in hurricane_dictionary[hurricane]['Areas Affected']:
            if areas in locations:
                locations[areas] += 1
            else:
                locations[areas] = 1
    return locations

area_hits = area_freq(hurricanes)           

# import operator to take advantage of python 3.6 dictionary sorting
# sort dictionary based on item values
#currently outputs in least vulnerable to most vulnerable
import operator
def vulnerability(locations_dictionary):
    vulnerable_places = sorted(locations_dictionary.items(), key=operator.itemgetter(1))
    return vulnerable_places
most_hit = vulnerability(area_hits)


# funtion iterates through dictionary and compares deaths
# compares the value of deaths on each hurricane in dictionary
# returns the most fatal hurricane as a name: deaths k,v

# this function was replaced by the greatest_measure function
# but to keep my thought process I am leaving this in for now 
def fatalities(hurricane_dictionary):
    most_deaths = 0
    for hurricane in hurricane_dictionary:
        hurricane_deaths = hurricane_dictionary[hurricane]['Deaths']
        if hurricane_deaths >= most_deaths:
            most_deaths = hurricane_deaths
            most_deadly = hurricane_dictionary[hurricane]['Name']
    most_fatal = {most_deadly: most_deaths}    
    return most_fatal

most_fatal_hurricane = fatalities(hurricanes)


# write your catgeorize by mortality function here:
def mortality_scale(hurricane_dictionary):
    mortality = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for hurricane in hurricane_dictionary:
        if hurricane_dictionary[hurricane]['Deaths'] <= 0:
            mortality[0].append(hurricane_dictionary[hurricane])
        elif hurricane_dictionary[hurricane]['Deaths'] > 0 and hurricane_dictionary[hurricane]['Deaths'] <=100:
            mortality[1].append(hurricane_dictionary[hurricane])
        elif hurricane_dictionary[hurricane]['Deaths'] > 100 and hurricane_dictionary[hurricane]['Deaths'] <=500:
            mortality[2].append(hurricane_dictionary[hurricane])
        elif hurricane_dictionary[hurricane]['Deaths'] > 500 and hurricane_dictionary[hurricane]['Deaths'] <=1000:
            mortality[3].append(hurricane_dictionary[hurricane])
        elif hurricane_dictionary[hurricane]['Deaths'] > 1000 and hurricane_dictionary[hurricane]['Deaths'] <=10000:
            mortality[4].append(hurricane_dictionary[hurricane])
        elif hurricane_dictionary[hurricane]['Deaths'] > 10000:
            mortality[5].append(hurricane_dictionary[hurricane])
        else:
            print('Something in the dictionary went wrong')
    return mortality

hurricane_mortality_scale = mortality_scale(hurricanes)


# This function will overwrite the deaths function
# passing the hurricane dictionary with whatever measure a user wants
# will output the hurricane with the greatest whatever
# in order to preserve the dictionary being the only argument, a user prompt
#can be inserted into the function and ask what they are trying to get the greatest measure of
def greatest_measure(hurricane_dictionary,measure):
    count = 0.0
    for hurricane in hurricane_dictionary:
        if isinstance(hurricane_dictionary[hurricane][measure], str):
            pass 
        else:
            hurricane_measure = hurricane_dictionary[hurricane][measure]
            if hurricane_measure >= count:
                count = hurricane_measure
                name = hurricane_dictionary[hurricane]['Name']
            most = {name: count}    
    return most
big_damage = greatest_measure(hurricanes, 'Damage')
print(big_damage)
most_dead = greatest_measure(hurricanes, 'Deaths')
print(most_dead)

# This function can be combined with the other scale function provided
# that string types were handled, and all keys were changed to a var argument
# such as measure in the greatest_measure function.  As of right now, I don't think
# this would save on lines of code or functionality in the same way. 
# otherwise this function works the same as the mortality_scale function.
def damage_scale(hurricane_dictionary):
    d_scale = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for hurricane in hurricane_dictionary:
        if isinstance(hurricane_dictionary[hurricane]['Damage'], str):
            d_scale[0].append(hurricane_dictionary[hurricane])
        elif hurricane_dictionary[hurricane]['Damage'] <= 0:
            d_scale[0].append(hurricane_dictionary[hurricane])
        elif hurricane_dictionary[hurricane]['Damage'] > 0              and hurricane_dictionary[hurricane]['Damage'] <= 100000000:
            d_scale[1].append(hurricane_dictionary[hurricane])
        elif hurricane_dictionary[hurricane]['Damage'] > 100000000      and hurricane_dictionary[hurricane]['Damage'] <= 1000000000:
            d_scale[2].append(hurricane_dictionary[hurricane])
        elif hurricane_dictionary[hurricane]['Damage'] > 1000000000     and hurricane_dictionary[hurricane]['Damage'] <= 10000000000:
            d_scale[3].append(hurricane_dictionary[hurricane])
        elif hurricane_dictionary[hurricane]['Damage'] > 10000000000    and hurricane_dictionary[hurricane]['Damage'] <= 50000000000:
            d_scale[4].append(hurricane_dictionary[hurricane])
        elif hurricane_dictionary[hurricane]['Damage'] > 50000000000:
            d_scale[5].append(hurricane_dictionary[hurricane])
        else:
            print('Something in the dictionary went wrong')
    return d_scale

hurricane_damage_scale = damage_scale(hurricanes)
print(hurricane_damage_scale)