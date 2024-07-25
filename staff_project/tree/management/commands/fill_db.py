from django.core.management.base import BaseCommand
from dataclasses import dataclass, field, asdict
from faker import Faker
from tree.models import Staff, Subdivisions

Faker.seed()
fake = Faker('ru_Ru')

@dataclass
class FakeStaff:
    name: str = field(default_factory=fake.name)
    position: str = field(default_factory=fake.job)
    salary: str = field(default_factory=lambda: str(fake.pyfloat(min_value=1000, max_value=100000, right_digits=2)))


class Command(BaseCommand):
    def handle(self, *args, **options):
        Staff.objects.all().delete()
        Subdivisions.objects.all().delete()
        for _ in range(25):
            parent_subdivision_obj = Subdivisions(title=fake.city()+' Главное отделение')
            parent_subdivision_obj.save()

            for _ in range(400):
                fake_staff_to_dict = asdict(FakeStaff())
                fake_staff_to_dict['subdivision'] = parent_subdivision_obj
                new_staff_data = Staff(**fake_staff_to_dict)
                new_staff_data.save()

            for _ in range(4):
                children_subdivision_obj = Subdivisions(title=fake.catch_phrase(), parent=parent_subdivision_obj)
                children_subdivision_obj.save()
                parent_subdivision_obj = children_subdivision_obj
                for _ in range(400):
                    fake_staff_to_dict = asdict(FakeStaff())
                    fake_staff_to_dict['subdivision'] = children_subdivision_obj
                    new_staff_data = Staff(**fake_staff_to_dict)
                    new_staff_data.save()
