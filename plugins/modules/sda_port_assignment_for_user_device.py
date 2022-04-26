#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_port_assignment_for_user_device
short_description: Resource module for Sda Port Assignment For User Device
description:
- Manage operations create and delete of the resource Sda Port Assignment For User Device.
- Add Port assignment for user device in SDA Fabric.
- Delete Port assignment for user device in SDA Fabric.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  authenticateTemplateName:
    description: Authenticate TemplateName associated to siteNameHierarchy. Allowed
      values are 'Open Authentication', 'Closed Authentication', 'Low Impact', 'No Authentication',
      ''.
    type: str
    version_added: 4.0.0
  dataIpAddressPoolName:
    description: Ip Pool Name, that is assigned to virtual network with traffic type
      as DATA(can't be empty if voiceIpAddressPoolName is empty).
    type: str
    version_added: 4.0.0
  deviceManagementIpAddress:
    description: DeviceManagementIpAddress query parameter.
    type: str
  interfaceDescription:
    description: Details or note of interface assignment.
    type: str
    version_added: 4.0.0
  interfaceName:
    description: InterfaceName query parameter.
    type: str
  scalableGroupName:
    description: Valid name of a scalable group associated with virtual network(Scalable
      groups are only supported on No Auth profile because the other profiles assign
      SGTs from ISE).
    type: str
    version_added: 4.0.0
  siteNameHierarchy:
    description: Site Name Hierarchy should be a valid fabric site name hierarchy. E.g
      Global/USA/San Jose.
    type: str
    version_added: 4.0.0
  voiceIpAddressPoolName:
    description: Ip Pool Name, that is assigned to virtual network with traffic type
      as VOICE(can't be empty if dataIpAddressPoolName is emty).
    type: str
    version_added: 4.0.0
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
notes:
  - SDK Method used are
    sda.Sda.add_port_assignment_for_user_device,
    sda.Sda.delete_port_assignment_for_user_device,

  - Paths used are
    post /dna/intent/api/v1/business/sda/hostonboarding/user-device,
    delete /dna/intent/api/v1/business/sda/hostonboarding/user-device,

"""

EXAMPLES = r"""
- name: Delete all
  cisco.dnac.sda_port_assignment_for_user_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    deviceManagementIpAddress: string
    interfaceName: string

- name: Create
  cisco.dnac.sda_port_assignment_for_user_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    authenticateTemplateName: string
    dataIpAddressPoolName: string
    deviceManagementIpAddress: string
    interfaceDescription: string
    interfaceName: string
    scalableGroupName: string
    siteNameHierarchy: string
    voiceIpAddressPoolName: string

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
