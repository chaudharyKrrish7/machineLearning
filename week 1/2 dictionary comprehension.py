citiesF = {'ggn' : '34' , 'delhi' : '45' , 'mumbai' : '56'}
citiesC = {key: round((int(value) - 32) * 5/9) for (key,value) in citiesF.items() }
weather = {'ggn' : 'sunny' , 'delhi' : 'cloudy' , 'mumbai' : 'rainy'}
print(citiesC)
sunnyC = {key : value for (key,value) in weather.items() if value == 'sunny'}
print(sunnyC)
citiesD = {key : ("warm" if value >= 40 else "cold") for (key,value) in citiesC.items()}
print(citiesD)