# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import datetime
from typing import Union
import six
from azure.core.credentials import AzureKeyCredential
from azure.core.pipeline.policies import AzureKeyCredentialPolicy
from azure.core.pipeline.policies import HttpLoggingPolicy
from ._generated.models import (
    BatchRequest as _BatchRequest,
    SourceInput as _SourceInput,
    TargetInput as _TargetInput,
)
from ._models import DocumentTranslationInput

COGNITIVE_KEY_HEADER = "Ocp-Apim-Subscription-Key"
POLLING_INTERVAL = 1


def get_translation_input(args, kwargs, continuation_token):
    try:
        inputs = kwargs.pop("inputs", None)
        if not inputs:
            inputs = args[0]
        request = (
            DocumentTranslationInput._to_generated_list(  # pylint: disable=protected-access
                inputs
            )
            if not continuation_token
            else None
        )
    except (AttributeError, TypeError, IndexError):
        try:
            source_url = kwargs.pop("source_url", None)
            if not source_url:
                source_url = args[0]
            target_url = kwargs.pop("target_url", None)
            if not target_url:
                target_url = args[1]
            target_language_code = kwargs.pop("target_language_code", None)
            if not target_language_code:
                target_language_code = args[2]
            request = [
                _BatchRequest(
                    source=_SourceInput(source_url=source_url),
                    targets=[
                        _TargetInput(
                            target_url=target_url, language=target_language_code
                        )
                    ],
                )
            ]
        except (AttributeError, TypeError, IndexError):
            raise ValueError(
                "Pass 'inputs' for multiple inputs or 'source_url', 'target_url', "
                "and 'target_language_code' for a single input."
            )

    return request


def get_authentication_policy(credential):
    authentication_policy = None
    if credential is None:
        raise ValueError("Parameter 'credential' must not be None.")
    if isinstance(credential, AzureKeyCredential):
        authentication_policy = AzureKeyCredentialPolicy(
            name=COGNITIVE_KEY_HEADER, credential=credential
        )
    elif credential is not None and not hasattr(credential, "get_token"):
        raise TypeError(
            "Unsupported credential: {}. Use an instance of AzureKeyCredential "
            "or a token credential from azure.identity".format(type(credential))
        )

    return authentication_policy


def get_http_logging_policy(**kwargs):
    http_logging_policy = HttpLoggingPolicy(**kwargs)
    http_logging_policy.allowed_header_names.update(
        {
            "Operation-Location",
            "Content-Encoding",
            "Vary",
            "apim-request-id",
            "X-RequestId",
            "Set-Cookie",
            "X-Powered-By",
            "Strict-Transport-Security",
            "x-content-type-options",
        }
    )
    http_logging_policy.allowed_query_params.update(
        {
            "$top",
            "$skip",
            "$maxpagesize",
            "ids",
            "statuses",
            "createdDateTimeUtcStart",
            "createdDateTimeUtcEnd",
            "$orderBy",
        }
    )
    return http_logging_policy


def convert_datetime(date_time):
    # type: (Union[str, datetime.datetime]) -> datetime.datetime
    if isinstance(date_time, datetime.datetime):
        return date_time
    if isinstance(date_time, six.string_types):
        try:
            return datetime.datetime.strptime(date_time, "%Y-%m-%d")
        except ValueError:
            try:
                return datetime.datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%SZ")
            except ValueError:
                return datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
    raise TypeError("Bad datetime type")
