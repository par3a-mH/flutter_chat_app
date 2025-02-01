from flet import *
import json
from time import sleep
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  
import socket
import time
import threading
import json
import os
import datetime
wallpaper = 'assets/icons/wallpaper.png'
w= 1000
h=800
color = {
    "ocean_blue_gradient": {
        "start": "#1b9fbb",
        "end": "#46b0e6"
    },
    "ocean_blue": "#1b9fbb",
    "gray_icon": "#636368",
    "white_text_font": "#b9b8ba",
    "online_status_green": "#0ac71c",
    "seen_double_tick": "#8bc854",
    "chat_bar_black": "#1e1e28",
    "search_bar_black": "#13131b",
    "type_bar_black": "#1e1e28",
    "side_bar_black": "#15151b"
}

blue_gradient=LinearGradient(['#1b9fbb', '#46b0e6'])
sbw = 50
s_bw = 270
csw = 300
dmw = w-300-50
br = 12
s_btn_w = 40
s_btn_h = 35 
sbc = '#13131b'
csc = '#1e1e28'
dmc = '#282828'
sb_ic = '#636368'
s_btn_h_c ='#E6353535'
ic = "#636368"
nac = '#25d366'
chat_screen_padding = 20
ih_br = 15
htc = "#b9b8ba"
rc = "#363636"
sc = "#035d4d"
mtc = "#689e94"
smc = "#e4e4e4"
get = '#e4e4e4'
# Login data
mypassword = 'dudj hfik tesh esac'  
email = 'prlava0012@gmail.com'  


def send_email(to_email, code):
    try:
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = to_email
        msg['Subject'] = 'Your Login Code'
        body = f'Your login code is: {code}'
        msg.attach(MIMEText(body, 'plain'))
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp_obj:
            smtp_obj.ehlo()
            smtp_obj.starttls()
            smtp_obj.login(email, mypassword)
            smtp_obj.send_message(msg)
        return True
    except Exception as e:
        print(e)
        return False

def check_internet_connection():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

class App(UserControl):
  def __init__(self, pg: Page):
        super().__init__()
        self.pg = pg
        self.pg.window_maximizable = True
        self.pg.window_minimizable = True
        self.pg.window_bgcolor = colors.TRANSPARENT
        self.pg.bgcolor = colors.TRANSPARENT
        self.enable = False
        self.files = [f for f in os.listdir('assets/profile/') if os.path.isfile(os.path.join('assets/profile/', f))]
        
        self.pg.window_title_bar_hidden = True
        self.pg.window_frameless = False
        self.login_data = self.load_login_data()
        with open('login_data.json', 'r') as file:
          user_data = json.load(file)
          self.userid = user_data['username']
          self.userpassword = user_data['password']
          self.useremail = user_data['email']

        if self.login_data:
            self.containers_init()
            self.init_helper()
        else:
            self.login_page()

  def load_login_data(self):
        try:
            with open('login_data.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return None

  def save_login_data(self, data):
        with open('login_data.json', 'w') as file:
            json.dump(data, file)
  

  def login_page(self):
      # Set up window properties  
        self.pg.window_max_width = 580  
        self.pg.window_max_height = 740  
        self.pg.padding = 0  
        self.pg.window_full_screen = True  
        # Create containers and components  
        self.username_field = TextField(  width=280,  height=40,  hint_text='Username',  border='underline',  color='#303030',prefix_icon=icons.PERSON_ADD, 
                                        border_radius=11, on_change=lambda e: self.update_username(e.control.value)  
                                    )
        self.username = Container(self.username_field, padding=padding.only(40, 20))


        self.password_field = TextField(width=280, height=40,  hint_text='Password',  border='underline',  can_reveal_password=True,  password=True,  color='#303030',prefix_icon=icons.LOCK,  
                                        border_radius=11,  
                                        on_change=lambda e: self.update_password(e.control.value)  
                                    )

        self.password = Container(self.password_field,padding=padding.only(40, 20) )



        self.email_field = TextField(width=280,  height=40,  hint_text='Email',  border='underline',  color='#303030',  prefix_icon=icons.EMAIL,
                                     on_change=lambda e: self.update_email(e.control.value)  
                                    )
        

        self.email = Container(      self.email_field,
                                     padding=padding.only(40, 20) 
                                )
        
        body = Container(  
            Container(  
                Stack([  
                    Container(  
                        border_radius=11,  
                        rotate=Rotate(0.98 * 3.14),  
                        width=360,  
                        height=560,  
                        bgcolor='#80ffffff'  
                    ),  
                    Container( 
                        Container(  
                            Column([  
                                Container(  
                                    Image(  
                                        src='assets/icons/logo.png',  
                                        width=60,  
                                    ), padding=padding.only(150, 20),  

                                ),  
                                Text(  
                                    "Sign Up",  
                                    width=360,  
                                    size=30,  
                                    weight='w900',  
                                    text_align='center'  
                                ),  
                                Text(  
                                    "Please Sign up to your account",  
                                    width=360,  
                                    text_align='center'  
                                ),  
                                self.username,

                                self.password,
                                  
                                self.email,

                                Container(  
                                    TextButton(  
                                        "I forgot my password"  
                                    ), padding=padding.only(40), on_click=self.handle_login

                                ),  
                                Container(  
                                    ElevatedButton(  
                                        content=Text(  
                                            'Sign Up',  
                                            color='white',  
                                            weight='w500',  

                                        ), width=280, bgcolor='black',
                                        on_click=self.handle_login,
                                        
                                    ), padding=padding.only(40, 10)  
                                ),  
                                Container(  
                                    Row([  
                                        TextButton(  
                                            "Already have an account?"  
                                        )  
                                    ]), padding=padding.only(40)  
                                )  

                            ]),  
                        ),  
                        width=360,  
                        height=560,  
                        bgcolor='#99ffffff',  
                        border_radius=11  
                    )  
                ]),  
                padding=110,  
                width=360,  
                height=560  
            ),  

            width=580,  
            height=740,  
            gradient=LinearGradient(['#4a90e2', '#50e3c2'])  
        )  

        # Add body to the page  
        self.pg.add(body)  

  def update_username(self, value: str):  
        self.username = value  

  def update_password(self, value: str):  
        self.password = value  

  def update_email(self, value: str):  
        self.email = value  
  

  def handle_login(self,e):
        if True:
            code = random.randint(10000, 99999)
            self.code = code
            if send_email(self.email, code):
                self.pg.controls.clear()  # پاک کردن محتوای فعلی صفحه
                self.timer_text = Container(
                                    content=Text(
                                        "1:00"
                                    ),padding=padding.only(40)
                                )
                
                self.recive_again_button = TextButton("Didn't you receive the code?", disabled=True, on_click=self.handle_login) #   
                self.recive_again = Container(self.recive_again_button, padding=padding.only(30)) # در یک Container قرار دادیم

                self.sub_button =  ElevatedButton(content=Text('Submit',color='white',weight='w500'),width=280, bgcolor='black',on_click=self.verify_code)
                self.submit_button = Container(self.sub_button,padding=padding.only(40, 10))

                self.recived_code_field =  TextField(  width=280,  height=40,  hint_text='Code',  border='underline',  color='#303030',  border_radius=11,  
                                        on_change=lambda e: self.update_username(e.control.value)  ,
                                        max_length=5,
                                        keyboard_type=KeyboardType.NUMBER  
                                    )
                self.recived_code = Container(  self.recived_code_field
                                    , padding=padding.only(40, 20)
                                )

                
                self.pg.add( Container(  
            Container(  
                Stack([  
                    Container(  
                        border_radius=11,  
                        rotate=Rotate(0.98 * 3.14),  
                        width=360,  
                        height=370,  
                        bgcolor='#80ffffff'  
                    ),  
                    Container( 
                        Container(  
                            Column([  
                                Text(  
                                    "Sign Up",  
                                    width=360,  
                                    size=30,  
                                    weight='w900',  
                                    text_align='center'  
                                ),  


                                Text(  
                                    "Please enter the code that was sent to your email.",  
                                    width=360,  
                                    text_align='center'
                                ),  
                                self.recived_code,

                                self.timer_text,
                                
                                self.recive_again,

                                self.submit_button,  
 

                            ]),  
                        ),  
                        width=360,  
                        height=370,  
                        bgcolor='#99ffffff',  
                        border_radius=11  
                    )  
                ]),  
                padding=110,  
                width=360,  
                height=560  
            ),  

            width=580,  
            height=740,  
            gradient=LinearGradient(['#4a90e2', '#50e3c2'])  
        
        ))
                self.code = code
                self.timer = 60
                self.start_timer()
                self.pg.update()
                



  def verify_code(self, e):

      code = self.recived_code_field.value

      if code == str(self.code):
        
          self.save_login_data({'username': self.username_field,'password':self.password_field,'email':self.email_field})
          self.pg.controls.clear()
          self.containers_init()
          self.init_helper()
      else:
          print('Incorrect code')

  def start_timer(self):
        threading.Thread(target=self.update_timer, daemon=True).start()  # شروع تایمر در یک نخ جداگانه


  def update_timer(self):
    total_seconds =  60  #  دقیقه به ثانیه
    while total_seconds >= 0:
        mins, secs = divmod(total_seconds, 60)
        self.timer_text.content.value = f"{mins:02}:{secs:02}"  # به‌روزرسانی متن تایمر
        self.timer_text.update()  # به‌روزرسانی فقط عنصر تایمر
        time.sleep(1)
        total_seconds -= 1
    self.recive_again.content.disabled = False
    self.recive_again.update()
    self.timer_text.update()  # به‌روزرسانی فقط عنصر تایمر
    


  


  def containers_init(self):
        self.chat_user_details()
        self.dm_screen_content_main()
        self.chats_column_f()
        self.chat_screen()
        self.sidebar()
        self.base_containers()
        # تنظیم ابعاد پنجره
        self.pg.window_max_width = 1000  # یا هر مقداری که مناسب است
        self.pg.window_max_height = 800  # یا هر مقداری که مناسب است
        self.pg.update()  #  برای اعمال تغییرات




  def init_helper(self):
    self.pg.window_full_screen = False
    self.pg.add(
      Container(
        clip_behavior=ClipBehavior.ANTI_ALIAS,
        border_radius=br,
        expand=True,
        bgcolor=dmc,
        content=Stack(
          expand=True,
          controls=[
            Row(
              spacing=0,
              controls=[
                self.sidebar,
                self.chats_screen,
                self.dm_screen,
              ]
            ),
            
            self.settings_popup,

            self.emoji_popup
            
            
          ]
        )
      )
    )  
  
  def containers_init(self):
    self.chat_user_details()
    self.dm_screen_content_main()
    self.chats_column_f()
    self.chat_screen()
    self.sidebar()
    self.base_containers()
    # تنظیم ابعاد پنجره
    self.pg.window_max_width = 1000  # یا هر مقداری که مناسب است
    self.pg.window_max_height = 800  # یا هر مقداری که مناسب است
    self.pg.update()  #  برای اعمال تغییرات
    
  def base_containers(self):
    self.sidebar = Container(
      padding=padding.only(top=50,bottom=50),
      width=sbw,
      bgcolor=color['side_bar_black'],
      content=self.sidebar_column,
    )
    self.chats_screen = Container(
      animate=animation.Animation(500,AnimationCurve.BOUNCE_OUT),
      width=csw,
      bgcolor=csc,
      content=self.chat_screen_items,
    )
    self.dm_screen = Container(
      expand=True,
      bgcolor=dmc,
      content=self.dm_screen_content
    )

  def sidebar_btn_hovered(self,e:HoverEvent):
    if e.data == 'true':
      e.control.bgcolor = s_btn_h_c
      
    else:  
      e.control.bgcolor = None
    e.control.update()  
  
  def show_hide_csa(self,e: TapEvent):
    if e.control.data == 'opened':
      self.chats_screen.width = 0
      self.sidebar.bgcolor = csc
      e.control.data = 'closed'
    else:
      self.chats_screen.width = csw
      self.sidebar.bgcolor = sbc
      e.control.data = 'opened'
        
    e.control.update()    
    self.sidebar.update()
    self.chats_screen.update()


  def sidebar(self):
    self.sidebar_column = Column(
      horizontal_alignment='center',
      alignment='spaceBetween',
      spacing=0,
      controls=[
        Column(
          controls=[
            Container(
              # on_hover=self.sidebar_btn_hovered,
              alignment=alignment.center,
              height=s_btn_h,
              width=s_btn_w,
              bgcolor = s_btn_h_c,
              border_radius=5,
              content=Row(
                spacing=0,
                alignment='spaceBetween',
                vertical_alignment='center',
                controls=[
                  Container(
                    offset=transform.Offset(0, 0),
                    animate_offset=animation.Animation(1000),
                    clip_behavior=ClipBehavior.ANTI_ALIAS,
                    height=17,
                    width=3,
                    bgcolor=ic,
                    border_radius=5
                  ),
                  
                  Container(
                    margin=margin.only(right=10),
                    content= Stack(
                      controls=[
                        Container(
                          clip_behavior=ClipBehavior.ANTI_ALIAS,
                          height=20,
                          width=20,
                          content=Image(
                            src='assets/icons/c.png',
                            fit=ImageFit.COVER,
                            color=sb_ic
                          )
                        ),
                        Container(
                          right=1,
                          top=1,
                          clip_behavior=ClipBehavior.ANTI_ALIAS,
                          height=8,
                          width=8,
                          bgcolor=nac,
                          border_radius=20
                        ),
                      ]
                    )
                
                  )
                 
                 ]
              )
            ),
            
            Container(
              on_hover=self.sidebar_btn_hovered,
              alignment=alignment.center,
              height=s_btn_h,
              width=s_btn_w,
              # bgcolor = s_btn_h_c,
              border_radius=ih_br,
              content=Row(
                spacing=0,
                alignment='spaceBetween',
                vertical_alignment='center',
                controls=[
                  Container(
                    offset=transform.Offset(0, 0),
                    animate_offset=animation.Animation(1000),
                    clip_behavior=ClipBehavior.ANTI_ALIAS,
                    height=17,
                    width=3,
                    # bgcolor=ic,
                    border_radius=5
                  ),
                  Container(
                    margin=margin.only(right=10),
                    content= Stack(
                      controls=[
                        Container(
                          clip_behavior=ClipBehavior.ANTI_ALIAS,
                          height=20,
                          width=20,
                          content=Image(
                            src='assets/icons/s.png',
                            fit=ImageFit.COVER,
                            color=sb_ic
                          )
                        ),
                        Container(
                          right=0,
                          top=1,
                          clip_behavior=ClipBehavior.ANTI_ALIAS,
                          height=9,
                          width=9,
                          bgcolor=nac,
                          border_radius=20,
                          # border=border.all(color=sbc,width=1)
                        ),
                      ]
                    )
                
                  )
                 ]
              )
            ),

          ]

        ),


        Column(
          spacing=5,
          controls=[
            Container(
              data = 'opened',
              on_hover=self.sidebar_btn_hovered,
              on_click=self.show_hide_csa,
              alignment=alignment.center,
              height=s_btn_h,
              width=s_btn_w,
              border_radius=5,
              content=Row(
                spacing=0,
                alignment='center',
                controls=[
                  Icon(
                    icons.MENU_OUTLINED,
                    size=20,
                    color=sb_ic
                  )
                ]
              )
            ),
            Container(
              on_hover=self.sidebar_btn_hovered,
              on_click=self.show_settings_popup,
              alignment=alignment.center,
              height=s_btn_h,
              width=s_btn_w,
              border_radius=5,
              content=Row(
                spacing=0,
                alignment='center',
                controls=[
                  Icon(
                    icons.SETTINGS_OUTLINED,
                    size=20,
                    color=sb_ic
                  )
                ]
              )
            ),


            Container(
              on_hover=self.sidebar_btn_hovered,
              on_click=self.show_settings_popup,
              alignment=alignment.center,
              height=s_btn_h,
              width=s_btn_w,
              border_radius=ih_br,
              content=Row(
                spacing=0,
                alignment='center',
                controls=[
                  Container(
                    clip_behavior=ClipBehavior.ANTI_ALIAS,
                    height=20,
                    width=20,
                    border_radius=20,
                    content=Image(
                      src='assets/dp.jpg',
                      fit=ImageFit.COVER
                    )
                  )
                ]
              )
            ),

            
          ]
        ),

      ]

    )
    
  def chat_screen(self):
    
    self.chat_screen_items = Stack(
      controls=[
        Column(
          controls=[
            Container(
              height=40,
              padding = padding.only(left=10),
              # margin=margin.only(bottom=10),
              content=Row(
                controls=[
                  Image(
                    src='assets/icons/logo.png',
                    color=color['white_text_font']

                  ),
                  Text(
                    value='Chait',
                    size=18,
                    color=color['white_text_font']
                  )

                ]
              )
            ), # whatsapp icon
            
            Container(
              padding = padding.only(left=chat_screen_padding,right=chat_screen_padding),
              content=Row(
                spacing=0,
                alignment='spaceBetween',
                vertical_alignment='center',
                controls=[
                  Text(
                    value='Chats',
                    size=24,
                    weight=FontWeight.W_500
                  ),
                  Row(
                    controls=[
                      Container(
                        on_hover=self.sidebar_btn_hovered,
                        height=40,
                        width=40,
                        border_radius=ih_br,
                        content=Image(
                          src='assets/icons/newchat.png',
                          color=sb_ic
                        ),
                      ),
                      Container(
                        on_hover=self.sidebar_btn_hovered,
                        height=40,
                        width=40,
                        border_radius=ih_br,
                        content=Image(
                          src='assets/icons/more.png',
                          color=sb_ic
                        ),
                      ),
                    ]
                  )
                ]
              )
            ), # Chats label text and new chat icon and more
            
            Container(
              content=Row(
                alignment='center',
                controls=[
                  Container(
                    
                    clip_behavior=ClipBehavior.ANTI_ALIAS,
                    border_radius = ih_br,
                    content=Container(
                      # on_hover=self.sidebar_btn_hovered,
                      clip_behavior=ClipBehavior.ANTI_ALIAS,
                      border_radius = ih_br,
                      height=35,
                      width=s_bw,
                      bgcolor=sbc,
                      border=border.only(bottom=border.BorderSide(width=1,color=htc)),
                      content=Row(
                        controls=[
                          Container(
                            width=230,
                            padding=padding.only(left=15,top=5),
                            content=TextField(
                              border=InputBorder.NONE,
                              hint_text='Search or start a new chat',
                              hint_style=TextStyle(
                                size=14,
                                font_family='arial',
                                color=htc
                              ),
                              color=sb_ic,
                              text_style=TextStyle(
                                size=14,
                                font_family='arial',
                                color=sb_ic
                              ),
                            ),
                          ),

                          Container(
                            height=25,
                            width=25,
                            border_radius=ih_br,
                            on_hover=self.sidebar_btn_hovered,
                            content=Icon(
                              icons.SEARCH_OUTLINED,
                              size=16,
                              color=htc
                            ),
                          )

                        ]
                      )
                    )
                  )
                ]

              )
            ), # search box
            
            Container(
              clip_behavior=ClipBehavior.ANTI_ALIAS,
              height=40,
              padding=padding.only(left=10,right=10),
              # border_radius=20,
              content=Container(
                border_radius=ih_br,
                on_hover=self.sidebar_btn_hovered,
                padding=padding.only(left=10,right=10),
                content=Row(
                  vertical_alignment='center',
                  alignment='spaceBetween',
                  controls=[
                    Icon(
                      icons.DELETE_OUTLINE
                    ),
                    Container(
                      content=Text(
                        value='Archived',
                        weight=FontWeight.W_600,
                        color='#e4e4e4'
                      ),
                      margin=margin.only(right=100)
                    ),
                    Text(
                      value='2',
                      color=ic,
                      weight=FontWeight.W_600
                    )

                  ]
                )
              )

            ), # archived chat button

            self.chats_contents_column,  
            
          ]
        ),
        
        Column(
          controls=[
            Container(), # whatsapp icon
            Container(), # Status text label
            Container(), # my stat
            Container(), # recent updates label
            Container(), # stats column container
          ]
        ),
      ]
    )
  
  def search_on_focus(self,e):
    pass

  def load_dummy(self):
     self.dm_screen_content = Stack(
      controls=[
        Container(
          content=Column(
            spacing=0,
            controls=[
              Row(
                alignment='spaceBetween',
                controls=[
                  WindowDragArea(
                      expand=True,
                      content=Container(height=40,)
                    ),
                    Row(
                      spacing=0,
                      controls=[
                        Container(
                          on_click=self.mini_window,
                          height=40,
                          width=40,
                          content=Image(
                            src='assets/icons/mini.png'
                          )

                        ),
                        Container(
                          on_click=self.max_window,
                          height=40,
                          width=40,
                          content=Image(
                            src='assets/icons/max.png'
                          )

                        ),
                        Container(
                          on_click=self.close_window,
                          height=40,
                          width=40,
                          content=Image(
                            src='assets/icons/close.png'
                          )

                        ),
                      ]
                    )
                ]
              ),
              
              Container(
                padding=padding.only(left=20,right=15),
                height=50,
                content=Row(
                  alignment='spaceBetween',
                  controls=[
                    Container(
                      on_click=self.show_chat_user_popup,
                      expand=True,
                      content=Row(
                        controls=[
                          Container(
                            height=40,
                            width=40,
                            border_radius=20,
                            bgcolor=rc,
                            content=Icon(
                              icons.PERSON
                            )
                          ),
                          Text(
                            value='#Se7en🙏',
                            color='#e4e4e4'
                          )
                          
                        ]
                      )
                    ),

                    Row(
                      controls=[
                        Container(
                          on_hover=self.sidebar_btn_hovered,
                          alignment=alignment.center,
                          height=s_btn_h,
                          width=s_btn_w,
                          border_radius=5,
                          content=Row(
                            spacing=0,
                            alignment='center',
                            controls=[
                              Icon(
                                icons.VIDEO_CALL_OUTLINED,
                                size=20,
                                color=sb_ic
                              )
                            ]
                          )
                        ),


                        Container(
                          on_hover=self.sidebar_btn_hovered,
                          alignment=alignment.center,
                          height=s_btn_h,
                          width=s_btn_w,
                          border_radius=5,
                          content=Row(
                            spacing=0,
                            alignment='center',
                            controls=[
                              Icon(
                                icons.CALL_OUTLINED,
                                size=20,
                                color=sb_ic
                              )
                            ]
                          )
                        ),
                        
                        Container(
                          height=25,
                          width=2,
                          bgcolor=s_btn_h_c
                        ),
                        
                        Container(
                          on_hover=self.sidebar_btn_hovered,
                          alignment=alignment.center,
                          height=s_btn_h,
                          width=s_btn_w,
                          border_radius=5,
                          content=Row(
                            spacing=0,
                            alignment='center',
                            controls=[
                              Icon(
                                icons.SEARCH_OUTLINED,
                                size=20,
                                color=sb_ic
                              )
                            ]
                          )
                        ),

                      ]
                    ),
                  ]
                )

              ),
              
              Container(
                alignment=alignment.top_left,
                padding=padding.only(left=20,right=20,top=10),
                expand=True,
                image_src=wallpaper,
                image_opacity=0.2,
                image_fit=ImageFit.COVER,
                bgcolor='#1a343434',
                content=Column(
                  scroll='auto',
                  spacing=10,
                  controls=[
                    self.messages_column,
                  ]
                )

              ),
              
              Container(
                margin=margin.only(left=2),
                padding=padding.only(left=10,right=10),
                height=50,
                bgcolor=color['type_bar_black'],
                content=Row(
                  controls=[
                    Container(
                      on_hover=self.sidebar_btn_hovered,
                      on_click=self.show_emojis_popup,
                      alignment=alignment.center,
                      height=40,
                      width=40,
                      border_radius=5,
                      content=Row(
                        spacing=0,
                        alignment='center',
                        controls=[
                          Icon(
                            icons.EMOJI_EMOTIONS_OUTLINED,
                            size=20,
                            color=sb_ic
                          )
                        ]
                      )
                    ),
                    
                    Container(
                      on_hover=self.sidebar_btn_hovered,
                      alignment=alignment.center,
                      height=40,
                      width=40,
                      border_radius=5,
                      content=Row(
                        spacing=0,
                        alignment='center',
                        controls=[
                          Icon(
                            icons.SHARE_OUTLINED,
                            size=20,
                            color=sb_ic
                          )
                        ]
                      )
                    ),
                    
                    Container(
                      on_hover=self.sidebar_btn_hovered,
                      expand=True,
                      content=TextField(
                          expand=True,
                          multiline=True,
                          border=InputBorder.NONE,
                          
                          hint_text='Type a message',
                          
                          hint_style=TextStyle(
                            size=14,
                            font_family='arial',
                            color=color['white_text_font']
                          ),
                          color=sb_ic,
                          text_style=TextStyle(
                            size=14,
                            font_family='arial',
                            color=sb_ic
                          ),
                        ),
                      ),
                    
                    self.send_msg_btn,

                  ]
                )

              ),
            
            ]
          )
        ),

        Container(
          content=Stack(
            controls=[
              self.chat_user_popup,
            ]
          )
        ),
      ]
    )
     


  
  def chats_column_f(self):
    def return_col():
      def load_user_chat(user):
          
          def create_message(text,time,received,send=False):
              _margin_ = 0 if  received else 450
              
                            
              container =  Container(
                  margin=margin.only(_margin_),
                  alignment=alignment.center_left,
                  animate=animation.Animation(1000,AnimationCurve.BOUNCE_OUT) if send else animation.Animation(300,AnimationCurve.BOUNCE_OUT),
                  width=500,
                  padding=10,
                  border_radius=ih_br,
                  content=Column(
                      spacing=4,
                      controls=[
                          Text(
                              value=text,
                              selectable=True,
                              color=smc,
                              weight=FontWeight.W_400,
                              size=14,
                          ),
                          Row( # بخش نمایش زمان پیام
                              spacing=4,
                              alignment='end',
                              controls=[
                                  Text(
                                      time,
                                      size=10,
                                      weight=FontWeight.W_600,
                                      color=mtc if received else color['gray_icon']
                                  ),
                                  Icon(
                                      icons.DONE,
                                      color=color['gray_icon'],
                                      size=10
                                  )
                              ]
                          )
                      ]
                  )
              )
          # message here
              if not received:
                 container.gradient = blue_gradient
              else:
                 container.bgcolor = color['side_bar_black']


              return container
          def send_message(r):
             def add_message(json_filepath, username, content,timestamps, reactions=None):
                    hour = now.strftime("%I").lstrip("0")  # %I for 12-hour format, lstrip("0") removes leading zero
                    if not hour:
                        hour = "24"
                    minute = now.strftime("%M")
                    am_pm = now.strftime("%p")
                    timestamp = f"{hour}:{minute} {am_pm}"

                    # Format the date
                    date = now.strftime("%Y/%m/%d")

                    timestamps= [timestamp, date]

                    try:
                        with open(json_filepath, 'r') as f:
                            data = json.load(f)
                    except FileNotFoundError:
                        print(f"Error: File '{json_filepath}' not found.")
                        return
                    except json.JSONDecodeError:
                        print(f"Error: Invalid JSON format in '{json_filepath}'.")
                        return

                    user_found = False
                    for user in data['users']:
                        if user['name'] == username:
                            user_found = True
                            new_message = {
                                "content": content,
                                "timestamps": timestamps,
                                "reactions": reactions if reactions else [],  # Handle optional reactions
                                "is_seen": False,
                                "received": False
                            }
                            user['all_messages'].append(new_message)
                            user['unread_messages'] += 1
                            break

                    if not user_found:
                        print(f"Error: User '{username}' not found.")
                        return

                    try:
                        with open(json_filepath, 'w') as f:
                            json.dump(data, f, indent=4)
                        print(f"Message added for '{username}' and saved to '{json_filepath}'")
                    except (IOError, OSError) as e:
                        print(f"Error: Could not write to '{json_filepath}'. Error: {e}")
             message = type_field.value
             now = datetime.datetime.now()
             current_time = now.strftime("%H:%M")

             self.messages_column.controls.append(create_message(message,current_time,False,True))
             add_message('login_data.json', user, message,current_time)
             type_field.value = ""
             self.pg.update()
             

          
          
          self.messages_column = Column(
    scroll='auto',
    expand=True,
    controls=[]  # با مجموعه‌ای خالی از کنترل‌ها شروع می‌شود
)
          msg = []

          
          file_path = 'login_data.json'  
          if os.path.exists(file_path):  
            # خواندن داده‌های موجود در فایل  
            with open(file_path, 'r', encoding='utf-8') as file:  
                data = json.load(file)  # بارگذاری داده‌های JSON  
                output = {}  # دیکشنری برای ذخیره نتایج  
                for user_data in data['users']:  
                    if user_data['name'] == user:
                        profile_image_path = user_data['profile']
                        break

                for user_data in data['users']:  
                    user_name = user_data['name']
                    messages = user_data['all_messages'] if user_data['all_messages'] else []  # مدیریت لیست‌های خالی

                    if messages:  # اگر پیام‌ها وجود دارند  
                        message_contents = [
                            {
                                "content": msg['content'],
                                "received": msg['received'],
                                "timestamp": msg['timestamps'][0]  # دریافت ساعت ارسال پیام
                                
                            }  
                            for msg in messages
                        ]  

                        output[user_name] = message_contents  # اضافه کردن به دیکشنری  
                    else:  
                        output[user_name] = [{"content": "No messages yet", "received": False, "timestamp": ""}]  # اگر پیام‌ها وجود ندارند  

          
          for message in output[user]:
             msg.append(message)
            
          self.messages_column.controls.clear()  # پاک کردن پیام‌های قبلی
          


          # پر کردن ستون پیام‌ها
          for message in msg:

              self.messages_column.controls.append(create_message(message["content"],message["timestamp"],message["received"]))
          
          send_msg_btn = Container(
      on_click=send_message,
      on_hover=self.sidebar_btn_hovered,
      alignment=alignment.center,
      height=40,
      width=40,
      border_radius=5,
      content=Row(
        spacing=0,
        alignment='center',
        controls=[
          Icon(
            icons.SEND,
            size=20,
            color=sb_ic
          )
        ]
      )
    )
          type_field = TextField(
                                expand=True,
                                multiline=True,
                                border=InputBorder.NONE,
                                
                                hint_text='Type something...',
                                
                                hint_style=TextStyle(
                                  size=14,
                                  color=color['white_text_font']

                                ),text_style=TextStyle(
                            size=14,
                            font_family='arial',
                            color=color['white_text_font']
                          ))
          type_bar = Container(
                            on_hover=self.sidebar_btn_hovered,
                            expand=True,
                            content=type_field,
                            
                            

                              )
                            
          dm_screen = Stack(
            controls=[
              Container(
                content=Column(
                  spacing=0,
                  controls=[
                    Row(
                      alignment='spaceBetween',
                      controls=[
                        WindowDragArea(
                            expand=True,
                            content=Container(height=40,)
                          ),
                          Row(
                            spacing=0,
                            controls=[
                              Container(
                                on_click=self.mini_window,
                                height=40,
                                width=40,
                                content=Image(
                                  src='assets/icons/mini.png'
                                )

                              ),
                              Container(
                                on_click=self.max_window,
                                height=40,
                                width=40,
                                content=Image(
                                  src='assets/icons/max.png'
                                )

                              ),
                              Container(
                                on_click=self.close_window,
                                height=40,
                                width=40,
                                content=Image(
                                  src='assets/icons/close.png'
                                )

                              ),
                            ]
                          )
                      ]
                    ),
                    
                    Container(
                      padding=padding.only(left=20,right=15),
                      height=50,
                      content=Row(
                        alignment='spaceBetween',
                        controls=[
                          Container(
                            on_click=self.show_chat_user_popup,
                            expand=True,
                            content=Row(
                              controls=[
                                Container(
                                  height=40,
                                  width=40,
                                  border_radius=20,
                                  bgcolor=rc,
                                  content=Image(
                              src=profile_image_path, # profileee
                              fit=ImageFit.COVER,
                            )
                                ),
                                Text(
                                  value=user,
                                  color='#e4e4e4'
                                )
                                
                              ]
                            )
                          ),

                          Row(
                            controls=[
                              
                              
                              Container( # splitline
                                height=25,
                                width=2,
                                bgcolor=s_btn_h_c
                              ),
                              
                              Container(
                                on_hover=self.sidebar_btn_hovered,
                                alignment=alignment.center,
                                height=s_btn_h,
                                width=s_btn_w,
                                border_radius=5,
                                content=Row(
                                  spacing=0,
                                  alignment='center',
                                  controls=[
                                    Icon(
                                      icons.SEARCH_OUTLINED,
                                      size=20,
                                      color=sb_ic
                                    )
                                  ]
                                )
                              ),
                              Container(
                                on_hover=self.sidebar_btn_hovered,
                                alignment=alignment.center,
                                height=s_btn_h,
                                width=s_btn_w,
                                border_radius=5,
                                content=Row(
                                  spacing=0,
                                  alignment='center',
                                  controls=[
                                    Icon(
                                      icons.MORE_VERT,
                                      size=20,
                                      color=sb_ic
                                    )
                                  ]
                                )
                              ),


                            ]
                          ),
                        ]
                      )

                    ),
                    
                    Container(
                      alignment=alignment.top_left,
                      padding=padding.only(left=20,right=20,top=10),
                      expand=True,
                      image_src=wallpaper,
                      image_opacity=0.2,
                      image_fit=ImageFit.COVER,
                      bgcolor='#1a343434',
                      content=Column(
                        scroll='auto',
                        spacing=10,
                        controls=[
                          self.messages_column,
                        ]
                      )

                    ),
                    
                    Container(
                      margin=margin.only(left=2),
                      padding=padding.only(left=10,right=10),
                      height=50,
                      bgcolor=color['type_bar_black'],
                      content=Row(
                        controls=[
                          Container(
                            on_hover=self.sidebar_btn_hovered,
                            on_click=self.show_emojis_popup,
                            alignment=alignment.center,
                            height=40,
                            width=40,
                            border_radius=5,
                            content=Row(
                              spacing=0,
                              alignment='center',
                              controls=[
                                Icon(
                                  icons.EMOJI_EMOTIONS_OUTLINED,
                                  size=20,
                                  color=sb_ic
                                )
                              ]
                            )
                          ),
                          
                          Container(
                            on_hover=self.sidebar_btn_hovered,
                            alignment=alignment.center,
                            height=40,
                            width=40,
                            border_radius=5,
                            content=Row(
                              spacing=0,
                              alignment='center',
                              controls=[
                                Icon(
                                  icons.SHARE_OUTLINED,
                                  size=20,
                                  color=sb_ic
                                )
                              ]
                            )
                          ),
                          
                          type_bar,
                          
                          send_msg_btn,

                        ]
                      )

                    ),
                  
                  ]
                )
              ),

              Container(
                content=Stack(
                  controls=[
                    self.chat_user_popup,
                  ]
                )
              ),
            ]
          )
          self.dm_screen.content = dm_screen
          self.pg.update()


      
      file_path = 'login_data.json' 
      ro = [] 
      if os.path.exists(file_path):  
          # خواندن داده‌های موجود در فایل  
          with open(file_path, 'r', encoding='utf-8') as file:  
              data = json.load(file)  # بارگذاری داده‌های JSON  
              for user_data in data['users']:  
                  user_name = user_data['name']  
                  profile_image_path = user_data['profile']  # دریافت مسیر تصویر پروفایل
                  last_message = user_data['all_messages'][-1]['content'] if user_data['all_messages'] else "No messages yet"  # مدیریت لیست‌های خالی  
                  timestamp = user_data['all_messages'][-1]['timestamps'][0] if user_data['all_messages'] else ""  # مدیریت لیست‌های خالی  
                  path = 'assets/profile/'


                  chat_row = Container(
                    height=70,
                    padding=padding.only(left=10,right=10),
                    content=Container(
                      border_radius=ih_br,
                      on_hover=self.sidebar_btn_hovered,
                      on_click=lambda e, user=user_name: load_user_chat(user), 
                      content=Row(
                        spacing=0,
                        alignment='spaceBetween',
                        vertical_alignment='center',
                        controls=[
                          Container(
                            height=50,
                            width=50,
                            border_radius=30,
                            clip_behavior=ClipBehavior.ANTI_ALIAS,
                            content=Image(
                              src=profile_image_path,
                              fit=ImageFit.COVER,
                            )
                          ),
                          
                          Column(
                            alignment='center',
                            horizontal_alignment='center',
                            controls=[
                              Container(
                                width=200,
                                content=Row(
                                    alignment='spaceBetween',
                                    # vertical_alignment='center',
                                    spacing=0,
                                    controls=[
                                      Container(
                                        clip_behavior=ClipBehavior.ANTI_ALIAS,
                                        width=120,
                                        content=Text(
                                        user_name,
                                        no_wrap=True,
                                        color='#e4e4e4'
                                      ),
                                      ),
                                      Text(
                                        timestamp,
                                        color='#e4e4e4'
                                      ),
                                    ]
                                  ),
                              ),
                              
                              


                              Container(
                                width=200,
                                content=Row(
                                    alignment='spaceBetween',
                                    # vertical_alignment='center',
                                    spacing=0,
                                    controls=[
                                      Container(
                                        clip_behavior=ClipBehavior.ANTI_ALIAS,
                                        width=120,
                                        content=Text(
                                          last_message,
                                          no_wrap=True,
                                          color='#e4e4e4'
                                        ),
                                      ),
                                    ]
                                  ),
                              ),
                              
                              

                              

                            ]
                          )
                        ]
                      )
                    )

                  )
                  ro.append(chat_row)
                  
      else:  
          print("فایل وجود ندارد.")  
          return None  # اگر فایل وجود نداشته باشد، None برمی‌گرداند  
      return ro



    self.chat_row = Container(
      height=70,
      padding=padding.only(left=10,right=10),
      content=Container(
        border_radius=ih_br,
        on_hover=self.sidebar_btn_hovered,
        content=Row(
          spacing=0,
          alignment='spaceBetween',
          vertical_alignment='center',
          controls=[
            Container(
              height=50,
              width=50,
              border_radius=30,
              clip_behavior=ClipBehavior.ANTI_ALIAS,
              content=Image(
                src='assets/dp.jpg',
                fit=ImageFit.COVER,
              )
            ),
            
            Column(
              alignment='center',
              horizontal_alignment='center',
              controls=[
                Container(
                  width=200,
                  content=Row(
                      alignment='spaceBetween',
                      # vertical_alignment='center',
                      spacing=0,
                      controls=[
                        Container(
                          clip_behavior=ClipBehavior.ANTI_ALIAS,
                          width=120,
                          content=Text(
                          '#Se7en',
                          no_wrap=True,
                          color='#e4e4e4'
                        ),
                        ),
                        Text(
                          '12:20AM',
                          color='#e4e4e4'
                        ),
                      ]
                    ),
                ),
                
                


                Container(
                  width=200,
                  content=Row(
                      alignment='spaceBetween',
                      # vertical_alignment='center',
                      spacing=0,
                      controls=[
                        Container(
                          clip_behavior=ClipBehavior.ANTI_ALIAS,
                          width=120,
                          content=Text(
                            'last message of chat',
                            no_wrap=True,
                            color='#e4e4e4'
                          ),
                        ),
                      ]
                    ),
                ),
                
                

                

              ]
            )
          ]
        )
      )

    )
    
            
    self.chats_contents_column = Column(
              scroll='auto',
              expand=True,
              controls=[
                self.chat_row
                
           
              ]
            ) # chats column container
    col = return_col()
    for i in col:
        self.chats_contents_column.controls.append(i) 

  def msg_hovered(self,e):
    if e.data == 'true':
      self.msg_hover_emoji.visible = True
    else:  
      self.msg_hover_emoji.visible = False
    self.msg_hover_emoji.update()

  def show_msg_menu(self,e:LongPressEndEvent):
    print(e.target)

  def close_window(self,e):
    self.pg.window_destroy()


  def mini_window(self,e):
    self.pg.window_minimized = True

    self.pg.update()


  def max_window(self,e):
    self.pg.window_maximized = True
    self.pg.update()
    



  def hide_emojis_popup(self,e):
    self.emoji_popup.offset = transform.Offset(0,1.5)
    self.emoji_popup.update()
    sleep(0.51)
    self.emoji_popup.height = 0
    self.emoji_popup.update()
  
  def show_emojis_popup(self,e):
    self.emoji_popup.height = None
    self.emoji_popup.offset = transform.Offset(0,0)
    self.emoji_popup.update()

  def enable_edit(self, e):
    # Toggle the edit mode
    self.editfield.disabled = not self.editfield.disabled  # Toggle disabled state
    self.editfield.border = 'underline' if not self.editfield.disabled else InputBorder.NONE
    self.pg.update()  # Update the UI



  def chat_user_details(self):

    self.editfield = TextField(
                  width=200,
                  value=self.userid,
                  text_size=20,
                  color='#CCffffff',
                  disabled=True,
                  border=InputBorder.NONE
                )
    
    self.editicon = Container(
                  margin=margin.only(right=15),
                  on_hover=self.sidebar_btn_hovered,
                  border_radius=ih_br,
                  height=35,
                  width=35,
                  on_click=self.enable_edit,
                  content=Icon(
                    icons.EDIT_OUTLINED,
                    size=14,
                    color=sb_ic
                  )
                )

    self.chat_user_details_sidebar_item_info =  Container(
                                  expand=True,
                                  padding=15,
                                  content=Column(
                                    # expand=True,
                                    height=475,
                                    scroll='auto',
                                    controls=[
                                      Row(
                                        alignment='center',
                                        controls=[
                                          Container(
                                            alignment=alignment.center,
                                            height=100,
                                            width=100,
                                            border_radius=80,
                                            bgcolor='white12',
                                            content=Icon(
                                              icons.PERSON,
                                              size=50
                                            ),
                                          ),
                                        ]
                                      ),
                                      Row(
                                        alignment='center',
                                        controls=[
                                          Text(
                                            'User',
                                            size=20,
                                            weight=FontWeight.W_600
                                          )
                                        ]
                                      ),
                                      Text(
                                        'About',
                                        size=14,
                                        weight=FontWeight.W_300,
                                        color='white24',
                                      ),
                                      Text(
                                        'Hey there! I am using WhatsApp',
                                        size=14,
                                        weight=FontWeight.W_400,
                                        color='#CCffffff',
                                      ),
                                      Text(
                                        'Phone number',
                                        size=14,
                                        weight=FontWeight.W_300,
                                        color='white24',
                                      ),
                                      Text(
                                        '+233 548 007 499',
                                        size=14,
                                        weight=FontWeight.W_400,
                                        color='#CCffffff',
                                      ),


                                      Text(
                                        'Disappearing messages',
                                        size=14,
                                        weight=FontWeight.W_300,
                                        color='white24',
                                      ),
                                      Text(
                                        'Off',
                                        size=14,
                                        weight=FontWeight.W_400,
                                        color='#CCffffff',
                                      ),
                                      Text(
                                        'Muted notifications',
                                        size=14,
                                        weight=FontWeight.W_300,
                                        color='white24',
                                      ),
                                      Container(
                                        width=120,
                                        height=35,
                                        bgcolor=s_btn_h_c,
                                        padding=padding.only(left=10),
                                        border_radius=ih_br,
                                        content=Row(
                                          controls=[
                                            # Image(
                                            #   src='assets/icons/audio.png',
                                            #   color='#CCffffff'
                                            # )
                                            Icon(
                                              icons.MUSIC_NOTE_OUTLINED,
                                              size=16,
                                              color='#CCffffff',

                                            ),
                                            Dropdown(
                                              alignment=alignment.center,
                                              label_style=TextStyle(size=12,color='#CCffffff',),
                                              expand=True,
                                              label='Mute',
                                              options=[
                                                  dropdown.Option("For 8hrs",),
                                                  dropdown.Option("For 1 Week"),
                                                  dropdown.Option("Always"),
                                              ],
                                              border_color=s_btn_h_c,

                                            ),
                                          ]

                                        ),
                                      ),

                                      Text(
                                        'Notification tone',
                                        size=14,
                                        weight=FontWeight.W_300,
                                        color='white24',
                                      ),
                                      Container(
                                        height=35,
                                        border_radius=ih_br,
                                        content=Row(
                                          spacing=10,
                                          controls=[
                                            # Image(
                                            #   src='assets/icons/audio.png',
                                            #   color='#CCffffff'
                                            # )
                                            Container(
                                              height=35,
                                              width=35 ,
                                              border_radius=ih_br,
                                              bgcolor=s_btn_h_c,
                                              content=Icon(
                                              icons.PLAY_ARROW_OUTLINED,
                                              size=16,
                                              color='#CCffffff',

                                            )
                                            ),
                                            Container(
                                              border_radius=ih_br,
                                              bgcolor=s_btn_h_c,
                                              width=120,
                                              content=Dropdown(
                                              # icon=icons.MUSIC_NOTE_OUTLINED,
                                              alignment=alignment.center,
                                              label_style=TextStyle(size=12,color='#CCffffff',),
                                              expand=True,
                                              label='Default',
                                              options=[
                                                  dropdown.Option("None",),
                                                  dropdown.Option("Default"),
                                                  dropdown.Option("Alert 1"),
                                                  dropdown.Option("Alert 2"),
                                                  dropdown.Option("Alert 3"),
                                              ],
                                              border_color=s_btn_h_c,

                                            ),
                                            )
                                          ]

                                        ),
                                      ),

                                      Container(
                                        # expand=True,
                                        width=500,
                                        height=1,
                                        bgcolor=s_btn_h_c
                                      ),
                                      Row(
                                        alignment='spaceBetween',
                                        controls=[
                                          Container(
                                            alignment=alignment.center,
                                            height=35,
                                            width=155,
                                            border_radius=ih_br,
                                            bgcolor=s_btn_h_c,
                                            content=Text(
                                              'Block',
                                              size=14,
                                              weight=FontWeight.W_400,
                                              color='#CCffffff',
                                            ),
                                          ),
                                          Container(
                                            alignment=alignment.center,
                                            height=35,
                                            width=155,
                                            border_radius=ih_br,
                                            bgcolor=s_btn_h_c,
                                            content=Text(
                                              'Report contact',
                                              size=14,
                                              weight=FontWeight.W_400,
                                              color='#CCffffff',
                                            ),
                                          ),
                                        ]
                                      )


                                    ]
                                  )
                                )

    

    self.settings_sidebar_details_column =  Container(
        expand=True,
        padding=15,
        content=Column(
          # expand=True,
          height=475,
          scroll='auto',
          controls=[
            Row(
              alignment='center',
              controls=[
                Container(
                  alignment=alignment.center,
                  height=100,
                  width=100,
                  border_radius=80,
                  bgcolor='white12',
                  content=Icon(
                    icons.PERSON,
                    size=50
                  ),
                ),
              ]
            ),
            Row(
              alignment='spaceBetween',
              controls=[
                # Text(
                #   '',
                  # size=20,
                #   weight=FontWeight.W_600
                # ),
                self.editfield,
                self.editicon
              ]
            ),
            
            Text(
              'About',
              size=14,
              weight=FontWeight.W_300,
              color='white24',
            ),
            Row(
              alignment='spaceBetween',
              controls=[
                TextField(
                  width=250,
                  multiline=True,
                  value='Hey there! WhatsApp is using me!',
                  text_size=14,
                  border=InputBorder.NONE,
                  text_style=TextStyle(
                    size=14,
                    weight=FontWeight.W_400,
                    color='#CCffffff',

                  )
                ),
                Container(
                  margin=margin.only(right=15),
                  on_hover=self.sidebar_btn_hovered,
                  border_radius=ih_br,
                  height=35,
                  width=35,
                  content=Icon(
                    icons.EDIT_OUTLINED,
                    size=14,
                    color=sb_ic
                  )
                )
              ]
            ),
            Text(
              'Phone number',
              size=14,
              weight=FontWeight.W_300,
              color='white24',
            ),
            Text(
              '+233 548 007 499',
              size=14,
              weight=FontWeight.W_400,
              color='#CCffffff',
            ),
          ]
        )
      )


    self.chat_user_details_sidebar_item  =  Container(
      bgcolor=s_btn_h_c,
      height=35,
      border_radius=ih_br,

      content=Row(
        spacing=12,
        # alignment='spaceBetween',
        vertical_alignment='center',
        controls=[
          Container(
            offset=transform.Offset(0, 0),
            animate_offset=animation.Animation(1000),
            clip_behavior=ClipBehavior.ANTI_ALIAS,
            height=17,
            width=3,
            bgcolor=ic,
            border_radius=5
          ),
          
          Row(
            vertical_alignment='center',
            spacing=10,
            controls = [
              Image(
                        src='assets/icons/info.png',
                        color=sb_ic,
                        # scale=0.5
                      ),
              Text(
                'Overview'
              )      
          ]
        ),
        
        
        ]
      ),
    )
                       
    
    self.settings_sidebar_item  =  Container(
      bgcolor=s_btn_h_c,
      height=35,
      border_radius=ih_br,

      content=Row(
        spacing=12,
        # alignment='spaceBetween',
        vertical_alignment='center',
        controls=[
          Container(
            offset=transform.Offset(0, 0),
            animate_offset=animation.Animation(1000),
            clip_behavior=ClipBehavior.ANTI_ALIAS,
            height=17,
            width=3,
            bgcolor=ic,
            border_radius=5
          ),
          
          Row(
            vertical_alignment='center',
            spacing=10,
            controls = [
              Image(
                        src='assets/icons/info.png',
                        color=sb_ic,
                        # scale=0.5
                      ),
              Text(
                'Overview'
              )      
          ]
        ),
        
        
        ]
      ),
    )


    self.chat_user_popup = Container(
      offset=transform.Offset(0,-1),
      clip_behavior=ClipBehavior.ANTI_ALIAS,
      height=0,
      animate_offset=animation.Animation(500,'decelerate'),
      bgcolor=sbc,
      content=Card(
        expand=True,
        elevation=15,
        content=Container(
          height=500,
          width=500,
          bgcolor=sbc,
          content=Row(
            controls=[
              Container(
                padding=8,
                width=140,
                bgcolor=csc,
                content=Column(
                  alignment='spaceBetween',
                  spacing=5,
                  controls=[
                    Column(
                      expand=True,
                      scroll='auto',
                      controls=[
                        self.chat_user_details_sidebar_item,
                      ]
                    ),
                    Column(
                      controls=[
                        Container(
                          on_click=self.close_chat_user_popup,
                          bgcolor=s_btn_h_c,
                          height=35,
                          border_radius=ih_br,

                          content=Row(
                            alignment='center',
                            vertical_alignment='center',
                            controls=[
                              Row(
                                vertical_alignment='center',
                                spacing=10,
                                controls = [
                                  Image(
                                            src='assets/icons/info.png',
                                            color=sb_ic,
                                            # scale=0.5
                                          ),
                                  Text(
                                    'Close'
                                  )      
                              ]
                            ),
                            
                            
                            ]
                          ),
                        )
                      ,
                      ]
                    )
                    
                  ]
                ),
              ),
              
              
              Column(
                expand=True,
                controls=[
                  Stack(
                    controls=[
                      self.chat_user_details_sidebar_item_info
                    ]
                  )
                ]
              ),
            
            
            ]
          ),
        )
      )
    )

   
    self.settings_popup = Container(
      border_radius=ih_br,
      bottom=30,
      left=80,
      height=0,
      offset=transform.Offset(0,1.5),
      animate_offset=animation.Animation(500,'decelerate'),
      bgcolor=sbc,
      content=Card(
        expand=True,
        elevation=15,
        content=Container(
          border_radius=ih_br,
          height=500,
          width=500,
          bgcolor=sbc,
          content=Row(
            controls=[
              Container(
                padding=8,
                width=140,
                bgcolor=csc,
                content=Column(
                  alignment='spaceBetween',
                  spacing=5,
                  controls=[
                    Column(
                      expand=True,
                      scroll='auto',
                      controls=[
                        self.settings_sidebar_item,
                      ]
                    ),
                    Column(
                      controls=[
                        Container(
                          on_click=self.close_settings_popup,
                          bgcolor=s_btn_h_c,
                          height=35,
                          border_radius=ih_br,

                          content=Row(
                            alignment='center',
                            vertical_alignment='center',
                            controls=[
                              Row(
                                vertical_alignment='center',
                                spacing=10,
                                controls = [
                                  Image(
                                    src='assets/icons/info.png',
                                    color=sb_ic,
                                    # scale=0.5
                                  ),
                                  Text(
                                    'Profile'
                                  )      
                              ]
                            ),
                            
                            
                            ]
                          ),
                        ),
                        Container(
                          on_click=self.close_settings_popup,
                          bgcolor=s_btn_h_c,
                          height=35,
                          border_radius=ih_br,

                          content=Row(
                            alignment='center',
                            vertical_alignment='center',
                            controls=[
                              Row(
                                vertical_alignment='center',
                                spacing=10,
                                controls = [
                                  Image(
                                            src='assets/icons/info.png',
                                            color=sb_ic,
                                            # scale=0.5
                                          ),
                                  Text(
                                    'Close'
                                  )      
                              ]
                            ),
                            
                            
                            ]
                          ),
                        ),
                     
                      ]
                    )
                    
                  ]
                ),
              ),
              
              
              Column(
                expand=True,
                controls=[
                  Stack(
                    controls=[
                      self.settings_sidebar_details_column
                    ]
                  )
                ]
              ),
            
            
            ]
          ),
        )
      )
    )


    self.emoji_popup = Container(
      animate_offset=animation.Animation(500,'decelerate'),
      border_radius=ih_br,
      bottom=50,
      left=120,
      height=0,
      offset=transform.Offset(0,1.5),
      content=Stack(
        controls=[
          Card(
            expand=True,
            elevation=30,
            height=380,
            width=500,
          ),
          
            Container(
              padding=padding.only(top=10,left=10,right=10),
              border_radius = ih_br,
              height=400,
              width=500,
              bgcolor=csc,
              
              content=Column(
                controls=[
                  Row(
                    alignment='spaceBetween',
                    controls=[
                      
                      Row(
                        controls=[
                          Text(
                            'Emoji',
                            size=16
                          ),
                          Text(
                            'GIFs',
                            size=16,
                            color='white24',
                          ),
                          Text(
                            'Stickers',
                            size=16,
                            color='white24',
                          ),
                        ]
                      ),

                      Container(
                        on_click=self.hide_emojis_popup,
                        height=20,width=20,border_radius=ih_br,bgcolor='white12',content=Icon(
                          icons.CLOSE,
                          size=12,

                        )
                      )
                    ]
                  ),

                  
                  Container(
                    height=35,
                    bgcolor=sbc,
                    border_radius = ih_br,
                    border=border.only(bottom=border.BorderSide(width=1,color=htc)),
                    content=Row(
                      alignment='spaceBetween',
                      controls=[
                        Container(
                          padding=padding.only(left=15,top=5),
                          content=TextField(
                            border=InputBorder.NONE,
                            hint_text='Search emojis',
                            hint_style=TextStyle(
                              size=14,
                              font_family='arial',
                              color=htc
                            ),
                            color=sb_ic,
                            text_style=TextStyle(
                              size=14,
                              font_family='arial',
                              color=sb_ic
                            ),
                          ),
                        ),

                        
                        Container(
                          height=25,
                          width=25,
                          border_radius=ih_br,
                          on_hover=self.sidebar_btn_hovered,
                          content=Icon(
                            icons.SEARCH_OUTLINED,
                            size=16,
                            color=htc
                          ),
                        ),


                      ]
                    )
                  )

                ]
              )
            )
        ]
      )
      
    )

  def load_messages(self, e):
    # Read the JSON file
    with open('login_data.json', 'r') as file:
        user_data = json.load(file)
        username = user_data['username']
        password = user_data['password']
        email = user_data['email']



    # Access the messages for the user
    messages = user_data["messages"]

    # Create a Column to display the messages
    messages_column = Column(
        scroll='auto',
        controls=[
            Container(
                content=Text(value=message["message"], size=14, color=sb_ic),
                padding=padding.only(top=10, bottom=10)
            )
            for message in messages
        ]
    )

    # Add the messages column to the UI
    self.dm_screen_content.content = messages_column
    self.dm_screen_content.update()

        



  def close_settings_popup(self,e):
    print('fired')
    self.settings_popup.offset = transform.Offset(0,1.5)
    self.settings_popup.update()
    sleep(0.51)
    self.settings_popup.height = 0
    self.settings_popup.update()
  
  def show_settings_popup(self,e):
    self.settings_popup.height = None
    self.settings_popup.offset = transform.Offset(0,0)
    self.settings_popup.update()




  def close_chat_user_popup(self,e):
    self.chat_user_popup.offset = transform.Offset(0,-1)
    self.chat_user_popup.update()
    sleep(0.51)
    self.chat_user_popup.height = 0
    self.chat_user_popup.update()
  
  def show_chat_user_popup(self,e):
    self.chat_user_popup.height = None
    self.chat_user_popup.offset = transform.Offset(0,0)
    self.chat_user_popup.update()



  
  def dm_screen_content_main(self):
    def create_message(text):
      

      return Container(
          margin=margin.only(right=6),
          alignment=alignment.center_left,
          width=500,
          padding=10,
          gradient=blue_gradient, # frediant here
          border_radius=ih_br,
          content=Column(
              spacing=4,
              controls=[
                  Text(
                      value=text,
                      selectable=True,
                      color=smc,
                      weight=FontWeight.W_400,
                      size=14,
                  ),
                  Row(
                      spacing=4,
                      alignment='end',
                      controls=[
                          Text(
                              '۵:۳۰ صبح',
                              size=10,
                              weight=FontWeight.W_600,
                              color=mtc
                          ),
                          Icon(
                              icons.DONE,
                              color=mtc,
                              size=10
                          )
                      ]
                  )
              ]
          )
      )
    


    self.send_msg_btn = Container(
      on_click=self.load_messages,
      on_hover=self.sidebar_btn_hovered,
      alignment=alignment.center,
      height=40,
      width=40,
      border_radius=5,
      content=Row(
        spacing=0,
        alignment='center',
        controls=[
          Icon(
            icons.SEND,
            size=20,
            color=sb_ic
          )
        ]
      )
    )


    self.msg_hover_emoji = PopupMenuButton(
        tooltip=None,
        content=Container(
          # on_click=
          tooltip=None,
          height=20,
          width=20,
          border_radius=25,
          content=Icon(
            icons.EMOJI_EMOTIONS_OUTLINED,
            color=htc
          ),
        ),
        items=[
            PopupMenuItem(
              content=Row(
                controls=[
                  Image(
                    src='assets/icons/laugh.png',
                  ),
                  Image(
                    src='assets/icons/laugh.png',
                  ),
                  Image(
                    src='assets/icons/laugh.png',
                  ),
                  Image(
                    src='assets/icons/laugh.png',
                  ),
                  Image(
                    src='assets/icons/laugh.png',
                  ),
                  Image(
                    src='assets/icons/laugh.png',
                  ),
                  Image(
                    src='assets/icons/laugh.png',
                  ),
                  Image(
                    src='assets/icons/laugh.png',
                  ),
                ]
              )
            )
           
        ]
    # )
    )

    self.msg_container = Stack(
      # spacing=0,
      controls=[
        Container(
          margin=margin.only(right=6),
          alignment=alignment.center_left,
          width = 500,
          padding=10,
          gradient=blue_gradient,
          border_radius=ih_br,
          content=Column(
            spacing=4,
            controls=[
              Text(
                value="سلام! خوش اومدی به برنامه",
                selectable=True,
                color=smc,
                weight=FontWeight.W_400,
                size=14,
                
              ),
              Row(
                spacing=4,
                alignment='end',
                controls=[
                  Text(
                    '5:30 AM',
                    size=10,
                    weight=FontWeight.W_600,
                    color=mtc
                  ),
                  Icon(
                    icons.DONE,
                    color=mtc,
                    size=10
                  )
                ]
              )
            ]
          )
        ),

        
      ]
    )
    self.messages_column = Column(
    scroll='auto',
    expand=True,
    controls=[]  # با مجموعه‌ای خالی از کنترل‌ها شروع می‌شود
)
    sample_messages = [
    "سلام! خوش آمدید به برنامه",
    "این یک پیام نمونه است",
    "تست ارسال پیام"
]

    # پر کردن ستون پیام‌ها
    for message in sample_messages:
        
        self.messages_column.controls.append(create_message(message))
        
    self.msg_obj = Container(
      on_long_press=self.show_msg_menu,
      on_hover=self.msg_hovered,
      
      content=Row(
        spacing=25,
        alignment='end',
        vertical_alignment='center',
        controls=[
          self.msg_hover_emoji,
          self.msg_container,
          
          
        ]
      )
    )
    
    self.msg_container2 = Stack(
      # spacing=0,
      controls=[
        Container(
          margin=margin.only(right=6),
          alignment=alignment.center_left,
          width = 500,
          padding=10,
          gradient=blue_gradient,
          border_radius=ih_br,
          content=Column(
            spacing=4,
            controls=[
              Text(
                value="سلام! خوش اومدی به اپپ",
                selectable=True,
                color=smc,
                weight=FontWeight.W_400,
                size=14,
                
              ),
              Row(
                spacing=4,
                alignment='end',
                controls=[
                  Text(
                    '5:30 AM',
                    size=10,
                    weight=FontWeight.W_600,
                    color=mtc
                  ),
                  Icon(
                    icons.DONE,
                    color=mtc,
                    size=10
                  )
                ]
              )
            ]
          )
        ),

        
      ]
    )

    self.msg_obj = Container(
      on_long_press=self.show_msg_menu,
      on_hover=self.msg_hovered,
      
      content=Row(
        spacing=25,
        alignment='end',
        vertical_alignment='center',
        controls=[
          self.msg_hover_emoji,
          self.msg_container,
          self.msg_container2
          
          
        ]
      )
    )

    self.dm_screen_content = Stack(
      controls=[
        Container(
          content=Column(
            spacing=0,
            controls=[
              Row(
                alignment='spaceBetween',
                controls=[
                  WindowDragArea(
                      expand=True,
                      content=Container(height=40,)
                    ),
                    Row(
                      spacing=0,
                      controls=[
                        Container(
                          on_click=self.mini_window,
                          height=40,
                          width=40,
                          content=Image(
                            src='assets/icons/mini.png'
                          )

                        ),
                        Container(
                          on_click=self.max_window,
                          height=40,
                          width=40,
                          content=Image(
                            src='assets/icons/max.png'
                          )

                        ),
                        Container(
                          on_click=self.close_window,
                          height=40,
                          width=40,
                          content=Image(
                            src='assets/icons/close.png'
                          )

                        ),
                      ]
                    )
                ]
              ),
              
              Container(
                padding=padding.only(left=20,right=15),
                height=50,
                content=Row(
                  alignment='spaceBetween',
                  controls=[
                    Container(
                      on_click=self.show_chat_user_popup,
                      expand=True,
                      content=Row(
                        controls=[
                          Container(
                            height=40,
                            width=40,
                            border_radius=20,
                            bgcolor=rc,
                            content=Icon(
                              icons.PERSON
                            )
                          ),
                          Text(
                            value='#Se7en🙏',
                            color='#e4e4e4'
                          )
                          
                        ]
                      )
                    ),

                    Row(
                      controls=[
                        Container(
                          on_hover=self.sidebar_btn_hovered,
                          alignment=alignment.center,
                          height=s_btn_h,
                          width=s_btn_w,
                          border_radius=5,
                          content=Row(
                            spacing=0,
                            alignment='center',
                            controls=[
                              Icon(
                                icons.VIDEO_CALL_OUTLINED,
                                size=20,
                                color=sb_ic
                              )
                            ]
                          )
                        ),


                        Container(
                          on_hover=self.sidebar_btn_hovered,
                          alignment=alignment.center,
                          height=s_btn_h,
                          width=s_btn_w,
                          border_radius=5,
                          content=Row(
                            spacing=0,
                            alignment='center',
                            controls=[
                              Icon(
                                icons.CALL_OUTLINED,
                                size=20,
                                color=sb_ic
                              )
                            ]
                          )
                        ),
                        
                        Container(
                          height=25,
                          width=2,
                          bgcolor=s_btn_h_c
                        ),
                        
                        Container(
                          on_hover=self.sidebar_btn_hovered,
                          alignment=alignment.center,
                          height=s_btn_h,
                          width=s_btn_w,
                          border_radius=5,
                          content=Row(
                            spacing=0,
                            alignment='center',
                            controls=[
                              Icon(
                                icons.SEARCH_OUTLINED,
                                size=20,
                                color=sb_ic
                              )
                            ]
                          )
                        ),

                      ]
                    ),
                  ]
                )

              ),
              
              Container(
                alignment=alignment.top_left,
                padding=padding.only(left=20,right=20,top=10),
                expand=True,
                image_src=wallpaper,
                image_opacity=0.2,
                image_fit=ImageFit.COVER,
                bgcolor='#1a343434',
                content=Column(
                  scroll='auto',
                  spacing=10,
                  controls=[
                    self.messages_column,
                  ]
                )

              ),
              
              Container(
                margin=margin.only(left=2),
                padding=padding.only(left=10,right=10),
                height=50,
                bgcolor=color['type_bar_black'],
                content=Row(
                  controls=[
                    Container(
                      on_hover=self.sidebar_btn_hovered,
                      on_click=self.show_emojis_popup,
                      alignment=alignment.center,
                      height=40,
                      width=40,
                      border_radius=5,
                      content=Row(
                        spacing=0,
                        alignment='center',
                        controls=[
                          Icon(
                            icons.EMOJI_EMOTIONS_OUTLINED,
                            size=20,
                            color=sb_ic
                          )
                        ]
                      )
                    ),
                    
                    Container(
                      on_hover=self.sidebar_btn_hovered,
                      alignment=alignment.center,
                      height=40,
                      width=40,
                      border_radius=5,
                      content=Row(
                        spacing=0,
                        alignment='center',
                        controls=[
                          Icon(
                            icons.SHARE_OUTLINED,
                            size=20,
                            color=sb_ic
                          )
                        ]
                      )
                    ),
                    
                    Container(
                      on_hover=self.sidebar_btn_hovered,
                      expand=True,
                      content=TextField(
                          expand=True,
                          multiline=True,
                          border=InputBorder.NONE,
                          
                          hint_text='Type a message',
                          
                          hint_style=TextStyle(
                            size=14,
                            font_family='arial',
                            color=color['white_text_font']
                          ),
                          color=sb_ic,
                          text_style=TextStyle(
                            size=14,
                            font_family='arial',
                            color=sb_ic
                          ),
                        ),
                      ),
                    
                    self.send_msg_btn,

                  ]
                )

              ),
            
            ]
          )
        ),

        Container(
          content=Stack(
            controls=[
              self.chat_user_popup,
            ]
          )
        ),
      ]
    )


t = App  

app(target=t,assets_dir='assets')
