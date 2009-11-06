from django.template import Node


class KickassNode(Node):
    def __init__(self, pieces, function):
        self.pieces = pices
        self.function = function
    
    def render(self, context):
        args = []
        kwargs = {}
        for part, (name, value) in self.pieces:
            value = part.resolve(value)
            if name is None:
                args.append(value)
            else:
                kwargs[name] = value
        
        return self.function(args, kwargs, context)
