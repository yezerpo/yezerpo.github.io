import os
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.cdn.v20180606 import cdn_client, models

def refresh_cdn_dirs(secret_id, secret_key, dirs):
    try:
        # 初始化认证信息
        cred = credential.Credential(secret_id, secret_key)
        
        # 配置HTTP profile
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cdn.tencentcloudapi.com"

        # 配置客户端profile
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile

        # 初始化客户端
        client = cdn_client.CdnClient(cred, "", clientProfile)

        # 构造请求参数
        req = models.PurgePathCacheRequest()
        req.Paths = dirs
        req.FlushType = "flush"  # flush表示刷新，delete表示删除（资源下线）

        # 发送请求
        resp = client.PurgePathCache(req)

        return True
    except Exception as e:
        print(f"目录刷新请求提交失败，错误信息：{e}")
        return False

if __name__ == "__main__":
    SECRET_ID = os.getenv("TENCENT_SECRET_ID")
    SECRET_KEY = os.getenv("TENCENT_SECRET_KEY")
    REFRESH_DIRS = [
        "https://yezer.cn/blog/",
    ]

    # 执行刷新
    success = refresh_cdn_dirs(
        SECRET_ID,
        SECRET_KEY,
        REFRESH_DIRS
    )

    if success:
        print("目录刷新请求提交成功。")