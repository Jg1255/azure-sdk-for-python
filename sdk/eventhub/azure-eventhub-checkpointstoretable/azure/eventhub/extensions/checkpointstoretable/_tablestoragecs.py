from typing import Sequence
from azure.data.tables import TableClient
from collections import defaultdict
from azure.eventhub.aio import CheckpointStore 
from azure.data.tables import TableServiceClient
from datetime import datetime
from azure.data.tables import UpdateMode
from azure.eventhub.aio import EventHubConsumerClient
from azure.core.exceptions import ResourceModifiedError, ResourceExistsError, ResourceNotFoundError 

class TableCheckpointStore:
    """A CheckpointStore that uses Azure Table Storage to store the partition ownership and checkpoint data.
    This class implements methods list_ownership, claim_ownership, update_checkpoint and list_checkpoints that are
    defined in class azure.eventhub.aio.CheckpointStore of package azure-eventhub.
    :param str table_account_url:
        The URI to the storage account.
    :param table_name:
        The name of the table for the tables.
    :type table_name: str
    :param credential:
        The credentials with which to authenticate. This is optional if the
        account URL already has a SAS token. The value can be a SAS token string, an account
        shared access key, or an instance of a TokenCredentials class from azure.identity.
        If the URL already has a SAS token, specifying an explicit credential will take priority.
    :keyword str api_version:
            The Storage API version to use for requests. Default value is '2019-07-07'.
    :keyword str secondary_hostname:
        The hostname of the secondary endpoint.
    """

    def __init__(self):
        pass

    def create_the_entity_checkpoint(self,eventhubname,namespace,consumergroup,partition_id,offset,sequencenumber):
        pass

    def create_the_entity_ownership(self,eventhubname,namespace,consumergroup,partition_id,owner_id,time):
        pass

    def list_ownership(self,eventhub,namespace,consumergroup):
        pass

    def list_checkpoints(self,eventhub,namespace,consumergroup):
        pass

    def update_checkpoint(self,checkpoint):
        pass

    def upload_ownership(self,ownership,metadata):
        pass


    def claim_one_partition(self,ownership):
        pass

    def claim_ownership(self,ownershiplist):
        pass
