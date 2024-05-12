from django import forms
from accounts.models import Users
from . models import WantItems, ToDoThings, AchievedThings
from datetime import datetime
from django.core.exceptions import ValidationError


class UserUpdateForm(forms.ModelForm):
  username = forms.CharField(label='名前',max_length=150, error_messages={'required': '名前を入力してください'})
  email = forms.EmailField(label='メールアドレス',max_length=255, error_messages={'required': 'メールアドレスを入力してください'})
  introduction = forms.CharField(label='ひとこと',max_length=1000, error_messages={'required': 'ひとことを入力してください'})
  picture = forms.ImageField(label='写真', error_messages={'required': '写真を選択してください'})

  class Meta:
    model = Users
    fields = ['username', 'email', 'introduction', 'picture', ]
    exclude = ()
  
  def save(self, commit=False):
    user = super().save(commit=False)
    user.update_at = datetime.now()
    user.save()
    return user
      

class RegistItemForm(forms.ModelForm):
  
  name = forms.CharField(label='ほしいものの名前', error_messages={'required': '名前を入力してください'})
  detail = forms.CharField(label='詳細', widget=forms.Textarea(), error_messages={'required': '詳細を入力してください'})
  price = forms.IntegerField(label='値段(円)', error_messages={'required': '値段を入力してください'})
  target_date = forms.DateField(label='いつまでに', widget=forms.DateInput(attrs={'placeholder': '例:2020-01-01'}), error_messages={'required': '時期を入力してください'})
  reason = forms.CharField(label='ほしい理由', widget=forms.Textarea(), error_messages={'required': 'ほしい理由を入力してください'})
  picture = forms.FileField(label='写真', required=False)
  
  class Meta:
    model = WantItems
    fields = ['name', 'detail', 'price', 'target_date', 'reason', 'picture', ]
  
  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user', None)
    super().__init__(*args, **kwargs)
  
  def clean_price(self):
    price = self.cleaned_data.get('price')
    if price:
      if price < 0:
        raise forms.ValidationError('値段は0円以上で入力してください')
    return price
  
  def clean_target_date(self):
    target_date = self.cleaned_data.get('target_date')
    if target_date:
      if target_date < datetime.now().date():
        raise forms.ValidationError('過去の日付は入力できません')
    return target_date
  
  def save(self, commit=False):
    item = super().save(commit=False)
    picture = self.cleaned_data.get('picture')
    if picture:
      item.picture = picture
    item.user = self.user
    item.create_at = datetime.now()
    item.update_at = datetime.now()
    item.save()
    return item


class ItemUpdateForm(forms.ModelForm):
  name = forms.CharField(label='名前',max_length=150, error_messages={'required': '名前を入力してください'})
  detail = forms.CharField(label='詳細', error_messages={'required': '詳細を入力してください'})
  price = forms.IntegerField(label='値段(円)', error_messages={'required': '値段を入力してください'})
  target_date = forms.DateField(label='いつまでに', widget=forms.DateInput(attrs={'placeholder': '例:2020-01-01'}), error_messages={'required': '時期を入力してください'})
  reason = forms.CharField(label='ほしい理由', widget=forms.Textarea(), error_messages={'required': 'ほしい理由を入力してください'})
  picture = forms.FileField(label='写真', required=False)
  
  class Meta:
    model = WantItems
    fields = ['name', 'detail', 'price', 'target_date', 'reason', 'picture', ]
  
  def clean_price(self):
    price = self.cleaned_data.get('price')
    if price:
      if price < 0:
        raise forms.ValidationError('値段は0円以上で入力してください')
    return price
  
  def clean_target_date(self):
    target_date = self.cleaned_data.get('target_date')
    if target_date:
      if target_date < datetime.now().date():
        raise forms.ValidationError('過去の日付は入力できません')
    return target_date
  
  def save(self, commit=False):
    item = super().save(commit=False)
    picture = self.cleaned_data.get('picture')
    if picture:
      item.picture = picture
    item.update_at = datetime.now()
    item.save()
    return item


class RegistThingForm(forms.ModelForm):
  
  name = forms.CharField(label='やりたいことの名前', error_messages={'required': '名前を入力してください'})
  detail = forms.CharField(label='詳細', widget=forms.Textarea(), error_messages={'required': '詳細を入力してください'})
  price = forms.IntegerField(label='値段(円)', error_messages={'required': '値段を入力してください'})
  target_date = forms.DateField(label='いつまでに', widget=forms.DateInput(attrs={'placeholder': '例:2020-01-01'}), error_messages={'required': '時期を入力してください'})
  reason = forms.CharField(label='やりたい理由', widget=forms.Textarea(), error_messages={'required': 'やりたい理由を入力してください'})
  picture = forms.FileField(label='写真', required=False)
  
  class Meta:
    model = ToDoThings
    fields = ['name', 'detail', 'price', 'target_date', 'reason', 'picture', ]
  
  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user', None)
    super().__init__(*args, **kwargs)
    
  def clean_price(self):
    price = self.cleaned_data.get('price')
    if price:
      if price < 0:
        raise forms.ValidationError('値段は0円以上で入力してください')
    return price
  
  def clean_target_date(self):
    target_date = self.cleaned_data.get('target_date')
    if target_date:
      if target_date < datetime.now().date():
        raise forms.ValidationError('過去の日付は入力できません')
    return target_date
  
  def save(self, commit=False):
    thing = super().save(commit=False)
    picture = self.cleaned_data.get('picture')
    if picture:
      thing.picture = picture
    thing.user = self.user
    thing.create_at = datetime.now()
    thing.update_at = datetime.now()
    thing.save()
    return thing
  

class ThingUpdateForm(forms.ModelForm):
  name = forms.CharField(label='名前',max_length=150, error_messages={'required': '名前を入力してください'})
  detail = forms.CharField(label='詳細', error_messages={'required': '詳細を入力してください'})
  price = forms.IntegerField(label='値段(円)', error_messages={'required': '値段を入力してください'})
  target_date = forms.DateField(label='いつまでに', widget=forms.DateInput(attrs={'placeholder': '例:2020-01-01'}), error_messages={'required': '時期を入力してください'})
  reason = forms.CharField(label='やりたい理由', widget=forms.Textarea(), error_messages={'required': 'やりたい理由を入力してください'})
  picture = forms.FileField(label='写真', required=False)
  
  class Meta:
    model = WantItems
    fields = ['name', 'detail', 'price', 'target_date', 'reason', 'picture', ]
  
  def clean_price(self):
    price = self.cleaned_data.get('price')
    if price:
      if price < 0:
        raise forms.ValidationError('値段は0円以上で入力してください')
    return price
  
  def clean_target_date(self):
    target_date = self.cleaned_data.get('target_date')
    if target_date:
      if target_date < datetime.now().date():
        raise forms.ValidationError('過去の日付は入力できません')
    return target_date
  
  def save(self, commit=False):
    thing = super().save(commit=False)
    picture = self.cleaned_data.get('picture')
    if picture:
      thing.picture = picture
    thing.update_at = datetime.now()
    thing.save()
    return thing


class ConfirmAchievedItemForm(forms.ModelForm):
  price = forms.IntegerField(label='かかった金額', error_messages={'required': '金額を入力してください'})
  achieved_date = forms.DateField(label='達成した日', widget=forms.DateInput(attrs={'placeholder': '例:2020-01-01'}), error_messages={'required': '達成した日を入力してください'})
  
  class Meta:
      model = AchievedThings
      fields = ['achieved_date', 'price']
  
  def clean_price(self):
    price = self.cleaned_data.get('price')
    if price:
      if price < 0:
        raise forms.ValidationError('値段は0円以上で入力してください')
    return price


class ConfirmAchievedThingForm(forms.ModelForm):
  price = forms.IntegerField(label='かかった金額', error_messages={'required': '金額を入力してください'})
  achieved_date = forms.DateField(label='達成した日', widget=forms.DateInput(attrs={'placeholder': '例:2020-01-01'}), error_messages={'required': '達成した日を入力してください'})
  
  class Meta:
      model = AchievedThings
      fields = ['achieved_date', 'price']
  
  def clean_price(self):
    price = self.cleaned_data.get('price')
    if price:
      if price < 0:
        raise forms.ValidationError('値段は0円以上で入力してください')
    return price