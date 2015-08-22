from django.db import models
# from django.core.urlresolvers import reverse_lazy
from django.core.validators import RegexValidator


class Users(models.Model):
    name = models.CharField(max_length=5)
    nickname = models.CharField(max_length=12)
    birthday = models.DateTimeField(blank=True)
    major = models.CharField(max_length=12, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="전화번호를 입력해주세요.")
    phone_number = models.CharField(max_length=30,
                                    validators=[phone_regex], blank=True)
    mail_address = models.EmailField(max_length=20)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "필명 : " + self.nickname


# 유저폼 백업
class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ('join_date', 'phone_regex')