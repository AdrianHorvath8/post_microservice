from django.forms import ModelForm
from .models import Post

class PostFormCreate(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class PostFormUpdate(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["user_id"]