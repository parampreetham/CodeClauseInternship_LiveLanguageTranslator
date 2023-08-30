from django.db import models



class Translation(models.Model):
    original_text = models.TextField()
    translated_text = models.TextField()
    source_language = models.ForeignKey('translator_app.Language', related_name='source_translations', on_delete=models.CASCADE)
    target_language = models.ForeignKey('translator_app.Language', related_name='target_translations', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.original_text} - {self.target_language}'

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'translator_app'

