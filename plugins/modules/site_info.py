#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: site_info
short_description: Information module for Site
description:
- Get all Site.
- Get site using siteNameHierarchy/siteId/type ,return all sites if these parameters are not given as input.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  name:
    description:
    - Name query parameter. SiteNameHierarchy (ex global/groupName).
    type: str
  siteId:
    description:
    - SiteId query parameter. Site id to which site details to retrieve.
    type: str
  type:
    description:
    - Type query parameter. Type (ex area, building, floor).
    type: str
  offset:
    description:
    - Offset query parameter. Offset/starting row.
    type: str
  limit:
    description:
    - Limit query parameter. Number of sites to be retrieved.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
notes:
  - SDK Method used are
    sites.Sites.get_site,

  - Paths used are
    get /dna/intent/api/v1/site,

"""

EXAMPLES = r"""
- name: Get all Site
  cisco.dnac.site_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    name: string
    siteId: string
    type: string
    offset: string
    limit: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "parentId": "string",
        "name": "string",
        "additionalInfo": [
          {
            "nameSpace": "string",
            "attributes": {
              "country": "string",
              "address": "string",
              "latitude": "string",
              "addressInheritedFrom": "string",
              "type": "string",
              "longitude": "string",
              "offsetX": "string",
              "offsetY": "string",
              "length": "string",
              "width": "string",
              "height": "string",
              "rfModel": "string",
              "floorIndex": "string"
            }
          }
        ],
        "siteHierarchy": "string",
        "siteNameHierarchy": "string",
        "instanceTenantId": "string",
        "id": "string"
      }
    ]
"""
