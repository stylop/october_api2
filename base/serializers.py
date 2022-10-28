from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Advocate, Company


class CompanySerializer(ModelSerializer):
    # employee_count = SerializerMethodField(read_only=True)
    class Meta:
        model = Company
        fields = ['name','logo']
    #
    # def get_employee_count(self,obj):
    #     count = obj.advocate_set.count()
    #     return count




class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Advocate
        fields = [
            'name',
            'username',
            'profile_pic',
            'bio',
            'twitter',
            'company',


        ]

class AdvocateDetailSerializer(ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Advocate
        fields = [
            'name',
            'username',
            'profile_pic',
            'bio',
            'twitter',
            'company',


        ]


