import struct
import zlib
import os

def putanja(datoteka):
    return r'{}'.format(os.path.dirname(os.path.abspath(__file__))) + f'{chr(92) if os.name == "nt" else "/"}{datoteka.replace("/",chr(92)) if os.name == "nt" else datoteka.replace(chr(92),"/")}'

def pisi_datoteku(naziv, podaci=''):
    datoteka = open(putanja(naziv), 'wb')
    datoteka.write(podaci)
    datoteka.close()

def napravi_png(visina, sirina, podaci):
    png_oznaka = b'\x89PNG\r\n\x1a\n'
    ihdr_komad = b'IHDR' + struct.pack("!I",sirina) + struct.pack("!I", visina) + b'\x01\x00\x00\x00\x00'
    ihdr_komad = struct.pack("!I",13) + ihdr_komad + struct.pack("!I", zlib.crc32(ihdr_komad))
    sazeti_podaci = zlib.compress(podaci)
    idat_komad = b'IDAT' + sazeti_podaci 
    idat_komad = struct.pack("!I",len(sazeti_podaci)) + idat_komad + struct.pack("!I", zlib.crc32(idat_komad))
    iend_komad = struct.pack("!I",0) + b'IEND' + struct.pack("!I", zlib.crc32(b'IEND'))
    return png_oznaka + ihdr_komad + idat_komad + iend_komad

pisi_datoteku('nmpngns.png', napravi_png(1,1,struct.pack("!h", 0)))


