import json
from datetime import datetime

from django.shortcuts import render
from .models import Patching
from .filters import PatchingFilter
import django_filters

class PatchFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='custom_filter', label='Search')

    class Meta:
        model = Patching
        fields = []

    def custom_filter(self, queryset, name, value):
        return queryset.filter(
            machine__icontains=value
        ) | queryset.filter(
            ip__icontains=value
        ) | queryset.filter(
            OS_support__icontains=value
        )

def patch_calendar(request):
    plans = []
    months = [
        ('jan', 1), ('feb', 2), ('mar', 3), ('apr', 4),
        ('may', 5), ('jun', 6), ('jul', 7), ('aug', 8),
        ('sep', 9), ('oct', 10), ('nov', 11), ('dec', 12)
    ]

    year = datetime.now().year  # Use current year or specify a fixed year

    # Fetch all Patching records
    patches = Patching.objects.all()

    # Loop through all patches
    for patch in patches:
        for month_str, month_num in months:
            # Get the actual date for the patch plan and patch execution
            plan_field = getattr(patch, f'patch_plan_{month_str}')
            exec_field = getattr(patch, f'patch_exec_{month_str}')

            # Check if there is a valid plan date
            if plan_field:  # if there is a planned patch
                status = 'executed' if exec_field else 'planned'
                date_str = plan_field.strftime('%Y-%m-%d')  # Use actual date from patch_plan
                color = 'green' if status == 'executed' else 'red'
                plans.append({
                    'date': date_str,
                    'status': patch.machine,  # Add the machine name for the status
                    'color': color,           # Red for planned, green for executed
                })

    # After processing all patches, render the template
    return render(request, 'patch_tool_app/calendar.html', {
        'plans': plans  # Pass all the plans
    })

def main_page(request):
    patch_filter = PatchFilter(request.GET, queryset=Patching.objects.all())
    return render(request, 'patch_tool_app/main.html', {'filter': patch_filter})
