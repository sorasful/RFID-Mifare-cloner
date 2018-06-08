# RFID Mifare Cloner

The purpose of this software is to provide an friendly interface to clone a rfid tag to an other tag.

## Requirements

- Usb tag reader (ACR122U in my case) 
- Python3.6+

## Missing dependencies ? 
###  Install ACR122U (Ubuntu)
- ` sudo apt-get install pcsc-tools pcscd libpcsclite-dev libpcsclite1 libusb-dev`  
- ` wget http://dl.bintray.com/nfc-tools/sources/libnfc-1.7.1.tar.bz2`  
- ` tar xjf libnfc-1.7.1.tar.bz2 `
- ` cd libnfc-1.7.1`
- ` .configure`
- ` make`
- ` make install`
- ` ldconfig`

Test it : 
` nfc-scan-device`



## RUN IT


## Additionnal ressources : 

http://tvaira.free.fr/rfid/tutoriel-nfc-acr122u.pdf