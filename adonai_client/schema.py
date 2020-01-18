import sgqlc.types
import sgqlc.types.datetime

schema = sgqlc.types.Schema()


########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

DateTime = sgqlc.types.datetime.DateTime

ID = sgqlc.types.ID

Int = sgqlc.types.Int


class PermissionType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("INTERNAL", "ACTION", "OBJECT")


String = sgqlc.types.String


########################################################################
# Input Objects
########################################################################

########################################################################
# Output Objects and Interfaces
########################################################################
class CreateDomain(sgqlc.types.Type):
    __schema__ = schema
    domain = sgqlc.types.Field("Domain", graphql_name="domain")


class CreatePermission(sgqlc.types.Type):
    __schema__ = schema
    permission = sgqlc.types.Field("Permission", graphql_name="permission")


class CreateProject(sgqlc.types.Type):
    __schema__ = schema
    project = sgqlc.types.Field("Project", graphql_name="project")


class CreateUser(sgqlc.types.Type):
    __schema__ = schema
    user = sgqlc.types.Field("User", graphql_name="user")


class CreateUserGroup(sgqlc.types.Type):
    __schema__ = schema
    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")


class DelegatePermissionGroup(sgqlc.types.Type):
    __schema__ = schema
    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")


class DelegatePermissionUser(sgqlc.types.Type):
    __schema__ = schema
    user = sgqlc.types.Field("User", graphql_name="user")


class DelegateUserGroup(sgqlc.types.Type):
    __schema__ = schema
    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")


class DemotePermissionGroup(sgqlc.types.Type):
    __schema__ = schema
    deleted = sgqlc.types.Field(Boolean, graphql_name="deleted")


class DemotePermissionUser(sgqlc.types.Type):
    __schema__ = schema
    deleted = sgqlc.types.Field(Boolean, graphql_name="deleted")


class DemoteUserGroup(sgqlc.types.Type):
    __schema__ = schema
    deleted = sgqlc.types.Field(Boolean, graphql_name="deleted")


class Domain(sgqlc.types.Type):
    __schema__ = schema
    created_at = sgqlc.types.Field(DateTime, graphql_name="createdAt")
    updated_at = sgqlc.types.Field(DateTime, graphql_name="updatedAt")
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="uuid")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    description = sgqlc.types.Field(String, graphql_name="description")
    is_active = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="isActive"
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    projects = sgqlc.types.Field(
        sgqlc.types.list_of("Project"), graphql_name="projects"
    )
    users = sgqlc.types.Field(sgqlc.types.list_of("User"), graphql_name="users")
    groups = sgqlc.types.Field(sgqlc.types.list_of("UserGroup"), graphql_name="groups")


class Mutation(sgqlc.types.Type):
    __schema__ = schema
    create_permission = sgqlc.types.Field(
        CreatePermission,
        graphql_name="createPermission",
        args=sgqlc.types.ArgDict(
            (
                (
                    "description",
                    sgqlc.types.Arg(String, graphql_name="description", default=None),
                ),
                (
                    "name",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="name", default=None
                    ),
                ),
                (
                    "project_id",
                    sgqlc.types.Arg(ID, graphql_name="projectId", default=None),
                ),
                (
                    "type",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="type", default=None
                    ),
                ),
            )
        ),
    )
    update_permission = sgqlc.types.Field(
        "UpdatePermission",
        graphql_name="updatePermission",
        args=sgqlc.types.ArgDict(
            (
                (
                    "description",
                    sgqlc.types.Arg(String, graphql_name="description", default=None),
                ),
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    toggle_permission = sgqlc.types.Field(
        "TogglePermission",
        graphql_name="togglePermission",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "is_active",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Boolean),
                        graphql_name="isActive",
                        default=None,
                    ),
                ),
            )
        ),
    )
    create_project = sgqlc.types.Field(
        CreateProject,
        graphql_name="createProject",
        args=sgqlc.types.ArgDict(
            (
                (
                    "description",
                    sgqlc.types.Arg(String, graphql_name="description", default=None),
                ),
                (
                    "domain_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="domainId", default=None
                    ),
                ),
                (
                    "name",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="name", default=None
                    ),
                ),
            )
        ),
    )
    update_project = sgqlc.types.Field(
        "UpdateProject",
        graphql_name="updateProject",
        args=sgqlc.types.ArgDict(
            (
                (
                    "description",
                    sgqlc.types.Arg(String, graphql_name="description", default=None),
                ),
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "name",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="name", default=None
                    ),
                ),
            )
        ),
    )
    toggle_project = sgqlc.types.Field(
        "ToggleProject",
        graphql_name="toggleProject",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "is_active",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Boolean),
                        graphql_name="isActive",
                        default=None,
                    ),
                ),
            )
        ),
    )
    create_user_group = sgqlc.types.Field(
        CreateUserGroup,
        graphql_name="createUserGroup",
        args=sgqlc.types.ArgDict(
            (
                (
                    "domain_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="domainId", default=None
                    ),
                ),
                (
                    "name",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="name", default=None
                    ),
                ),
            )
        ),
    )
    update_user_group = sgqlc.types.Field(
        "UpdateUserGroup",
        graphql_name="updateUserGroup",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                ("name", sgqlc.types.Arg(String, graphql_name="name", default=None)),
            )
        ),
    )
    toggle_user_group = sgqlc.types.Field(
        "ToggleUserGroup",
        graphql_name="toggleUserGroup",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "is_active",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Boolean),
                        graphql_name="isActive",
                        default=None,
                    ),
                ),
            )
        ),
    )
    delegate_permission_to_user_group = sgqlc.types.Field(
        DelegatePermissionGroup,
        graphql_name="delegatePermissionToUserGroup",
        args=sgqlc.types.ArgDict(
            (
                (
                    "group_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="groupId", default=None
                    ),
                ),
                (
                    "permission_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="permissionId",
                        default=None,
                    ),
                ),
            )
        ),
    )
    demote_permission_from_user_group = sgqlc.types.Field(
        DemotePermissionGroup,
        graphql_name="demotePermissionFromUserGroup",
        args=sgqlc.types.ArgDict(
            (
                (
                    "group_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="groupId", default=None
                    ),
                ),
                (
                    "permission_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="permissionId",
                        default=None,
                    ),
                ),
            )
        ),
    )
    delegate_user_to_user_group = sgqlc.types.Field(
        DelegateUserGroup,
        graphql_name="delegateUserToUserGroup",
        args=sgqlc.types.ArgDict(
            (
                (
                    "group_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="groupId", default=None
                    ),
                ),
                (
                    "user_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="userId", default=None
                    ),
                ),
            )
        ),
    )
    demote_user_from_user_group = sgqlc.types.Field(
        DemoteUserGroup,
        graphql_name="demoteUserFromUserGroup",
        args=sgqlc.types.ArgDict(
            (
                (
                    "group_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="groupId", default=None
                    ),
                ),
                (
                    "user_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="userId", default=None
                    ),
                ),
            )
        ),
    )
    create_user = sgqlc.types.Field(
        CreateUser,
        graphql_name="createUser",
        args=sgqlc.types.ArgDict(
            (
                (
                    "domain_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="domainId", default=None
                    ),
                ),
                (
                    "first_name",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="firstName",
                        default=None,
                    ),
                ),
                (
                    "internal_auth",
                    sgqlc.types.Arg(Boolean, graphql_name="internalAuth", default=None),
                ),
                (
                    "last_name",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="lastName",
                        default=None,
                    ),
                ),
                (
                    "login",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="login", default=None
                    ),
                ),
                (
                    "password",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="password",
                        default=None,
                    ),
                ),
            )
        ),
    )
    update_user = sgqlc.types.Field(
        "UpdateUser",
        graphql_name="updateUser",
        args=sgqlc.types.ArgDict(
            (
                (
                    "first_name",
                    sgqlc.types.Arg(String, graphql_name="firstName", default=None),
                ),
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "last_name",
                    sgqlc.types.Arg(String, graphql_name="lastName", default=None),
                ),
                (
                    "password",
                    sgqlc.types.Arg(String, graphql_name="password", default=None),
                ),
            )
        ),
    )
    toggle_user = sgqlc.types.Field(
        "ToggleUser",
        graphql_name="toggleUser",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "is_active",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Boolean),
                        graphql_name="isActive",
                        default=None,
                    ),
                ),
            )
        ),
    )
    delegate_permission_to_user = sgqlc.types.Field(
        DelegatePermissionUser,
        graphql_name="delegatePermissionToUser",
        args=sgqlc.types.ArgDict(
            (
                (
                    "permission_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="permissionId",
                        default=None,
                    ),
                ),
                (
                    "user_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="userId", default=None
                    ),
                ),
            )
        ),
    )
    demote_permission_from_user = sgqlc.types.Field(
        DemotePermissionUser,
        graphql_name="demotePermissionFromUser",
        args=sgqlc.types.ArgDict(
            (
                (
                    "permission_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="permissionId",
                        default=None,
                    ),
                ),
                (
                    "user_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="userId", default=None
                    ),
                ),
            )
        ),
    )
    create_domain = sgqlc.types.Field(
        CreateDomain,
        graphql_name="createDomain",
        args=sgqlc.types.ArgDict(
            (
                (
                    "description",
                    sgqlc.types.Arg(String, graphql_name="description", default=None),
                ),
                (
                    "name",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="name", default=None
                    ),
                ),
            )
        ),
    )
    update_domain = sgqlc.types.Field(
        "UpdateDomain",
        graphql_name="updateDomain",
        args=sgqlc.types.ArgDict(
            (
                (
                    "description",
                    sgqlc.types.Arg(String, graphql_name="description", default=None),
                ),
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                ("name", sgqlc.types.Arg(String, graphql_name="name", default=None)),
            )
        ),
    )
    toggle_domain = sgqlc.types.Field(
        "ToggleDomain",
        graphql_name="toggleDomain",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "is_active",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Boolean),
                        graphql_name="isActive",
                        default=None,
                    ),
                ),
            )
        ),
    )


class Permission(sgqlc.types.Type):
    __schema__ = schema
    created_at = sgqlc.types.Field(DateTime, graphql_name="createdAt")
    updated_at = sgqlc.types.Field(DateTime, graphql_name="updatedAt")
    project_id = sgqlc.types.Field(Int, graphql_name="projectId")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    description = sgqlc.types.Field(String, graphql_name="description")
    type = sgqlc.types.Field(PermissionType, graphql_name="type")
    is_active = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="isActive"
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    project = sgqlc.types.Field("Project", graphql_name="project")


class Project(sgqlc.types.Type):
    __schema__ = schema
    created_at = sgqlc.types.Field(DateTime, graphql_name="createdAt")
    updated_at = sgqlc.types.Field(DateTime, graphql_name="updatedAt")
    domain_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="domainId")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="uuid")
    description = sgqlc.types.Field(String, graphql_name="description")
    is_active = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="isActive"
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    domain = sgqlc.types.Field(Domain, graphql_name="domain")
    permissions = sgqlc.types.Field(
        sgqlc.types.list_of(Permission), graphql_name="permissions"
    )


class Query(sgqlc.types.Type):
    __schema__ = schema
    permissions = sgqlc.types.Field(
        sgqlc.types.list_of(Permission), graphql_name="permissions"
    )
    get_permission = sgqlc.types.Field(
        Permission,
        graphql_name="getPermission",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    projects = sgqlc.types.Field(sgqlc.types.list_of(Project), graphql_name="projects")
    get_project = sgqlc.types.Field(
        Project,
        graphql_name="getProject",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    user_groups = sgqlc.types.Field(
        sgqlc.types.list_of("UserGroup"), graphql_name="userGroups"
    )
    get_user_group = sgqlc.types.Field(
        "UserGroup",
        graphql_name="getUserGroup",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    users = sgqlc.types.Field(sgqlc.types.list_of("User"), graphql_name="users")
    get_user = sgqlc.types.Field(
        "User",
        graphql_name="getUser",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    domains = sgqlc.types.Field(sgqlc.types.list_of(Domain), graphql_name="domains")
    get_domain = sgqlc.types.Field(
        Domain,
        graphql_name="getDomain",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )


class ToggleDomain(sgqlc.types.Type):
    __schema__ = schema
    domain = sgqlc.types.Field(Domain, graphql_name="domain")


class TogglePermission(sgqlc.types.Type):
    __schema__ = schema
    permission = sgqlc.types.Field(Permission, graphql_name="permission")


class ToggleProject(sgqlc.types.Type):
    __schema__ = schema
    project = sgqlc.types.Field(Project, graphql_name="project")


class ToggleUser(sgqlc.types.Type):
    __schema__ = schema
    user = sgqlc.types.Field("User", graphql_name="user")


class ToggleUserGroup(sgqlc.types.Type):
    __schema__ = schema
    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")


class UpdateDomain(sgqlc.types.Type):
    __schema__ = schema
    domain = sgqlc.types.Field(Domain, graphql_name="domain")


class UpdatePermission(sgqlc.types.Type):
    __schema__ = schema
    permission = sgqlc.types.Field(Permission, graphql_name="permission")


class UpdateProject(sgqlc.types.Type):
    __schema__ = schema
    project = sgqlc.types.Field(Project, graphql_name="project")


class UpdateUser(sgqlc.types.Type):
    __schema__ = schema
    user = sgqlc.types.Field("User", graphql_name="user")


class UpdateUserGroup(sgqlc.types.Type):
    __schema__ = schema
    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")


class User(sgqlc.types.Type):
    __schema__ = schema
    created_at = sgqlc.types.Field(DateTime, graphql_name="createdAt")
    updated_at = sgqlc.types.Field(DateTime, graphql_name="updatedAt")
    domain_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="domainId")
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="login")
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="uuid")
    first_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="firstName"
    )
    last_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="lastName")
    internal_auth = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="internalAuth"
    )
    is_active = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="isActive"
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    domain = sgqlc.types.Field(Domain, graphql_name="domain")
    groups = sgqlc.types.Field(sgqlc.types.list_of("UserGroup"), graphql_name="groups")
    permissions = sgqlc.types.Field(
        sgqlc.types.list_of(Permission), graphql_name="permissions"
    )
    internal_permissions = sgqlc.types.Field(
        sgqlc.types.list_of(Permission), graphql_name="internalPermissions"
    )


class UserGroup(sgqlc.types.Type):
    __schema__ = schema
    created_at = sgqlc.types.Field(DateTime, graphql_name="createdAt")
    updated_at = sgqlc.types.Field(DateTime, graphql_name="updatedAt")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    domain_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="domainId")
    is_active = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="isActive"
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    domain = sgqlc.types.Field(Domain, graphql_name="domain")
    permissions = sgqlc.types.Field(
        sgqlc.types.list_of(Permission), graphql_name="permissions"
    )
    members = sgqlc.types.Field(sgqlc.types.list_of(User), graphql_name="members")


########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = Mutation
schema.subscription_type = None
