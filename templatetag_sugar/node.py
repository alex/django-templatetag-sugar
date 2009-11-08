from django.template import Node


class SugarNode(Node):
    def __init__(self, pieces, function):
        self.pieces = pieces
        self.function = function
    
    def render(self, context):
        args = []
        kwargs = {}
        for part, name, value in self.pieces:
            value = part.resolve(context, value)
            if name is None:
                args.append(value)
            else:
                kwargs[name] = value
        
        return self.function(context, *args, **kwargs)
