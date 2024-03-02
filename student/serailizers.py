from django.core.validators import MinValueValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from student.models import Student,Book



class BookSerializer(serializers.ModelSerializer):
    book_id = serializers.CharField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

    def validate_title(self, title):
        if len(title) < 4:
            raise serializers.ValidationError({"status":False, "message":"Title must be at least 4 characters"})
        elif Book.objects.filter(title=title).exists():
            raise serializers.ValidationError({"status":False, "message":"Title already exists"})

        return title












def validate_age(age):
    if age<15:
        raise serializers.ValidationError("Age is too young")
    else:
        return age


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, validators=[UniqueValidator(queryset=Student.objects.all())])
    age = serializers.IntegerField(validators=[validate_age])
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance





