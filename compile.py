import sys

f = open(sys.argv[2], 'w')

output = '''
-- Copyright (C) 1991-2008 Altera Corporation
-- Your use of Altera Corporation's design tools, logic functions 
-- and other software and tools, and its AMPP partner logic 
-- functions, and any output files from any of the foregoing 
-- (including device programming or simulation files), and any 
-- associated documentation or information are expressly subject 
-- to the terms and conditions of the Altera Program License 
-- Subscription Agreement, Altera MegaCore Function License 
-- Agreement, or other applicable license agreement, including, 
-- without limitation, that your use is for the sole purpose of 
-- programming logic devices manufactured by Altera and sold by 
-- Altera or its authorized distributors.  Please refer to the 
-- applicable agreement for further details.

-- Quartus II generated Memory Initialization File (.mif)
''';
print(output)

f.write(output)

width = 32
depth = 256

output = '''
WIDTH=%d;
DEPTH=%d;

ADDRESS_RADIX=UNS;
DATA_RADIX=HEX;
''' % (width, depth);
print(output)
f.write(output);

cmds = {
	'NOP':         0x00,
	'SET':        0x01,
	'READ':       0x02,
	'WRITE':   0x03,
	'ADD':  0x04,
	'SUB':         0x05,
	'ADD_TO':   0x06,
	'SUB_FROM':    0x07,

	'JUMP':         0x08,
	'JUMP_IF':      0x09,
	'JUMP_ACUM':    0x0A,
	
	'A_WRITE': 0x10,
	'A_WRITE_ADDR':          0x11,
	'A_COPY':          0x12,
	'A_ADD':     0x13,
	'A_SUB':     0x14,
	'A_ADD_ADDR':     0x15,
	'A_SUB_ADDR':     0x16,
	'A_ADD_TO':          0x17,
	'A_SUB_FROM':     0x18,
	'A_JUMP_IF_ADDR':     0x19,

	'RESET':        0xFF
}

str = 'CONTENT BEGIN\n'
print(str)
f.write(str)

index = 0
for line in open(sys.argv[1]):
	parts = line.strip().split()
	if len(parts) > 0:
		cmd = cmds[parts[0].upper()]
		arg1 = 0;
		arg2 = 0;
		arg3 = 0;
		if len(parts) > 1:
			arg1 = int(parts[1])
		if len(parts) > 2:
			arg2 = int(parts[2])
		if len(parts) > 3:
			arg3 = int(parts[3])
		output = '\t%d : %02X%02X%02X%02X;\n' % (index, cmd, arg1, arg2, arg3)
		print(output)
		f.write(output)
		index += 1

output = '\t[%d..%d] : 00000000;\n' % (index, depth - 1)
print(output)
f.write(output)

output = 'END;';
print(output)
f.write(output)
