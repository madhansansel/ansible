#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_device_role_info
short_description: Information module for Sda Device Role
description:
- Get all Sda Device Role.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceManagementIpAddress:
    description:
    - DeviceManagementIpAddress query parameter. Device Management IP Address.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Sda Device Role reference
  description: Complete reference of the Sda Device Role object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Sda Device Role
  cisco.dnac.sda_device_role_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    deviceManagementIpAddress: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "status": "string",
        "description": "string",
        "roles": [
          "string"
        ]
      },
      "version": "string"
    }
"""