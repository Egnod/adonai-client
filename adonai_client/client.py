from http import HTTPStatus
from urllib.parse import urljoin

import httpx
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation, Selection

from .enum import QueryType
from .exception import AdonaiClientException
from .schema import schema


class AdonaiClient:
    def __init__(
        self,
        server_root_endpoint: str,
        username: str,
        password: str,
        auth_route: str = "/auth",
        api_route: str = "/",
        token_prefix: str = "JWT ",
    ):
        """
        :param server_root_endpoint: url to server, example http://localhost:5000
        :type server_root_endpoint: str

        :param username: user login name
        :type username: str

        :param password: user password
        :type password: str

        :param auth_route: auth route on server, defaults to "/auth"
        :type auth_route: str, optional

        :param api_route: api route on server, defaults to "/"
        :type api_route: str, optional

        :param token_prefix: bearer token prefix with space after, defaults to "JWT "
        :type token_prefix: str, optional
        """
    
        self._username = username
        self._password = password

        self._auth_endpoint = urljoin(server_root_endpoint, auth_route)
        self._api_endpoint = urljoin(server_root_endpoint, api_route)

        self._token = self._get_auth_token()

        self._gql_endpoint = HTTPEndpoint(
            self._api_endpoint,
            base_headers={"Authorization": f"{token_prefix}{self._token}"},
        )

    def _get_auth_token(self) -> None:
        """
        :raises AdonaiClientException: raises on server response status not OK (200)
        :return: JWT token by user auth data
        :rtype: str
        """
        
        response = httpx.post(
            self._auth_endpoint,
            json={"username": self._username, "password": self._password},
        )

        if response.status_code != HTTPStatus.OK:
            raise AdonaiClientException(
                f"Auth failed with code {response.status_code}", response.text
            )

        return response.json()["access_token"]

    def _refresh_token(self) -> None:
        self._token = self._get_auth_token()

    def query(self) -> schema.query_type:
        """        
        :return: operation based on query
        :rtype: schema.query_type
        """
        return Operation(schema.query_type)

    def mutation(self) -> schema.query_type:
        """
        :return: operation based on mutation
        :rtype: schema.query_type
        """
        return Operation(schema.mutation_type)

    
    def execute(self, operation: Selection, attempt: int = 0, interpret: bool = True):
        """
        :param operation: queyr or mutation operation
        :type operation: Selection
        :return: result of query
        """
        response = self._gql_endpoint(operation)

        if "errors" in response:
            if "token" in response["errors"][0]["message"] and attempt == 0:
                self._refresh_token()
                return self.execute(operation, attempt=attempt + 1)
            
            raise AdonaiClientException("Error on query execute", response["errors"])
        
        if interpret:
            return operation + response

        return response["data"]

    def fields(self, query_selection: Selection, **fields):
        return query_selection.__fields__(**fields)
