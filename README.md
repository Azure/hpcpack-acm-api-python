# HPC Pack ACM API for Python

## Requirements.

Python 2.7, 3.5 or 3.6.

## Installation & Usage

```sh
python -m pip install --user hpc-acm
```

Then import the package:
```python
import hpc_acm
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# Set your API Base Point
hpc_acm.configuration.host = 'https://YOUR_SERVER_NAME/YOUR_PATH'
# Configure HTTP basic authorization: basic_auth
hpc_acm.configuration.username = 'YOUR_USERNAME'
hpc_acm.configuration.password = 'YOUR_PASSWORD'
# create an instance of the API class
api_instance = hpc_acm.DefaultApi()

try:
    # Get a list of nodes
    nodes = api_instance.get_nodes()
except ApiException as e:
    print(e)
else:
    for node in nodes:
        print(node)

```

## Documentation for API Endpoints

All URIs are relative to API Base Point, which is be set by `host` in configuration as shown above.

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**cancel_clusrun_job**](docs/DefaultApi.md#cancel_clusrun_job) | **PATCH** /clusrun/{id} | Cancel a clusrun
*DefaultApi* | [**cancel_diagnostic_job**](docs/DefaultApi.md#cancel_diagnostic_job) | **PATCH** /diagnostics/{id} | Cancel a diagnostic test run
*DefaultApi* | [**create_clusrun_job**](docs/DefaultApi.md#create_clusrun_job) | **POST** /clusrun | Create a clusrun
*DefaultApi* | [**create_diagnostic_job**](docs/DefaultApi.md#create_diagnostic_job) | **POST** /diagnostics | Create a diagnostic test run
*DefaultApi* | [**get_clus_run_job_summary**](docs/DefaultApi.md#get_clus_run_job_summary) | **GET** /dashboard/clusrun | Get summary of ClusRun jobs
*DefaultApi* | [**get_clusrun_job**](docs/DefaultApi.md#get_clusrun_job) | **GET** /clusrun/{id} | Get a clusrun
*DefaultApi* | [**get_clusrun_job_aggregation_result**](docs/DefaultApi.md#get_clusrun_job_aggregation_result) | **GET** /clusrun/{id}/aggregationResult | Get aggregation result of a clusrun job
*DefaultApi* | [**get_clusrun_jobs**](docs/DefaultApi.md#get_clusrun_jobs) | **GET** /clusrun | Get a list of clusruns
*DefaultApi* | [**get_clusrun_output**](docs/DefaultApi.md#get_clusrun_output) | **GET** /output/clusrun/{key}/raw | Get the whole output of a task
*DefaultApi* | [**get_clusrun_output_in_page**](docs/DefaultApi.md#get_clusrun_output_in_page) | **GET** /output/clusrun/{key}/page | Get partial output of a task
*DefaultApi* | [**get_clusrun_task**](docs/DefaultApi.md#get_clusrun_task) | **GET** /clusrun/{id}/tasks/{taskId} | Get a task of a clusrun
*DefaultApi* | [**get_clusrun_task_result**](docs/DefaultApi.md#get_clusrun_task_result) | **GET** /clusrun/{id}/tasks/{taskId}/result | Get a task result of a clusrun
*DefaultApi* | [**get_clusrun_tasks**](docs/DefaultApi.md#get_clusrun_tasks) | **GET** /clusrun/{id}/tasks | Get tasks of a clusrun
*DefaultApi* | [**get_diagnostic_job**](docs/DefaultApi.md#get_diagnostic_job) | **GET** /diagnostics/{id} | Get a diagnostic test run
*DefaultApi* | [**get_diagnostic_job_aggregation_result**](docs/DefaultApi.md#get_diagnostic_job_aggregation_result) | **GET** /diagnostics/{id}/aggregationResult | Get aggregation result of a diagnostic job
*DefaultApi* | [**get_diagnostic_job_summary**](docs/DefaultApi.md#get_diagnostic_job_summary) | **GET** /dashboard/diagnostics | Get summary of diagnostic jobs
*DefaultApi* | [**get_diagnostic_jobs**](docs/DefaultApi.md#get_diagnostic_jobs) | **GET** /diagnostics | Get a list of diagnostic test runs
*DefaultApi* | [**get_diagnostic_task**](docs/DefaultApi.md#get_diagnostic_task) | **GET** /diagnostics/{id}/tasks/{taskId} | Get a task of a diagnostic test run
*DefaultApi* | [**get_diagnostic_task_result**](docs/DefaultApi.md#get_diagnostic_task_result) | **GET** /diagnostics/{id}/tasks/{taskId}/result | Get a task result of a diagnostic test run
*DefaultApi* | [**get_diagnostic_tasks**](docs/DefaultApi.md#get_diagnostic_tasks) | **GET** /diagnostics/{id}/tasks | Get tasks of a diagnostic test run
*DefaultApi* | [**get_diagnostic_tests**](docs/DefaultApi.md#get_diagnostic_tests) | **GET** /diagnostics/tests | Get available diagnostic tests
*DefaultApi* | [**get_metric_categories**](docs/DefaultApi.md#get_metric_categories) | **GET** /metrics/categories | Get node metric categories
*DefaultApi* | [**get_metrics_of_category**](docs/DefaultApi.md#get_metrics_of_category) | **GET** /metrics/{category} | Get node merics in a category
*DefaultApi* | [**get_node**](docs/DefaultApi.md#get_node) | **GET** /nodes/{id} | Get a node
*DefaultApi* | [**get_node_events**](docs/DefaultApi.md#get_node_events) | **GET** /nodes/{id}/events | Get events of a node
*DefaultApi* | [**get_node_jobs**](docs/DefaultApi.md#get_node_jobs) | **GET** /nodes/{id}/jobs | Get jobs of a node
*DefaultApi* | [**get_node_metadata**](docs/DefaultApi.md#get_node_metadata) | **GET** /nodes/{id}/metadata | get metadata of a node
*DefaultApi* | [**get_node_metric_history**](docs/DefaultApi.md#get_node_metric_history) | **GET** /nodes/{id}/metricHistory | Get metric history of a node
*DefaultApi* | [**get_node_scheduled_events**](docs/DefaultApi.md#get_node_scheduled_events) | **GET** /nodes/{id}/scheduledEvents | get scheduled events of a node
*DefaultApi* | [**get_node_summary**](docs/DefaultApi.md#get_node_summary) | **GET** /dashboard/nodes | Get summary of nodes
*DefaultApi* | [**get_nodes**](docs/DefaultApi.md#get_nodes) | **GET** /nodes | Get a list of nodes


## Documentation For Models

 - [DiagnoticTest](docs/DiagnoticTest.md)
 - [Event](docs/Event.md)
 - [IpV4](docs/IpV4.md)
 - [IpV6](docs/IpV6.md)
 - [Job](docs/Job.md)
 - [JobState](docs/JobState.md)
 - [JobSummary](docs/JobSummary.md)
 - [JobType](docs/JobType.md)
 - [JobUpdate](docs/JobUpdate.md)
 - [MacAddress](docs/MacAddress.md)
 - [Metrics](docs/Metrics.md)
 - [MetricsValues](docs/MetricsValues.md)
 - [Node](docs/Node.md)
 - [NodeGpu](docs/NodeGpu.md)
 - [NodeJob](docs/NodeJob.md)
 - [NodeMetadata](docs/NodeMetadata.md)
 - [NodeMetadataCompute](docs/NodeMetadataCompute.md)
 - [NodeMetadataNetwork](docs/NodeMetadataNetwork.md)
 - [NodeMetadataNetworkInterface](docs/NodeMetadataNetworkInterface.md)
 - [NodeMetadataNetworkIpv4](docs/NodeMetadataNetworkIpv4.md)
 - [NodeMetadataNetworkIpv4IpAddress](docs/NodeMetadataNetworkIpv4IpAddress.md)
 - [NodeMetadataNetworkIpv4Subnet](docs/NodeMetadataNetworkIpv4Subnet.md)
 - [NodeMetadataNetworkIpv6](docs/NodeMetadataNetworkIpv6.md)
 - [NodeMetrics](docs/NodeMetrics.md)
 - [NodeMetricsData](docs/NodeMetricsData.md)
 - [NodeMetricsMetricItems](docs/NodeMetricsMetricItems.md)
 - [NodeNetwork](docs/NodeNetwork.md)
 - [NodeRegistration](docs/NodeRegistration.md)
 - [NodeSummary](docs/NodeSummary.md)
 - [ScheduledEvent](docs/ScheduledEvent.md)
 - [ScheduledEvents](docs/ScheduledEvents.md)
 - [Task](docs/Task.md)
 - [TaskOutput](docs/TaskOutput.md)
 - [TaskResult](docs/TaskResult.md)
 - [TaskState](docs/TaskState.md)


## Documentation For Authorization


## basic_auth

- **Type**: HTTP basic authentication

