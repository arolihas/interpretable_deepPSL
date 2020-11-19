# coding: utf-8

"""
    Peptide Match OpenAPI 2.0

    This is PeptideMatch OpenAPI.

    OpenAPI spec version: 2.0.0
    Contact: chenc@udel.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Report(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'number_found': 'int',
        'qtime': 'int',
        'status': 'int',
        'search_parameters': 'ReportSearchParameters',
        'results': 'list[ReportResults]'
    }

    attribute_map = {
        'number_found': 'numberFound',
        'qtime': 'qtime',
        'status': 'status',
        'search_parameters': 'searchParameters',
        'results': 'results'
    }

    def __init__(self, number_found=None, qtime=None, status=None, search_parameters=None, results=None):
        """
        Report - a model defined in Swagger
        """

        self._number_found = None
        self._qtime = None
        self._status = None
        self._search_parameters = None
        self._results = None

        if number_found is not None:
          self.number_found = number_found
        if qtime is not None:
          self.qtime = qtime
        if status is not None:
          self.status = status
        if search_parameters is not None:
          self.search_parameters = search_parameters
        if results is not None:
          self.results = results

    @property
    def number_found(self):
        """
        Gets the number_found of this Report.
        Number of documents found.

        :return: The number_found of this Report.
        :rtype: int
        """
        return self._number_found

    @number_found.setter
    def number_found(self, number_found):
        """
        Sets the number_found of this Report.
        Number of documents found.

        :param number_found: The number_found of this Report.
        :type: int
        """

        self._number_found = number_found

    @property
    def qtime(self):
        """
        Gets the qtime of this Report.
        Query response time in milliseocnds.

        :return: The qtime of this Report.
        :rtype: int
        """
        return self._qtime

    @qtime.setter
    def qtime(self, qtime):
        """
        Sets the qtime of this Report.
        Query response time in milliseocnds.

        :param qtime: The qtime of this Report.
        :type: int
        """

        self._qtime = qtime

    @property
    def status(self):
        """
        Gets the status of this Report.
        Query response status.

        :return: The status of this Report.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Report.
        Query response status.

        :param status: The status of this Report.
        :type: int
        """

        self._status = status

    @property
    def search_parameters(self):
        """
        Gets the search_parameters of this Report.

        :return: The search_parameters of this Report.
        :rtype: ReportSearchParameters
        """
        return self._search_parameters

    @search_parameters.setter
    def search_parameters(self, search_parameters):
        """
        Sets the search_parameters of this Report.

        :param search_parameters: The search_parameters of this Report.
        :type: ReportSearchParameters
        """

        self._search_parameters = search_parameters

    @property
    def results(self):
        """
        Gets the results of this Report.

        :return: The results of this Report.
        :rtype: list[ReportResults]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this Report.

        :param results: The results of this Report.
        :type: list[ReportResults]
        """

        self._results = results

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Report):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
