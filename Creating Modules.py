from sales import calc_shipping, calc_tax
#when import can use ctrl + space to see all objects defined in the module
#can use an asterisk * to import all modules, this is bad practice as you could import contradicting or overwriting

import sales

sales.calc_shipping()

calc_shipping()
calc_tax()

#can import the entire module as an object that can be called, sales.calc_shipping(), or
#you can import specific objects from module from, from sales import calc_shipping, calc_tax