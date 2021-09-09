from uber.decorators import all_renderable


@all_renderable(public=True)
class Root:
    def index(self, **params):
        return {
            'message': params.get('message', ''),
            'email':   params.get('email', ''),
            'original_location': params.get('original_location'),
        }

    def invalid(self, **params):
        return {'message': params.get('message')}
