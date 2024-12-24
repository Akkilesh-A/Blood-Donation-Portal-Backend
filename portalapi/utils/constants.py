from enum import Enum

BLOOD_CHOICES = [
    ("O +ve", "O +ve"),
    (
        "O -ve",
        "O -ve",
    ),
    (
        "A +ve",
        "A +ve",
    ),
    (
        "A -ve",
        "A -ve",
    ),
    (
        "B +ve",
        "B +ve",
    ),
    (
        "B -ve",
        "B -ve",
    ),
    ("AB +ve", "AB +ve"),
    ("AB -ve", "AB -ve"),
]

COMPATIBLE_TYPES = [
    ("A +ve,AB +ve", "A +ve,AB +ve"),
    ("O +ve,A +ve,;B +ve,AB +ve", "O +ve,A +ve,B +ve,AB +ve"),
    (";B +ve,AB +ve", "B +ve,AB +ve"),
    ("AB +ve", "AB +ve"),
    ("A +ve,A -ve,AB -ve,AB +ve", "A +ve,A -ve,AB -ve,AB +ve"),
    (
        "A +ve,A -ve,O -ve,O +ve,AB +ve,AB -ve,;B +ve,;B -ve",
        "A +ve,A -ve,O -ve,O +ve,AB +ve,AB -ve,B +ve,B -ve",
    ),
    (";B +ve,;B -ve,AB -ve,AB +ve", "B +ve,B -ve,AB -ve,AB +ve"),
    ("AB +ve,AB -ve", "AB +ve,AB -ve"),
]

DEFAULT_BLOOD_DATA = [
    {
        "blood_type": "O +ve",
        "compatible_with": "O +ve, A +ve, B +ve, AB +ve",
    },
    {
        "blood_type": "O -ve",
        "compatible_with": "O -ve, A -ve, B -ve, AB -ve",
    },
    {
        "blood_type": "A +ve",
        "compatible_with": "A +ve, AB +ve",
    },
    {
        "blood_type": "A -ve",
        "compatible_with": "A -ve, AB -ve",
    },
    {
        "blood_type": "B +ve",
        "compatible_with": "B +ve, AB +ve",
    },
    {
        "blood_type": "B -ve",
        "compatible_with": "B -ve, AB -ve",
    },
    {
        "blood_type": "AB +ve",
        "compatible_with": "AB +ve",
    },
    {
        "blood_type": "AB -ve",
        "compatible_with": "AB -ve",
    },
    {
        "blood_type": "A1 +ve",
        "compatible_with": "A1 +ve, A1B +ve",
    },
    {
        "blood_type": "A1 -ve",
        "compatible_with": "A1 -ve, A1B -ve",
    },
    {
        "blood_type": "A1B +ve",
        "compatible_with": "A1B +ve",
    },
    {
        "blood_type": "A1B -ve",
        "compatible_with": "A1B -ve",
    },
    {
        "blood_type": "A2 +ve",
        "compatible_with": "A2 +ve, A2B +ve",
    },
    {
        "blood_type": "A2 -ve",
        "compatible_with": "A2 -ve, A2B -ve",
    },
    {
        "blood_type": "A2B +ve",
        "compatible_with": "A2B +ve",
    },
    {
        "blood_type": "A2B -ve",
        "compatible_with": "A2B -ve",
    },
    {
        "blood_type": "Bombay Blood Group",
        "compatible_with": "Bombay Blood Group",
    },
    {
        "blood_type": "INRA",
        "compatible_with": "Specific INRA blood group compatibility",
    },
]


class ResponseMessage(Enum):
    USERLOGGEDINSUCCESSFULLY = "Logged in Successfully"
    USERREGISTEREDSUCCESSFULLY = "Registered Successfully"
