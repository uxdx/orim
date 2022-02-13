# 클라우드 환경에서 사용할 때 False로 바꿔주어야함.
# True인 경우, secrets.json이 같은 디렉토리 내에 있어야함.

DEBUG_MODE = True
BASE_URL = "http://localhost" if DEBUG_MODE else "https://orim-exa2k3vk2q-du.a.run.app"