import os

import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProjectApi.settings")


django.setup()

from firm_api.models import HierarchyLevels


def populate_levels():
    for i in range(1, 6):
        HierarchyLevels.objects.create(
            level=i
        )

# from django_seed import Seed
#
# seeder = Seed.seeder()
#
# from firm_api.models import HierarchyLevels
# seeder.add_entity(HierarchyLevels, 5)


# inserted_pks = seeder.execute()
if __name__ == "__main__":
    populate_levels()


