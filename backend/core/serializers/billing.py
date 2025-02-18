from rest_framework import serializers
from core.models.billing.plan import Plan
from core.models.billing.subscription import Subscription

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

    def validate_price_per_max_students(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return data
