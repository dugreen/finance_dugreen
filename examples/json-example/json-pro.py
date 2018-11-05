#!coding:utf-8

import json

def main():
    data = {'name' : 'ACME','shares' : 100,'price' : 542.23}
    
    # 字典转json字串(字符串)
    json_str = json.dumps(data)
    # json字串转字典
    data = json.loads(json_str)

    with open('data.json','wt') as f:
        json.dump(data,f)
    
    exit()
    with open('data.json','rt') as f:
        data = json.load(f)


if __name__ == "__main__":
    main()
