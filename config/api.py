import datetime

from ninja import NinjaAPI
from ninja.renderers import JSONRenderer
from ninja.responses import NinjaJSONEncoder


class MyJsonEncoder(NinjaJSONEncoder):
    def default(self, value):
        if isinstance(value, datetime.datetime):
            return value.strftime('%Y-%m-%d %H:%M:%S')
        return super().default(value)


class MyJsonRenderer(JSONRenderer):
    encoder_class = MyJsonEncoder


api = NinjaAPI(
    title='接口文档',
    renderer=MyJsonRenderer(),
)

@api.get('/index')
def index(request):
    return {'hello', 'world'}
