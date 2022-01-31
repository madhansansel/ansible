#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_site
short_description: Resource module for Sda Fabric Site
description:
- Manage operations create and delete of the resource Sda Fabric Site.
- Delete Site from SDA Fabric.
- Add Site in SDA Fabric.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  fabricName:
    version_added: "4.0.0"
    description: Fabric Name (should be existing fabric name).
    type: str
  siteNameHierarchy:
    description: SiteNameHierarchy query parameter. Site Name Hierarchy.
    type: str
requirements:
- dnacentersdk >= 2.4.4
- python >= 3.5
notes:
  - SDK Method used are
    sda.Sda.add_site
  - Paths used are delete /dna/intent/api/v1/business/sda/fabric-site,
    post /dna/intent/api/v1/business/sda/fabric-site
"""

EXAMPLES = r"""
- name: Delete all
  cisco.dnac.sda_fabric_site:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    siteNameHierarchy: string

- name: Create
  cisco.dnac.sda_fabric_site:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    fabricName: string
    siteNameHierarchy: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "description": "string",
      "taskId": "string",
      "taskStatusUrl": "string",
      "executionStatusUrl": "string",
      "executionId": "string"
    }
"""
