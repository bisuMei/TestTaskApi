from django_seed import Seed
from firm_api.models import Employee, Position, Boss, HierarchyLevels

seeder = Seed.seeder()

# seeder.add_entity(Boss, 15)
# seeder.add_entity(Position, 15)
seeder.add_entity(HierarchyLevels, 5)
# seeder.add_entity(Employee, 15)



inserted_pks = seeder.execute()