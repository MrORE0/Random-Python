def calcWindChillIndex ():
    air_temp = float(input("Please put the air temperature here: "))
    wind_speed = float(input("Please put the wind speed here: "))
    wind_chill_index = round(13.12 + (0.6215 * air_temp) - (11.37 * (wind_speed**0.16)) + (0.3965 * air_temp * (wind_speed**0.16)))
    return wind_chill_index

