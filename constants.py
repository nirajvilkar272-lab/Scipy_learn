import scipy
import scipy.constants as c


#All the constants available in Scipy
print(dir(c)) 

# Angle Constants
print("Angle Constants:")
print("pi =", c.pi)
print("degree =", c.degree)
print("arcmin =", c.arcmin)
print("arcsec =", c.arcsec)


# Time Constants
print("Time Constants:")
print("minute =", c.minute)
print("hour =", c.hour)
print("day =", c.day)
print("year =", c.year)
print()

# Length Constants
print("Length Constants:")
print("inch =", c.inch)
print("foot =", c.foot)
print("mile =", c.mile)
print("nautical mile =", c.nautical_mile)
print("angstrom =", c.angstrom)
print("light year =", c.light_year)
print("parsec =", c.parsec)
print()

# Mass Constants
print("Mass Constants:")
print("gram =", c.gram)
print("pound =", c.pound)
print("atomic mass unit =", c.atomic_mass)
print()

# Energy Constants
print("Energy Constants:")
print("electron volt =", c.electron_volt)
print("calorie =", c.calorie)
print()

# Temperature Constants
print("Temperature Constants:")
print("zero Celsius =", c.zero_Celsius)
print()

# Universal Physical Constants
print("Universal Constants:")
print("speed of light =", c.c)
print("Planck constant =", c.h)
print("Boltzmann constant =", c.k)
print("Avogadro constant =", c.Avogadro)
print("Gravitational constant =", c.G)