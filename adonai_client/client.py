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

    def _get_auth_token(self) -> str:
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

    @property
    def query(self) -> schema.query_type:
        """        
        :return: operation based on query
        :rtype: schema.query_type
        """
        return Operation(schema.query_type)

    @property
    def mutation(self) -> schema.query_type:
        """
        :return: operation based on mutation
        :rtype: schema.query_type
        """
        return Operation(schema.mutation_type)

    def execute(self, operation: Selection):
        """
        :param operation: queyr or mutation operation
        :type operation: Selection
        :return: result of query
        """
        return self._gql_endpoint(operation)

    def get_query(
        self, query_type: QueryType, query_name: str, exclude_fields: tuple = ()
    ) -> Operation:
        """
        :param query_type: query or mutation
        :type query_type: QueryType
        :param query_name: query or mutation name
        :type query_name: str
        :param exclude_fields: excluded fields from final query, defaults to ()
        :type exclude_fields: tuple, optional
        :raises AdonaiClientException: unexpected query type
        :raises AdonaiClientException: unexpected query name
        :return: query
        :rtype: Operation
        """

        query = None

        if query_type == QueryType.query:
            query = self.query

        elif query_type == QueryType.mutation:
            query = self.mutation

        else:
            raise AdonaiClientException("Unexpected query type", str(query_type))

        query_selection = getattr(query, query_name, None)

        if query_selection is None:
            raise AdonaiClientException(
                f"Unexpected {str(query_type.value)} name", str(query_name)
            )

        query_selection = query_selection()

        for field in exclude_fields:
            query_selection.__fields__(**{field: False})

        return query
