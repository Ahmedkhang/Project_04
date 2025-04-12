def main():
    user_input = float(input('Enter your weight: '))
    choose_planet = input('Enter the planet : ').lower()
    if choose_planet == 'mars':
        mars_weight = user_input * 0.378
        rounded_weight = round(mars_weight,2)
        print(rounded_weight)
    elif choose_planet == 'mercury':
        mercury_weight = user_input * 0.376
        rounded_mercury = round(mercury_weight,2)
        print(rounded_mercury)
    elif choose_planet == 'venus':
        venus_weight = user_input * 0.889
        rounded_weight = round(venus_weight,2)
        print(rounded_weight)
    elif choose_planet == 'jupiter':
         jupiter_weight = user_input * 2.36
         rounded_jupiter = round(jupiter_weight,2)
         print(rounded_jupiter)
    elif choose_planet == 'saturn':
        saturn_weight = user_input * 1.081
        rounded_saturn = round(saturn_weight,2)
        print(rounded_saturn)

    elif choose_planet == 'uranus': 
        uranus_weight = user_input * 0.815
        rounded_uranus = round(uranus_weight,2)
        print(rounded_uranus)           
    elif choose_planet == 'neptune':   
        neptune_weight = user_input * 1.140
        rounded_neptune = round(neptune_weight,2)
        print(rounded_neptune)
    else:
        print('Invalid Planet name')    

main()        