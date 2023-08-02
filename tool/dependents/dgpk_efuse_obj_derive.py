#!/usr/bin/env python3
#
# Copyright (C) 2023 Amlogic, Inc. All rights reserved.
#
#
# This source code is subject to the terms and conditions defined in the
# file 'LICENSE' which is part of this source code package.

def get_args():
	from argparse import ArgumentParser

	parser = ArgumentParser()
	parser.add_argument('--soc', type = str, required = True, help = 'soc')
	parser.add_argument('--dgpk', type = str, required = True, help = 'dgpk file')
	parser.add_argument('--out_dir', type = str, required = True, help = 'output directory')

	return parser.parse_args()

def main():
	import os
	import sys
	import binascii

	args = get_args()

	if not os.path.exists(args.dgpk):
		print(args.dgpk + ' not exist')
		sys.exit(1)

	if not os.path.exists(args.out_dir):
		os.mkdir(args.out_dir)

	f = open(args.dgpk, 'rb')
	dgpk = bytes.decode(binascii.b2a_hex(f.read()))
	f.close()

	fpath = args.out_dir + '/' + args.soc + '_dgpk.bin.efuse.obj'
	f = open(fpath, 'wb')
	cmd = 'efuse_obj set DGPK ' + dgpk + '\n' \
	    + 'efuse_obj lock DGPK'
	f.write(cmd.encode())
	f.close()

	print(os.path.abspath(fpath) + ' derived successfully')

if __name__ == '__main__':
	main()
