# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._request_builders_py3 import build_create_or_update_data_flow_request_initial
    from ._request_builders_py3 import build_get_data_flow_request
    from ._request_builders_py3 import build_delete_data_flow_request_initial
    from ._request_builders_py3 import build_rename_data_flow_request_initial
    from ._request_builders_py3 import build_get_data_flows_by_workspace_request
except (SyntaxError, ImportError):
    from ._request_builders import build_create_or_update_data_flow_request_initial  # type: ignore
    from ._request_builders import build_get_data_flow_request  # type: ignore
    from ._request_builders import build_delete_data_flow_request_initial  # type: ignore
    from ._request_builders import build_rename_data_flow_request_initial  # type: ignore
    from ._request_builders import build_get_data_flows_by_workspace_request  # type: ignore

__all__ = [
    "build_create_or_update_data_flow_request_initial",
    "build_get_data_flow_request",
    "build_delete_data_flow_request_initial",
    "build_rename_data_flow_request_initial",
    "build_get_data_flows_by_workspace_request",
]
