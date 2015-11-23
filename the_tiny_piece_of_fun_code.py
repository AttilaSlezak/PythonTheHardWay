__author__ = 'Slezak Attila'
# -- coding: utf-8 --

while True:
    for j in range(100):
        for i in ["/", "-", "|", "\\", "|"]:
            print("%s\r" % i, end=" ")
    break

# Valószínűleg túl gyors a gép ahhoz, hogy bármit lássunk a "forgó vonalból"