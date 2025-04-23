import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker_app.models import YourModel  # Replace 'YourModel' with your actual model name

# Add test data
def populate():
    # Example: Replace with your actual fields and data
    test_data = [
        {'field1': 'value1', 'field2': 'value2'},
        {'field1': 'value3', 'field2': 'value4'},
    ]

    for data in test_data:
        obj, created = YourModel.objects.get_or_create(**data)
        if created:
            print(f"Created: {obj}")
        else:
            print(f"Already exists: {obj}")

if __name__ == "__main__":
    populate()
