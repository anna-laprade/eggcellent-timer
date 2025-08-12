import math 

# calculates boiling point at given altitude in feet/Fahrenheit
def altitude_to_boiling_point_F(alt_in_feet: float):
    boilingInF = 212 - (alt_in_feet / 500)
    
    return boilingInF


# calculates boiling point at given altitude in meters/Celcius 
def altitude_to_boiling_point_C(alt_in_meters: float):
    boilingInF = 100 - (alt_in_meters / 285)
    
    return boilingInF


# calculates time to boil the Perfect Egg in Fahrenheit 
def adjusted_egg_time_F(boiling_point_f, base_time_sec, k=0.018):
    return round(base_time_sec * math.exp(k * (212 - boiling_point_f)))


# calculates time to boil the Perfect Egg in Celcius 
def adjusted_egg_time_C(boiling_point_celsius, base_time_sec, k=0.05):
    return round(base_time_sec * math.exp(k * (100 - boiling_point_celsius)))


