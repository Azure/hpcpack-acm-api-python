# Job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**JobType**](JobType.md) |  | [optional] 
**id** | **int** | job id | [optional] 
**name** | **str** | job name give by user | [optional] 
**command_line** | **str** | Available only for ClusRun job | [optional] 
**diagnostic_test** | [**DiagnoticTest**](DiagnoticTest.md) | Available only for Diagnostics job | [optional] 
**state** | [**JobState**](JobState.md) |  | [optional] 
**target_nodes** | **list[str]** | Nodes on which the job runs | [optional] 
**progress** | **float** | Job progress | [optional] 
**requeue_count** | **int** | The number of times the job is requeued | [optional] 
**fail_job_on_task_failure** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


