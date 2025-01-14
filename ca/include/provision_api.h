/*
 * Copyright (C) 2014-2017 Amlogic, Inc. All rights reserved.
 *
 * All information contained herein is Amlogic confidential.
 *
 * This software is provided to you pursuant to Software License Agreement
 * (SLA) with Amlogic Inc ("Amlogic"). This software may be used
 * only in accordance with the terms of this agreement.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification is strictly prohibited without prior written permission from
 * Amlogic.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#ifndef _PROVISION_API_H_
#define _PROVISION_API_H_

#include "key_type_def.h"

// PFID: Provision Field ID
#define PROVISION_PFID_LENGTH                          (16)

// DAC: Device Authentication Code
#define PROVISION_DAC_LENGTH                           (32)

#define PROVISION_KEY_CHECKSUM_LENGTH                  (32)

#define TEE_STORAGE_PRIVATE_REE      0x80000000
#define TEE_STORAGE_PRIVATE_RPMB     0x80000100
#define TEE_STORAGE_PRIVATE_EFUSE    0xF0000000

#ifdef __cplusplus
extern "C" {
#endif
int32_t key_provision_store(
		uint8_t *name_buff,
		uint32_t name_size,
		uint8_t *key_buff,
		uint32_t key_size);

int32_t key_provision_query(
		uint8_t *name_buff,
		uint32_t name_size,
		uint32_t key_type,
		uint32_t *storage,
		uint32_t *key_size);

int32_t key_provision_query_v2(
		uint8_t *name_buff,
		uint32_t name_size,
		uint32_t key_type,
		uint8_t *uuid,
		uint32_t *storage,
		uint32_t *key_size);

int32_t key_provision_get_pfid(uint8_t *pfid, uint32_t *id_size);
int32_t key_provision_get_dac(uint8_t *dac, uint32_t *dac_size);
int32_t key_provision_get_dac_v2(const uint8_t *nonce, uint32_t nonce_size,
		uint8_t *dac, uint32_t *dac_size);

int32_t key_provision_checksum(uint32_t key_type, uint8_t *name_buff,
		uint32_t name_size, uint8_t *checksum);

int32_t key_provision_checksum_v2(uint32_t key_type, uint8_t *name_buff,
		uint32_t name_size, uint8_t *uuid, uint8_t *checksum);

int32_t key_provision_delete(uint32_t key_type, const uint8_t* uuid);

int32_t key_provision_calc_checksum(const uint8_t *keybox, uint32_t keybox_size,
		uint8_t checksum[PROVISION_KEY_CHECKSUM_LENGTH]);
#ifdef __cplusplus
}
#endif

#endif /* _PROVISION_API_H_ */
