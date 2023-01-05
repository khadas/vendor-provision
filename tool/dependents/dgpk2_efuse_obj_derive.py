#!/usr/bin/env python3
#
# Copyright (C) 2021 Amlogic, Inc. All rights reserved.
#
# This source code is subject to the terms and conditions defined in the
# file 'LICENSE' which is part of this source code package.

MAX_IDX = 100000000
DERIVED_FILE_NUM = 0

def get_args():
	from argparse import ArgumentParser

	parser = ArgumentParser()
	parser.add_argument('--soc', type = str, required = True, help = 'soc')
	parser.add_argument('--dgpk2', type = str, required = True, help = 'dgpk2 file or directory')
	parser.add_argument('--pfid', type = str, required = True, help = 'pfid file or directory')
	parser.add_argument('--out_dir', type = str, required = True, help = 'output directory')
	return parser.parse_args()

def derive_efuse_obj(file_dgpk2, file_pfid, out_dir, idx, soc):
	import os
	import sys
	import binascii

	if int(idx) > MAX_IDX:
		print('the number of files exceeds the limit')
		sys.exit(1)

	f = open(file_dgpk2, 'rb')
	dgpk2 = bytes.decode(binascii.b2a_hex(f.read()))
	f.close()

	f = open(file_pfid, 'rb')
	pfid = bytes.decode(binascii.b2a_hex(f.read()))
	f.close()

	file_obj = out_dir + '/' + soc + '_dgpk2_' + idx + '.bin.efuse.obj'
	f = open(file_obj, 'wb')
	cmd = 'efuse_obj set DGPK2 ' + dgpk2 + ';\r\n' \
	      + 'efuse_obj lock DGPK2;\r\n' \
	      + 'efuse_obj set DGPK1_DGPK2_CID ' + pfid + ';\r\n' \
	      + 'efuse_obj lock DGPK1_DGPK2_CID;'
	f.write(cmd.encode())
	f.close()

	global DERIVED_FILE_NUM
	DERIVED_FILE_NUM = DERIVED_FILE_NUM + 1
	print(os.path.abspath(file_obj) + ' derived successfully')

def main():
	import os
	import sys

	args = get_args()

	if not os.path.exists(args.out_dir):
		os.mkdir(args.out_dir)

	if os.path.isfile(args.dgpk2) and os.path.isfile(args.pfid):
		derive_efuse_obj(args.dgpk2, args.pfid, args.out_dir, '000000001', args.soc)
	elif os.path.isdir(args.dgpk2) and os.path.isdir(args.pfid):
		for parent, dnames, fnames in os.walk(args.dgpk2):
			for fname in fnames:
				idx = fname[-13 : -4]
				file_pfid = args.pfid + '/' + args.soc + '_pfid_' + idx + '.bin'
				file_dgpk2 = os.path.join(parent, fname)
				if os.path.exists(file_pfid):
					derive_efuse_obj(file_dgpk2, file_pfid, args.out_dir, idx, args.soc)
	else:
		print('input parameter error')
		sys.exit(1)

	print(str(DERIVED_FILE_NUM) + ' ' + args.soc + '_dgpk2_efuse_object files derived successfully')

if __name__ == '__main__':
	main()
