import json
import os

# 클라우드 환경에서 사용할 때 False로 바꿔주어야함.
# True인 경우, secrets.json이 같은 디렉토리 내에 있어야함.

DEBUG_MODE = True

def access_secret(secret:str) -> str:
    def access_secret_as_env(secret:str):
        env = os.environ.get(secret)
        if env.__contains__('{'):
            # 환경변수값이 json 파일인 경우
            return json.loads(env)
        else:
            # 환경변수값이 문자열 인 경우
            return env
    def access_secret_as_file(secret:str):
        with open("secrets.json") as jsonFile:
            secrets = json.load(jsonFile)
            jsonFile.close()
        return secrets[secret]

    return access_secret_as_file(secret) if DEBUG_MODE else access_secret_as_env(secret)



if __name__ == '__main__':
    print(access_secret('FLASK_KEY'))
    pass