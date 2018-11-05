from uuid import UUID
import json

class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)

def dump(obj, **kwargs):
    return json.dumps(obj, **kwargs, ensure_ascii=False, cls=UUIDEncoder)

def dictify(obj, **kwargs):
    if isinstance(obj, list):
        return [dictify(o) for o in obj]

    res = {}
    _obj = obj.to_dict(with_collections=True, related_objects=True)
    for key, val in _obj.items():
        try:
            if isinstance(val, list):
                res[key] = [v.to_dict(**kwargs) for v in val]
            else:
                res[key] = val.to_dict(**kwargs)
        except AttributeError:
            res[key] = val
    return res
