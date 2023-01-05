#!/usr/bin/env python3
#
# Copyright (C) 2021 Amlogic, Inc. All rights reserved.
#
# This source code is subject to the terms and conditions defined in the
# file 'LICENSE' which is part of this source code package.

import sys

sys.dont_write_bytecode = True
import soc

DERIVED_FILE_NUM = 0
TARGET_NAME = soc.SOC + '_efuse_obj_pack'

LOCK = 1
UNLOCK = 0

PACK_MAGIC = 0x45465553 #'EFUS'
PACK_VERSION = 1

MAX_SIZE_OBJ_NAME = 47
MAX_SIZE_OBJ_DATA = 32

def get_args():
	from argparse import ArgumentParser

	parser = ArgumentParser()
	parser.add_argument('--MUTE_CONFIG_0', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--MUTE_CONFIG_1', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--DEVICE_SCS_SEGID', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--DEVICE_VENDOR_SEGID', type = str, default = '', help = 'file or hex string')
	#parser.add_argument('--CHIPSET_PART_CONFIG', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--AUDIO_VENDOR_ID', type = str, default = '', help = 'file or hex string')
	#parser.add_argument('--DEVICE_SCS_VERS', type = str, default = '', help = 'file or hex string')
	#parser.add_argument('--DEVICE_TEE_VERS', type = str, default = '', help = 'file or hex string')
	#parser.add_argument('--DEVICE_REE_VERS', type = str, default = '', help = 'file or hex string')
	#parser.add_argument('--AMLOGIC_CHIPID', type = str, default = '', help = 'file or hex string')
	#parser.add_argument('--ACGK_ACUK_CID', type = str, default = '', help = 'file or hex string')
	#parser.add_argument('--DVGK_CID', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--DVUK_CID', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--PFID', type = str, default = '', help = 'file or hex string or directory')
	parser.add_argument('--DVGK', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--DVUK', type = str, default = '', help = 'file or hex string')
	#parser.add_argument('--DGPK1', type = str, default = '', help = 'file or hex string or directory')
	parser.add_argument('--DGPK2', type = str, default = '', help = 'file or hex string or directory')
	parser.add_argument('--HASH_NORMAL_DEVICE_ROOTCERT', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--HASH_DFU_DEVICE_ROOTCERT', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_DEVICE_SCS_SIG', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_NORMAL_DEVICE_ROOTCERT_0', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_NORMAL_DEVICE_ROOTCERT_1', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_NORMAL_DEVICE_ROOTCERT_2', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_NORMAL_DEVICE_ROOTCERT_3', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_DEVICE_ROOT_PUBRSA_PROT', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_DEVICE_LVL1_PUBRSA_PROT', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_DEVICE_VENDOR_SIG', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_DEVICE_PROT', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_DEVICE_LVLX_PUBRSA_PROT', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_DFU_DEVICE_ROOTCERT_0', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_DFU_DEVICE_ROOTCERT_1', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_DFU_DEVICE_ROOTCERT_2', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_DFU_DEVICE_ROOTCERT_3', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_BOOT_NORMAL_SPI_NOR', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_BOOT_NORMAL_NAND', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_BOOT_NORMAL_EMMC', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_BOOT_NORMAL_SDCARD', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_BOOT_NORMAL_SPI_NAND', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_BOOT_DFU_SPI_NOR', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_BOOT_DFU_NAND', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_BOOT_DFU_EMMC', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_BOOT_DFU_SDCARD', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_BOOT_DFU_SPI_NAND', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_BOOT_DFU_USB', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_BOOT_ALTSRC', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_BOOT_NORMAL_FALLBACK2USB', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_DFU_ON_LOCKED_DIF', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_SW_BOOT_OVERRIDE', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_EXT_BOOT_OVERRIDE', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_ACPU_ROM_PRINT_VERBOSE', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_ACPU_ROM_PRINT_ALL', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_DDR_FIP_CONTAINER', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_USB_AUTH', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_MUTE', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_DIF_MASTER_PROT', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_DIF_MASTER', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_SOCBRG_JTAG_PROT', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_SOCBRG_JTAG', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_ACPU_JTAG_PROT', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_ACPU_JTAG', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_ACPU_TEE_JTAG', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_AOCPU_JTAG_PROT', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_AOCPU_JTAG', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_DIF_SECPU_JTAG', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_AUCPU_JTAG', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_DSP_JTAG_PROT', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_DSP_JTAG', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_DIF_SCAN', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_DIF_SCAN_PROT', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_DVUK_DERIVE_WITH_CID', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_USB_PWD_MRK_DGPK2', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_25MHZ_EMMC', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_25MHZ_NAND', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_SNOR_2BIT', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_SNAND_4BIT', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_NBL2_SNOR', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_NBL2_SNAND', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_4BL2_SNOR', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_8BL2_SNAND', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_32MHZ_SNOR', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_64MHZ_SNOR', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_32MHZ_SNAND', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_64MHZ_SNAND', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_4SEC_SNAND', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_EMMC_USER', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_EMMC_BOOT_0', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_EMMC_BOOT_1', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_NAND_MLC', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_NBL2_NAND', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_DISABLE_8BL2_NAND', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_SNAND_2PLANE_ADDR', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_EMMC_BOOTMODE_HS', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_EMMC_BOOTMODE', type = str, default = '', help = 'file or hex string')
	parser.add_argument('--FEAT_ENABLE_EMMC_BOOTMODE_8BITS', type = str, default = '', help = 'file or hex string')

	parser.add_argument('--out_dir', type = str, default = './' + soc.SOC + '-efuse-object-packs/', help = 'output directory')

	return parser.parse_args()

def derive_object(obj_name, value, lock, exp_data_size):
	import os
	import sys
	import struct
	import binascii

	if len(obj_name) > MAX_SIZE_OBJ_NAME:
		print(obj_name + ' name size exceeded')
		sys.exit(1)

	if os.path.isfile(value) == False:
		if len(value) > MAX_SIZE_OBJ_DATA * 2:
			print(obj_name + ' data string exceeded')
			sys.exit(1)
		if len(value) % 2:
			print(obj_name + ' data string cannot be odd-length')
			sys.exit(1)

	if len(value) == 0:
		return (False, bytes())

	if os.path.isfile(value):
		data_size = os.stat(value).st_size
	else:
		data_size = len(value) // 2

	if data_size != exp_data_size:
		print(obj_name + ' data size is incorrect')
		sys.exit(1)

	if os.path.isfile(value):
		f = open(value, 'rb')
		data = f.read()
		f.close()
	else:
		data = binascii.unhexlify(value)

	ret = str.encode(obj_name.ljust(MAX_SIZE_OBJ_NAME + 1, '\0'))
	ret = ret + struct.pack('<I', data_size)
	ret = ret + data + (MAX_SIZE_OBJ_DATA - len(data)) * b'\0'
	ret = ret + struct.pack('<I', lock)

	return (True, ret)

def derive_pack(args, dgpk2_para, pfid_para):
	import os
	import sys
	import binascii
	import struct
	import time
	from Cryptodome.Hash import SHA256

	obj_list = (
		('MUTE_CONFIG_0', args.MUTE_CONFIG_0, LOCK, 4),
		('MUTE_CONFIG_1', args.MUTE_CONFIG_1, LOCK, 4),
		('DEVICE_SCS_SEGID', args.DEVICE_SCS_SEGID, LOCK, 4),
		('DEVICE_VENDOR_SEGID', args.DEVICE_VENDOR_SEGID, LOCK, 4),
		#('CHIPSET_PART_CONFIG', args.CHIPSET_PART_CONFIG, UNLOCK, 4), #not supported
		('AUDIO_VENDOR_ID', args.AUDIO_VENDOR_ID, LOCK, 4),
		#('DEVICE_SCS_VERS', args.DEVICE_SCS_VERS, UNLOCK, 4), #not supported
		#('DEVICE_TEE_VERS', args.DEVICE_TEE_VERS, UNLOCK, 4), #not supported
		#('DEVICE_REE_VERS', args.DEVICE_REE_VERS, UNLOCK, 4), #not supported

		#('AMLOGIC_CHIPID', args.AMLOGIC_CHIPID, UNLOCK, 8) #not supported
		#('ACGK_ACUK_CID', args.ACGK_ACUK_CID, UNLOCK, 8), #not supported
		#('DVGK_CID', args.DVGK_CID, UNLOCK, 8), #not supported
		('DVUK_CID', args.DVUK_CID, LOCK, 8),
		#('PFID', args.PFID, UNLOCK, 16), #processed separately

		('DVGK', args.DVGK, LOCK, 16),
		('DVUK', args.DVUK, LOCK, 16),
		#('DGPK1', args.DGPK1, LOCK, 16), #not supported
		#('DGPK2', args.DGPK2, LOCK, 16), #processed separately

		('HASH_NORMAL_DEVICE_ROOTCERT', args.HASH_NORMAL_DEVICE_ROOTCERT, LOCK, 32),
		('HASH_DFU_DEVICE_ROOTCERT', args.HASH_DFU_DEVICE_ROOTCERT, LOCK, 32),

		('FEAT_ENABLE_DEVICE_SCS_SIG', args.FEAT_ENABLE_DEVICE_SCS_SIG, UNLOCK, 1),
		('FEAT_DISABLE_NORMAL_DEVICE_ROOTCERT_0', args.FEAT_DISABLE_NORMAL_DEVICE_ROOTCERT_0, UNLOCK, 1),
		('FEAT_DISABLE_NORMAL_DEVICE_ROOTCERT_1', args.FEAT_DISABLE_NORMAL_DEVICE_ROOTCERT_1, UNLOCK, 1),
		('FEAT_DISABLE_NORMAL_DEVICE_ROOTCERT_2', args.FEAT_DISABLE_NORMAL_DEVICE_ROOTCERT_2, UNLOCK, 1),
		('FEAT_DISABLE_NORMAL_DEVICE_ROOTCERT_3', args.FEAT_DISABLE_NORMAL_DEVICE_ROOTCERT_3, UNLOCK, 1),
		('FEAT_ENABLE_DEVICE_ROOT_PUBRSA_PROT', args.FEAT_ENABLE_DEVICE_ROOT_PUBRSA_PROT, UNLOCK, 1),
		('FEAT_ENABLE_DEVICE_LVL1_PUBRSA_PROT', args.FEAT_ENABLE_DEVICE_LVL1_PUBRSA_PROT, UNLOCK, 1),
		('FEAT_ENABLE_DEVICE_VENDOR_SIG', args.FEAT_ENABLE_DEVICE_VENDOR_SIG, UNLOCK, 1),
		('FEAT_ENABLE_DEVICE_PROT', args.FEAT_ENABLE_DEVICE_PROT, UNLOCK, 1),
		('FEAT_ENABLE_DEVICE_LVLX_PUBRSA_PROT', args.FEAT_ENABLE_DEVICE_LVLX_PUBRSA_PROT, UNLOCK, 1),
		('FEAT_DISABLE_DFU_DEVICE_ROOTCERT_0', args.FEAT_DISABLE_DFU_DEVICE_ROOTCERT_0, UNLOCK, 1),
		('FEAT_DISABLE_DFU_DEVICE_ROOTCERT_1', args.FEAT_DISABLE_DFU_DEVICE_ROOTCERT_1, UNLOCK, 1),
		('FEAT_DISABLE_DFU_DEVICE_ROOTCERT_2', args.FEAT_DISABLE_DFU_DEVICE_ROOTCERT_2, UNLOCK, 1),
		('FEAT_DISABLE_DFU_DEVICE_ROOTCERT_3', args.FEAT_DISABLE_DFU_DEVICE_ROOTCERT_3, UNLOCK, 1),
		('FEAT_DISABLE_BOOT_NORMAL_SPI_NOR', args.FEAT_DISABLE_BOOT_NORMAL_SPI_NOR, UNLOCK, 1),
		('FEAT_DISABLE_BOOT_NORMAL_NAND', args.FEAT_DISABLE_BOOT_NORMAL_NAND, UNLOCK, 1),
		('FEAT_DISABLE_BOOT_NORMAL_EMMC', args.FEAT_DISABLE_BOOT_NORMAL_EMMC, UNLOCK, 1),
		('FEAT_DISABLE_BOOT_NORMAL_SDCARD', args.FEAT_DISABLE_BOOT_NORMAL_SDCARD, UNLOCK, 1),
		('FEAT_DISABLE_BOOT_NORMAL_SPI_NAND', args.FEAT_DISABLE_BOOT_NORMAL_SPI_NAND, UNLOCK, 1),
		('FEAT_DISABLE_BOOT_DFU_SPI_NOR', args.FEAT_DISABLE_BOOT_DFU_SPI_NOR, UNLOCK, 1),
		('FEAT_DISABLE_BOOT_DFU_NAND', args.FEAT_DISABLE_BOOT_DFU_NAND, UNLOCK, 1),
		('FEAT_DISABLE_BOOT_DFU_EMMC', args.FEAT_DISABLE_BOOT_DFU_EMMC, UNLOCK, 1),
		('FEAT_DISABLE_BOOT_DFU_SDCARD', args.FEAT_DISABLE_BOOT_DFU_SDCARD, UNLOCK, 1),
		('FEAT_DISABLE_BOOT_DFU_SPI_NAND', args.FEAT_DISABLE_BOOT_DFU_SPI_NAND, UNLOCK, 1),
		('FEAT_DISABLE_BOOT_DFU_USB', args.FEAT_DISABLE_BOOT_DFU_USB, UNLOCK, 1),
		('FEAT_DISABLE_BOOT_ALTSRC', args.FEAT_DISABLE_BOOT_ALTSRC, UNLOCK, 1),
		('FEAT_DISABLE_BOOT_NORMAL_FALLBACK2USB', args.FEAT_DISABLE_BOOT_NORMAL_FALLBACK2USB, UNLOCK, 1),
		('FEAT_DISABLE_DFU_ON_LOCKED_DIF', args.FEAT_DISABLE_DFU_ON_LOCKED_DIF, UNLOCK, 1),
		('FEAT_DISABLE_SW_BOOT_OVERRIDE', args.FEAT_DISABLE_SW_BOOT_OVERRIDE, UNLOCK, 1),
		('FEAT_DISABLE_EXT_BOOT_OVERRIDE', args.FEAT_DISABLE_EXT_BOOT_OVERRIDE, UNLOCK, 1),
		('FEAT_DISABLE_ACPU_ROM_PRINT_VERBOSE', args.FEAT_DISABLE_ACPU_ROM_PRINT_VERBOSE, UNLOCK, 1),
		('FEAT_DISABLE_ACPU_ROM_PRINT_ALL', args.FEAT_DISABLE_ACPU_ROM_PRINT_ALL, UNLOCK, 1),
		('FEAT_DISABLE_DDR_FIP_CONTAINER', args.FEAT_DISABLE_DDR_FIP_CONTAINER, UNLOCK, 1),
		('FEAT_ENABLE_USB_AUTH', args.FEAT_ENABLE_USB_AUTH, UNLOCK, 1),
		('FEAT_ENABLE_MUTE', args.FEAT_ENABLE_MUTE, UNLOCK, 1),
		('FEAT_ENABLE_DIF_MASTER_PROT', args.FEAT_ENABLE_DIF_MASTER_PROT, UNLOCK, 1),
		('FEAT_DISABLE_DIF_MASTER', args.FEAT_DISABLE_DIF_MASTER, UNLOCK, 1),
		('FEAT_ENABLE_SOCBRG_JTAG_PROT', args.FEAT_ENABLE_SOCBRG_JTAG_PROT, UNLOCK, 1),
		('FEAT_DISABLE_SOCBRG_JTAG', args.FEAT_DISABLE_SOCBRG_JTAG, UNLOCK, 1),
		('FEAT_ENABLE_ACPU_JTAG_PROT', args.FEAT_ENABLE_ACPU_JTAG_PROT, UNLOCK, 1),
		('FEAT_DISABLE_ACPU_JTAG', args.FEAT_DISABLE_ACPU_JTAG, UNLOCK, 1),
		('FEAT_DISABLE_ACPU_TEE_JTAG', args.FEAT_DISABLE_ACPU_TEE_JTAG, UNLOCK, 1),
		('FEAT_ENABLE_AOCPU_JTAG_PROT', args.FEAT_ENABLE_AOCPU_JTAG_PROT, UNLOCK, 1),
		('FEAT_DISABLE_AOCPU_JTAG', args.FEAT_DISABLE_AOCPU_JTAG, UNLOCK, 1),
		('FEAT_DISABLE_DIF_SECPU_JTAG', args.FEAT_DISABLE_DIF_SECPU_JTAG, UNLOCK, 1),
		('FEAT_DISABLE_AUCPU_JTAG', args.FEAT_DISABLE_AUCPU_JTAG, UNLOCK, 1),
		('FEAT_ENABLE_DSP_JTAG_PROT', args.FEAT_ENABLE_DSP_JTAG_PROT, UNLOCK, 1),
		('FEAT_DISABLE_DSP_JTAG', args.FEAT_DISABLE_DSP_JTAG, UNLOCK, 1),
		('FEAT_DISABLE_DIF_SCAN', args.FEAT_DISABLE_DIF_SCAN, UNLOCK, 1),
		('FEAT_ENABLE_DIF_SCAN_PROT', args.FEAT_ENABLE_DIF_SCAN_PROT, UNLOCK, 1),
		('FEAT_ENABLE_DVUK_DERIVE_WITH_CID', args.FEAT_ENABLE_DVUK_DERIVE_WITH_CID, UNLOCK, 1),
		('FEAT_ENABLE_USB_PWD_MRK_DGPK2', args.FEAT_ENABLE_USB_PWD_MRK_DGPK2, UNLOCK, 1),
		('FEAT_ENABLE_25MHZ_EMMC', args.FEAT_ENABLE_25MHZ_EMMC, UNLOCK, 1),
		('FEAT_ENABLE_25MHZ_NAND', args.FEAT_ENABLE_25MHZ_NAND, UNLOCK, 1),
		('FEAT_ENABLE_SNOR_2BIT', args.FEAT_ENABLE_SNOR_2BIT, UNLOCK, 1),
		('FEAT_ENABLE_SNAND_4BIT', args.FEAT_ENABLE_SNAND_4BIT, UNLOCK, 1),
		('FEAT_DISABLE_NBL2_SNOR', args.FEAT_DISABLE_NBL2_SNOR, UNLOCK, 1),
		('FEAT_DISABLE_NBL2_SNAND', args.FEAT_DISABLE_NBL2_SNAND, UNLOCK, 1),
		('FEAT_ENABLE_4BL2_SNOR', args.FEAT_ENABLE_4BL2_SNOR, UNLOCK, 1),
		('FEAT_ENABLE_8BL2_SNAND', args.FEAT_ENABLE_8BL2_SNAND, UNLOCK, 1),
		('FEAT_ENABLE_32MHZ_SNOR', args.FEAT_ENABLE_32MHZ_SNOR, UNLOCK, 1),
		('FEAT_ENABLE_64MHZ_SNOR', args.FEAT_ENABLE_64MHZ_SNOR, UNLOCK, 1),
		('FEAT_ENABLE_32MHZ_SNAND', args.FEAT_ENABLE_32MHZ_SNAND, UNLOCK, 1),
		('FEAT_ENABLE_64MHZ_SNAND', args.FEAT_ENABLE_64MHZ_SNAND, UNLOCK, 1),
		('FEAT_ENABLE_4SEC_SNAND', args.FEAT_ENABLE_4SEC_SNAND, UNLOCK, 1),
		('FEAT_DISABLE_EMMC_USER', args.FEAT_DISABLE_EMMC_USER, UNLOCK, 1),
		('FEAT_DISABLE_EMMC_BOOT_0', args.FEAT_DISABLE_EMMC_BOOT_0, UNLOCK, 1),
		('FEAT_DISABLE_EMMC_BOOT_1', args.FEAT_DISABLE_EMMC_BOOT_1, UNLOCK, 1),
		('FEAT_DISABLE_NAND_MLC', args.FEAT_DISABLE_NAND_MLC, UNLOCK, 1),
		('FEAT_DISABLE_NBL2_NAND', args.FEAT_DISABLE_NBL2_NAND, UNLOCK, 1),
		('FEAT_DISABLE_8BL2_NAND', args.FEAT_DISABLE_8BL2_NAND, UNLOCK, 1),
		('FEAT_ENABLE_SNAND_2PLANE_ADDR', args.FEAT_ENABLE_SNAND_2PLANE_ADDR, UNLOCK, 1),
		('FEAT_ENABLE_EMMC_BOOTMODE_HS', args.FEAT_ENABLE_EMMC_BOOTMODE_HS, UNLOCK, 1),
		('FEAT_ENABLE_EMMC_BOOTMODE', args.FEAT_ENABLE_EMMC_BOOTMODE, UNLOCK, 1),
		('FEAT_ENABLE_EMMC_BOOTMODE_8BITS', args.FEAT_ENABLE_EMMC_BOOTMODE_8BITS, UNLOCK, 1)
	)

	payload = bytes()
	obj_num = 0

	if len(dgpk2_para) != 0 and len(pfid_para) != 0:
		ret = derive_object('DGPK2', dgpk2_para, LOCK, 16)
		if ret[0] == True:
			payload = payload + ret[1]
			obj_num = obj_num + 1

		ret = derive_object('PFID', pfid_para, LOCK, 16)
		if ret[0] == True:
			payload = payload + ret[1]
			obj_num = obj_num + 1

	for ele in obj_list:
		ret = derive_object(ele[0], ele[1], ele[2], ele[3])
		if ret[0] == True:
			payload = payload + ret[1]
			obj_num = obj_num + 1
	if len(payload) == 0:
		print('no payload derived')
		return

	pack_hdr = struct.pack('<I', PACK_MAGIC)
	pack_hdr = pack_hdr + struct.pack('<I', PACK_VERSION)
	pack_hdr = pack_hdr + struct.pack('<I', obj_num)
	pack_hdr = pack_hdr + struct.pack('<I', len(payload))
	pack_hdr = pack_hdr + 48 * b'\0'

	hdr_sha256 = SHA256.new()
	hdr_sha256.update(pack_hdr)
	pack_checker = hdr_sha256.digest()

	payload_sha256 = SHA256.new()
	payload_sha256.update(payload)
	pack_checker = pack_checker + payload_sha256.digest()

	if len(pfid_para) != 0:
		if os.path.isfile(pfid_para):
			f = open(pfid_para, 'rb')
			pfid = bytes.decode(binascii.b2a_hex(f.read()))
			f.close()
		else:
			pfid = pfid_para
		file_pack = args.out_dir + '/' + TARGET_NAME + '_PFID-' + pfid + '.bin'
	else:
		file_pack = args.out_dir + '/' + TARGET_NAME + '_' + time.strftime('%Y%02m%02d%02H%02M%02S', time.localtime()) + '.bin'
	f = open(file_pack, 'wb')
	f.write(pack_hdr + pack_checker + payload)
	f.close()

	global DERIVED_FILE_NUM
	DERIVED_FILE_NUM = DERIVED_FILE_NUM + 1
	print(os.path.abspath(file_pack) + ' derived successfully')

def main():
	import os
	import sys

	args = get_args()

	if not os.path.exists(args.out_dir):
		os.mkdir(args.out_dir)

	if len(args.DGPK2) == 0 and len(args.PFID) == 0:
		derive_pack(args, '', '')
	elif os.path.isfile(args.DGPK2) and os.path.isfile(args.PFID):
		derive_pack(args, args.DGPK2, args.PFID)
	elif os.path.isdir(args.DGPK2) and os.path.isdir(args.PFID):
		dgpk2_dir = os.listdir(args.DGPK2)
		pfid_dir = os.listdir(args.PFID)
		for file_dgpk2 in dgpk2_dir:
			idx = file_dgpk2[-13 : -4]
			for file_pfid in pfid_dir:
				if file_pfid.endswith(idx + '.bin'):
					path_dgpk2 = os.path.join(args.DGPK2, file_dgpk2)
					path_pfid = os.path.join(args.PFID, file_pfid)
					derive_pack(args, path_dgpk2, path_pfid)
					break
	elif len(args.DGPK2) == 32 and len(args.PFID) == 32:
	    derive_pack(args, args.DGPK2, args.PFID)
	else:
		print('Type of DGPK2 and PFID needs to be the same')
		sys.exit(1)

	print(str(DERIVED_FILE_NUM) + ' ' + TARGET_NAME + ' files derived successfully')

if __name__ == '__main__':
	main()
