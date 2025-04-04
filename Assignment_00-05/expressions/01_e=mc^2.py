C : int = 299792458
def main():

  mass_in_KG : float = float(input('Enter the mass in kilos : '))
  energy_In_Joules = mass_in_KG * (C ** 2)
  print('e = m * C^2 ...')
  print('m = ' + str(mass_in_KG) + ' KG')
  print('C = ' + str(C) + ' m/s')
  print(energy_In_Joules)
  


if __name__ == '__main__':
    main()