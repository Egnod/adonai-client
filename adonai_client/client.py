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
        self._username = username
        self._password = password

        self._auth_endpoint = urljoin(server_root_endpoint, auth_route)
        self._api_endpoint = urljoin(server_root_endpoint, api_route)

        self._token = self._get_auth_token()

        self._gql_endpoint = HTTPEndpoint(
            self._api_endpoint,
            base_headers={"Authorization": f"{token_prefix}{self._token}"},
        )

    def _get_auth_token(self):
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
        return Operation(schema.query_type)

    @property
    def mutation(self) -> schema.query_type:
        return Operation(schema.mutation_type)

    def execute(self, operation: Selection):
        return self._gql_endpoint(operation)

    def get_query(
        self, query_type: QueryType, query_name: str, exclude_fields: tuple = ()
    ):
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
