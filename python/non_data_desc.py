from weakref import WeakKeyDictionary


class Positive:

    def __init__(self):
        self.value =100
    def __get__(self, instance, owner):
        print("__get__ called ", instance)
        return self.value

class Planet:
    radius_metres = Positive()
    mass_kilograms = Positive()
    orbital_period_seconds = Positive()
    surface_temperature_kelvin = Positive()


def main():
    mercury = Planet()
    import pdb;pdb.set_trace()
if __name__ == '__main__':
  main()