proc loadbinary { addr filename } {

        # Open the file, and set up to process it in binary mode.
    set zzfid2 [open $filename r]
        fconfigure $zzfid2 -translation binary -encoding binary
        transdata $addr $zzfid2
}

proc transdata {addr fid} {

        while { ! [ eof $fid ] } {

           #Convert byte from file as parameter good for poke-function
	    set hex [getbyteff $fid]

	    if {$hex ne "" } {
              poke $addr 0x$hex
              incr addr

	    }
        }
    }


proc getbyteff {fid} {
    set s [read $fid 1]
           binary scan $s H*@0 hex
           return $hex
}
