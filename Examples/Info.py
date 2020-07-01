from EasyConversion import info
#Imports

print("We are version " + info.version.current.name)
#Print the version number
#Outputs:
#   We are version 0.5.1

get_version = info.version.get_version("0.2.0")
print("Version " + get_version.name + " was released on " + get_version.release_date + ".")
#Prints the version name with release date
#Outputs:
#   Version 0.2.0 released on June 27th 2020.
