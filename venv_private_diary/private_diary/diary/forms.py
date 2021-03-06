from django import forms

from django.core.mail import EmailMessage
#models.pyからDiaryモデルクラスをインポート
from .models import CareerDiary

#問い合わせ用フォーム
class InquiryForm(forms.Form):
    name = forms.CharField(label = 'お名前', max_length=30)
    email = forms.EmailField(label = 'メールアドレス')
    title = forms.CharField(label = 'タイトル', max_length= 30)
    message = forms.CharField(label = 'メッセージ', widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        '''
        fields["フィールド名"].widget.attrs['class'] = 'クラス名'
        fields["フィールド名"].widget.attrs['placeholder'] = 'プレースホルダー名'
        attrsメソッドでHTML属性のプロパティを取得
        '''
        
        self.fields['name'].widget.attrs['class'] = 'form-control col-9'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前を入力してください'
        
        self.fields['email'].widget.attrs['class'] = 'form-control col-11'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスを入力してください'
        
        self.fields['title'].widget.attrs['class'] = 'form-control col-11'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルを入力してください'
        
        self.fields['message'].widget.attrs['class'] = 'form-control col-12'
        self.fields['message'].widget.attrs['placeholder'] = 'タイトルを入力してください'
    
    #メールを送るメソッド
    def send_email(self):
        #フォームバリデーションを通ったデータを取得して代入
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']
        
        #件名（subject）を設定
        subject = f'お問い合わせ{title}'
        #本文を設定
        message = f'送信者名：{name}\nメールアドレス：{email}\nメッセージ：{message}'
        #送信者を設定
        from_email = 'admin@example.com'
        #受信者のリスト
        to_list = [
            'test@example.com'
        ]
        #ccのリスト
        cc_list = [
            email
        ]
        
        #EmailMessageインスタンスを作成
        message = EmailMessage(
            subject = subject,
            body = message,
            from_email = from_email,
            to = to_list,
            cc = cc_list,
        )
        
        #send()メソッドを使用してメッセージを作成する
        message.send()


#CareerDiary作成フォーム
class CareerDiaryCreateForm(forms.ModelForm):
    class Meta:
        model = CareerDiary
        fields = [
            'company_name',
            'interview_date',
            'selection_stage',
            'content',
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
