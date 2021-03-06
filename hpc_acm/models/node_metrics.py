# coding: utf-8

"""
    HPC Web API

    Preview  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from hpc_acm.models.node_metrics_data import NodeMetricsData  # noqa: F401,E501


class NodeMetrics(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'range_seconds': 'float',
        'data': 'list[NodeMetricsData]'
    }

    attribute_map = {
        'range_seconds': 'rangeSeconds',
        'data': 'data'
    }

    def __init__(self, range_seconds=None, data=None):  # noqa: E501
        """NodeMetrics - a model defined in Swagger"""  # noqa: E501

        self._range_seconds = None
        self._data = None
        self.discriminator = None

        if range_seconds is not None:
            self.range_seconds = range_seconds
        if data is not None:
            self.data = data

    @property
    def range_seconds(self):
        """Gets the range_seconds of this NodeMetrics.  # noqa: E501

        Time span in second of the metric data  # noqa: E501

        :return: The range_seconds of this NodeMetrics.  # noqa: E501
        :rtype: float
        """
        return self._range_seconds

    @range_seconds.setter
    def range_seconds(self, range_seconds):
        """Sets the range_seconds of this NodeMetrics.

        Time span in second of the metric data  # noqa: E501

        :param range_seconds: The range_seconds of this NodeMetrics.  # noqa: E501
        :type: float
        """

        self._range_seconds = range_seconds

    @property
    def data(self):
        """Gets the data of this NodeMetrics.  # noqa: E501


        :return: The data of this NodeMetrics.  # noqa: E501
        :rtype: list[NodeMetricsData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this NodeMetrics.


        :param data: The data of this NodeMetrics.  # noqa: E501
        :type: list[NodeMetricsData]
        """

        self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodeMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
