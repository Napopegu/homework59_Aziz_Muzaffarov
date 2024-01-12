from django import forms
from webapp.models import Issue


class IssueForm(forms.ModelForm):
    # summary = forms.CharField(max_length=50, label='Краткое описание')
    # description = forms.CharField(widget=forms.Textarea, required=False, label='Полное описание')
    # status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус')
    # types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label='Тип', widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'types']
        widgets ={
            'types': forms.CheckboxSelectMultiple()
        }