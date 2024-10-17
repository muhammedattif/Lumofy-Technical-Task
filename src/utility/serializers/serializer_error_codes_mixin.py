# First Party Imports
from src.response_codes import GeneralCodes


class SerializerErrorCodesMixin(object):
    """SerializerErrorCodesMixin class
    Gives the serializers more power to return error codes of invalid fields instead of error messages.

    if you set RETURN_CODES_AS_LIST to True:
        - self.error_codes will be a list of error codes based on fields defined in ERROR_CODES_DICT
        - self.error_code will be None
        - If invalid fields does not match any key in ERROR_CODES_DICT, self.error_codes will be equal to a list that has only the default code (INVALID_DATA)

    if you set RETURN_CODES_AS_LIST to False: (Which is the default case)
        - self.error_code will equal to the code of the first match in ERROR_CODES_DICT
        - self.error_codes will be an empty list
        - If invalid fields does not match any key in ERROR_CODES_DICT, self.error_code will equal to the default INVALID_DATA code.
    """

    ERROR_CODES_DICT = {}
    INITIAL_ERROR_CODE = None
    # Error Codes Dict format: key: <Field Name>, value: <Error Code>
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.OVERRIDED_CODES_DICT = {}
        self.RETURN_CODES_AS_LIST = False
        self._INITIAL_ERROR_CODE = self.INITIAL_ERROR_CODE or GeneralCodes.INVALID_DATA
        self.error_code = None
        self.error_codes = []

    def is_valid(self, raise_exception=False):
        is_valid = super().is_valid(raise_exception=raise_exception)
        if is_valid:
            return is_valid

        self._set_error_codes()
        return is_valid

    def _get_error_codes(self, fields: list, is_list: bool = False) -> set:
        _error_codes = set()
        ERROR_CODES_DICT = self.child.ERROR_CODES_DICT if is_list else self.ERROR_CODES_DICT
        for field in fields:
            error_code = self.OVERRIDED_CODES_DICT.get(field) or ERROR_CODES_DICT.get(field)
            if error_code:
                _error_codes.add(error_code)

        return _error_codes

    def _set_error_codes(self) -> None:
        """Set self.error_code or self.error_codes based on user's settings"""
        _error_codes = set(self.error_codes)
        if isinstance(self._errors, list):
            for dictionary in self._errors:
                _error_codes = self._get_error_codes(fields=dictionary.keys(), is_list=True)
        else:
            _error_codes = self._get_error_codes(fields=self._errors.keys())

        _error_codes = list(_error_codes)
        if self.RETURN_CODES_AS_LIST:
            self.error_codes = _error_codes or [self._INITIAL_ERROR_CODE]
        else:
            self.error_code = _error_codes[0] if _error_codes else self._INITIAL_ERROR_CODE

    def override_field_error_code(self, field_name: str, code: str) -> None:
        """Set Dierld error code

        Args:
            field_name (str): Field name to Override its value
            code (str): Code
        """
        self.OVERRIDED_CODES_DICT[field_name] = code
