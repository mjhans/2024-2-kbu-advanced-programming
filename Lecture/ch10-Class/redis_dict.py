import json
import redis


# get 함수 구현을 하고 싶은데...
class RedisDict(dict):

    def __init__(self, host='127.0.0.1', password=None, port=6379, db=0):
        self.rd = redis.StrictRedis(host=host, port=port, db=db, password=password)

    def __getitem__(self, key):
        _v = self.rd.get(key)
        return dict() if _v is None else json.loads(_v)

    def __missing__(self, key):
        return dict()

    def __setitem__(self, key, dict_value):

        if type(dict_value) == dict:
            self.rd.set(key, json.dumps(dict_value))
        else:
            raise ValueError("Value must be a dictionary")

    def __str__(self):
        return str(self.rd.keys())

    def __delitem__(self, key):
        self.rd.delete(key)


if __name__ == '__main__':
    rd = RedisDict()
    rd['a'] = {'a': 1, 'b': 2}
    print(rd['a'])
    print(rd['b'])
    print(rd)
    del rd['a']
    print(rd)
    print(rd['a'])
    rd['a'] = {'a': 1, 'b': 2}