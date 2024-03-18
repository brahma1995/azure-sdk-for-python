# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.cosmosdb import CosmosDBManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-cosmosdb
# USAGE
    python cosmos_db_sql_container_create_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CosmosDBManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.sql_resources.begin_create_update_sql_container(
        resource_group_name="rg1",
        account_name="ddb1",
        database_name="databaseName",
        container_name="containerName",
        create_update_sql_container_parameters={
            "location": "West US",
            "properties": {
                "options": {},
                "resource": {
                    "clientEncryptionPolicy": {
                        "includedPaths": [
                            {
                                "clientEncryptionKeyId": "keyId",
                                "encryptionAlgorithm": "AEAD_AES_256_CBC_HMAC_SHA256",
                                "encryptionType": "Deterministic",
                                "path": "/path",
                            }
                        ],
                        "policyFormatVersion": 2,
                    },
                    "computedProperties": [{"name": "cp_lowerName", "query": "SELECT VALUE LOWER(c.name) FROM c"}],
                    "conflictResolutionPolicy": {"conflictResolutionPath": "/path", "mode": "LastWriterWins"},
                    "defaultTtl": 100,
                    "id": "containerName",
                    "indexingPolicy": {
                        "automatic": True,
                        "excludedPaths": [],
                        "includedPaths": [
                            {
                                "indexes": [
                                    {"dataType": "String", "kind": "Range", "precision": -1},
                                    {"dataType": "Number", "kind": "Range", "precision": -1},
                                ],
                                "path": "/*",
                            }
                        ],
                        "indexingMode": "consistent",
                    },
                    "partitionKey": {"kind": "Hash", "paths": ["/AccountNumber"]},
                    "uniqueKeyPolicy": {"uniqueKeys": [{"paths": ["/testPath"]}]},
                },
            },
            "tags": {},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/cosmos-db/resource-manager/Microsoft.DocumentDB/preview/2024-02-15-preview/examples/CosmosDBSqlContainerCreateUpdate.json
if __name__ == "__main__":
    main()
