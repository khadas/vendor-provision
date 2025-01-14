/*
 * Copyright (C) 2023 Amlogic, Inc. All rights reserved.
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

#ifndef _KEY_TYPE_DEF_H_
#define _KEY_TYPE_DEF_H_

/* Provision Key Type Definition */
#define PROVISION_KEY_TYPE_WIDEVINE                             0x11
#define PROVISION_KEY_TYPE_WIDEVINE_RENEW                       0x12
#define PROVISION_KEY_TYPE_WIDEVINE_ATSC_PRIVATE_CERT           0x13
#define PROVISION_KEY_TYPE_PLAYREADY_PRIVATE                    0x21
#define PROVISION_KEY_TYPE_PLAYREADY_PUBLIC                     0x22
#define PROVISION_KEY_TYPE_HDCP_TX14                            0x31
#define PROVISION_KEY_TYPE_HDCP_TX22                            0x32
#define PROVISION_KEY_TYPE_HDCP_RX14                            0x33
#define PROVISION_KEY_TYPE_HDCP_RX22_WFD                        0x34
#define PROVISION_KEY_TYPE_HDCP_RX22_FW                         0x35
#define PROVISION_KEY_TYPE_HDCP_RX22_FW_PRIVATE                 0x36
#define PROVISION_KEY_TYPE_KEYMASTER                            0x41
#define PROVISION_KEY_TYPE_KEYMASTER_3                          0x42
#define PROVISION_KEY_TYPE_KEYMASTER_3_ATTEST_DEV_ID_BOX        0x43
#define PROVISION_KEY_TYPE_EFUSE                                0x51
#define PROVISION_KEY_TYPE_CIPLUS                               0x61
#define PROVISION_KEY_TYPE_CIPLUS_ECP                           0x62
#define PROVISION_KEY_TYPE_NAGRA_DEV_UUID                       0x71
#define PROVISION_KEY_TYPE_NAGRA_DEV_SECRET                     0x72
#define PROVISION_KEY_TYPE_PFID                                 0x81
#define PROVISION_KEY_TYPE_PFPK                                 0x82
#define PROVISION_KEY_TYPE_YOUTUBE_SECRET                       0x91
#define PROVISION_KEY_TYPE_NETFLIX_ESN                          0xA1
#define PROVISION_KEY_TYPE_NETFLIX_MGKID                        0xA2
#define PROVISION_KEY_TYPE_WIDEVINE_CAS                         0xB1
#define PROVISION_KEY_TYPE_DOLBY_ID                             0xC1
#define PROVISION_KEY_TYPE_DLB_CID_HEADER                       0xC2
#define PROVISION_KEY_TYPE_SESG_LIC_0                           0xD0
#define PROVISION_KEY_TYPE_SESG_LIC_1                           0xD1
#define PROVISION_KEY_TYPE_SESG_LIC_2                           0xD2
#define PROVISION_KEY_TYPE_SESG_LIC_3                           0xD3
#define PROVISION_KEY_TYPE_SESG_LIC_4                           0xD4
#define PROVISION_KEY_TYPE_SESG_LIC_5                           0xD5
#define PROVISION_KEY_TYPE_SESG_LIC_6                           0xD6
#define PROVISION_KEY_TYPE_SESG_LIC_7                           0xD7
#define PROVISION_KEY_TYPE_SESG_LIC_8                           0xD8
#define PROVISION_KEY_TYPE_SESG_LIC_9                           0xD9
#define PROVISION_KEY_TYPE_SESG_LIC_A                           0xDA
#define PROVISION_KEY_TYPE_SESG_LIC_B                           0xDB
#define PROVISION_KEY_TYPE_FVP_SIGN                             0xE1
#define PROVISION_KEY_TYPE_FVP_DEVICE                           0xE2
#define PROVISION_KEY_TYPE_AIRPLAY_FAIRPLAY_OBJECT              0xF1
#define PROVISION_KEY_TYPE_AIRPLAY_MFI_BASE_KEY                 0xF2
#define PROVISION_KEY_TYPE_AIRPLAY_MFI_OBJECT                   0xF3
#define PROVISION_KEY_TYPE_CUSTOMER_DEF_MIN                     0x1001
#define PROVISION_KEY_TYPE_INVALID                              0xFFFFFFFF

#endif /* _KEY_TYPE_DEF_H_ */
