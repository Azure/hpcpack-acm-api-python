# coding: utf-8

"""
    HPC Web API

    Preview  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import hpc_acm
from hpc_acm.api.default_api import DefaultApi  # noqa: E501
from hpc_acm.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = hpc_acm.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_clusrun_job(self):
        """Test case for cancel_clusrun_job

        Cancel a clusrun  # noqa: E501
        """
        pass

    def test_cancel_diagnostic_job(self):
        """Test case for cancel_diagnostic_job

        Cancel a diagnostic test run  # noqa: E501
        """
        pass

    def test_create_clusrun_job(self):
        """Test case for create_clusrun_job

        Create a clusrun  # noqa: E501
        """
        pass

    def test_create_diagnostic_job(self):
        """Test case for create_diagnostic_job

        Create a diagnostic test run  # noqa: E501
        """
        pass

    def test_get_clus_run_job_summary(self):
        """Test case for get_clus_run_job_summary

        Get summary of ClusRun jobs  # noqa: E501
        """
        pass

    def test_get_clusrun_job(self):
        """Test case for get_clusrun_job

        Get a clusrun  # noqa: E501
        """
        pass

    def test_get_clusrun_job_aggregation_result(self):
        """Test case for get_clusrun_job_aggregation_result

        Get aggregation result of a clusrun job  # noqa: E501
        """
        pass

    def test_get_clusrun_jobs(self):
        """Test case for get_clusrun_jobs

        Get a list of clusruns  # noqa: E501
        """
        pass

    def test_get_clusrun_output(self):
        """Test case for get_clusrun_output

        Get the whole output of a task  # noqa: E501
        """
        pass

    def test_get_clusrun_output_in_page(self):
        """Test case for get_clusrun_output_in_page

        Get partial output of a task  # noqa: E501
        """
        pass

    def test_get_clusrun_task(self):
        """Test case for get_clusrun_task

        Get a task of a clusrun  # noqa: E501
        """
        pass

    def test_get_clusrun_task_result(self):
        """Test case for get_clusrun_task_result

        Get a task result of a clusrun  # noqa: E501
        """
        pass

    def test_get_clusrun_tasks(self):
        """Test case for get_clusrun_tasks

        Get tasks of a clusrun  # noqa: E501
        """
        pass

    def test_get_diagnostic_job(self):
        """Test case for get_diagnostic_job

        Get a diagnostic test run  # noqa: E501
        """
        pass

    def test_get_diagnostic_job_aggregation_result(self):
        """Test case for get_diagnostic_job_aggregation_result

        Get aggregation result of a diagnostic job  # noqa: E501
        """
        pass

    def test_get_diagnostic_job_summary(self):
        """Test case for get_diagnostic_job_summary

        Get summary of diagnostic jobs  # noqa: E501
        """
        pass

    def test_get_diagnostic_jobs(self):
        """Test case for get_diagnostic_jobs

        Get a list of diagnostic test runs  # noqa: E501
        """
        pass

    def test_get_diagnostic_task(self):
        """Test case for get_diagnostic_task

        Get a task of a diagnostic test run  # noqa: E501
        """
        pass

    def test_get_diagnostic_task_result(self):
        """Test case for get_diagnostic_task_result

        Get a task result of a diagnostic test run  # noqa: E501
        """
        pass

    def test_get_diagnostic_tasks(self):
        """Test case for get_diagnostic_tasks

        Get tasks of a diagnostic test run  # noqa: E501
        """
        pass

    def test_get_diagnostic_tests(self):
        """Test case for get_diagnostic_tests

        Get available diagnostic tests  # noqa: E501
        """
        pass

    def test_get_metric_categories(self):
        """Test case for get_metric_categories

        Get node metric categories  # noqa: E501
        """
        pass

    def test_get_metrics_of_category(self):
        """Test case for get_metrics_of_category

        Get node merics in a category  # noqa: E501
        """
        pass

    def test_get_node(self):
        """Test case for get_node

        Get a node  # noqa: E501
        """
        pass

    def test_get_node_events(self):
        """Test case for get_node_events

        Get events of a node  # noqa: E501
        """
        pass

    def test_get_node_jobs(self):
        """Test case for get_node_jobs

        Get jobs of a node  # noqa: E501
        """
        pass

    def test_get_node_metadata(self):
        """Test case for get_node_metadata

        get metadata of a node  # noqa: E501
        """
        pass

    def test_get_node_metric_history(self):
        """Test case for get_node_metric_history

        Get metric history of a node  # noqa: E501
        """
        pass

    def test_get_node_scheduled_events(self):
        """Test case for get_node_scheduled_events

        get scheduled events of a node  # noqa: E501
        """
        pass

    def test_get_node_summary(self):
        """Test case for get_node_summary

        Get summary of nodes  # noqa: E501
        """
        pass

    def test_get_nodes(self):
        """Test case for get_nodes

        Get a list of nodes  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
