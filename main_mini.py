_OO00OO00OOO0OO00O ='//button[(contains(text(), "Đăng nhập") or contains(text(), "Log in")) and @data-e2e="top-login-button"]'#line:1
_OO0O000000O0OO00O ='slider'#line:2
_O0OOOO0O0O0OO0O00 ='rotate'#line:3
_O0OOO00OO00O0O00O ='//div[@class="secsdk-captcha-drag-icon sc-kEYyzF fiQtnm"]'#line:4
_OOOOO0O0OOOOO0OOO ='Height:'#line:5
_O0OOOOO0O000OOO0O ='Width:'#line:6
_OOOO0000OOOOOOOOO ='height'#line:7
_OOO00OO0OO000O0OO ='\\GoLogin\\profiles'#line:8
_O0O0OO0OO0OO0O0O0 ='LOCALAPPDATA'#line:9
_O00O0OO0OOOO0O00O ='width_view'#line:10
_O0000O000OOO0O0O0 ='application/json'#line:11
_OOO0O0O00O00O0O0O ='https://www.tiktok.com/'#line:12
_OOOO000000O0OO000 ='name'#line:13
_OOO0O0O0O0OOO0000 ='https://omocaptcha.com/api/createJob'#line:14
_O0O0O00OO0OOO00OO ='image_base64'#line:15
_O000O0OOOO0OO00OO ='type_job_id'#line:16
_OOO000OOO0OO00000 ='data'#line:17
_OOOOOO0OO00OOO0O0 =None #line:18
_OOOOOO00O00O0OO00 ='px'#line:19
_O0O0OO00OOO00O0O0 ='job_id'#line:20
_OOO0OO00OO0000000 ='error'#line:21
_OOO0O0O0OO0OO000O ='\n'#line:22
_O00OO0OOOO0O000OO ='src'#line:23
_OO0O0OO0OOO000OOO ='api_token'#line:24
_OO000O00OO0OO00O0 ='utf-8'#line:25
_OO0O00OOOO0O00OOO ='MainWindow'#line:26
_O00O00OOO000000O0 =True #line:27
_O00000O00000O00O0 =False #line:28
import requests ,time ,base64 #line:29
from PyQt5 import QtCore ,QtGui ,QtWidgets #line:30
import random ,os ,json #line:31
from undetected_chromedriver import Chrome ,ChromeOptions #line:32
from selenium .webdriver .common .by import By #line:33
from selenium .webdriver .common .keys import Keys #line:34
from selenium .webdriver .common .action_chains import ActionChains #line:35
from selenium .webdriver .support .ui import Select #line:36
from selenium .webdriver .support .ui import WebDriverWait #line:37
from selenium .webdriver .support import expected_conditions as EC #line:38
import sys ,openpyxl #line:39
from PyQt5 .QtWidgets import QMainWindow ,QApplication ,QWidget ,QMenu ,QAction ,QTableWidgetItem #line:40
from PyQt5 .QtCore import QThread ,pyqtSignal ,QSemaphore #line:41
from PyQt5 .QtGui import QCursor #line:42
from tkinter import messagebox #line:43
class OmoCaptcha :#line:44
        def __init__ (OO000O000O0O000OO ,O00OOO0O0OO0OOOO0 ):OO000O000O0O000OO .key =O00OOO0O0OO0OOOO0 ;OO000O000O0O000OO .headers ={'Host':'omocaptcha.com','Content-Type':_O0000O000OOO0O0O0 }#line:45
        def download_image (O00O00O000O0000OO ,O00000000OO00OOOO ,file_path ='captcha.png'):#line:46
                OO000OOO0OO0O00OO =requests .get (O00000000OO00OOOO )#line:47
                if OO000OOO0OO0O00OO .status_code ==200 :#line:48
                        with open (file_path ,'wb')as OO0O000O00O000OOO :OO0O000O00O000OOO .write (OO000OOO0OO0O00OO .content )#line:49
                        print ('Download completed.')#line:50
                else :print ('Failed to download the image.')#line:51
        def convert_img_to_base64 (O00O0O0O00OOOO0O0 ,OOOOO00OOO0OO0OOO ):#line:52
                with open (OOOOO00OOO0OO0OOO ,'rb')as O00OO0000O0000OO0 :O000OO0OO0O0000OO =base64 .b64encode (O00OO0000O0000OO0 .read ());return O000OO0OO0O0000OO .decode ('utf8')#line:53
        def getBalance (O0OO0OOOO0O000000 ):#line:54
                O0OO00OO0OOOOOOO0 ={_OO0O0OO0OOO000OOO :O0OO0OOOO0O000000 .key };O000O00O0O000OO00 =requests .post ('https://omocaptcha.com/api/getBalance',headers =O0OO0OOOO0O000000 .headers ,json =O0OO00OO0OOOOOOO0 )#line:55
                if O000O00O0O000OO00 .status_code ==200 :#line:56
                        if O000O00O0O000OO00 .json ()[_OOO0OO00OO0000000 ]==_O00000O00000O00O0 :return O000O00O0O000OO00 .json ()['balance']#line:57
                        else :return _O00000O00000O00O0 #line:58
                else :return _O00000O00000O00O0 #line:59
        def getJobResult (O0OOOOOO00OO0OO00 ,OO0O0O0O0O0000O0O ):#line:60
                O00OO0O0OO0O0OOOO ={_OO0O0OO0OOO000OOO :O0OOOOOO00OO0OO00 .key ,_O0O0OO00OOO00O0O0 :OO0O0O0O0O0000O0O }#line:61
                while _O00O00OOO000000O0 :#line:62
                        O00O0OOO0OOOOOOOO =requests .post ('https://omocaptcha.com/api/getJobResult',headers =O0OOOOOO00OO0OO00 .headers ,json =O00OO0O0OO0O0OOOO )#line:63
                        if O00O0OOO0OOOOOOOO .status_code ==200 :#line:64
                                print (O00O0OOO0OOOOOOOO .json ());O0O0OOOOOOO000O0O =O00O0OOO0OOOOOOOO .json ();OOO00O0OO0OO0OO00 =O0O0OOOOOOO000O0O ['status']#line:65
                                if OOO00O0OO0OO0OO00 =='waiting':continue #line:66
                                elif OOO00O0OO0OO0OO00 =='running':continue #line:67
                                elif OOO00O0OO0OO0OO00 =='fail':return _O00000O00000O00O0 #line:68
                                else :return O0O0OOOOOOO000O0O ['result']#line:69
                        else :return _O00000O00000O00O0 #line:70
        def creatTaskTwoObjectWeb (OO0OOOOO0OOO0O000 ,O0OO00O00OO0000OO ,OO00OO0O0OOOOOO00 ,OO0O00O0OO0OOO0OO ):#line:71
                OO0OOOOO0O0O000O0 ={_OO0O0OO0OOO000OOO :OO0OOOOO0OOO0O000 .key ,_OOO000OOO0OO00000 :{_O000O0OOOO0OO00OO :'22',_O0O0O00OO0OOO00OO :OO0OOOOO0OOO0O000 .convert_img_to_base64 (O0OO00O00OO0000OO ),_O00O0OO0OOOO0O00O :OO00OO0O0OOOOOO00 ,'height_view':OO0O00O0OO0OOO0OO }};O00OO00O0O0O00000 =requests .post (_OOO0O0O0O0OOO0000 ,headers =OO0OOOOO0OOO0O000 .headers ,json =OO0OOOOO0O0O000O0 )#line:72
                if O00OO00O0O0O00000 .status_code ==200 :#line:73
                        print (O00OO00O0O0O00000 .json ())#line:74
                        if O00OO00O0O0O00000 .json ()[_OOO0OO00OO0000000 ]==_O00000O00000O00O0 :return O00OO00O0O0O00000 .json ()[_O0O0OO00OOO00O0O0 ]#line:75
                        else :return _O00000O00000O00O0 #line:76
                else :return _O00000O00000O00O0 #line:77
        def creatTaskRotateCaptchaWeb (O0000O00O00000OOO ,O00O00O00O0OOOO00 ,OO0O0OOOOO0OO00OO ):#line:78
                O00OOO00O00O00O0O ={_OO0O0OO0OOO000OOO :O0000O00O00000OOO .key ,_OOO000OOO0OO00000 :{_O000O0OOOO0OO00OO :'23',_O0O0O00OO0OOO00OO :f"{O0000O00O00000OOO.convert_img_to_base64(O00O00O00O0OOOO00)}|{O0000O00O00000OOO.convert_img_to_base64(OO0O0OOOOO0OO00OO)}"}};O0OO00O0OO0OOOO00 =requests .post (_OOO0O0O0O0OOO0000 ,headers =O0000O00O00000OOO .headers ,json =O00OOO00O00O00O0O )#line:79
                if O0OO00O0OO0OOOO00 .status_code ==200 :#line:80
                        print (O0OO00O0OO0OOOO00 .json ())#line:81
                        if O0OO00O0OO0OOOO00 .json ()[_OOO0OO00OO0000000 ]==_O00000O00000O00O0 :return O0OO00O0OO0OOOO00 .json ()[_O0O0OO00OOO00O0O0 ]#line:82
                        else :return _O00000O00000O00O0 #line:83
                else :return _O00000O00000O00O0 #line:84
        def creatTaskSliderCaptchaWeb (O00OO00O0OOOO0000 ,O0O00O0OO00O00OO0 ,OO0000000000O0O00 ):#line:85
                O00000OO00000OO00 ={_OO0O0OO0OOO000OOO :O00OO00O0OOOO0000 .key ,_OOO000OOO0OO00000 :{_O000O0OOOO0OO00OO :'21',_O0O0O00OO0OOO00OO :O00OO00O0OOOO0000 .convert_img_to_base64 (O0O00O0OO00O00OO0 ),_O00O0OO0OOOO0O00O :OO0000000000O0O00 }};O0O0000O0OOOO0O0O =requests .post (_OOO0O0O0O0OOO0000 ,headers =O00OO00O0OOOO0000 .headers ,json =O00000OO00000OO00 )#line:86
                if O0O0000O0OOOO0O0O .status_code ==200 :#line:87
                        print (O0O0000O0OOOO0O0O .json ())#line:88
                        if O0O0000O0OOOO0O0O .json ()[_OOO0OO00OO0000000 ]==_O00000O00000O00O0 :return O0O0000O0OOOO0O0O .json ()[_O0O0OO00OOO00O0O0 ]#line:89
                        else :return _O00000O00000O00O0 #line:90
                else :return _O00000O00000O00O0 #line:91
class Ui_MainWindow :#line:92
        def setupUi (O0O0OOOOO000OOO0O ,OO000OO00O0OOOOO0 ):OO0000OO0O0000O00 =OO000OO00O0OOOOO0 ;OO0000OO0O0000O00 .setObjectName (_OO0O00OOOO0O00OOO );OO0000OO0O0000O00 .resize (1095 ,640 );O0O0OOOOO000OOO0O .centralwidget =QtWidgets .QWidget (OO0000OO0O0000O00 );O0O0OOOOO000OOO0O .centralwidget .setObjectName ('centralwidget');O0O0OOOOO000OOO0O .gridLayout =QtWidgets .QGridLayout (O0O0OOOOO000OOO0O .centralwidget );O0O0OOOOO000OOO0O .gridLayout .setObjectName ('gridLayout');O0O0OOOOO000OOO0O .frame =QtWidgets .QFrame (O0O0OOOOO000OOO0O .centralwidget );O0O0OOOOO000OOO0O .frame .setFrameShape (QtWidgets .QFrame .StyledPanel );O0O0OOOOO000OOO0O .frame .setFrameShadow (QtWidgets .QFrame .Raised );O0O0OOOOO000OOO0O .frame .setObjectName ('frame');O0O0OOOOO000OOO0O .gridLayout_2 =QtWidgets .QGridLayout (O0O0OOOOO000OOO0O .frame );O0O0OOOOO000OOO0O .gridLayout_2 .setObjectName ('gridLayout_2');O0O0OOOOO000OOO0O .frame_2 =QtWidgets .QFrame (O0O0OOOOO000OOO0O .frame );O0O0OOOOO000OOO0O .frame_2 .setFrameShape (QtWidgets .QFrame .StyledPanel );O0O0OOOOO000OOO0O .frame_2 .setFrameShadow (QtWidgets .QFrame .Raised );O0O0OOOOO000OOO0O .frame_2 .setObjectName ('frame_2');O0O0OOOOO000OOO0O .horizontalLayout =QtWidgets .QHBoxLayout (O0O0OOOOO000OOO0O .frame_2 );O0O0OOOOO000OOO0O .horizontalLayout .setObjectName ('horizontalLayout');O0O0OOOOO000OOO0O .label =QtWidgets .QLabel (O0O0OOOOO000OOO0O .frame_2 );OO000OO0OO000000O =QtGui .QFont ();OO000OO0OO000000O .setPointSize (9 );O0O0OOOOO000OOO0O .label .setFont (OO000OO0OO000000O );O0O0OOOOO000OOO0O .label .setObjectName ('label');O0O0OOOOO000OOO0O .horizontalLayout .addWidget (O0O0OOOOO000OOO0O .label );O0O0OOOOO000OOO0O .spinBox =QtWidgets .QSpinBox (O0O0OOOOO000OOO0O .frame_2 );OO000OO0OO000000O =QtGui .QFont ();OO000OO0OO000000O .setPointSize (9 );O0O0OOOOO000OOO0O .spinBox .setFont (OO000OO0OO000000O );O0O0OOOOO000OOO0O .spinBox .setMaximum (9999 );O0O0OOOOO000OOO0O .spinBox .setObjectName ('spinBox');O0O0OOOOO000OOO0O .horizontalLayout .addWidget (O0O0OOOOO000OOO0O .spinBox );O0O0OOOOO000OOO0O .checkBox =QtWidgets .QCheckBox (O0O0OOOOO000OOO0O .frame_2 );OO000OO0OO000000O =QtGui .QFont ();OO000OO0OO000000O .setPointSize (9 );O0O0OOOOO000OOO0O .checkBox .setFont (OO000OO0OO000000O );O0O0OOOOO000OOO0O .checkBox .setObjectName ('checkBox');O0O0OOOOO000OOO0O .horizontalLayout .addWidget (O0O0OOOOO000OOO0O .checkBox );O00O0OO0000000O00 =QtWidgets .QSpacerItem (884 ,20 ,QtWidgets .QSizePolicy .Expanding ,QtWidgets .QSizePolicy .Minimum );O0O0OOOOO000OOO0O .horizontalLayout .addItem (O00O0OO0000000O00 );O0O0OOOOO000OOO0O .gridLayout_2 .addWidget (O0O0OOOOO000OOO0O .frame_2 ,0 ,0 ,1 ,1 );O0O0OOOOO000OOO0O .tableWidget =QtWidgets .QTableWidget (O0O0OOOOO000OOO0O .frame );O0O0OOOOO000OOO0O .tableWidget .setContextMenuPolicy (QtCore .Qt .CustomContextMenu );O0O0OOOOO000OOO0O .tableWidget .setObjectName ('tableWidget');O0O0OOOOO000OOO0O .tableWidget .setColumnCount (4 );O0O0OOOOO000OOO0O .tableWidget .setRowCount (0 );OOOO00OO0O000OOOO =QtWidgets .QTableWidgetItem ();O0O0OOOOO000OOO0O .tableWidget .setHorizontalHeaderItem (0 ,OOOO00OO0O000OOOO );OOOO00OO0O000OOOO =QtWidgets .QTableWidgetItem ();O0O0OOOOO000OOO0O .tableWidget .setHorizontalHeaderItem (1 ,OOOO00OO0O000OOOO );OOOO00OO0O000OOOO =QtWidgets .QTableWidgetItem ();O0O0OOOOO000OOO0O .tableWidget .setHorizontalHeaderItem (2 ,OOOO00OO0O000OOOO );OOOO00OO0O000OOOO =QtWidgets .QTableWidgetItem ();O0O0OOOOO000OOO0O .tableWidget .setHorizontalHeaderItem (3 ,OOOO00OO0O000OOOO );O0O0OOOOO000OOO0O .gridLayout_2 .addWidget (O0O0OOOOO000OOO0O .tableWidget ,1 ,0 ,1 ,1 );O0O0OOOOO000OOO0O .gridLayout .addWidget (O0O0OOOOO000OOO0O .frame ,0 ,0 ,1 ,1 );OO0000OO0O0000O00 .setCentralWidget (O0O0OOOOO000OOO0O .centralwidget );O0O0OOOOO000OOO0O .menubar =QtWidgets .QMenuBar (OO0000OO0O0000O00 );O0O0OOOOO000OOO0O .menubar .setGeometry (QtCore .QRect (0 ,0 ,1095 ,26 ));O0O0OOOOO000OOO0O .menubar .setObjectName ('menubar');OO0000OO0O0000O00 .setMenuBar (O0O0OOOOO000OOO0O .menubar );O0O0OOOOO000OOO0O .statusbar =QtWidgets .QStatusBar (OO0000OO0O0000O00 );O0O0OOOOO000OOO0O .statusbar .setObjectName ('statusbar');OO0000OO0O0000O00 .setStatusBar (O0O0OOOOO000OOO0O .statusbar );O0O0OOOOO000OOO0O .retranslateUi (OO0000OO0O0000O00 );QtCore .QMetaObject .connectSlotsByName (OO0000OO0O0000O00 )#line:93
        def retranslateUi (OO0000OO0000OOO0O ,OO0O000OOOOO0OOOO ):OO00OOOOOOOOOOO0O =QtCore .QCoreApplication .translate ;OO0O000OOOOO0OOOO .setWindowTitle (OO00OOOOOOOOOOO0O (_OO0O00OOOO0O00OOO ,_OO0O00OOOO0O00OOO ));OO0000OO0000OOO0O .label .setText (OO00OOOOOOOOOOO0O (_OO0O00OOOO0O00OOO ,'Số luồng: '));OO0000OO0000OOO0O .checkBox .setText (OO00OOOOOOOOOOO0O (_OO0O00OOOO0O00OOO ,'Profile Gologin'));O00OOO00O0O0O00OO =OO0000OO0000OOO0O .tableWidget .horizontalHeaderItem (0 );O00OOO00O0O0O00OO .setText (OO00OOOOOOOOOOO0O (_OO0O00OOOO0O00OOO ,'User ID'));O00OOO00O0O0O00OO =OO0000OO0000OOO0O .tableWidget .horizontalHeaderItem (1 );O00OOO00O0O0O00OO .setText (OO00OOOOOOOOOOO0O (_OO0O00OOOO0O00OOO ,'PassWord'));O00OOO00O0O0O00OO =OO0000OO0000OOO0O .tableWidget .horizontalHeaderItem (2 );O00OOO00O0O0O00OO .setText (OO00OOOOOOOOOOO0O (_OO0O00OOOO0O00OOO ,'Cookie'));O00OOO00O0O0O00OO =OO0000OO0000OOO0O .tableWidget .horizontalHeaderItem (3 );O00OOO00O0O0O00OO .setText (OO00OOOOOOOOOOO0O (_OO0O00OOOO0O00OOO ,'Trạng Thái'))#line:94
class DriverOptions :#line:95
        def __init__ (O00OO00O00O00O000 ,O0O0000O00000000O ):O0000OO0O0OO00O00 =O0O0000O00000000O ;OOO0OOO000O00OOO0 ='prefs';O00OO00O00O00O000 .realPath =os .path .join (os .environ [_O0O0OO0OO0OO0O0O0 ],'Temp')+_OOO00OO0OO000O0OO ;O00OO00O00O00O000 .options =ChromeOptions ();O00OO00O00O00O000 .options .add_argument ('--app=https://iphey.com');O00OO00O00O00O000 .options .add_argument ('--lang=vi');O00OO00O00O00O000 .options .add_argument ('--mute-audio');O00OO00O00O00O000 .options .add_argument ('--use-fake-ui-for-media-stream');O00OO00O00O00O000 .options .add_argument ('--disable-user-media-security=true');O00OO00O00O00O000 .options .add_argument ('--disable-gpu');O00OO00O00O00O000 .options .add_argument ('--disable-infobars');O00OO00O00O00O000 .options .add_argument ('--disable-dev-shm-usage');O00OO00O00O00O000 .options .add_argument ('--no-sandbox');O00OO00O00O00O000 .options .add_argument ('--disable-notifications');O00OO00O00O00O000 .options .add_argument ('--disable-popup-blocking');O00OO00O00O00O000 .options .add_argument ('--disable-save-password-bubble');O0O0OOO000OOO0O00 ={'profile.default_content_setting_values.notifications':2 };O00OO00O00O00O000 .options .add_experimental_option (OOO0OOO000O00OOO0 ,O0O0OOO000OOO0O00 );O000OOO00O0O00OOO ={'webrtc.ip_handling_policy':'disable_non_proxied_udp','webrtc.multiple_routes_enabled':_O00000O00000O00O0 ,'webrtc.nonproxied_udp_enabled':_O00000O00000O00O0 };O00OO00O00O00O000 .options .add_experimental_option (OOO0OOO000O00OOO0 ,O000OOO00O0O00OOO );O0OO00000O0O0OOOO ={'credentials_enable_service':_O00000O00000O00O0 ,'profile.password_manager_enabled':_O00000O00000O00O0 };O00OO00O00O00O000 .options .add_experimental_option (OOO0OOO000O00OOO0 ,O0OO00000O0O0OOOO );print (f"{O00OO00O00O00O000.realPath}\\{O0000OO0O0OO00O00}");O00OO00O00O00O000 .options .add_argument (f"--user-data-dir={O00OO00O00O00O000.realPath}\\{O0000OO0O0OO00O00}");O00OO00O00O00O000 .options .add_argument ('--disable-blink-features=AutomationControlled')#line:96
class WebDriver (DriverOptions ):#line:97
        def __init__ (O0O00000OO00000OO ,O0O0OO00OOO00OO0O ,O0O0O00OOOOOOO0O0 ):DriverOptions .__init__ (O0O00000OO00000OO ,O0O0O00OOOOOOO0O0 );O0O00000OO00000OO .omo =OmoCaptcha (O0O0OO00OOO00OO0O )#line:98
        def windowScroll (O00000O00000OOO0O ):O00000O00000OOO0O .driver .execute_script ('window.scrollTo(0, document.body.scrollHeight);')#line:99
        def checkElement (O00O0OOO00000000O ,_OO0OOO0000O00O000 ,_time =15 ,mode =By .XPATH ):#line:100
                try :#line:101
                        O0000OO000OO0000O =WebDriverWait (O00O0OOO00000000O .driver ,_time ).until (EC .visibility_of_element_located ((mode ,_OO0OOO0000O00O000 )))#line:102
                        if O0000OO000OO0000O :return _O00O00OOO000000O0 #line:103
                        else :return _O00000O00000O00O0 #line:104
                except :return _O00000O00000O00O0 #line:105
        def waitAndClick (OOOO0OOO00O000000 ,_O00000OO00OO0OOOO ,mode =By .XPATH ):#line:106
                OO0OOO0O00OOO0000 =_O00000OO00OO0OOOO #line:107
                try :#line:108
                        try :OOOOO00OOO000O0O0 =WebDriverWait (OOOO0OOO00O000000 .driver ,15 ).until (EC .element_to_be_clickable ((mode ,OO0OOO0O00OOO0000 )))#line:109
                        except :OOOOO00OOO000O0O0 =WebDriverWait (OOOO0OOO00O000000 .driver ,15 ).until (EC .visibility_of_element_located ((mode ,OO0OOO0O00OOO0000 )))#line:110
                        time .sleep (.5 );OOOOO00OOO000O0O0 .click ();return _O00O00OOO000000O0 #line:111
                except :return _O00000O00000O00O0 #line:112
        def waitAndSend (O000OOOO00OOOOOOO ,_O0O00OOO00O0OOO00 ,OOOO00OO0OOO00OOO ,mode =By .XPATH ):#line:113
                O00O0OO0O0O0OO000 =_O0O00OOO00O0OOO00 #line:114
                try :#line:115
                        try :O0O0OOO0OOO000OO0 =WebDriverWait (O000OOOO00OOOOOOO .driver ,15 ).until (EC .visibility_of_element_located ((mode ,O00O0OO0O0O0OO000 )))#line:116
                        except :O0O0OOO0OOO000OO0 =WebDriverWait (O000OOOO00OOOOOOO .driver ,15 ).until (EC .element_to_be_clickable ((mode ,O00O0OO0O0O0OO000 )))#line:117
                        time .sleep (.5 );O0O0OOO0OOO000OO0 .send_keys (OOOO00OO0OOO00OOO );return _O00O00OOO000000O0 #line:118
                except :return _O00000O00000O00O0 #line:119
        def waitAndGetText (OOOOOO0O00O0000OO ,_OOO0OOO0OO0OOOOOO ,mode =By .XPATH ):#line:120
                O00OOOO0000000OO0 =_OOO0OOO0OO0OOOOOO #line:121
                try :#line:122
                        try :OO0OO0000O0O00O0O =WebDriverWait (OOOOOO0O00O0000OO .driver ,15 ).until (EC .visibility_of_element_located ((mode ,O00OOOO0000000OO0 )))#line:123
                        except :OO0OO0000O0O00O0O =WebDriverWait (OOOOOO0O00O0000OO .driver ,15 ).until (EC .element_to_be_clickable ((mode ,O00OOOO0000000OO0 )))#line:124
                        time .sleep (.5 );OO000000OO00O00O0 =OO0OO0000O0O00O0O .text .strip ();return OO000000OO00O00O0 #line:125
                except :return _O00000O00000O00O0 #line:126
        def gotoLink (OO0O000O0OOO0OOOO ,OO0O0O0OO0O00OOO0 ):OO0O000O0OOO0OOOO .driver .get (OO0O0O0OO0O00OOO0 );OO0O000O0OOO0OOOO .driver .set_page_load_timeout (100 );time .sleep (1 )#line:127
        def loginCookie (OO000OO0O0O000O00 ,OO000O00O0O00000O ):#line:128
                O00000O0OO0OO00OO =OO000O00O0O00000O .replace (' ','').split (';')#line:129
                for O000OO000O0O000O0 in O00000O0OO0OO00OO :#line:130
                        if O000OO000O0O000O0 !='':O0OO0000OO0O000OO =O000OO000O0O000O0 .split ('=');OO000OO0O0O000O00 .driver .add_cookie ({_OOOO000000O0OO000 :O0OO0000OO0O000OO [0 ],'value':O0OO0000OO0O000OO [1 ]})#line:131
                time .sleep (5 );OO000OO0O0O000O00 .driver .refresh ();OO000OO0O0O000O00 .driver .set_page_load_timeout (60 )#line:132
        def deleteAllCookie (O0OO0OOOO0OO00O0O ):O0OO0OOOO0OO00O0O .driver .delete_all_cookies ()#line:133
        def getCookieTikTok (O000OOOOOO0O0OOO0 ):#line:134
                OO0OOOO0OO0OOOO00 ='';O00OO00OOOO00O000 =O000OOOOOO0O0OOO0 .driver .get_cookies ()#line:135
                for O0O00OO0000OOOOO0 in range (len (O00OO00OOOO00O000 )):OO0000OOOO0O0O0OO =O00OO00OOOO00O000 [O0O00OO0000OOOOO0 ][_OOOO000000O0OO000 ];O00O0OOOOOO00O00O =O00OO00OOOO00O000 [O0O00OO0000OOOOO0 ]['value'];OO0OOOO0OO0OOOO00 +=f"{OO0000OOOO0O0O0OO}={O00O0OOOOOO00O00O}; "#line:136
                print (OO0OOOO0OO0OOOO00 [0 :len (OO0OOOO0OO0OOOO00 )-2 ]);return OO0OOOO0OO0OOOO00 [0 :len (OO0OOOO0OO0OOOO00 )-2 ]#line:137
        def killDriver (OOO000O00000O0O0O ):OOO000O00000O0O0O .driver .close ()#line:138
        def gotoHomeTikTok (OOOO00OO0O0O00OOO ):#line:139
                if OOOO00OO0O0O00OOO .driver .current_url !=_OOO0O0O00O00O0O0O :OOOO00OO0O0O00OOO .gotoLink (_OOO0O0O00O00O0O0O )#line:140
                else :print ('current url')#line:141
        def reloadPage (OO0OO000000O00O00 ):OO0OO000000O00O00 .driver .refresh ();OO0OO000000O00O00 .driver .set_page_load_timeout (100 );time .sleep (1 )#line:142
        def gotoProfile (OO00000OO00OO00O0 ):#line:143
                OO00000OO00OO00O0 .gotoHomeTikTok ();OO00O00O0000000O0 ='//span[contains(text(), "Hồ sơ") or contains(text(), "Profile")]';OOO0OOOO0O0000O0O =OO00000OO00OO00O0 .checkElement (OO00O00O0000000O0 ,7 )#line:144
                if OOO0OOOO0O0000O0O ==_O00000O00000O00O0 :OO00000OO00OO00O0 .waitAndClick ('//div[@id="header-more-menu-icon"]');OO00000OO00OO00O0 .waitAndClick ('//*[contains(text(), "Xem hồ sơ") or contains(text(), "View profile")]')#line:145
                else :OO00000OO00OO00O0 .waitAndClick (OO00O00O0000000O0 )#line:146
                O0OOO00OOOO0OOO0O =OO00000OO00OO00O0 .waitAndGetText ('//h1[@data-e2e="user-title"]');print ('user: ',O0OOO00OOOO0OOO0O );return O0OOO00OOOO0OOO0O #line:147
        def upPostTikTok (O0O0OO0OOOOO000OO ,OOOO0O0OO00OOOOO0 ,caption ='Hi'):#line:148
                OO0OOO0000O0OOOO0 ='//div[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]';O0000O0OO0000O000 ='//span[contains(text(), "Tải lên ") or contains(text(), "Upload ")]';O0OO0000O00000O0O =O0O0OO0OOOOO000OO .checkElement (O0000O0OO0000O000 ,15 )#line:149
                if O0OO0000O00000O0O :#line:150
                        O0O0OO0OOOOO000OO .waitAndClick (O0000O0OO0000O000 )#line:151
                        for OOOOO0OO0OO00OOOO in range (5 ):#line:152
                                OOO0O0000OOO00O00 =WebDriverWait (O0O0OO0OOOOO000OO .driver ,15 ).until (EC .presence_of_element_located ((By .CSS_SELECTOR ,'iframe')));O0O0OO0OOOOO000OO .driver .switch_to .frame (OOO0O0000OOO00O00 );OOO0O0OOO0O0O00OO =WebDriverWait (O0O0OO0OOOOO000OO .driver ,15 ).until (EC .presence_of_element_located ((By .CSS_SELECTOR ,'input[type="file"]')));OOO0O0OOO0O0O00OO .send_keys (OOOO0O0OO00OOOOO0 );O0OOO0O0O000OOOOO =O0O0OO0OOOOO000OO .checkElement (OO0OOO0000O0OOOO0 ,15 )#line:153
                                if O0OOO0O0O000OOOOO ==_O00000O00000O00O0 :O0O0OO0OOOOO000OO .reloadPage ();continue #line:154
                                else :break #line:155
                        O0O0OO0OOOOO000OO .waitAndSend (OO0OOO0000O0OOOO0 ,'');O0O0OO0OOOOO000OO .waitAndSend (OO0OOO0000O0OOOO0 ,caption );time .sleep (5 )#line:156
                        for OOOOO0OO0OO00OOOO in range (3 ):O0O0OO0OOOOO000OO .windowScroll ();time .sleep (.1 )#line:157
                        print ('click');time .sleep (5 );O0O0OO0OOOOO000OO .waitAndClick ('//button[@class="css-y1m958"]');OO0O0O0OOO00OOOO0 =O0O0OO0OOOOO000OO .checkElement ('//div[contains(text(), "Video của bạn đang được tải lên TikTok!") or contains(text(), "Your videos are being uploaded to TikTok!")]',45 )#line:158
                        if OO0O0O0OOO00OOOO0 ==_O00O00OOO000000O0 :O0O0OO0OOOOO000OO .waitAndClick ('//div[contains(text(), "Quản lý bài đăng của bạn")]');print ('upload Video Thành Công');return _O00O00OOO000000O0 #line:159
                        else :return _O00000O00000O00O0 #line:160
        def bypassCaptchaTwoObject (O0O0OO0OOO00O0OOO ):#line:161
                OO000OOO0OOOOOOOO =WebDriverWait (O0O0OO0OOO00O0OOO .driver ,15 ).until (EC .visibility_of_element_located ((By .XPATH ,"//img[@id='captcha-verify-image']")));OOOO0O00O0OO0O00O =OO000OOO0OOOOOOOO .get_attribute (_O00OO0OOOO0O000OO );OOO0O0OOO00O0O0O0 =f"image{random.randint(1,1000000)}.png";O0O0OO0OOO00O0OOO .omo .download_image (OOOO0O00O0OO0O00O ,OOO0O0OOO00O0O0O0 );O00O0OO0O0OO0O0O0 =int (OO000OOO0OOOOOOOO .size ['width']);O0OO00OOO00000O00 =int (OO000OOO0OOOOOOOO .size [_OOOO0000OOOOOOOOO ]);print (_O0OOOOO0O000OOO0O ,O00O0OO0O0OO0O0O0 ,_OOOOOO00O00O0OO00 );print (_OOOOO0O0OOOOO0OOO ,O0OO00OOO00000O00 ,_OOOOOO00O00O0OO00 );O0O00OOOOOO0O00O0 =O0O0OO0OOO00O0OOO .omo .creatTaskTwoObjectWeb (OOO0O0OOO00O0O0O0 ,O00O0OO0O0OO0O0O0 ,O0OO00OOO00000O00 )#line:162
                try :os .remove (OOO0O0OOO00O0O0O0 )#line:163
                except :pass #line:164
                if O0O00OOOOOO0O00O0 !=_O00000O00000O00O0 :OOOOO0000OOOOOOOO =O0O0OO0OOO00O0OOO .omo .getJobResult (O0O00OOOOOO0O00O0 );O000000OO0O0OO0O0 =str (OOOOO0000OOOOOOOO ).split ('|');OO00O00O00O000OO0 =list (map (int ,O000000OO0O0OO0O0 ));OO00O0O0000OO0O00 ,O00O000OOOOO00OO0 ,O00O00O0O0OO0O0O0 ,OOOO00O000O0OOOOO =OO00O00O00O000OO0 [0 ],OO00O00O00O000OO0 [1 ],OO00O00O00O000OO0 [2 ],OO00O00O00O000OO0 [3 ];print (OO00O0O0000OO0O00 ,O00O000OOOOO00OO0 ,O00O00O0O0OO0O0O0 ,OOOO00O000O0OOOOO );O0O0OO0OOO00O0OOO .actions .move_by_offset (OO00O0O0000OO0O00 ,O00O000OOOOO00OO0 ).click ().perform ();time .sleep (1 );O0O0OO0OOO00O0OOO .actions .move_by_offset (O00O00O0O0OO0O0O0 ,OOOO00O000O0OOOOO ).click ().perform ();time .sleep (1 );O0O0OO0OOO00O0OOO .waitAndClick ('//div[contains(text(), "Xác nhận")]');return _O00O00OOO000000O0 #line:165
                else :return _O00000O00000O00O0 #line:166
        def bypassRotateCaptcha (OOOOO0000000OO0O0 ):#line:167
                OO000000O0O00O00O =WebDriverWait (OOOOO0000000OO0O0 .driver ,15 ).until (EC .visibility_of_element_located ((By .XPATH ,'//img[@data-testid="whirl-inner-img"]'))).get_attribute (_O00OO0OOOO0O000OO );O00O00OOOO00OO000 =WebDriverWait (OOOOO0000000OO0O0 .driver ,15 ).until (EC .visibility_of_element_located ((By .XPATH ,'//img[@data-testid="whirl-outer-img"]'))).get_attribute (_O00OO0OOOO0O000OO );OOO0000O0000O00OO =f"image{random.randint(1,1000000)}.png";OOOOO0000000OO0O0 .omo .download_image (OO000000O0O00O00O ,OOO0000O0000O00OO );O0000000OOO000O00 =f"image{random.randint(1,1000000)}.png";OOOOO0000000OO0O0 .omo .download_image (O00O00OOOO00OO000 ,O0000000OOO000O00 );O00OO00OOO00OO0OO =OOOOO0000000OO0O0 .omo .creatTaskRotateCaptchaWeb (OOO0000O0000O00OO ,O0000000OOO000O00 )#line:168
                try :os .remove (OOO0000O0000O00OO );os .remove (O0000000OOO000O00 )#line:169
                except :pass #line:170
                if O00OO00OOO00OO0OO !=_O00000O00000O00O0 :#line:171
                        OO0O0OOOOOOO0OOO0 =int (OOOOO0000000OO0O0 .omo .getJobResult (O00OO00OOO00OO0OO ));OO0OO00O0O0O000OO =WebDriverWait (OOOOO0000000OO0O0 .driver ,15 ).until (EC .visibility_of_element_located ((By .XPATH ,_O0OOO00OO00O0O00O )));OOOOO0000000OO0O0 .actions .click_and_hold (OO0OO00O0O0O000OO ).perform ();OOO0O0O00OOOO0000 =.1 ;OOO0O0O000OOOOO0O =10 ;O0OO0OOOOOO0OO0OO =round (OO0O0OOOOOOO0OOO0 /OOO0O0O000OOOOO0O )#line:172
                        for OO000O0OOOOO000O0 in range (OOO0O0O000OOOOO0O -1 ):OOOOO0000000OO0O0 .actions .move_by_offset (O0OO0OOOOOO0OO0OO ,0 ).perform ();time .sleep (OOO0O0O00OOOO0000 )#line:173
                        OOOOO0000000OO0O0 .actions .move_by_offset (OO0O0OOOOOOO0OOO0 -(OOO0O0O000OOOOO0O -1 )*O0OO0OOOOOO0OO0OO ,0 ).perform ();OOOOO0000000OO0O0 .actions .release ().perform ();return _O00O00OOO000000O0 #line:174
                else :return _O00000O00000O00O0 #line:175
        def bypassCaptchaSlider (OO000OOOO000OO0OO ):#line:176
                O000OOOO0O000000O =WebDriverWait (OO000OOOO000OO0OO .driver ,15 ).until (EC .visibility_of_element_located ((By .XPATH ,'//img[@id="captcha-verify-image"]')));OO0O000000OO00OO0 =O000OOOO0O000000O .get_attribute (_O00OO0OOOO0O000OO );OO0O000000OO00OO0 =O000OOOO0O000000O .get_attribute (_O00OO0OOOO0O000OO );OOO00OO0O000000OO =f"image{random.randint(1,1000000)}.png";OO000OOOO000OO0OO .omo .download_image (OO0O000000OO00OO0 ,OOO00OO0O000000OO );O0OO0OO0O000O000O =int (O000OOOO0O000000O .size ['width']);O0O0OO0O000OO000O =int (O000OOOO0O000000O .size [_OOOO0000OOOOOOOOO ]);print (_O0OOOOO0O000OOO0O ,O0OO0OO0O000O000O ,_OOOOOO00O00O0OO00 );print (_OOOOO0O0OOOOO0OOO ,O0O0OO0O000OO000O ,_OOOOOO00O00O0OO00 );O00O0OOO0OO0000O0 =OO000OOOO000OO0OO .omo .creatTaskSliderCaptchaWeb (OOO00OO0O000000OO ,O0OO0OO0O000O000O )#line:177
                try :os .remove (OOO00OO0O000000OO )#line:178
                except :pass #line:179
                if O00O0OOO0OO0000O0 !=_O00000O00000O00O0 :#line:180
                        OOO0OO00O00OO0OOO =int (OO000OOOO000OO0OO .omo .getJobResult (O00O0OOO0OO0000O0 ));OOO0O0O00OO0OO0OO =WebDriverWait (OO000OOOO000OO0OO .driver ,15 ).until (EC .visibility_of_element_located ((By .XPATH ,_O0OOO00OO00O0O00O )));OO000OOOO000OO0OO .actions .click_and_hold (OOO0O0O00OO0OO0OO ).perform ();O0000OO0OOO0O0OO0 =.1 ;OOO0O00000O000O0O =10 ;O0OOOOO0O00O0O00O =round (OOO0OO00O00OO0OOO /OOO0O00000O000O0O )#line:181
                        for O00OOOOO0O000O00O in range (OOO0O00000O000O0O -1 ):OO000OOOO000OO0OO .actions .move_by_offset (O0OOOOO0O00O0O00O ,0 ).perform ();time .sleep (O0000OO0OOO0O0OO0 )#line:182
                        OO000OOOO000OO0OO .actions .move_by_offset (OOO0OO00O00OO0OOO -(OOO0O00000O000O0O -1 )*O0OOOOO0O00O0O00O ,0 ).perform ();OO000OOOO000OO0OO .actions .release ().perform ();return _O00O00OOO000000O0 #line:183
                else :return _O00000O00000O00O0 #line:184
        def getTypeCaptcha (OO0OOO00O00O0O00O ):#line:185
                O0O0OOO0O0O0O000O ='//div[contains(text(), "Kéo thanh trượt để ghép hình") or contains(text(), "Drag the slider to fit the puzzle")]';O00O0OO0OO0OO0O00 ='//div[contains(text(), "Chọn 2 đối tượng có hình dạng giống nhau:")]';OO00O000OOO0O0OO0 ='//div[contains(text(), "Xác minh để tiếp tục:")]';O0OOO0OOO0OO00OOO =OO0OOO00O00O0O00O .checkElement (O0O0OOO0O0O0O000O ,8 )#line:186
                if O0OOO0OOO0OO00OOO ==_O00O00OOO000000O0 :OO0000O00O00O000O =_O0OOOO0O0O0OO0O00 ;return OO0000O00O00O000O #line:187
                O0OOO0OOO0OO00OOO =OO0OOO00O00O0O00O .checkElement (O00O0OO0OO0OO0O00 ,8 )#line:188
                if O0OOO0OOO0OO00OOO ==_O00O00OOO000000O0 :OO0000O00O00O000O ='twoobject';return OO0000O00O00O000O #line:189
                O0OOO0OOO0OO00OOO =OO0OOO00O00O0O00O .checkElement (OO00O000OOO0O0OO0 ,8 )#line:190
                if O0OOO0OOO0OO00OOO ==_O00O00OOO000000O0 :OO0000O00O00O000O =_OO0O000000O0OO00O ;return OO0000O00O00O000O #line:191
        def loginTikTok (O0OO0O00OO0OO0OOO ,OOO00O00OOOOO000O ,OO0OO0OOOO0OO000O ):#line:192
                OOOO00O00OO00OOO0 ='//span[contains(text(), "Làm mới") or contains(text(), "Refresh")]';O0OO0O00OO0OO0OOO .waitAndClick (_OO00OO00OOO0OO00O );O0OO0O00OO0OO0OOO .waitAndClick ('//p[contains(text(), "Số điện thoại / Email / TikTok ID") or contains(text(), "Use phone / email / username")]');O0OO0O00OO0OO0OOO .waitAndClick ('//a[contains(text(), "Đăng nhập bằng email hoặc TikTok ID") or contains(text(), "Log in with email or username")]');O0OO0O00OO0OO0OOO .waitAndSend ('//input[(@placeholder="Email hoặc TikTok ID" or @placeholder="Email or username") and @name="username"]',OOO00O00OOOOO000O );O0OO0O00OO0OO0OOO .waitAndSend ('//input[@placeholder="Mật khẩu" or @placeholder="Password"]',OO0OO0OOOO0OO000O )#line:193
                for O0000OO00OO0O000O in range (10 ):#line:194
                        OO0000O0O000O0O00 ='//button[(contains(text(), "Đăng nhập") or contains(text(), "Log in")) and @type="submit"]';O0OO0O00OO0OO0OOO .waitAndClick (OO0000O0O000O0O00 );OOO000000O0OO0O0O =O0OO0O00OO0OO0OOO .checkElement (OOOO00O00OO00OOO0 ,10 )#line:195
                        if OOO000000O0OO0O0O :#line:196
                                OOOO0O0O0O0000O00 =O0OO0O00OO0OO0OOO .getTypeCaptcha ()#line:197
                                for O0000OO00OO0O000O in range (6 ):#line:198
                                        if OOOO0O0O0O0000O00 ==_OOOOOO0OO00OOO0O0 :break #line:199
                                        elif OOOO0O0O0O0000O00 ==_O0OOOO0O0O0OO0O00 :#line:200
                                                O0OO0O00OO0OO0OOO .bypassRotateCaptcha ();time .sleep (6 );OOO000000O0OO0O0O =O0OO0O00OO0OO0OOO .checkElement (OOOO00O00OO00OOO0 ,5 )#line:201
                                                if OOO000000O0OO0O0O ==_O00O00OOO000000O0 :continue #line:202
                                                else :break #line:203
                                        elif OOOO0O0O0O0000O00 ==_OO0O000000O0OO00O :#line:204
                                                O0OO0O00OO0OO0OOO .bypassCaptchaSlider ();time .sleep (6 );OOO000000O0OO0O0O =O0OO0O00OO0OO0OOO .checkElement (OOOO00O00OO00OOO0 ,5 )#line:205
                                                if OOO000000O0OO0O0O ==_O00O00OOO000000O0 :continue #line:206
                                                else :break #line:207
                                        else :#line:208
                                                O0OO0O00OO0OO0OOO .bypassCaptchaTwoObject ();time .sleep (6 );OOO000000O0OO0O0O =O0OO0O00OO0OO0OOO .checkElement (OOOO00O00OO00OOO0 ,5 )#line:209
                                                if OOO000000O0OO0O0O ==_O00O00OOO000000O0 :continue #line:210
                                                else :break #line:211
                        time .sleep (5 )#line:212
                        if O0OO0O00OO0OO0OOO .checkElement (OO0000O0O000O0O00 ,10 )==_O00O00OOO000000O0 :continue #line:213
                        else :break #line:214
                return _O00O00OOO000000O0 #line:215
        def moveChrome (O0OO0O0O0OOOO00OO ,O00O00OO0OO00000O ):O0OO0O0O0OOOO00OO .driver .execute_script (f"window.moveTo({O00O00OO0OO00000O%5*400}, {O00O00OO0OO00000O//5*200})")#line:216
        def get_driver (OO00OOO0OOO00O00O ):OO00OOO0OOO00O00O .driver =Chrome (options =OO00OOO0OOO00O00O .options ,driver_executable_path ='chromedriver.exe');OO00OOO0OOO00O00O .driver .execute_script ("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})");OO00OOO0OOO00O00O .driver .execute_cdp_cmd ('Page.addScriptToEvaluateOnNewDocument',{'source':'const newProto = navigator.__proto__;delete newProto.webdriver;navigator.__proto__ = newProto;'});OO00OOO0OOO00O00O .actions =ActionChains (OO00OOO0OOO00O00O .driver );return OO00OOO0OOO00O00O .driver #line:217
class Gologin :#line:218
        def __init__ (O000OOOOOO000000O ,O00OO0000O00O0O00 ):O000OOOOOO000000O .realPath =os .path .join (os .environ [_O0O0OO0OO0OO0O0O0 ],'Temp')+_OOO00OO0OO000O0OO ;O000OOOOOO000000O .token =O00OO0000O00O0O00 ;O000OOOOOO000000O .headers ={'Authorization':f"Bearer {O000OOOOOO000000O.token}",'Content-type':_O0000O000OOO0O0O0 }#line:219
        def getListProfile (OO00O0O00O0000OOO ):#line:220
                O0OOO0OOO0000O0OO =[];OO0O0000OOOO000O0 ='https://api.gologin.com/browser/v2';O0OO000000OOO00OO =requests .get (url =OO0O0000OOOO000O0 ,headers =OO00O0O00O0000OOO .headers ).json ();OOOO00O00O0O0O00O =O0OO000000OOO00OO ['profiles']#line:221
                for O000000O0OOOO0O00 in range (len (OOOO00O00O0O0O00O )):OO00O000OO0O00OOO =dict (name =OOOO00O00O0O0O00O [O000000O0OOOO0O00 ][_OOOO000000O0OO000 ],id =OOOO00O00O0O0O00O [O000000O0OOOO0O00 ]['id']);O0OOO0OOO0000O0OO .append (OO00O000OO0O00OOO )#line:222
                return O0OOO0OOO0000O0OO #line:223
        def clearCookieProfile (O00O0OO0O00O0OO0O ,OOO00OO0OO000O0O0 ):O0OO0O0O00OO00000 =f"https://api.gologin.com/browser/{OOO00OO0OO000O0O0}/cookies?cleanCookies=true";O0O00000O0OO00OO0 =json .dumps ([]);OOO00OOO0000O0OOO =requests .post (O0OO0O0O00OO00000 ,headers =O00O0OO0O00O0OO0O .headers ,data =O0O00000O0OO00OO0 )#line:224
class MainWindow (QMainWindow ):#line:225
        def __init__ (OO0OOOO0OO00OO000 ):#line:226
                super ().__init__ ();OO0OOOO0OO00OO000 .ui =Ui_MainWindow ();OO0OOOO0OO00OO000 .ui .setupUi (OO0OOOO0OO00OO000 );O00OOOO00O00OOO00 =[200 ,200 ,240 ,405 ]#line:227
                for O0000000000O0O0OO in range (OO0OOOO0OO00OO000 .ui .tableWidget .columnCount ()):OO0OOOO0OO00OO000 .ui .tableWidget .setColumnWidth (O0000000000O0O0OO ,O00OOOO00O00OOO00 [O0000000000O0O0OO ])#line:228
                OO0OOOO0OO00OO000 .ui .tableWidget .customContextMenuRequested .connect (OO0OOOO0OO00OO000 .contextMenu );OO0OOOO0OO00OO000 ._Thread ={};OO0OOOO0OO00OO000 .apiKeyOmo =open ('apiKey.txt','r',encoding =_OO000O00OO0OO00O0 ).read ().strip ();OO0OOOO0OO00OO000 .tokenGologin =open ('token_gologin.txt','r',encoding =_OO000O00OO0OO00O0 ).read ().strip ();OO0OOOO0OO00OO000 .gologin =Gologin (OO0OOOO0OO00OO000 .tokenGologin );OO0OOOO0OO00OO000 .listProfile =OO0OOOO0OO00OO000 .gologin .getListProfile ();OO0OOOO0OO00OO000 .indexProfile =0 ;OO0OOOO0OO00OO000 .positon =0 #line:229
        def setDelay (O000OO0OOOOO0OO00 ,OOOOOOO00O0000O00 ):O000000O000OO000O =QtCore .QEventLoop ();QtCore .QTimer .singleShot (int (1000 *OOOOOOO00O0000O00 ),O000000O000OO000O .quit );O000000O000OO000O .exec ()#line:230
        def setItemTable (O00000OOOO00O00OO ,O0O00OO00O0O0OO00 ,OOO0O0OOO00000O00 ,OO0OOOOO000OO00O0 ):O0O00OO00O0O0000O =QTableWidgetItem (OO0OOOOO000OO00O0 );O00000OOOO00O00OO .ui .tableWidget .setItem (O0O00OO00O0O0OO00 ,OOO0O0OOO00000O00 ,O0O00OO00O0O0000O )#line:231
        def getItemTable (O0000OO0O0000OOO0 ,OOO0O0OO0O000O0O0 ,O00OOO00O0000O00O ):OO0OOOO00O0OOOO00 =O0000OO0O0000OOO0 .ui .tableWidget .item (OOO0O0OO0O000O0O0 ,O00OOO00O0000O00O ).text ();return OO0OOOO00O0OOOO00 #line:232
        def contextMenu (O00O000O0OO0O0OO0 ):#line:233
                OOOOO00OOOOO0OO0O =QMenu ();OOOOO0O000O00OOOO =QAction ('Load File Data');OOOOO00OOOOO0OO0O .addAction (OOOOO0O000O00OOOO );O00O0OOO0000000OO =QMenu ('a');OOOOO000000O0OOO0 =QAction ('Load File Excel');OOOOOO0OO00OOO00O =QAction ('Load File Txt');O00O0OOO0000000OO .addActions ([OOOOO000000O0OOO0 ,OOOOOO0OO00OOO00O ]);OOOOO0O000O00OOOO .setMenu (O00O0OOO0000000OO );O0O00O00O0OO0O000 =QAction ('Bắt Đầu');OOOOO00OOOOO0OO0O .addAction (O0O00O00O0OO0O000 );O00OO000O00O0O0OO =QAction ('Kết Thúc');OOOOO00OOOOO0OO0O .addAction (O00OO000O00O0O0OO );OOO00O00OO0O0OO0O =QAction ('Xuất File Cookie');OOOOO00OOOOO0OO0O .addAction (OOO00O00OO0O0OO0O );OO0O0OOO0O0OOO00O =OOOOO00OOOOO0OO0O .exec (QCursor .pos ())#line:234
                if OO0O0OOO0O0OOO00O ==OOOOO000000O0OOO0 :#line:235
                        O000OO00O0O00OOO0 =openpyxl .load_workbook ('data.xlsx');O00OOO0OOO0OOOO00 =O000OO00O0O00OOO0 .active #line:236
                        for O0OOOOOO0OOOO0OOO in O00OOO0OOO0OOOO00 .iter_rows ():#line:237
                                OO0OO00O0OO0OO000 =O0OOOOOO0OOOO0OOO [0 ].value ;OO000OO0O0000OOO0 =O0OOOOOO0OOOO0OOO [1 ].value #line:238
                                if OO0OO00O0OO0OO000 !=_OOOOOO0OO00OOO0O0 and OO000OO0O0000OOO0 !=_OOOOOO0OO00OOO0O0 :O0OO0OO0O000000O0 =O00O000O0OO0O0OO0 .ui .tableWidget .rowCount ();O00O000O0OO0O0OO0 .ui .tableWidget .insertRow (O0OO0OO0O000000O0 );O00O000O0OO0O0OO0 .setItemTable (O0OO0OO0O000000O0 ,0 ,OO0OO00O0OO0OO000 );O00O000O0OO0O0OO0 .setItemTable (O0OO0OO0O000000O0 ,1 ,OO000OO0O0000OOO0 )#line:239
                if OO0O0OOO0O0OOO00O ==OOOOOO0OO00OOO00O :#line:240
                        OO0O00O0OO0O00O0O =open ('data.txt','r',encoding =_OO000O00OO0OO00O0 ).read ().split (_OOO0O0O0OO0OO000O )#line:241
                        for OO00OOOO00O0O0000 in range (len (OO0O00O0OO0O00O0O )):#line:242
                                if '|'in OO0O00O0OO0O00O0O [OO00OOOO00O0O0000 ]and len (OO0O00O0OO0O00O0O [OO00OOOO00O0O0000 ])>10 :O0O00O0OOOOO0OOOO =OO0O00O0OO0O00O0O [OO00OOOO00O0O0000 ].strip ().split ('|');OO0OO00O0OO0OO000 ,OO000OO0O0000OOO0 =O0O00O0OOOOO0OOOO [0 ],O0O00O0OOOOO0OOOO [1 ];O0OO0OO0O000000O0 =O00O000O0OO0O0OO0 .ui .tableWidget .rowCount ();O00O000O0OO0O0OO0 .ui .tableWidget .insertRow (O0OO0OO0O000000O0 );O00O000O0OO0O0OO0 .setItemTable (O0OO0OO0O000000O0 ,0 ,OO0OO00O0OO0OO000 );O00O000O0OO0O0OO0 .setItemTable (O0OO0OO0O000000O0 ,1 ,OO000OO0O0000OOO0 )#line:243
                if OO0O0OOO0O0OOO00O ==O0O00O00O0OO0O000 :#line:244
                        if O00O000O0OO0O0OO0 .ui .tableWidget .rowCount ()==0 :messagebox .showwarning (title ='Warning',message ='Vui Lòng Load File Data Trước Khi Chạy')#line:245
                        else :#line:246
                                OOOOO0O00OOOO000O =O00O000O0OO0O0OO0 .ui .spinBox .value ()#line:247
                                if OOOOO0O00OOOO000O >len (O00O000O0OO0O0OO0 .listProfile ):messagebox .showerror (title ='Error',message ='Số Profile Không Được Nhỏ Hơn Số Luồng')#line:248
                                else :#line:249
                                        if OOOOO0O00OOOO000O ==0 :OOOOO0O00OOOO000O =1 #line:250
                                        O00O000O0OO0O0OO0 .semaphore =QSemaphore (OOOOO0O00OOOO000O )#line:251
                                        for OO00OOOO00O0O0000 in range (O00O000O0OO0O0OO0 .ui .tableWidget .rowCount ()):#line:252
                                                OO0OO00O0OO0OO000 =O00O000O0OO0O0OO0 .getItemTable (OO00OOOO00O0O0000 ,0 );OO000OO0O0000OOO0 =O00O000O0OO0O0OO0 .getItemTable (OO00OOOO00O0O0000 ,1 )#line:253
                                                if O00O000O0OO0O0OO0 .indexProfile >len (O00O000O0OO0O0OO0 .listProfile )-1 :O00O000O0OO0O0OO0 .indexProfile =0 #line:254
                                                O00O000O0OO0O0OO0 ._Thread [OO00OOOO00O0O0000 ]=Program (O00O000O0OO0O0OO0 ,OO00OOOO00O0O0000 ,OO0OO00O0OO0OO000 ,OO000OO0O0000OOO0 ,O00O000O0OO0O0OO0 .apiKeyOmo ,O00O000O0OO0O0OO0 .listProfile [O00O000O0OO0O0OO0 .indexProfile ]['id']);O00O000O0OO0O0OO0 ._Thread [OO00OOOO00O0O0000 ].start ();O00O000O0OO0O0OO0 ._Thread [OO00OOOO00O0O0000 ].callBackData .connect (O00O000O0OO0O0OO0 .setItemTable );O00O000O0OO0O0OO0 .indexProfile +=1 ;O00O000O0OO0O0OO0 .setDelay (1 )#line:255
                if OO0O0OOO0O0OOO00O ==OOO00O00OO0O0OO0O :#line:256
                        if O00O000O0OO0O0OO0 .ui .tableWidget .rowCount ()>0 :#line:257
                                OO0O00O0OO0O00O0O =open ('cookies.txt','w',encoding =_OO000O00OO0OO00O0 )#line:258
                                for OO00OOOO00O0O0000 in range (O00O000O0OO0O0OO0 .ui .tableWidget .rowCount ()):OO0OO0OOOO00OOOOO =O00O000O0OO0O0OO0 .getItemTable (OO00OOOO00O0O0000 ,2 );OO0O00O0OO0O00O0O .write (OO0OO0OOOO00OOOOO +_OOO0O0O0OO0OO000O )#line:259
        def killThread (O0000OOOOO000O000 ,OO0OOO0OO000O00O0 ):#line:260
                try :O0000OOOOO000O000 ._Thread [OO0OOO0OO000O00O0 ].terminate ();O0000OOOOO000O000 .setItemTable (OO0OOO0OO000O00O0 ,3 ,' Kết Thúc')#line:261
                except :O0000OOOOO000O000 .setItemTable (OO0OOO0OO000O00O0 ,3 ,' Luồng Chưa Khởi Chạy Hoặc Có Lỗi Khác')#line:262
class Program (QThread ):#line:263
        callBackData =pyqtSignal (int ,int ,str )#line:264
        def __init__ (O00O00000O000OO0O ,O000O000O00O0000O ,O0O00O0OO00OOOO00 ,O0O0O0OOO00OOO0O0 ,O0O0OO0OO00OOOO00 ,O0O0OO00O0O0O00O0 ,O00000OOO00O00OO0 ):super ().__init__ ();O00O00000O000OO0O .path =O000O000O00O0000O ;O00O00000O000OO0O .row =O0O00O0OO00OOOO00 ;O00O00000O000OO0O .tk =O0O0O0OOO00OOO0O0 ;O00O00000O000OO0O .mk =O0O0OO0OO00OOOO00 ;O00O00000O000OO0O .apiKey =O0O0OO00O0O0O00O0 ;O00O00000O000OO0O .idProfile =O00000OOO00O00OO0 #line:265
        def run (O00O0OO000OOOOOO0 ):#line:266
                O0O0O0OOOO0O0OO00 ='error.txt';O0O00O00OOO0O0OOO ='a+'#line:267
                try :#line:268
                        O00O0OO000OOOOOO0 .path .semaphore .acquire ();O00O0OO000OOOOOO0 .callBackData .emit (O00O0OO000OOOOOO0 .row ,3 ,'Start');O0OO0OOOO000OOOOO =WebDriver (O00O0OO000OOOOOO0 .apiKey ,O00O0OO000OOOOOO0 .idProfile )#line:269
                        try :O00OO00OOO0OOO000 =O0OO0OOOO000OOOOO .get_driver ()#line:270
                        except :time .sleep (5 );O00OO00OOO0OOO000 =O0OO0OOOO000OOOOO .get_driver ()#line:271
                        O00O0OO000OOOOOO0 .callBackData .emit (O00O0OO000OOOOOO0 .row ,3 ,' Tiến hành mở Chrome');O0OO0OOOO000OOOOO .deleteAllCookie ();O00O0OO000OOOOOO0 .callBackData .emit (O00O0OO000OOOOOO0 .row ,3 ,' Di chuyển đến Trang chủ TikTok');O0OO0OOOO000OOOOO .gotoLink (_OOO0O0O00O00O0O0O );O0OOOO0O000O0OOOO =O0OO0OOOO000OOOOO .checkElement (_OO00OO00OOO0OO00O ,10 )#line:272
                        if O0OOOO0O000O0OOOO ==_O00000O00000O00O0 :O00O0OO000OOOOOO0 .callBackData .emit (O00O0OO000OOOOOO0 .row ,3 ,' Tiến hành clear cookie');O0OO0OOOO000OOOOO .deleteAllCookie ();O00O0OO000OOOOOO0 .path .gologin .clearCookieProfile (O00O0OO000OOOOOO0 .idProfile );O0OO0OOOO000OOOOO .reloadPage ()#line:273
                        O00O0OO000OOOOOO0 .callBackData .emit (O00O0OO000OOOOOO0 .row ,3 ,' Tiến hành đăng nhập');O0OO0OOOO000OOOOO .loginTikTok (O00O0OO000OOOOOO0 .tk ,O00O0OO000OOOOOO0 .mk );O0O0O000O0000OOO0 ='//span[contains(text(), "Bạn truy cập dịch vụ của chúng tôi quá thường xuyên."")]'#line:274
                        if O0OO0OOOO000OOOOO .checkElement (O0O0O000O0000OOO0 ,10 )==_O00O00OOO000000O0 :#line:275
                                O00O0OO000OOOOOO0 .callBackData .emit (O00O0OO000OOOOOO0 .row ,3 ,' Dính truy cập thường xuyên')#line:276
                                try :O0OO0OOOO000OOOOO .killDriver ()#line:277
                                except :pass #line:278
                                with open (O0O0O0OOOO0O0OO00 ,O0O00O00OOO0O0OOO ,encoding =_OO000O00OO0OO00O0 )as O0O00000OO0000O00 :O0O00000OO0000O00 .write (f"{O00O0OO000OOOOOO0.tk}|{O00O0OO000OOOOOO0.mk}"+_OOO0O0O0OO0OO000O )#line:279
                                time .sleep (5 );O00O0OO000OOOOOO0 .path .semaphore .release ()#line:280
                        O0OO0O0OOOOO0OO0O =os .listdir (f"{os.getcwd()}\\video");OOOOOOOOOOO0OO0O0 =f"{os.getcwd()}\\video\\{random.choice(O0OO0O0OOOOO0OO0O)}";print (OOOOOOOOOOO0OO0O0 );O00O0OO000OOOOOO0 .callBackData .emit (O00O0OO000OOOOOO0 .row ,3 ,' Tiến hành up video');O0OO0OOOO000OOOOO .upPostTikTok (OOOOOOOOOOO0OO0O0 );OO00O000O0O0O0O0O =_OOOOOO0OO00OOO0O0 ;O00O0OO000OOOOOO0 .callBackData .emit (O00O0OO000OOOOOO0 .row ,3 ,' Lấy tên User')#line:281
                        for OOOO0OOOO0O0OOO00 in range (3 ):#line:282
                                OO00O000O0O0O0O0O =O0OO0OOOO000OOOOO .gotoProfile ()#line:283
                                if OO00O000O0O0O0O0O ==_O00000O00000O00O0 :O0OO0OOOO000OOOOO .reloadPage ();time .sleep (3 );continue #line:284
                                else :break #line:285
                        O00O0OO000OOOOOO0 .callBackData .emit (O00O0OO000OOOOOO0 .row ,3 ,' Tiến hành get cookie');OOO0O0O0OO0OOOOOO =O0OO0OOOO000OOOOO .getCookieTikTok ();O00O0OO000OOOOOO0 .callBackData .emit (O00O0OO000OOOOOO0 .row ,2 ,OOO0O0O0OO0OOOOOO );O00O0OO000OOOOOO0 .callBackData .emit (O00O0OO000OOOOOO0 .row ,3 ,' Lưu dữ liệu vào file');O0O00000OO0000O00 =open ('output.txt',O0O00O00OOO0O0OOO ,encoding =_OO000O00OO0OO00O0 );O0O00000OO0000O00 .write (f"{OO00O000O0O0O0O0O}|{OOO0O0O0OO0OOOOOO}"+_OOO0O0O0OO0OO000O );O00O0OO000OOOOOO0 .callBackData .emit (O00O0OO000OOOOOO0 .row ,3 ,' Kết thúc');O0OO0OOOO000OOOOO .deleteAllCookie ();O00O0OO000OOOOOO0 .path .gologin .clearCookieProfile (O00O0OO000OOOOOO0 .idProfile );O0OO0OOOO000OOOOO .killDriver ();time .sleep (2 );O00O0OO000OOOOOO0 .path .semaphore .release ();time .sleep (2 )#line:286
                except Exception as O00O00O0O0OOOO000 :#line:287
                        print (O00O00O0O0OOOO000 );O00O0OO000OOOOOO0 .callBackData .emit (O00O0OO000OOOOOO0 .row ,3 ,' Lỗi khi thao tác trên trình duyệt')#line:288
                        try :O0OO0OOOO000OOOOO .killDriver ()#line:289
                        except :pass #line:290
                        with open (O0O0O0OOOO0O0OO00 ,O0O00O00OOO0O0OOO ,encoding =_OO000O00OO0OO00O0 )as O0O00000OO0000O00 :O0O00000OO0000O00 .write (f"{O00O0OO000OOOOOO0.tk}|{O00O0OO000OOOOOO0.mk}"+_OOO0O0O0OO0OO000O )#line:291
                        time .sleep (5 );O00O0OO000OOOOOO0 .path .semaphore .release ()#line:292
if __name__ =='__main__':app =QApplication (sys .argv );app .setStyle ('Fusion');main_win =MainWindow ();main_win .show ();app .exec ()