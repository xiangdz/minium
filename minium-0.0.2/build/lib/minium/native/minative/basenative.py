#!/usr/bin/env python3
class BaseNative:
 def __init__(self,json_conf):
  self.json_conf=json_conf
 def release(self):
  raise NotImplementedError()
 def start_wechat(self):
  raise NotImplementedError()
 def stop_wechat(self):
  raise NotImplementedError()
 def connect_weapp(self,path):
  raise NotImplementedError()
 def screen_shot(self,filename,return_format="raw"):
  raise NotImplementedError()
 def pick_media_file(self,cap_type="camera",media_type="photo",original=False,duration=5.0,names=None,):
  raise NotImplementedError()
 def input_text(self,text):
  raise NotImplementedError()
 def input_clear(self):
  raise NotImplementedError()
 def textarea_text(self,text,index=1):
  raise NotImplementedError()
 def textarea_clear(self,index=0):
  raise NotImplementedError()
 def allow_login(self):
  raise NotImplementedError()
 def allow_get_user_info(self,answer=True):
  raise NotImplementedError()
 def allow_get_location(self,answer=True):
  raise NotImplementedError()
 def handle_modal(self,btn_text="确定",title=None):
  raise NotImplementedError()
 def handle_action_sheet(self,item):
  raise NotImplementedError()
 def forward_miniprogram(self,names:list,text:str=None,create_new_chat:bool=True):
  raise NotImplementedError()
 def forward_miniprogram_inside(self,names:list,create_new_chat:bool=True):
  raise NotImplementedError()
 def send_custom_message(self,message=None):
  raise NotImplementedError()
 def phone_call(self):
  raise NotImplementedError()
 def map_select_location(self,name):
  raise NotImplementedError()
 def map_back_to_mp(self):
  raise NotImplementedError()
 def deactivate(self,duration):
  raise NotImplementedError()
 def get_authorize_settings(self):
  raise NotImplementedError()
 def back_from_authorize_setting(self):
  raise NotImplementedError()
 def authorize_page_checkbox_enable(self,name,enable):
  raise NotImplementedError()
class NativeError(RuntimeError):
 pass
# Created by pyminifier (https://github.com/liftoff/pyminifier)
