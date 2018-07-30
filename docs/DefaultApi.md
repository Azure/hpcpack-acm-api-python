# hpc_acm.DefaultApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_clusrun_job**](DefaultApi.md#cancel_clusrun_job) | **PATCH** /clusrun/{id} | Cancel a clusrun
[**cancel_diagnostic_job**](DefaultApi.md#cancel_diagnostic_job) | **PATCH** /diagnostics/{id} | Cancel a diagnostic test run
[**create_clusrun_job**](DefaultApi.md#create_clusrun_job) | **POST** /clusrun | Create a clusrun
[**create_diagnostic_job**](DefaultApi.md#create_diagnostic_job) | **POST** /diagnostics | Create a diagnostic test run
[**get_clus_run_job_summary**](DefaultApi.md#get_clus_run_job_summary) | **GET** /dashboard/clusrun | Get summary of ClusRun jobs
[**get_clusrun_job**](DefaultApi.md#get_clusrun_job) | **GET** /clusrun/{id} | Get a clusrun
[**get_clusrun_job_aggregation_result**](DefaultApi.md#get_clusrun_job_aggregation_result) | **GET** /clusrun/{id}/aggregationResult | Get aggregation result of a clusrun job
[**get_clusrun_jobs**](DefaultApi.md#get_clusrun_jobs) | **GET** /clusrun | Get a list of clusruns
[**get_clusrun_output**](DefaultApi.md#get_clusrun_output) | **GET** /output/clusrun/{key}/raw | Get the whole output of a task
[**get_clusrun_output_in_page**](DefaultApi.md#get_clusrun_output_in_page) | **GET** /output/clusrun/{key}/page | Get partial output of a task
[**get_clusrun_task**](DefaultApi.md#get_clusrun_task) | **GET** /clusrun/{id}/tasks/{taskId} | Get a task of a clusrun
[**get_clusrun_task_result**](DefaultApi.md#get_clusrun_task_result) | **GET** /clusrun/{id}/tasks/{taskId}/result | Get a task result of a clusrun
[**get_clusrun_tasks**](DefaultApi.md#get_clusrun_tasks) | **GET** /clusrun/{id}/tasks | Get tasks of a clusrun
[**get_diagnostic_job**](DefaultApi.md#get_diagnostic_job) | **GET** /diagnostics/{id} | Get a diagnostic test run
[**get_diagnostic_job_aggregation_result**](DefaultApi.md#get_diagnostic_job_aggregation_result) | **GET** /diagnostics/{id}/aggregationResult | Get aggregation result of a diagnostic job
[**get_diagnostic_job_summary**](DefaultApi.md#get_diagnostic_job_summary) | **GET** /dashboard/diagnostics | Get summary of diagnostic jobs
[**get_diagnostic_jobs**](DefaultApi.md#get_diagnostic_jobs) | **GET** /diagnostics | Get a list of diagnostic test runs
[**get_diagnostic_task**](DefaultApi.md#get_diagnostic_task) | **GET** /diagnostics/{id}/tasks/{taskId} | Get a task of a diagnostic test run
[**get_diagnostic_task_result**](DefaultApi.md#get_diagnostic_task_result) | **GET** /diagnostics/{id}/tasks/{taskId}/result | Get a task result of a diagnostic test run
[**get_diagnostic_tasks**](DefaultApi.md#get_diagnostic_tasks) | **GET** /diagnostics/{id}/tasks | Get tasks of a diagnostic test run
[**get_diagnostic_tests**](DefaultApi.md#get_diagnostic_tests) | **GET** /diagnostics/tests | Get available diagnostic tests
[**get_metric_categories**](DefaultApi.md#get_metric_categories) | **GET** /metrics/categories | Get node metric categories
[**get_metrics_of_category**](DefaultApi.md#get_metrics_of_category) | **GET** /metrics/{category} | Get node merics in a category
[**get_node**](DefaultApi.md#get_node) | **GET** /nodes/{id} | Get a node
[**get_node_events**](DefaultApi.md#get_node_events) | **GET** /nodes/{id}/events | Get events of a node
[**get_node_jobs**](DefaultApi.md#get_node_jobs) | **GET** /nodes/{id}/jobs | Get jobs of a node
[**get_node_metadata**](DefaultApi.md#get_node_metadata) | **GET** /nodes/{id}/metadata | get metadata of a node
[**get_node_metric_history**](DefaultApi.md#get_node_metric_history) | **GET** /nodes/{id}/metricHistory | Get metric history of a node
[**get_node_scheduled_events**](DefaultApi.md#get_node_scheduled_events) | **GET** /nodes/{id}/scheduledEvents | get scheduled events of a node
[**get_node_summary**](DefaultApi.md#get_node_summary) | **GET** /dashboard/nodes | Get summary of nodes
[**get_nodes**](DefaultApi.md#get_nodes) | **GET** /nodes | Get a list of nodes


# **cancel_clusrun_job**
> cancel_clusrun_job(id, job=job)

Cancel a clusrun

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 56 # int | Job id
job = hpc_acm.JobUpdate() # JobUpdate |  (optional)

try:
    # Cancel a clusrun
    api_instance.cancel_clusrun_job(id, job=job)
except ApiException as e:
    print("Exception when calling DefaultApi->cancel_clusrun_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Job id | 
 **job** | [**JobUpdate**](JobUpdate.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_diagnostic_job**
> cancel_diagnostic_job(id, job=job)

Cancel a diagnostic test run

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 56 # int | Job id
job = hpc_acm.JobUpdate() # JobUpdate |  (optional)

try:
    # Cancel a diagnostic test run
    api_instance.cancel_diagnostic_job(id, job=job)
except ApiException as e:
    print("Exception when calling DefaultApi->cancel_diagnostic_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Job id | 
 **job** | [**JobUpdate**](JobUpdate.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_clusrun_job**
> Job create_clusrun_job(job=job)

Create a clusrun

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
job = hpc_acm.Job() # Job |  (optional)

try:
    # Create a clusrun
    api_response = api_instance.create_clusrun_job(job=job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_clusrun_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | [**Job**](Job.md)|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_diagnostic_job**
> Job create_diagnostic_job(job=job)

Create a diagnostic test run

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
job = hpc_acm.Job() # Job |  (optional)

try:
    # Create a diagnostic test run
    api_response = api_instance.create_diagnostic_job(job=job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_diagnostic_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | [**Job**](Job.md)|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clus_run_job_summary**
> JobSummary get_clus_run_job_summary()

Get summary of ClusRun jobs

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()

try:
    # Get summary of ClusRun jobs
    api_response = api_instance.get_clus_run_job_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_clus_run_job_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JobSummary**](JobSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusrun_job**
> Job get_clusrun_job(id)

Get a clusrun

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 56 # int | Job id

try:
    # Get a clusrun
    api_response = api_instance.get_clusrun_job(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_clusrun_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Job id | 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusrun_job_aggregation_result**
> object get_clusrun_job_aggregation_result(id)

Get aggregation result of a clusrun job

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 56 # int | Job id

try:
    # Get aggregation result of a clusrun job
    api_response = api_instance.get_clusrun_job_aggregation_result(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_clusrun_job_aggregation_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Job id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusrun_jobs**
> list[Job] get_clusrun_jobs(last_id=last_id, count=count, reverse=reverse)

Get a list of clusruns

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
last_id = 56 # int | The object id since which(but not included) the objects are requested (optional)
count = 1000 # int | Requested number of objects (optional) (default to 1000)
reverse = false # bool | Get the results in reverse order (optional) (default to false)

try:
    # Get a list of clusruns
    api_response = api_instance.get_clusrun_jobs(last_id=last_id, count=count, reverse=reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_clusrun_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_id** | **int**| The object id since which(but not included) the objects are requested | [optional] 
 **count** | **int**| Requested number of objects | [optional] [default to 1000]
 **reverse** | **bool**| Get the results in reverse order | [optional] [default to false]

### Return type

[**list[Job]**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusrun_output**
> file get_clusrun_output(key)

Get the whole output of a task

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
key = 'key_example' # str | Result key of a task

try:
    # Get the whole output of a task
    api_response = api_instance.get_clusrun_output(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_clusrun_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Result key of a task | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusrun_output_in_page**
> TaskOutput get_clusrun_output_in_page(key, offset=offset, page_size=page_size)

Get partial output of a task

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
key = 'key_example' # str | Result key of a task
offset = 56 # int | The distance from the beginning of the output (optional)
page_size = 56 # int | The size of requested piece of output (optional)

try:
    # Get partial output of a task
    api_response = api_instance.get_clusrun_output_in_page(key, offset=offset, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_clusrun_output_in_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Result key of a task | 
 **offset** | **int**| The distance from the beginning of the output | [optional] 
 **page_size** | **int**| The size of requested piece of output | [optional] 

### Return type

[**TaskOutput**](TaskOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusrun_task**
> Task get_clusrun_task(id, task_id)

Get a task of a clusrun

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 56 # int | Job id
task_id = 56 # int | Task id

try:
    # Get a task of a clusrun
    api_response = api_instance.get_clusrun_task(id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_clusrun_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Job id | 
 **task_id** | **int**| Task id | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusrun_task_result**
> TaskResult get_clusrun_task_result(id, task_id)

Get a task result of a clusrun

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 56 # int | Job id
task_id = 56 # int | Task id

try:
    # Get a task result of a clusrun
    api_response = api_instance.get_clusrun_task_result(id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_clusrun_task_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Job id | 
 **task_id** | **int**| Task id | 

### Return type

[**TaskResult**](TaskResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusrun_tasks**
> list[Task] get_clusrun_tasks(id, last_id=last_id, count=count, requeue_count=requeue_count)

Get tasks of a clusrun

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 56 # int | Job id
last_id = 56 # int | The object id since which(but not included) the objects are requested (optional)
count = 1000 # int | Requested number of objects (optional) (default to 1000)
requeue_count = 56 # int | The number of times a job/task is requeued (optional)

try:
    # Get tasks of a clusrun
    api_response = api_instance.get_clusrun_tasks(id, last_id=last_id, count=count, requeue_count=requeue_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_clusrun_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Job id | 
 **last_id** | **int**| The object id since which(but not included) the objects are requested | [optional] 
 **count** | **int**| Requested number of objects | [optional] [default to 1000]
 **requeue_count** | **int**| The number of times a job/task is requeued | [optional] 

### Return type

[**list[Task]**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagnostic_job**
> Job get_diagnostic_job(id)

Get a diagnostic test run

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 56 # int | Job id

try:
    # Get a diagnostic test run
    api_response = api_instance.get_diagnostic_job(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_diagnostic_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Job id | 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagnostic_job_aggregation_result**
> object get_diagnostic_job_aggregation_result(id)

Get aggregation result of a diagnostic job

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 56 # int | Job id

try:
    # Get aggregation result of a diagnostic job
    api_response = api_instance.get_diagnostic_job_aggregation_result(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_diagnostic_job_aggregation_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Job id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagnostic_job_summary**
> JobSummary get_diagnostic_job_summary()

Get summary of diagnostic jobs

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()

try:
    # Get summary of diagnostic jobs
    api_response = api_instance.get_diagnostic_job_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_diagnostic_job_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JobSummary**](JobSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagnostic_jobs**
> list[Job] get_diagnostic_jobs(last_id=last_id, count=count, reverse=reverse)

Get a list of diagnostic test runs

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
last_id = 56 # int | The object id since which(but not included) the objects are requested (optional)
count = 1000 # int | Requested number of objects (optional) (default to 1000)
reverse = false # bool | Get the results in reverse order (optional) (default to false)

try:
    # Get a list of diagnostic test runs
    api_response = api_instance.get_diagnostic_jobs(last_id=last_id, count=count, reverse=reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_diagnostic_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_id** | **int**| The object id since which(but not included) the objects are requested | [optional] 
 **count** | **int**| Requested number of objects | [optional] [default to 1000]
 **reverse** | **bool**| Get the results in reverse order | [optional] [default to false]

### Return type

[**list[Job]**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagnostic_task**
> Task get_diagnostic_task(id, task_id)

Get a task of a diagnostic test run

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 56 # int | Job id
task_id = 56 # int | Task id

try:
    # Get a task of a diagnostic test run
    api_response = api_instance.get_diagnostic_task(id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_diagnostic_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Job id | 
 **task_id** | **int**| Task id | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagnostic_task_result**
> TaskResult get_diagnostic_task_result(id, task_id)

Get a task result of a diagnostic test run

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 56 # int | Job id
task_id = 56 # int | Task id

try:
    # Get a task result of a diagnostic test run
    api_response = api_instance.get_diagnostic_task_result(id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_diagnostic_task_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Job id | 
 **task_id** | **int**| Task id | 

### Return type

[**TaskResult**](TaskResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagnostic_tasks**
> list[Task] get_diagnostic_tasks(id, last_id=last_id, count=count, requeue_count=requeue_count)

Get tasks of a diagnostic test run

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 56 # int | Job id
last_id = 56 # int | The object id since which(but not included) the objects are requested (optional)
count = 1000 # int | Requested number of objects (optional) (default to 1000)
requeue_count = 56 # int | The number of times a job/task is requeued (optional)

try:
    # Get tasks of a diagnostic test run
    api_response = api_instance.get_diagnostic_tasks(id, last_id=last_id, count=count, requeue_count=requeue_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_diagnostic_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Job id | 
 **last_id** | **int**| The object id since which(but not included) the objects are requested | [optional] 
 **count** | **int**| Requested number of objects | [optional] [default to 1000]
 **requeue_count** | **int**| The number of times a job/task is requeued | [optional] 

### Return type

[**list[Task]**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagnostic_tests**
> list[DiagnoticTest] get_diagnostic_tests()

Get available diagnostic tests

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()

try:
    # Get available diagnostic tests
    api_response = api_instance.get_diagnostic_tests()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_diagnostic_tests: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DiagnoticTest]**](DiagnoticTest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metric_categories**
> list[str] get_metric_categories()

Get node metric categories

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()

try:
    # Get node metric categories
    api_response = api_instance.get_metric_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_metric_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics_of_category**
> Metrics get_metrics_of_category(category, last_node_id=last_node_id, count=count)

Get node merics in a category

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
category = 'category_example' # str | 
last_node_id = 'last_node_id_example' # str |  (optional)
count = 1000 # int | Requested number of objects (optional) (default to 1000)

try:
    # Get node merics in a category
    api_response = api_instance.get_metrics_of_category(category, last_node_id=last_node_id, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_metrics_of_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | 
 **last_node_id** | **str**|  | [optional] 
 **count** | **int**| Requested number of objects | [optional] [default to 1000]

### Return type

[**Metrics**](Metrics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node**
> Node get_node(id)

Get a node

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 'id_example' # str | Node id

try:
    # Get a node
    api_response = api_instance.get_node(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Node id | 

### Return type

[**Node**](Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_events**
> list[Event] get_node_events(id)

Get events of a node

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 'id_example' # str | Node id

try:
    # Get events of a node
    api_response = api_instance.get_node_events(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_node_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Node id | 

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_jobs**
> list[NodeJob] get_node_jobs(id)

Get jobs of a node

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 'id_example' # str | Node id

try:
    # Get jobs of a node
    api_response = api_instance.get_node_jobs(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_node_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Node id | 

### Return type

[**list[NodeJob]**](NodeJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_metadata**
> NodeMetadata get_node_metadata(id)

get metadata of a node

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 'id_example' # str | Node id

try:
    # get metadata of a node
    api_response = api_instance.get_node_metadata(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_node_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Node id | 

### Return type

[**NodeMetadata**](NodeMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_metric_history**
> NodeMetrics get_node_metric_history(id)

Get metric history of a node

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 'id_example' # str | Node id

try:
    # Get metric history of a node
    api_response = api_instance.get_node_metric_history(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_node_metric_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Node id | 

### Return type

[**NodeMetrics**](NodeMetrics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_scheduled_events**
> ScheduledEvents get_node_scheduled_events(id)

get scheduled events of a node

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
id = 'id_example' # str | Node id

try:
    # get scheduled events of a node
    api_response = api_instance.get_node_scheduled_events(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_node_scheduled_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Node id | 

### Return type

[**ScheduledEvents**](ScheduledEvents.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_summary**
> NodeSummary get_node_summary()

Get summary of nodes

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()

try:
    # Get summary of nodes
    api_response = api_instance.get_node_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_node_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeSummary**](NodeSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes**
> list[Node] get_nodes(last_id=last_id, count=count)

Get a list of nodes

### Example
```python
from __future__ import print_function
import time
import hpc_acm
from hpc_acm.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hpc_acm.DefaultApi()
last_id = 56 # int | The object id since which(but not included) the objects are requested (optional)
count = 1000 # int | Requested number of objects (optional) (default to 1000)

try:
    # Get a list of nodes
    api_response = api_instance.get_nodes(last_id=last_id, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_id** | **int**| The object id since which(but not included) the objects are requested | [optional] 
 **count** | **int**| Requested number of objects | [optional] [default to 1000]

### Return type

[**list[Node]**](Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

