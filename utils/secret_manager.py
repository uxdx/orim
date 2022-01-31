import imp
import json
import os

from settings import DEBUG_MODE

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