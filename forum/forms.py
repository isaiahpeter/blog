from django import forms
from .models import Post, Comment, Category
from django.utils.text import slugify
class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
        
    class Meta:
        model = Post
        fields = ['category', 'title', 'content', 'author', 'status', 'image']
        #widgets = {'content':forms.Textarea(attrs={'cols':80})}
    def clean_title(self):
        title = self.cleaned_data['title']
        slug = slugify(title)
        if Post.objects.filter(slug=slug).exists():
            raise forms.ValidationError('A post with this title already exists')
        return title
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance       



class EditForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = ['content', 'status', 'image']
    
