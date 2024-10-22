# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import DailyActivity, User
# import json

# @csrf_exempt
# def insert_activity(request):
#     if request.method == 'POST':
#         try:
#             # Parse the JSON data
#             data = json.loads(request.body)

#             # Extract data from the request
#             email = data.get('email')
#             steps = data.get('steps')
#             active_minutes = data.get('active_minutes')
#             calories_burned = data.get('calories_burned')
#             activity_date = data.get('activity_date')

#             # Find the user by email
#             user = User.objects.get(email=email)

#             # Create the DailyActivity record
#             activity = DailyActivity.objects.create(
#                 user=user,
#                 steps=steps,
#                 active_minutes=active_minutes,
#                 calories_burned=calories_burned,
#                 activity_date=activity_date
#             )

#             return JsonResponse({'success': True, 'message': 'Activity inserted successfully'})

#         except User.DoesNotExist:
#             return JsonResponse({'success': False, 'message': 'User not found'}, status=404)
#         except Exception as e:
#             return JsonResponse({'success': False, 'message': str(e)}, status=500)

#     return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)
