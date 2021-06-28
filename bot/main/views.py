from django.views.decorators.csrf import csrf_exempt

from bot.generics import *

import csv

@csrf_exempt
def stock(request):
    try:
        data = request.POST.copy()
        url = settings.API_STOCK_ROOT_DIR.replace('stock_code', str(data.get('stock_code')))
        content = ''
        with requests.get(url, stream=True) as r:
            lines = (line.decode('utf-8') for line in r.iter_lines())
            for row in csv.reader(lines):
                Symbol,Date,Time,Open,High,Low,Close,Volume = row
                if Symbol.upper() == str(data.get('stock_code')).upper():
                    content = Symbol + ' quote is $' + Close + ' per share'
        data['content'] = content
        return requestApi(request, 'messages/create/bot/', method='POST', data=data)
    except Exception as e:
        return JsonResponse({'detail': str(e), 'error': 0})
