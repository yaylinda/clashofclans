# coding: utf-8

"""
    Clash of Clans API

    Check out <a href=\"https://developer.clashofclans.com/#/getting-started\" target=\"_parent\">Getting Started</a> for instructions and links to other resources. Clash of Clans API uses <a href=\"https://jwt.io/\" target=\"_blank\">JSON Web Tokens</a> for authorizing the requests. Tokens are created by developers on <a href=\"https://developer.clashofclans.com/#/account\" target=\"_parent\">My Account</a> page and must be passed in every API request in Authorization HTTP header using Bearer authentication scheme. Correct Authorization header looks like this: \"Authorization: Bearer API_TOKEN\".   # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PlayersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_player(self, player_tag, **kwargs):  # noqa: E501
        """Get player information  # noqa: E501

        Get information about a single player by player tag. Player tags can be found either in game or by from clan member lists. Note that player tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example player tag '#2ABC' would become '%232ABC' in the URL.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player(player_tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str player_tag: Tag of the player. (required)
        :return: Player
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_player_with_http_info(player_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.get_player_with_http_info(player_tag, **kwargs)  # noqa: E501
            return data

    def get_player_with_http_info(self, player_tag, **kwargs):  # noqa: E501
        """Get player information  # noqa: E501

        Get information about a single player by player tag. Player tags can be found either in game or by from clan member lists. Note that player tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example player tag '#2ABC' would become '%232ABC' in the URL.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_with_http_info(player_tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str player_tag: Tag of the player. (required)
        :return: Player
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['player_tag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_player" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'player_tag' is set
        if ('player_tag' not in params or
                params['player_tag'] is None):
            raise ValueError("Missing the required parameter `player_tag` when calling `get_player`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'player_tag' in params:
            path_params['playerTag'] = params['player_tag']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/players/{playerTag}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Player',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def verify_token(self, body, player_tag, **kwargs):  # noqa: E501
        """Verify player API token that can be found from the game settings.  # noqa: E501

        Verify player API token that can be found from the game settings. This API call can be used to check that players own the game accounts they claim to own as they need to provide the one-time use API token that exists inside the game.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_token(body, player_tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VerifyTokenRequest body: Request body (required)
        :param str player_tag: Tag of the player. (required)
        :return: VerifyTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.verify_token_with_http_info(body, player_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.verify_token_with_http_info(body, player_tag, **kwargs)  # noqa: E501
            return data

    def verify_token_with_http_info(self, body, player_tag, **kwargs):  # noqa: E501
        """Verify player API token that can be found from the game settings.  # noqa: E501

        Verify player API token that can be found from the game settings. This API call can be used to check that players own the game accounts they claim to own as they need to provide the one-time use API token that exists inside the game.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_token_with_http_info(body, player_tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VerifyTokenRequest body: Request body (required)
        :param str player_tag: Tag of the player. (required)
        :return: VerifyTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'player_tag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method verify_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `verify_token`")  # noqa: E501
        # verify the required parameter 'player_tag' is set
        if ('player_tag' not in params or
                params['player_tag'] is None):
            raise ValueError("Missing the required parameter `player_tag` when calling `verify_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'player_tag' in params:
            path_params['playerTag'] = params['player_tag']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/players/{playerTag}/verifytoken', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VerifyTokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
