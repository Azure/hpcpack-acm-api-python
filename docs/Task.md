# Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | task id | [optional] 
**job_id** | **int** | Id of the job the task belongs to | [optional] 
**job_type** | [**JobType**](JobType.md) | Type of the job the task belongs to | [optional] 
**state** | [**TaskState**](TaskState.md) | Task state | [optional] 
**command_line** | **str** | Available only when task&#39;s job type is ClusRun | [optional] 
**node** | **str** | The node on which the task runs | [optional] 
**parent_ids** | **list[int]** |  | [optional] 
**child_ids** | **list[int]** |  | [optional] 
**remaining_parent_ids** | **list[int]** |  | [optional] 
**customized_data** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


