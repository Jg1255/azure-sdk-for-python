# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AppliedScopeType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the Applied Scope.
    """

    SINGLE = "Single"
    SHARED = "Shared"

class CalculateExchangeOperationResultStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the operation.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    PENDING = "Pending"

class ErrorResponseCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    INTERNAL_SERVER_ERROR = "InternalServerError"
    SERVER_TIMEOUT = "ServerTimeout"
    AUTHORIZATION_FAILED = "AuthorizationFailed"
    BAD_REQUEST = "BadRequest"
    CLIENT_CERTIFICATE_THUMBPRINT_NOT_SET = "ClientCertificateThumbprintNotSet"
    INVALID_REQUEST_CONTENT = "InvalidRequestContent"
    OPERATION_FAILED = "OperationFailed"
    HTTP_METHOD_NOT_SUPPORTED = "HttpMethodNotSupported"
    INVALID_REQUEST_URI = "InvalidRequestUri"
    MISSING_TENANT_ID = "MissingTenantId"
    INVALID_TENANT_ID = "InvalidTenantId"
    INVALID_RESERVATION_ORDER_ID = "InvalidReservationOrderId"
    INVALID_RESERVATION_ID = "InvalidReservationId"
    RESERVATION_ID_NOT_IN_RESERVATION_ORDER = "ReservationIdNotInReservationOrder"
    RESERVATION_ORDER_NOT_FOUND = "ReservationOrderNotFound"
    INVALID_SUBSCRIPTION_ID = "InvalidSubscriptionId"
    INVALID_ACCESS_TOKEN = "InvalidAccessToken"
    INVALID_LOCATION_ID = "InvalidLocationId"
    UNAUTHENTICATED_REQUESTS_THROTTLED = "UnauthenticatedRequestsThrottled"
    INVALID_HEALTH_CHECK_TYPE = "InvalidHealthCheckType"
    FORBIDDEN = "Forbidden"
    BILLING_SCOPE_ID_CANNOT_BE_CHANGED = "BillingScopeIdCannotBeChanged"
    APPLIED_SCOPES_NOT_ASSOCIATED_WITH_COMMERCE_ACCOUNT = "AppliedScopesNotAssociatedWithCommerceAccount"
    PATCH_VALUES_SAME_AS_EXISTING = "PatchValuesSameAsExisting"
    ROLE_ASSIGNMENT_CREATION_FAILED = "RoleAssignmentCreationFailed"
    RESERVATION_ORDER_CREATION_FAILED = "ReservationOrderCreationFailed"
    RESERVATION_ORDER_NOT_ENABLED = "ReservationOrderNotEnabled"
    CAPACITY_UPDATE_SCOPES_FAILED = "CapacityUpdateScopesFailed"
    UNSUPPORTED_RESERVATION_TERM = "UnsupportedReservationTerm"
    RESERVATION_ORDER_ID_ALREADY_EXISTS = "ReservationOrderIdAlreadyExists"
    RISK_CHECK_FAILED = "RiskCheckFailed"
    CREATE_QUOTE_FAILED = "CreateQuoteFailed"
    ACTIVATE_QUOTE_FAILED = "ActivateQuoteFailed"
    NONSUPPORTED_ACCOUNT_ID = "NonsupportedAccountId"
    PAYMENT_INSTRUMENT_NOT_FOUND = "PaymentInstrumentNotFound"
    MISSING_APPLIED_SCOPES_FOR_SINGLE = "MissingAppliedScopesForSingle"
    NO_VALID_RESERVATIONS_TO_RE_RATE = "NoValidReservationsToReRate"
    RE_RATE_ONLY_ALLOWED_FOR_EA = "ReRateOnlyAllowedForEA"
    OPERATION_CANNOT_BE_PERFORMED_IN_CURRENT_STATE = "OperationCannotBePerformedInCurrentState"
    INVALID_SINGLE_APPLIED_SCOPES_COUNT = "InvalidSingleAppliedScopesCount"
    INVALID_FULFILLMENT_REQUEST_PARAMETERS = "InvalidFulfillmentRequestParameters"
    NOT_SUPPORTED_COUNTRY = "NotSupportedCountry"
    INVALID_REFUND_QUANTITY = "InvalidRefundQuantity"
    PURCHASE_ERROR = "PurchaseError"
    BILLING_CUSTOMER_INPUT_ERROR = "BillingCustomerInputError"
    BILLING_PAYMENT_INSTRUMENT_SOFT_ERROR = "BillingPaymentInstrumentSoftError"
    BILLING_PAYMENT_INSTRUMENT_HARD_ERROR = "BillingPaymentInstrumentHardError"
    BILLING_TRANSIENT_ERROR = "BillingTransientError"
    BILLING_ERROR = "BillingError"
    FULFILLMENT_CONFIGURATION_ERROR = "FulfillmentConfigurationError"
    FULFILLMENT_OUT_OF_STOCK_ERROR = "FulfillmentOutOfStockError"
    FULFILLMENT_TRANSIENT_ERROR = "FulfillmentTransientError"
    FULFILLMENT_ERROR = "FulfillmentError"
    CALCULATE_PRICE_FAILED = "CalculatePriceFailed"

class ExchangeOperationResultStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the operation.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    PENDING_REFUNDS = "PendingRefunds"
    PENDING_PURCHASES = "PendingPurchases"

class InstanceFlexibility(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Turning this on will apply the reservation discount to other VMs in the same VM size group.
    Only specify for VirtualMachines reserved resource type.
    """

    ON = "On"
    OFF = "Off"

class OperationStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the individual operation.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    PENDING = "Pending"

class PaymentStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Describes whether the payment is completed, failed, cancelled or scheduled in the future.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    SCHEDULED = "Scheduled"
    CANCELLED = "Cancelled"

class QuotaRequestState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The quota request status.
    """

    ACCEPTED = "Accepted"
    INVALID = "Invalid"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    IN_PROGRESS = "InProgress"

class ReservationBillingPlan(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Represent the billing plans.
    """

    UPFRONT = "Upfront"
    MONTHLY = "Monthly"

class ReservationStatusCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "None"
    PENDING = "Pending"
    ACTIVE = "Active"
    PURCHASE_ERROR = "PurchaseError"
    PAYMENT_INSTRUMENT_ERROR = "PaymentInstrumentError"
    SPLIT = "Split"
    MERGED = "Merged"
    EXPIRED = "Expired"
    SUCCEEDED = "Succeeded"

class ReservationTerm(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Represent the term of Reservation.
    """

    P1_Y = "P1Y"
    P3_Y = "P3Y"

class ReservedResourceType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the resource that is being reserved.
    """

    VIRTUAL_MACHINES = "VirtualMachines"
    SQL_DATABASES = "SqlDatabases"
    SUSE_LINUX = "SuseLinux"
    COSMOS_DB = "CosmosDb"
    RED_HAT = "RedHat"
    SQL_DATA_WAREHOUSE = "SqlDataWarehouse"
    V_MWARE_CLOUD_SIMPLE = "VMwareCloudSimple"
    RED_HAT_OSA = "RedHatOsa"
    DATABRICKS = "Databricks"
    APP_SERVICE = "AppService"
    MANAGED_DISK = "ManagedDisk"
    BLOCK_BLOB = "BlockBlob"
    REDIS_CACHE = "RedisCache"
    AZURE_DATA_EXPLORER = "AzureDataExplorer"
    MY_SQL = "MySql"
    MARIA_DB = "MariaDb"
    POSTGRE_SQL = "PostgreSql"
    DEDICATED_HOST = "DedicatedHost"
    SAP_HANA = "SapHana"
    SQL_AZURE_HYBRID_BENEFIT = "SqlAzureHybridBenefit"

class ResourceType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The resource types.
    """

    STANDARD = "standard"
    DEDICATED = "dedicated"
    LOW_PRIORITY = "lowPriority"
    SHARED = "shared"
    SERVICE_SPECIFIC = "serviceSpecific"
