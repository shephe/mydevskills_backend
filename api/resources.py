from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from tastypie import fields
from api.models import User
from api.models import Skill
from tastypie.authorization import Authorization

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()


class SkillResource(ModelResource):
    user_id = fields.ForeignKey(UserResource, 'user_id')
    class Meta:
        queryset = Skill.objects.all()
        resource_name = 'skill'
        authorization = Authorization()
        fields = ['description', 'user_id', 'skill_level']
        filtering = {
            'user_id': ALL_WITH_RELATIONS
        }