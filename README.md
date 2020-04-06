# RFID Mifare Cloner

The purpose of this software is to provide an friendly interface to clone a RFID tag to an other tag and to train me 
writing a CLI with specific graphics.

![Alt text](rfid_cloner.png?raw=true "Title")



## Run with docker

1) Plug your RFID reader in your computer

2) Build the image :  
`docker build -t rfid-cloner .`  

3) Run the image with --privilegied on, because we need to access device's USB ports.  
`docker run -it --privileged rfid-cloner `


You're good to go ! 

## Troubleshooting : (Device or resource busy) 

This may happen if your kernel version (uname -a) is superior to 3.5 . So yoou need to do this **ON YOUR HOST** and not in your container.

`sudo nano /etc/modprobe.d/blacklist-libnfc.conf`  

Copy this in the file and save: 

```
blacklist nfc
blacklist pn533
blacklist pn533_usb
```

Then run :  

`sudo modprobe -r pn533_usb`  
`sudo modprobe -r pn533`  

It's possible that you may need to run this in **YOUR CONTAINER** : 

`service pcscd restart`


## Additionnal ressources : 

http://tvaira.free.fr/rfid/tutoriel-nfc-acr122u.pdf
