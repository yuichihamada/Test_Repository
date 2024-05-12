from django import forms
from . models import Users
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from datetime import datetime
from django.contrib.auth.password_validation import (
  MinimumLengthValidator, 
  CommonPasswordValidator, 
  NumericPasswordValidator,
  UserAttributeSimilarityValidator,
)

class RegistForm(forms.ModelForm):
  username = forms.CharField(label='名前', error_messages={'required': '名前を入力してください'})
  email = forms.EmailField(label='メールアドレス', error_messages={'required': 'メールアドレスを入力してください'})
  password = forms.CharField(label='パスワード', widget=forms.PasswordInput(), error_messages={'required': 'パスワードを入力してください'})
  confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput(), error_messages={'required': 'パスワードを再入力してください'})
  picture = forms.FileField(label='写真', error_messages={'required': '写真を選択してください'})
  introduction = forms.CharField(label='ひとこと', widget=forms.Textarea(), error_messages={'required': 'ひとことを入力してください'})
  
  class Meta:
    model = Users
    fields = ['username', 'email', 'introduction', 'password', ]
  
  def clean_username(self):
    username = self.cleaned_data['username']
    if Users.objects.filter(username=username).exists():
      raise ValidationError('その名前は既に登録されています')
    return username
  
  def clean_email(self):
    email = self.cleaned_data['email']
    if Users.objects.filter(email=email).exists():
      raise ValidationError('そのメールアドレスは既に登録されています')
    return email
  
  def clean_password(self):
    password = self.cleaned_data.get('password')
    if password:
      errors = []
      validators = [
        {'validator': MinimumLengthValidator(8), 'message': 'パスワードは8文字以上にしてください'},
        {'validator': CommonPasswordValidator(), 'message': '一般的な文字列ではないパスワードにしてください'},
        {'validator': NumericPasswordValidator(), 'message': '数字のみではないパスワードにしてください'},
        {'validator': UserAttributeSimilarityValidator(), 'message': 'ユーザー名またはメールアドレスがパスワードの一部に含まれています'}
      ]
      for validator_info in validators:
        try:
          validator_info['validator'].validate(password)
        except ValidationError as e:
          errors.append(validator_info['message'])
      if errors:
        raise forms.ValidationError(errors)
    return password
  
  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get('password')
    confirm_password = cleaned_data.get('confirm_password')
    if password != confirm_password:
      raise ValidationError('パスワードが一致しません')
  
  def save(self, commit=False):
    user = super().save(commit=False)
    validate_password(self.cleaned_data['password'], user)
    user.set_password(self.cleaned_data['password'])
    picture = self.cleaned_data.get('picture')
    if picture:
      user.picture = picture
    user.create_at = datetime.now()
    user.update_at = datetime.now()
    user.save()
    return user


class UserLoginForm(AuthenticationForm):
  username = forms.EmailField(label='メールアドレス', error_messages={'required': 'メールアドレスを入力してください', 'invalid': '有効なメールアドレスを入力してください'})
  password = forms.CharField(label='パスワード', widget=forms.PasswordInput(), error_messages={'required': 'パスワードを入力してください'})
  remember = forms.BooleanField(label='ログイン状態を保持する', required=False)