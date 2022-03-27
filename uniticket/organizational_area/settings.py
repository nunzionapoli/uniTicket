from django.conf import settings

# default office parameters
DEFAULT_ORGANIZATIONAL_STRUCTURE_OFFICE = getattr(
    settings,
    "DEFAULT_ORGANIZATIONAL_STRUCTURE_OFFICE",
    "Help-Desk"
)
DEFAULT_ORGANIZATIONAL_STRUCTURE_OFFICE_DESC = getattr(
    settings,
    "DEFAULT_ORGANIZATIONAL_STRUCTURE_OFFICE_DESC",
    "Help-Desk Office"
)

# system upload folders
LOGOS_FOLDER = getattr(
    settings,
    "LOGOS_FOLDER",
    'logos'
)
STRUCTURES_FOLDER = getattr(
    settings,
    "STRUCTURES_FOLDER",
    'structures'
)
