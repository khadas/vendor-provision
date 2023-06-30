#!/usr/bin/env python3
#
# Copyright (C) 2022 Amlogic, Inc. All rights reserved.
#
#
# This source code is subject to the terms and conditions defined in the
# file 'LICENSE' which is part of this source code package.
#

def get_args():
	from argparse import ArgumentParser

	parser = ArgumentParser()
	parser.add_argument('--pcpk', default='null', required = True, help='provision common protect key')
	parser.add_argument('--in', dest='inf', default='null', required = True, help='input Secure OS image file')
	parser.add_argument('--out', type=str, default='null', help='output Secure OS image file')
	return parser.parse_args()

def read_key(key):
	with open(key, 'rb+') as f:
		return f.read()

def is_signed_bl32(infile):
	import struct

	dtb_header_len = 32
	with open(infile, 'rb+') as f:
		raw = f.read()
		offs = raw.index(b"BTD@") + dtb_header_len
		f.seek(offs)
		dtb_magic = struct.unpack('<I', f.read(4))[0]
		if (dtb_magic == 0xedfe0dd0):
			return True

		return False

def main():
	import struct
	import array
	import base64
	import os
	from pyfdt.pyfdt import Fdt, FdtNode, FdtPropertyStrings, FdtPropertyWords, FdtBlobParse

	tmpfile = ".tmp"
	dtb_header_len = 32
	dtb_len_max = 12 * 1024 - dtb_header_len

	args = get_args()
	if args.out == 'null':
		args.out = args.inf

	if is_signed_bl32(args.inf) == False:
		print('Not a signed bl32 image!')
		exit(0)

	with open(args.pcpk, 'rb+') as f:
		pcpk = f.read()
		pcpk_size = len(pcpk)
		if pcpk_size != 16:
			print('PCPK key size must be 16 byte')
			exit(0)

		pcpk_b64 = base64.b64encode(pcpk)

	with open(args.inf, 'rb+') as f, open(tmpfile, 'wb+') as fdtb:
		raw = f.read()
		offs = raw.index(b"BTD@") + dtb_header_len
		f.seek(offs)
		fdtb.write(f.read(dtb_len_max))

	with open(tmpfile, 'rb+') as fdtb:
		dtb = FdtBlobParse(fdtb)
		fdt = dtb.to_fdt()
		os.remove(tmpfile)

	node = fdt.resolve_path('/keys')
	node.remove('pcpk')
	node.remove('pcpk_size')
	node.add_subnode(FdtPropertyStrings("pcpk", [bytes.decode(pcpk_b64)]))
	node.add_subnode(FdtPropertyWords("pcpk_size", [pcpk_size]))

	if args.out != 'null':
		dtb_len = len(fdt.to_dtb())
		if dtb_len > dtb_len_max:
			print ("dtb size(%d) exceed(max is %d)!" %(dtb_len, dtb_len_max))
			exit(-1)

		print ('Packing ...')
		if args.pcpk != 'null':
			pcpk_size = len(read_key(args.pcpk))
			print ('               pcpk.name = ' + args.pcpk)
			print ('               pcpk.size = ' + str(pcpk_size))

		print ('             image.name = ' + args.inf)
		print ('    Output:  image.name = ' + args.out)

		with open(args.inf, 'rb+') as f:
			raw = f.read()

		with open(args.out, 'wb+') as f:
			f.write(raw)
			offs = raw.index(b"BTD@") + dtb_header_len
			f.seek(offs)
			f.write(fdt.to_dtb())

if __name__ == "__main__":
	main()
