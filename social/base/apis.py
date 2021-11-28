from django.core.exceptions import ImproperlyConfigured


class MultipleSerializerMixins(object):
    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]

        return super(MultipleSerializerMixins, self).get_serializer_class()
