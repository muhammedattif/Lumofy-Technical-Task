# Other Third Party Imports
from decouple import config

# Migration Structure
MIGRATION_PATH_DICT = {
    "PRODUCTION": "migrations.production",
    "STAGING": "migrations.staging",
}

ENVIRONMENT = config("ENVIRONMENT", default="LOCAL")
MIGRATION_PATH = MIGRATION_PATH_DICT.get(ENVIRONMENT, "migrations.local")
MIGRATION_MODULES = {
    "src": "src." + MIGRATION_PATH,
}
