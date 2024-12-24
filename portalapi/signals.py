import logging

from django.db.models.signals import post_migrate
from django.dispatch import receiver

from portalapi.utils.constants import DEFAULT_BLOOD_DATA

from .models import BloodType

logger = logging.getLogger(__name__)


@receiver(post_migrate)
def create_default_blood_type(sender, **kwargs):
    _ = sender
    logger.info("Populating default blood types...")

    for blood_data in DEFAULT_BLOOD_DATA:
        _, created = BloodType.objects.get_or_create(
            blood_type=blood_data["blood_type"],
            defaults={"compatible_with": blood_data["compatible_with"]},
        )

        if created:
            logger.info("Created blood type")
        else:
            logger.info("Blood type already exists")

    logger.info("Default blood types populated successfully.")
