class Planet:
    def __init__(self, name, planet_type, star):
        if not isinstance(name, str):
            raise TypeError('name, planet type, and star must be strings')
        if name == '':
            raise ValueError('name, planet_type, and star must be non-empty strings')
        self.name = name

        if not isinstance(planet_type, str):
            raise TypeError('name, planet type, and star must be strings')
        if planet_type == '':
            raise ValueError('name, planet_type, and star must be non-empty strings')        
        self.planet_type = planet_type

        if not isinstance(star, str):
            raise TypeError('name, planet type, and star must be strings')
        if star == '':
            raise ValueError('name, planet_type, and star must be non-empty strings')        
        self.star = star

    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'
    
    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'
    
planet_1 = Planet('Venus', 'Planet', 'Sun')
print(planet_1)
planet_1.orbit()
print(planet_1.orbit())
planet_2 = Planet('Mars', 'Planet', 'Sun')
print(planet_2)
planet_2.orbit()
print(planet_2.orbit())
planet_3 = Planet('Pluto', 'Dwarf Planet', 'Sun')
print(planet_3)
planet_3.orbit()
print(planet_3.orbit())