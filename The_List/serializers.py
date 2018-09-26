from rest_framework import serializers
from .models import Bucketlist
class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

   # owner = serializers.ReadOnlyField(source='owner.username') # ADD THIS LINE

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Bucketlist
        fields = ('item', 'target_age', 'added_date', 'status', 'country') # ADD 'owner'
        read_only_fields = ('added_date')
