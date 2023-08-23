from django import forms
from django.core.mail.message import EmailMessage

class ContatoForms(forms.Form):
    nome = forms.CharField(label='nome', max_length=100)
    email = forms.EmailField(label='email', max_length=100)
    assunto = forms.CharField(label='assunto', max_length=100)
    mensagem = forms.CharField(label='mensagem', max_length=1000)

    def send_email(self):
        nome = self.cleaned_data['nome']
        email=self.cleaned_data['email']
        assunto=self.cleaned_data['assunto']
        mensagem=self.cleaned_data['mensagem']

        conteudo = f'nome: {nome}\n email: {email}\n assunto:{assunto}\n mensagem: {mensagem}'

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contato@dfusion.com.br',
            to=['contato@fusion.com.br',],
            headers={'reply-to': email}
        )
        mail.send()

