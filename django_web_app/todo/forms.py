from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(
        label='やること',
        max_length=300,
        required=True)

    is_done = forms.ChoiceField(
      label='完了ステータス',
      initial=False,
      choices=(
          (False, '未完'),
          (True, '完了')),
      required=True)