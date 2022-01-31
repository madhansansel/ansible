#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: path_trace
short_description: Resource module for Path Trace
description:
- Manage operations create and delete of the resource Path Trace.
- Initiates a new flow analysis with periodic refresh and stat collection options. Returns a request id and a task id to get results and follow progress.
- Deletes a flow analysis request by its id.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  controlPath:
    description: ControlPath flag.
    type: bool
  destIP:
    description: Path Trace's destIP.
    type: str
  destPort:
    description: Path Trace's destPort.
    type: str
  flowAnalysisId:
    description: FlowAnalysisId path parameter. Flow analysis request id.
    type: str
  inclusions:
    description: Path Trace's inclusions.
    elements: str
    type: list
  periodicRefresh:
    description: PeriodicRefresh flag.
    type: bool
  protocol:
    description: Path Trace's protocol.
    type: str
  sourceIP:
    description: Path Trace's sourceIP.
    type: str
  sourcePort:
    description: Path Trace's sourcePort.
    type: str
requirements:
- dnacentersdk >= 2.4.4
- python >= 3.5
notes:
  - SDK Method used are
    path_trace.PathTrace.initiate_a_new_pathtrace,
    path_trace.PathTrace.deletes_pathtrace_by_id
  - Paths used are post /dna/intent/api/v1/flow-analysis,
    delete /dna/intent/api/v1/flow-analysis/{flowAnalysisId}
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.path_trace:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    controlPath: true
    destIP: string
    destPort: string
    inclusions:
    - string
    periodicRefresh: true
    protocol: string
    sourceIP: string
    sourcePort: string

- name: Delete by id
  cisco.dnac.path_trace:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    flowAnalysisId: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "flowAnalysisId": "string",
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
