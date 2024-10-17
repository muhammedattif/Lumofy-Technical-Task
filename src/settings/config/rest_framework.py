# RestFramework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PAGINATION_CLASS": "src.utility.pagination_classes.CustomPageNumberPagination",
    "PAGE_SIZE": 10,
}
