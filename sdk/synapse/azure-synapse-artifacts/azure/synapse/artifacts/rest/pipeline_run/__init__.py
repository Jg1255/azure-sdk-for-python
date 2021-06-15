# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._request_builders_py3 import build_query_pipeline_runs_by_workspace_request
    from ._request_builders_py3 import build_get_pipeline_run_request
    from ._request_builders_py3 import build_query_activity_runs_request
    from ._request_builders_py3 import build_cancel_pipeline_run_request
except (SyntaxError, ImportError):
    from ._request_builders import build_query_pipeline_runs_by_workspace_request  # type: ignore
    from ._request_builders import build_get_pipeline_run_request  # type: ignore
    from ._request_builders import build_query_activity_runs_request  # type: ignore
    from ._request_builders import build_cancel_pipeline_run_request  # type: ignore

__all__ = [
    "build_query_pipeline_runs_by_workspace_request",
    "build_get_pipeline_run_request",
    "build_query_activity_runs_request",
    "build_cancel_pipeline_run_request",
]
