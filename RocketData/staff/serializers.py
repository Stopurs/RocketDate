from rest_framework import serializers
from .models import Staffmodels


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffmodels
        fields = (
            'parent', 'position', 'name', 'date_employment', 'salary', 'salary_all'
        )

    def get_fields(self):
        fields = super(StaffSerializer, self).get_fields()
        fields['children'] = StaffSerializer(many=True)
        return fields
