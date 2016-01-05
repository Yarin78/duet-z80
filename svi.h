; SVI bios doc: http://www.samdal.com/svbasicrom.htm

VDP_DW:  equ 0x80
VDP_CW:  equ 0x81
VDP_DR:  equ 0x84
VDP_CR:  equ 0x85

INITXT:  equ 0x0047  ; MODE 1
INIGRP:  equ 0x004A  ; MODE 2

CHSNS:   equ 0x003B  ; Tests the status of the keyboard buffer, set Z if no key
CHGET:   equ 0x003E  ; One character input (waiting), output in A
