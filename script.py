from bilibili_api import Credential,live,user,sync
from win10toast import ToastNotifier
room = live.LiveDanmaku(2450440)
toaster = ToastNotifier()
@room.on('DANMU_MSG')
async def get_dan(e):
    if e['data']['info'][2][0]==33605910:
        toaster.show_toast("啵啵小狗341发布了新弹幕",e['data']['info'][1],duration=10)
sync(room.connect())
