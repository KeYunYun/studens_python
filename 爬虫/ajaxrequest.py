import urllib.request
import ssl

url='https://user.qzone.qq.com/944869444/infocenter'

headers={
    'Host': 'isdspeed.qq.com',
    'Connection':'keep-alive',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Referer':'https://user.qzone.qq.com/944869444/infocenter',
    'Cookie':'tvfe_boss_uuid=a4888980bdf763d8; RK=MbVas8xqS7; pgv_pvi=4898652160; __Q_w_s__QZN_TodoMsgCnt=1; o_cookie=944869444; pac_uid=1_944869444; __Q_w_s_hat_seed=1; pgv_si=s9098013696; ptisp=cm; ptcz=ffc39837b5ac90609eb945f15a716c997b757f701a8d1194bf090b93b552787d; pt2gguin=o0944869444; uin=o0944869444; skey=@tWKyhwrd0; p_uin=o0944869444; p_skey=QWCCFkg5-amHyETL5NK6McUo6De9lLshti2WqdMqzcE_; pt4_token=4Rhi9L862nxM4w9iiPzAgC20l7KdZSw7T4U9yJLtED8_; Loading=Yes; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; qzmusicplayer=qzone_player_944869444_1505383521742; qz_screen=1366x768; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=28; pgv_pvid=5661819260; pgv_info=ssid=s4969711163&pgvReferrer=; rv2=80101ECC46BE0B3173EC00490837E14238C13275EC20229577; property20=40ABC0745216ACFA158FDE30BF9A6CE35334C333A2C3E0BFB143B96FEDE6F5C5BF944296B7667639; x-stgw-ssl-info=06d1d76e9dd6314e4de91dff821cf9eb|0.303|1505385864.194|5|r|I|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|237000|0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71'
}

context=ssl._create_unverified_context()

request=urllib.request.Request(url,headers=headers)

respond=urllib.request.urlopen(request,context)

print(respond.read().encode('uft8'))