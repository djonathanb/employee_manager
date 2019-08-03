from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

api_schema_view = get_schema_view(
    title='Employee Manager API',
    description='Luizalabs recruitment process test')

api_ui_view = TemplateView.as_view(
    template_name='docs-ui.html',
    extra_context={'schema_url': 'api-docs-schema'})
