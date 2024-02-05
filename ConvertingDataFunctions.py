#Define ST as venue 0 and HV as 1
def convert_venue(venue):
    if venue == "ST":
        return 0
    return 1

#Config becomes number from 0 to 5
def convert_config(config):
    configs = ['A','A+3','B','B+2','C','C+3']
    return configs.index(config)

#Going becomes number from 0 to 9
def convert_going(going):
    goings = ['GOOD TO FIRM','GOOD','GOOD TO YIELDING','WET SLOW',
             'FAST','YIELDING','YIELDING TO SOFT','SOFT','WET FAST','SLOW']
    return goings.index(going)

#Country becomes number from 0 to 15
def convert_country(country):
    countries = ['AUS','NZ','SAF','GB','USA','IRE','FR',
                 'CAN','ARG','GER','ZIM','JPN','BRZ','GR','ITY','SPA']
    return countries.index(country)

#Horse type becomes number from 0 to 8
def convert_horse_type(type):
    types = ['Gelding','Mare','Horse','Brown','Rig','Colt','Roan','Filly','Grey']
    return types.index(type)

#Becomes number of horse gear
def convert_horse_gear(type):
    return type.count('/')

#Prize money, 0 if null
def convert_prizes(prize):
    if prize != prize:
        return 0
    return int(prize)
