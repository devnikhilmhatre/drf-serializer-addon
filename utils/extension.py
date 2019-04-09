class SerializerAddOn:

    def __init__(self, *args, **kwargs):
        try:
            print('Add on')
            only = kwargs.pop('only')
            self.Meta.fields = only
        except KeyError:
            pass
        return super().__init__(*args, **kwargs)
