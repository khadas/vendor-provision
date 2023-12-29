/*
 * Copyright (C) 2023 Amlogic, Inc. All rights reserved.
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

#ifndef _CIPLUS_KEYBOX_MAKER_H_
#define _CIPLUS_KEYBOX_MAKER_H_

#ifdef __cplusplus
extern "C" {
#endif

/* input:
       root_cert: root cert data
       root_cert_size: root cert data size
       brand_cert: brand cert data
       brand_cert_size: brand cert data size
       dev_cert: device cert data
       dev_key_size: device cert data size
       dev_key: device key data
       dev_key_size: device key data size
       type: 0 is not ecp; 1 is ecp
   output:
       keybox_buf: output keybox
       sha256_buf: output keybox's sha256
   input / output:
       keybox_size: input keybox buffer size(min value: root_cert_size + brand_cert_size + dev_cert_size + dev_key_size + 740) / output keybox size
       sha256_size: input sha256 buffer size(min value: 32) / output sha256 size

   return value: 0 means success, "> 0" means needed keybox buffer size, "< 0" means failed;
 */
int make_ciplus_keybox(
		const uint8_t *root_cert,
		uint32_t root_cert_size,
		const uint8_t *brand_cert,
		uint32_t brand_cert_size,
		const uint8_t *dev_cert,
		uint32_t dev_cert_size,
		const uint8_t *dev_key,
		uint32_t dev_key_size,
		uint32_t type,
		uint8_t *keybox_buf,
		uint32_t *keybox_size,
		uint8_t *sha256_buf,
		uint32_t *sha256_size
		);

/* input:
       data: data to set
       size: data size
   return value: 0 means success, "> 0" means needed data size, "< 0" means failed;
 */
int set_prng_seed(const uint8_t *data, uint32_t size);
int set_prng_key_k(const uint8_t *data, uint32_t size);
int set_dh_p(const uint8_t *data, uint32_t size);
int set_dh_g(const uint8_t *data, uint32_t size);
int set_dh_q(const uint8_t *data, uint32_t size);
int set_siv(const uint8_t *data, uint32_t size);
int set_slk(const uint8_t *data, uint32_t size);
int set_clk(const uint8_t *data, uint32_t size);

#ifdef __cplusplus
}
#endif

#endif /* _CIPLUS_KEYBOX_MAKER_H_ */
