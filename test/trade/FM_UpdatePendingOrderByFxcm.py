# -*- coding:utf-8 -*
import requests,json,gc,sys,yaml,time
import unittest,json
sys.path.append("../../lib/common")
sys.path.append("../../lib/webAPI")
sys.path.append("../../lib/tradeOnline")
import FMCommon,TradeOnline,Auth,Account,Trade
from socketIO_client import SocketIO

userData = FMCommon.loadWebAPIYML()
userDataWebSocket = FMCommon.loadTradeOnlineYML()

userDataAuth=FMCommon.loadAuthYML()
userDataAccount=FMCommon.loadAccountYML()
userDataTrade=FMCommon.loadTradeYML()
userDataSocial=FMCommon.loadSocialYML()

class UpdatePendingOrderByFxcm(unittest.TestCase):
    def setUp(self):
        # 登录
        datas = {"account": userData['waccount'], "password": userData['wpasswd'], "remember": "false"}
        traderLoginRes = Auth.signin(userData['hostName'] + userDataAuth['signin_url'], userData['headers'], datas)
        self.assertEqual(traderLoginRes.status_code, userData['status_code_200'])
        self.token = json.loads(traderLoginRes.text)['data']['token']

    def test_UpdatePendingOrderByFxcm(self):
        '''登录->切换到MT4账号->获取交易token->新建一个挂单->修改挂单的止损止盈->退出登录'''
        userData['headers'][userData['Authorization']] = userData['Bearer'] + self.token
        # 获取福汇交易员的accountindex
        self.tradeAccountIndex = Account.getSpecialAccountIndex(headers=userData['headers'], brokerID=4)
        # 切换到MT4账号
        switchAccountRes = Account.switchAccount(userData['hostName'] + userDataAccount['switchAccount'], userData['headers'],
                                                 self.tradeAccountIndex[0])
        self.assertEqual(switchAccountRes.status_code, userData['status_code_200'])

        # 获取交易token
        getTokenRes = Trade.getToken(userData['hostName'] + userDataAccount["getToken_url"], userData['headers'])
        FMCommon.printLog('getTokenRes: ' + getTokenRes.text)
        self.assertEqual(getTokenRes.status_code, userData['status_code_200'])
        tradeToken = str(json.loads(getTokenRes.content)["data"]["Token"]).replace("=", "@")

        # 开仓获取开仓价格
        openParam = {userDataWebSocket['orderParam_cmd']: userDataWebSocket['order_cmd'],
                     userDataWebSocket['orderParam_code']: userDataWebSocket['ws_code_210'],
                     userDataWebSocket['orderParam_symbol']: "EUR/AUD",
                     userDataWebSocket['orderParam_volume']: 1000}
        openPositionRes = TradeOnline.OnlineTradeEvent.tradeEvent(self, userDataWebSocket['ws_host'], userDataWebSocket['ws_port'], {'token': "" + tradeToken}, openParam)
        self.assertEqual(openPositionRes["code"], userDataWebSocket['ws_code_0'])
        self.assertEqual(openPositionRes["rcmd"], userDataWebSocket['ws_code_210'])
        self.orderID = openPositionRes["order"]["order_id"]
        self.price = openPositionRes["order"]["price"]

        time.sleep(2)
        # 建立挂单
        createPendParam = {userDataWebSocket['orderParam_code']: userDataWebSocket['ws_code_213'],
                           userDataWebSocket['pendingParam_price']: self.price + userDataWebSocket['points'],
                           userDataWebSocket['orderParam_symbol']: "EUR/AUD",
                           userDataWebSocket['pendingParam_volume']: 1000}
        createPendingRes = TradeOnline.OnlineTradeEvent.tradeEvent(
            self, userDataWebSocket['ws_host'], userDataWebSocket['ws_port'], {'token': "" + tradeToken},createPendParam)
        self.assertEqual(createPendingRes["code"], userDataWebSocket['ws_code_0'])
        self.assertEqual(createPendingRes["rcmd"], userDataWebSocket['ws_code_213'])
        self.assertEqual(createPendingRes["order"]["symbol"], "EUR/AUD")
        self.assertEqual(createPendingRes["order"]["volume"], 1000)
        self.pending = createPendingRes["order"]["order_id"]

        time.sleep(2)
        # 删除挂单
        deletePendParam = {userDataWebSocket['orderParam_code']: userDataWebSocket['ws_code_214'],
                           userDataWebSocket['orderParam_ticket']: self.pending}
        deletePendRes = TradeOnline.OnlineTradeEvent.tradeEvent(
            self, userDataWebSocket['ws_host'], userDataWebSocket['ws_port'], {'token': "" + tradeToken},
            deletePendParam)
        self.assertEqual(deletePendRes["code"], userDataWebSocket['ws_code_0'])
        self.assertEqual(deletePendRes["rcmd"], userDataWebSocket['ws_code_214'])
        self.assertEqual(deletePendRes["order"]["order_id"], self.pending)

        time.sleep(2)
        # 平仓
        closeOrder = {userDataWebSocket['orderParam_code']: userDataWebSocket['ws_code_211'],
                      userDataWebSocket['orderParam_ticket']: self.orderID,
                      userDataWebSocket['orderParam_volume']: 1000}
        closeOrderRes = TradeOnline.OnlineTradeEvent.tradeEvent(self, userDataWebSocket['ws_host'],
                                                                userDataWebSocket['ws_port'],
                                                                {'token': "" + tradeToken}, closeOrder)
        self.assertEqual(closeOrderRes["code"], userDataWebSocket['ws_code_0'])
        self.assertEqual(closeOrderRes["rcmd"], userDataWebSocket['ws_code_211'])
        self.assertEqual(closeOrderRes['order']["order_id"], self.orderID)
        self.assertEqual(closeOrderRes["order"]["volume"], 1000)

    def tearDown(self):
        # 退出登录
        userData['headers'][userData['Authorization']] = userData['Bearer'] + self.token
        signoutRes = Auth.signout(userData['hostName'] + userDataAuth['signout_url'], datas=userData['headers'])
        self.assertEqual(signoutRes.status_code, userData['status_code_200'])

if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(UpdatePendingOrderByFxcm))
    unittest.TextTestRunner(verbosity=2).run(suite)
