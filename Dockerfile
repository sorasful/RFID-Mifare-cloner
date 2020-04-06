FROM  ubuntu:18.04

WORKDIR /tmp


# dependencies for libnfc 
RUN apt update && apt install -y autoconf pcsc-tools pcscd libpcsclite-dev libpcsclite1 libusb-dev wget build-essential git pkg-config
RUN apt-get install -y libpcsclite-dev libpcsclite1 pcsc-tools pcscd
RUN apt-get install -y automake autoconf libtool libusb-dev

RUN wget http://dl.bintray.com/nfc-tools/sources/libnfc-1.7.1.tar.bz2 

RUN tar xjf libnfc-1.7.1.tar.bz2

RUN cd libnfc-1.7.1 && autoreconf -i &&  ./configure && make && make install && ldconfig



# dependencies for mfoc
RUN git clone https://github.com/nfc-tools/mfoc.git

RUN cd mfoc && autoreconf -is && ./configure && make && make install


# dependencies for running the python script
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update
RUN apt install -y python3.7 python3-pip


WORKDIR /app

COPY . .

RUN  pip3  install -r requirements.txt

CMD python3 RFID_mifare_cloner/rfid_mifare_cloner.py
