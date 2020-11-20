# coding: utf-8

"""
    Peptide Match OpenAPI 2.0

    This is PeptideMatch OpenAPI.

    OpenAPI spec version: 2.0.0
    Contact: chenc@udel.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class PeptideMatchAPI20Api(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def match_get_get(self, peptides, **kwargs):
        """
        Do peptide match using GET method.
        Retrieve UniProtKB protein sequences that would exactly match to the query peptides using GET method.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.match_get_get(peptides, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str peptides: A list of comma-separated peptide sequences (up to 100). Each sequence consists of 3 or more amino acids. (required)
        :param str taxonids: A list fo comma-separated NCBI taxonomy IDs.
        :param bool swissprot: Only search SwissProt protein sequences.
        :param bool isoform: Include isforms.
        :param bool uniref100: Only search UniRef100 protein sequences.
        :param bool leqi: Treat Leucine (L) and Isoleucine (I) equivalent.
        :param int offset: Off set, page starting point, with default value 0.
        :param int size: Page size with default value 100. When page size is -1, it returns all records and offset will be ignored.
        :return: Report
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.match_get_get_with_http_info(peptides, **kwargs)
        else:
            (data) = self.match_get_get_with_http_info(peptides, **kwargs)
            return data

    def match_get_get_with_http_info(self, peptides, **kwargs):
        """
        Do peptide match using GET method.
        Retrieve UniProtKB protein sequences that would exactly match to the query peptides using GET method.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.match_get_get_with_http_info(peptides, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str peptides: A list of comma-separated peptide sequences (up to 100). Each sequence consists of 3 or more amino acids. (required)
        :param str taxonids: A list fo comma-separated NCBI taxonomy IDs.
        :param bool swissprot: Only search SwissProt protein sequences.
        :param bool isoform: Include isforms.
        :param bool uniref100: Only search UniRef100 protein sequences.
        :param bool leqi: Treat Leucine (L) and Isoleucine (I) equivalent.
        :param int offset: Off set, page starting point, with default value 0.
        :param int size: Page size with default value 100. When page size is -1, it returns all records and offset will be ignored.
        :return: Report
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['peptides', 'taxonids', 'swissprot', 'isoform', 'uniref100', 'leqi', 'offset', 'size']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method match_get_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'peptides' is set
        if ('peptides' not in params) or (params['peptides'] is None):
            raise ValueError("Missing the required parameter `peptides` when calling `match_get_get`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'peptides' in params:
            query_params.append(('peptides', params['peptides']))
        if 'taxonids' in params:
            query_params.append(('taxonids', params['taxonids']))
        if 'swissprot' in params:
            query_params.append(('swissprot', params['swissprot']))
        if 'isoform' in params:
            query_params.append(('isoform', params['isoform']))
        if 'uniref100' in params:
            query_params.append(('uniref100', params['uniref100']))
        if 'leqi' in params:
            query_params.append(('leqi', params['leqi']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'size' in params:
            query_params.append(('size', params['size']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml', 'text/x-fasta', 'text/tab-separated-values'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/match_get', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Report',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def match_post_post(self, peptides, **kwargs):
        """
        Do peptide match using POST method.
        Retrieve UniProtKB protein sequences that would exactly match to the query peptides using POST method.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.match_post_post(peptides, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str peptides: A list of comma-separated peptide sequences (up to 100). Each sequence consists of 3 or more amino acids. (required)
        :param str taxonids: A list fo comma-separated NCBI taxonomy IDs.
        :param bool swissprot: Only search SwissProt protein sequences.
        :param bool isoform: Include isoforms.
        :param bool uniref100: Only search UniRef100 protein sequences.
        :param bool leqi: Treat Leucine (L) and Isoleucine (I) equivalent.
        :param int offset: Off set, page starting point, with default value 0.
        :param int size: Page size with default value 100. When page size is -1, it returns all records and offset will be ignored.
        :return: Report
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.match_post_post_with_http_info(peptides, **kwargs)
        else:
            (data) = self.match_post_post_with_http_info(peptides, **kwargs)
            return data

    def match_post_post_with_http_info(self, peptides, **kwargs):
        """
        Do peptide match using POST method.
        Retrieve UniProtKB protein sequences that would exactly match to the query peptides using POST method.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.match_post_post_with_http_info(peptides, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str peptides: A list of comma-separated peptide sequences (up to 100). Each sequence consists of 3 or more amino acids. (required)
        :param str taxonids: A list fo comma-separated NCBI taxonomy IDs.
        :param bool swissprot: Only search SwissProt protein sequences.
        :param bool isoform: Include isoforms.
        :param bool uniref100: Only search UniRef100 protein sequences.
        :param bool leqi: Treat Leucine (L) and Isoleucine (I) equivalent.
        :param int offset: Off set, page starting point, with default value 0.
        :param int size: Page size with default value 100. When page size is -1, it returns all records and offset will be ignored.
        :return: Report
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['peptides', 'taxonids', 'swissprot', 'isoform', 'uniref100', 'leqi', 'offset', 'size']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method match_post_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'peptides' is set
        if ('peptides' not in params) or (params['peptides'] is None):
            raise ValueError("Missing the required parameter `peptides` when calling `match_post_post`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'peptides' in params:
            form_params.append(('peptides', params['peptides']))
        if 'taxonids' in params:
            form_params.append(('taxonids', params['taxonids']))
        if 'swissprot' in params:
            form_params.append(('swissprot', params['swissprot']))
        if 'isoform' in params:
            form_params.append(('isoform', params['isoform']))
        if 'uniref100' in params:
            form_params.append(('uniref100', params['uniref100']))
        if 'leqi' in params:
            form_params.append(('leqi', params['leqi']))
        if 'offset' in params:
            form_params.append(('offset', params['offset']))
        if 'size' in params:
            form_params.append(('size', params['size']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml', 'text/x-fasta', 'text/tab-separated-values'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/match_post', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Report',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)