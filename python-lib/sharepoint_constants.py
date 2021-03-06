class SharePointConstants(object):
    COLUMNS = 'columns'
    COMMENT_COLUMN = 'comment'
    ENTITY_PROPERTY_NAME = 'EntityPropertyName'
    ERROR_CONTAINER = 'error'
    EXPENDABLES_FIELDS = {"Author": "Title", "Editor": "Title"}
    FALLBACK_TYPE = "Text"
    FORM_DIGEST_VALUE = "FormDigestValue"
    GET_FOLDER_URL_STRUCTURE = "{0}/{1}/_api/Web/GetFolderByServerRelativeUrl('/{1}/{2}{3}')"
    GET_SITE_APP_TOKEN_URL = "https://accounts.accesscontrol.windows.net/{tenant_id}/tokens/OAuth/2"
    HIDDEN_COLUMN = 'Hidden'
    LENGTH = 'Length'
    LOOKUP_FIELD = 'LookupField'
    MESSAGE = 'message'
    MOVE_TO = "MoveTo"
    NAME = 'Name'
    NAME_COLUMN = 'name'
    NEXT_PAGE = '__next'
    READ_ONLY_FIELD = 'ReadOnlyField'
    RESULTS = 'results'
    RESULTS_CONTAINER_V2 = 'd'
    SHAREPOINT_ONLINE_RESSOURCE = "00000003-0000-0ff1-ce00-000000000000"
    STATIC_NAME = 'StaticName'
    TIME_LAST_MODIFIED = 'TimeLastModified'
    TITLE_COLUMN = 'Title'
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
    TYPES = {
        "Text": "string",
        "Number": "string",
        "DateTime": "date",
        "Boolean": "string",
        "URL": "object",
        "Location": "object",
        "Computed": None,
        "Attachments": None
    }
    TYPE_AS_STRING = 'TypeAsString'
    TYPE_COLUMN = 'type'
    VALUE = 'value'
