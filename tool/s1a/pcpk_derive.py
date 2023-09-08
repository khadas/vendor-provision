#!/usr/bin/env python3
#
# Copyright (C) 2023 Amlogic, Inc. All rights reserved.
#
# This source code is subject to the terms and conditions defined in the
# file 'LICENSE' which is part of this source code package.

import sys

sys.dont_write_bytecode = True
import soc

TARGET_NAME = 'pcpk'
SCRIPT_PATH = sys.path[0] + '/../dependents/pcpk_derive.py'
KEY_TOOL_PATH = sys.path[0] + '/../../../../../../bootloader/uboot-repo/fip/' + soc.SOC + '/binary-tool/vendor-keytool'

def get_args():
	from argparse import ArgumentParser

	parser = ArgumentParser()
	parser.add_argument('--dgpk', type = str, required = True, help = 'dgpk file')
	parser.add_argument('--out_dir', type = str, default = './' + soc.SOC + '-' + TARGET_NAME + '/', help = 'output directory')
	return parser.parse_args()

def main():
	import os
	import sys
	import subprocess

	args = get_args()

	cmd = [sys.executable, SCRIPT_PATH]
	cmd.extend(['--soc=' + soc.SOC])
	cmd.extend(['--key_tool=' + KEY_TOOL_PATH])
	cmd.extend(['--dgpk1=' + args.dgpk])
	cmd.extend(['--out_dir=' + args.out_dir])
	sub = subprocess.Popen(cmd)
	sub.communicate()

if __name__ == '__main__':
	main()