; MSX bios doc: http://map.grauw.nl/resources/msxbios.php

VDP_DW:  equ 0x98
VDP_CW:  equ 0x99
VDP_DR:  equ 0x98
VDP_CR:  equ 0x99

INITXT:  equ 0x006C  ; MODE 1
INIGRP:  equ 0x0072  ; MODE 2
DCOMPR:  equ 0x0020  ; Compare DE and HL

CHSNS:   equ 0x009C  ; Tests the status of the keyboard buffer, set Z if no key
CHGET:   equ 0x009F  ; One character input (waiting), output in A
