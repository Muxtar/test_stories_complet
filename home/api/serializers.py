from django.contrib.auth.models import User
from home.models import Category, Story
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class CategorySerial(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    image = serializers.ImageField()
    slug = serializers.SlugField(read_only = True)
    create_date = serializers.DateTimeField(read_only = True)
    update_date = serializers.DateField(read_only = True)

    # modelde olmayan field ucun serial duzeldir
    date = serializers.SerializerMethodField(read_only = True)
    def get_date(self, obj):
        data = obj.create_date
        return f'{data.year}/{data.month}/{data.day}'

    def create(self, validated_data):
        data = Category(**validated_data)
        data.save()
        return data

class CategorySerial2(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']

class StoryCreatSerial(serializers.ModelSerializer):
    # fname = serializers.StringRelatedField(source = 'user.username')
    # lname = serializers.StringRelatedField(source = 'user.last_name')
    # user = UserSerial()
    class Meta:
        model = Story
        fields = '__all__'
        read_only_fields = ['id', 'create_date', 'update_date', 'slug']

class StorySerial(serializers.ModelSerializer):
    # fname = serializers.StringRelatedField(source = 'user.username')
    # lname = serializers.StringRelatedField(source = 'user.last_name')
    user = UserSerial()
    category = CategorySerial2()
    class Meta:
        model = Story
        fields = '__all__'
        read_only_fields = ['id', 'create_date', 'update_date', 'slug']