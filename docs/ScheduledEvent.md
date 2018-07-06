# ScheduledEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Globally unique identifier for this event | [optional] 
**event_type** | **str** | Impact this event causes | [optional] 
**resource_type** | **str** | Type of resource this event impacts | [optional] 
**resources** | **list[str]** | List of resources this event impacts. This is guaranteed to contain machines from at most one Update Domain, but may not contain all machines in the UD. | [optional] 
**event_status** | **str** | No Completed or similar status is ever provided; the event will no longer be returned when the event is completed. | [optional] 
**not_before** | **datetime** | Time after which this event may start | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


