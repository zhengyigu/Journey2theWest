import flet as ft
import requests
import time
import math
import asyncio
items = ["aaa","bbb","ccc"]
flag = 0
currant_page  = ""
choice = 0
type_choice = 0
story_choice = 0
character_choice = 0
setting_round =False 
setting_container = None
if_day = 1
#page = ft.Page()
BRAND_VIDEO = [
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\开头品牌.mp4"),
    ]
START_VIDEO = [
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\主界面（循环播放）.mp4"),
    ]
GAMING_VIDEO1 = [ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\背景_animation.mp4")]
MAIN_VIDEO = [
    
        # ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\选项界面(空白).mp4"),
        # ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\选项界面（空白2）.mp4"),
        # ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\选项界面（空白2）.mp4"),
        # ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\选项界面（空白2）.mp4"),
        # ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\选项界面（空白2）.mp4"),
        # ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\选项界面（空白2）.mp4"),
        # ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\选项界面（空白2）.mp4"),
        # ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\选项界面（空白2）.mp4"),
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\选项界面3.mp4"),
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\选项界面(循环).mp4"),
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\选项界面(循环).mp4"),
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\选项界面(循环).mp4"),
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\选项界面(循环).mp4"),
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\选项界面(循环).mp4"),
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\选项界面(循环).mp4"),
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\选项界面(循环).mp4"),
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\选项界面转游戏.mp4")
]
STORY_VIDEO = [
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\故事选择start.mp4"),
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\AI改图-56034ea5b787e45f92da63...-7xh013-1920x1096_animation.mp4"),
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\AI改图-56034ea5b787e45f92da63...-7xh013-1920x1096_animation.mp4"),
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\AI改图-56034ea5b787e45f92da63...-7xh013-1920x1096_animation.mp4"),
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\AI改图-56034ea5b787e45f92da63...-7xh013-1920x1096_animation.mp4"),
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\AI改图-56034ea5b787e45f92da63...-7xh013-1920x1096_animation.mp4"),
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\AI改图-56034ea5b787e45f92da63...-7xh013-1920x1096_animation.mp4"),
        ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\故事选择结束black.mp4")]
STORY_START1 = [ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\story_start1.2.mp4")]
STORY_START2 = [ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\story_start2.2.mp4")]
STORY_START3 = [ft.VideoMedia(r"E:\pythoncode\项目Google\assets\素材\story_start3.2.mp4")]
choice_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\\开始游戏.png",width=300, height=66),
                ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\\系统设置.png",width=300, height=66),
                ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\\退出.png",width=300, height=66),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=0,
        ),
        #alignment=ft.alignment.center_right,
        padding=ft.Padding(100,410,30,0),
        alignment = ft.Alignment(1.0, 1.0)
    )
title_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\标题.png",width=400, height=400),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=0,
        ),
        #alignment=ft.alignment.center_right,
        padding=ft.Padding(100,100,600,0),
        alignment = ft.Alignment(1.0, 1.0)
    )
td = ft.Stack(expand=True)
all_stack = ft.Stack(expand=True)
stack_a = ft.Stack(expand=True)
window_width = 1280
window_height = 760

video_start= ft.Video(
        alignment=ft.Alignment(-1,-1),
            # width=1920,
            # height=1080,
            playlist=START_VIDEO,
            playlist_mode=ft.PlaylistMode.LOOP,
            fill_color=ft.colors.WHITE70,
            aspect_ratio=1980/1080,
            volume=60,
            autoplay=True,
            filter_quality=ft.FilterQuality.HIGH,
            muted=False,
            show_controls=False,
            # on_loaded=lambda e: video_start_ended(),
            # on_enter_fullscreen=lambda e: print("Video entered fullscreen!"),
    )
video_main= ft.Video(
        alignment=ft.Alignment(-1,-1),
            # width=1920,
            # height=1080,
            playlist=MAIN_VIDEO,
            playlist_mode=ft.PlaylistMode.LOOP,
            fill_color=ft.colors.WHITE70,
            aspect_ratio=window_width/window_height,
            volume=60,
            autoplay=True,
            filter_quality=ft.FilterQuality.HIGH,
            muted=False,
            show_controls=False,
            # on_loaded=lambda e: video_start_ended(),
            # on_enter_fullscreen=lambda e: print("Video entered fullscreen!"),
    )
video_story= ft.Video(
        alignment=ft.Alignment(-1,-1),
            playlist=STORY_VIDEO,
            playlist_mode=ft.PlaylistMode.LOOP,
            fill_color=ft.colors.WHITE70,
            aspect_ratio=window_width/window_height,
            volume=60,
            autoplay=True,
            filter_quality=ft.FilterQuality.HIGH,
            muted=False,
            show_controls=False,
            # on_loaded=lambda e: video_start_ended(),
            # on_enter_fullscreen=lambda e: print("Video entered fullscreen!"),
    )
story_start1= ft.Video(#修改startvideo
        alignment=ft.Alignment(-1,-1),
            playlist=STORY_START1,
            playlist_mode=ft.PlaylistMode.NONE,
            fill_color=ft.colors.BLACK,
            aspect_ratio=window_width/window_height,
            volume=100,
            autoplay=False,
            filter_quality=ft.FilterQuality.HIGH,
            muted=False,
            show_controls=False,
            # on_loaded=lambda e: video_start_ended(),
            # on_enter_fullscreen=lambda e: print("Video entered fullscreen!"),
    )
story_start2= ft.Video(
        alignment=ft.Alignment(-1,-1),
            playlist=STORY_START2,
            playlist_mode=ft.PlaylistMode.NONE,
            fill_color=ft.colors.BLACK,
            aspect_ratio=window_width/window_height,
            volume=100,
            autoplay=False,
            filter_quality=ft.FilterQuality.HIGH,
            muted=False,
            show_controls=False,
            # on_loaded=lambda e: video_start_ended(),
            # on_enter_fullscreen=lambda e: print("Video entered fullscreen!"),
    )
story_start3= ft.Video(
        alignment=ft.Alignment(-1,-1),
            playlist=STORY_START3,
            playlist_mode=ft.PlaylistMode.NONE,
            fill_color=ft.colors.BLACK,
            aspect_ratio=window_width/window_height,
            volume=100,
            autoplay=False,
            filter_quality=ft.FilterQuality.HIGH,
            muted=False,
            show_controls=False,
            # on_loaded=lambda e: video_start_ended(),
            # on_enter_fullscreen=lambda e: print("Video entered fullscreen!"),
    )
background_audio1 = ft.Audio(
        #src=r"E:\pythoncode\项目Google\assets\素材\背景音乐.wav", autoplay=True,release_mode=ft.audio.ReleaseMode.LOOP
        src=r"E:\pythoncode\项目Google\assets\素材\背景音乐final.mp3", autoplay=True,release_mode=ft.audio.ReleaseMode.LOOP,volume=1.0
    )
background_audio2 = ft.Audio(
        #src=r"E:\pythoncode\项目Google\assets\素材\背景音乐.wav", autoplay=True,release_mode=ft.audio.ReleaseMode.LOOP
        src=r"E:\pythoncode\项目Google\assets\素材\气氛焦灼.mp3", autoplay=True,release_mode=ft.audio.ReleaseMode.LOOP,volume=0.3
    )
background_audio3 = ft.Audio(
        #src=r"E:\pythoncode\项目Google\assets\素材\背景音乐.wav", autoplay=True,release_mode=ft.audio.ReleaseMode.LOOP
        src=r"E:\pythoncode\项目Google\assets\素材\开始平静中的危机感.mp3", autoplay=True,release_mode=ft.audio.ReleaseMode.LOOP,volume=0.3
    )
thunder = ft.Audio(src = r"E:\pythoncode\项目Google\assets\素材\雷声_01.mp3",autoplay=True,volume=0.7)
image1 = ft.Image(
        src=r"E:\pythoncode\项目Google\assets\素材\故事图标1.png",
        width=315,
        height=450,
    )
image11 = ft.Image(
        src=r"E:\pythoncode\项目Google\assets\素材\人物1.png",
        width=315,
        height=450,
    )
container1 = ft.Container(
        content=image1,
        width=340,
        height=500,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.with_opacity(0,ft.colors.BLACK),
    )
container11 = ft.Container(
        content=image11,
        width=340,
        height=500,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.with_opacity(0,ft.colors.BLACK),
    )
    
    # 第二个容器中的图片
image2 = ft.Image(
        src=r"E:\pythoncode\项目Google\assets\素材\故事图标2.png",
        width=315,
        height=450,
    )
image21 = ft.Image(
        src=r"E:\pythoncode\项目Google\assets\素材\人物2.png",
        width=315,
        height=450,
    )
container2 = ft.Container(
        content=image2,
        width=340,
        height=500,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.with_opacity(0,ft.colors.BLACK),
    )
container21 = ft.Container(
        content=image21,
        width=340,
        height=500,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.with_opacity(0,ft.colors.BLACK),
    )
    # 第三个容器中的图片
image3 = ft.Image(
        src=r"E:\pythoncode\项目Google\assets\素材\故事图标3.png",
        width=315,
        height=450,
    )
image31 = ft.Image(
        src=r"E:\pythoncode\项目Google\assets\素材\人物3.png",
        width=315,
        height=450,
    )
container3 = ft.Container(
        content=image3,
        width=340,
        height=500,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.with_opacity(0,ft.colors.BLACK),
    )
container31 = ft.Container(
        content=image31,
        width=340,
        height=500,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.with_opacity(0,ft.colors.BLACK),
    )
    
    # 在 Row 中放置三个容器
row = ft.Row(
        controls=[container1, container2, container3],
        alignment=ft.MainAxisAlignment.CENTER,  # 设置为居中对齐并等距排列
        spacing=10
    )
row1 = ft.Row(
        controls=[container11, container21, container31],
        alignment=ft.MainAxisAlignment.CENTER,  # 设置为居中对齐并等距排列
        spacing=10
    )
story_container = ft.Container(
            content=ft.Column(
                controls=[
                ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\故事选择.png",width=400,fit=ft.ImageFit.CONTAIN),
                row
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=1100,
            height=630,
            padding=ft.padding.all(20),
            bgcolor=ft.colors.with_opacity(0.5,ft.colors.BLACK),
            border_radius=ft.border_radius.all(20),
            alignment=ft.alignment.center
                    )
character_container = ft.Container(
            content=ft.Column(
                controls=[
                ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\人物选择.png",width=400,fit=ft.ImageFit.CONTAIN),
                row1
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=1100,
            height=630,
            padding=ft.padding.all(20),
            bgcolor=ft.colors.with_opacity(0.5,ft.colors.BLACK),
            border_radius=ft.border_radius.all(20),
            alignment=ft.alignment.center
                    )
gaming_video= ft.Video(
        alignment=ft.Alignment(-1,-1),
            playlist=GAMING_VIDEO1,
            playlist_mode=ft.PlaylistMode.LOOP,
            fill_color=ft.colors.WHITE70,
            aspect_ratio=1920/1080,
            volume=60,
            autoplay=True,
            filter_quality=ft.FilterQuality.HIGH,
            muted=False,
            show_controls=False,
            # on_loaded=lambda e: video_start_ended(),
            # on_enter_fullscreen=lambda e: print("Video entered fullscreen!"),
    )
def change_music(page:ft.Page):
    pass
def gaming(e: ft.KeyboardEvent, page: ft.Page, td: ft.Stack):
    global currant_page
    if currant_page!= "MAIN_GAMING":
        return
    if e.key == "Escape":
        def handle_close(e):
            page.window.close()
        def handle_keep(e):
            global flag
            page.close(dlg_modal)
            flag-=1
        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.Text("Do you really want to log out the game?"),
            actions=[
                ft.TextButton("Yes", on_click=handle_close),
                ft.TextButton("No", on_click=handle_keep),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.open(dlg_modal)
        page.update()
def text_fade_color(page:ft.Page,text_container:ft.Text):
    text_container.color = ft.colors.WHITE
    page.update()
def text_fade_out_color(page:ft.Page,text_container:ft.Text):
    text_container.color = ft.colors.BLACK
    page.update()
async def container_fade_out_color(container, duration=0.5, steps=30):
    step_duration = duration / steps
    for i in range(steps):
        progress = (i + 1) / steps

        # 渐变颜色，从黑色到白色
        new_color_value = int(progress * 255)
        container.bgcolor = f"#{new_color_value:02x}{new_color_value:02x}{new_color_value:02x}"  # 黑色到白色的渐变
        container.opacity = 0.5 - (progress * 0.4)
        container.update()
        await asyncio.sleep(step_duration)
async def container_fade_color(container, duration=0.5, steps=30):
    step_duration = duration / steps
    for i in range(steps):
        progress = (i + 1) / steps

        # 渐变颜色，从白色到黑色
        new_color_value = int((1 - progress) * 255)
        container.bgcolor = f"#{new_color_value:02x}{new_color_value:02x}{new_color_value:02x}"  # 白色到黑色的渐变

        # 渐变透明度
        container.opacity = 0.2 + (progress * 0.3)  # 从 0.2 逐渐变到 0.5

        container.update()
        await asyncio.sleep(step_duration)
def turn_to_night(page:ft.Page):
    global if_day
    if_day = 0
    for text in page.controls[0].controls[1].controls[1].content.controls[0].content.controls[0].content.controls[1].controls:
        text.color = ft.colors.WHITE
    page.update()
    text_fade_color(page,page.controls[0].controls[1].controls[1].content.controls[0].content.controls[0].content.controls[0].content.controls[0])
    page.controls[0].controls[1].controls[1].content.controls[0].content.controls[0].content.controls[0].content.controls[1].value = "夜晚"
    page.update()
    text_fade_out_color(page,page.controls[0].controls[1].controls[1].content.controls[0].content.controls[0].content.controls[0].content.controls[1])
    asyncio.run(container_fade_color(page.controls[0].controls[1].controls[0]))
def turn_to_day(page:ft.Page):
    global if_day
    if_day = 1
    for text in page.controls[0].controls[1].controls[1].content.controls[0].content.controls[0].content.controls[1].controls:
        text.color = ft.colors.BLACK
    page.update()
    text_fade_out_color(page,page.controls[0].controls[1].controls[1].content.controls[0].content.controls[0].content.controls[0].content.controls[0])
    page.controls[0].controls[1].controls[1].content.controls[0].content.controls[0].content.controls[0].content.controls[1].value = "白天"
    page.update()
    text_fade_color(page,page.controls[0].controls[1].controls[1].content.controls[0].content.controls[0].content.controls[0].content.controls[1])
    asyncio.run(container_fade_out_color(page.controls[0].controls[1].controls[0]))
def submit_move(event,page:ft.Page):#交互后端接口（用户输入的信息and后端传入的信息）
    if event.control.value.strip():
        global if_day
        if event.control.value == "":
            return
        if event.control.value == "\背包":
            global type_choice
            if type_choice == 0:
                page.controls[0].controls[1].controls[1].content.controls[1].content.controls[0].value = ""
                page.controls[0].controls[1].controls[1].content.controls[0].content.controls[0].content.controls[1].controls.append(ft.Text("当前模式不支持背包系统", no_wrap=False,size=20,color= ft.colors.RED_200))
                page.update()
                return
            if type_choice == 1:
                page.controls[0].controls[1].controls[1].content.controls[1].content.controls[0].value = ""
                global items
                def on_leave(e):
                    async def fade_out_container():
                        for i in range(10):
                            page.controls[0].controls[-1].controls[0].opacity =1 - i / 10
                            await page.update_async()
                            await asyncio.sleep(0.02)  # 控制渐变速度
                        page.controls[0].controls[-1].controls[0].opacity = 0.0  # 确保完全透明
                        await page.update_async()
                        await asyncio.sleep(0.3)  # 每张图片延迟0.5秒消失
                    asyncio.run(fade_out_container())
                    page.update()
                    page.controls[0].controls[1].controls[1].content.controls[0].content.controls[0].content.controls[1].controls.append(ft.Text(f"您使用了：{e.control.content.content.value}", no_wrap=False,size=20,color= ft.colors.BLACK if if_day == 1 else ft.colors.WHITE))
                    page.update()
                    print(e.control.content.content.value)
                item_list_view = ft.ListView(
                        controls=[
                            ft.Container(ft.DragTarget(content = ft.Draggable(content=ft.Text(i, size=20,color=ft.colors.WHITE),data=i),on_will_accept=lambda e: e.data == "Dragged Text",on_leave=on_leave,),alignment=ft.alignment.center) for i in items
                        ],
                        width=300,
                        height=500,
                        spacing=10
                    )
                item_container = ft.Container(
                    content=item_list_view,
                    bgcolor=ft.colors.with_opacity(0.5,ft.colors.BLACK),  # 半透明黑色背景
                    width=300,
                    height=500,
                    border_radius=ft.border_radius.all(10),
                )
                bag_container = ft.Container(content=item_container,padding=ft.Padding(870,80,40,40),)
                stack_bag = ft.Stack(
                    controls=[bag_container],
                    alignment=ft.Alignment(1,1)
                )
                async def fade_in_container():
                    for i in range(10):
                        page.controls[0].controls[-1].controls[0].opacity = i / 10
                        await page.update_async()
                        await asyncio.sleep(0.1)  # 控制渐变速度
                    await asyncio.sleep(0.5)  # 每张图片延迟0.5秒出现
                page.controls[0].controls.append(stack_bag)
                page.update()
                asyncio.run(fade_in_container())
                page.update()
            #打开背包
            return
        page.controls[0].controls[1].controls[1].content.controls[0].content.controls[0].content.controls[1].controls.append(ft.Text(f"您选择：{event.control.value}", no_wrap=False,size=20,color= ft.colors.BLACK if if_day == 1 else ft.colors.WHITE))
        page.controls[0].controls[1].controls[1].content.controls[1].content.controls[0].hint_text="请输入下一步的动作"
        page.controls[0].controls[1].controls[1].content.controls[1].content.controls[0].value = ""
        page.update()
def gaming_page(page: ft.Page):
    global story_choice
    async def fade_in_images():
        for i in range(10):
            page.controls[-1].controls[1].controls[0].opacity = i / 10
            page.controls[-1].controls[0].opacity = i / 10
            await page.update_async()
            await asyncio.sleep(0.1)  # 控制渐变速度
        await asyncio.sleep(0.5)  # 每张图片延迟0.5秒出现
    if story_choice == 1:
        first_character_shadow = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\角色1black.png")
    elif story_choice ==2:
        pass
    elif story_choice == 3:
        pass
    #明天任务：4.沙悟净的行囊装配，5.后端接口,6.音乐
    black_mask = ft.Container(
        width=1160,
        height=640,
        padding=ft.padding.all(10),
        bgcolor=ft.colors.with_opacity(0.2,ft.colors.WHITE),
        border_radius=ft.border_radius.all(40),
        alignment=ft.alignment.center,
    )
    #TEXT位置：page.controls[0].controls[1].controls[1].content.controls[0].content.controls[0].content.controls[1].controls(Text列表)
    #时间表位置：page.controls[0].controls[1].controls[1].content.controls[0].content.controls[0].content.controls[0].content
    
    container_inside = ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    content=ft.Row(
                                        controls=[
                                                    ft.Container(
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Container(
                                                                    content= ft.Row(
                                                                        controls = [
                                                                            ft.Text("时间：",color=ft.colors.BLACK,size=30),
                                                                            ft.Text("白天",color=ft.colors.WHITE,size=30)
                                                                            ]
                                                                    ),
                                                                    padding = ft.Padding(25,0,25,0),
                                                                    border_radius=ft.border_radius.all(20),
                                                                    width=200, height=50, bgcolor=ft.colors.with_opacity(0.4,ft.colors.WHITE70)),##时间表
                                                                ft.ListView(
                                                                    controls = [ft.Text("event.control.value", no_wrap=False,size=20,color= ft.colors.BLACK)],
                                                                    auto_scroll = True,
                                                                    width=800, height=460)###主要内容
                                                                # ft.Container(
                                                                #     content=ft.Text(
                                                                #         value = "",
                                                                #         color=ft.colors.BLACK ,size=20
                                                                #     ),
                                                                #     width=800, height=460, bgcolor=ft.colors.with_opacity(0.0,ft.colors.BLACK))###主要内容
                                                            ]
                                                        ),
                                                        width=800, height=520, bgcolor=ft.colors.with_opacity(0.0,ft.colors.BLACK)),
                                                    ft.Container(
                                                        content = first_character_shadow,padding=ft.Padding(0,30,0,0),###人物图像
                                                        width=300, height=520, bgcolor=ft.colors.with_opacity(0.0,ft.colors.BLACK))]
                                    ),
                                    width=1100, height=540, bgcolor=ft.colors.with_opacity(0.0,ft.colors.BLACK)),
                                ft.Container(
                                    content = ft.Row(
                                        controls=[ft.TextField(
                                            hint_text="请输入下一步的动作",
                                            bgcolor=ft.colors.with_opacity(0.4,ft.colors.WHITE70),
                                            border_color="transparent",
                                            border_radius=ft.border_radius.all(20),
                                            content_padding=ft.padding.only(left=10, right=10),
                                            expand=True,
                                            on_submit=lambda event: submit_move(event, page)
                                        ),
                                        ft.Container(
                                            content = ft.Text("沙悟净的行囊",color=ft.colors.BLACK,size=20),
                                            alignment=ft.alignment.center,
                                            width=300,height=47,bgcolor=ft.colors.with_opacity(0.4,ft.colors.WHITE70), border_radius=ft.border_radius.all(20))]
                                    ),
                                    width=1100, height=60,bgcolor=ft.colors.with_opacity(0.0,ft.colors.WHITE70), border_radius=ft.border_radius.all(20))
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        width=1160,
                        height=640,
                        padding=ft.padding.all(10),
                        bgcolor=ft.colors.with_opacity(0.0,ft.colors.BLACK),
                        border_radius=ft.border_radius.all(40),
                        alignment=ft.alignment.center,
                    )
    stack_a1= ft.Stack(
                        [black_mask,container_inside],
                        width=1920,
                        height=1080,alignment=ft.Alignment(0,-0.5),opacity=1)
    stack = ft.Stack(
        controls=[
            gaming_video,        # 视频放在最底层
            stack_a1,  # 最上层的容器
        ],
        width=1280,
        height=760
    )
    page.controls.append(stack)
    asyncio.run(fade_in_images())
    page.add(background_audio3)
    page.update()
    # time.sleep(4)
    # turn_to_night(page)时间变化调用方式
    
def starting_game(e: ft.KeyboardEvent, page: ft.Page, td: ft.Stack):
    global currant_page
    global story_choice
    if currant_page != "STARTING_GAME":
        return
    if e.key == "Enter":
        currant_page = "MAIN_GAMING"
        td.controls[-2].play()
        page.update()
        time.sleep(7)
        async def fade_out_container(container1,container2):
            for i in range(10):
                container1.opacity =1 - i / 10
                container2.opacity =1 - i / 10
                await page.update_async()
                await asyncio.sleep(0.05)  # 控制渐变速度
            container1.opacity = 0.0  # 确保完全透明
            container2.opacity = 0.0
            await page.update_async()
            await asyncio.sleep(0.5)  # 每张图片延迟0.5秒消失
        def fade_out(audio_control, duration=3):
            steps = 50  # 分成多少步
            print(page.controls[-1].volume)
            print(td.controls[-2])
            step_duration = duration / steps  # 每步的时间
            volume_decrement = page.controls[-1].volume / steps  # 每步减少的音量
            for i in range(steps):
                if i == 20:
                    asyncio.run(fade_out_container(td.controls[-1],td.controls[-2]))
                new_volume = max(0, audio_control.volume - volume_decrement)
                audio_control.volume = new_volume
                audio_control.update()
                time.sleep(step_duration)
        fade_out(page.controls[-1])
        td.controls.pop()
        td.controls.pop()
        page.controls.pop()
        page.clean()
        page.update()
        gaming_page(page)
        page.on_keyboard_event = lambda e:gaming(e,page,td)
        print(page.controls)
        if story_choice == 1:
            pass
        if story_choice == 2:
            pass
        if story_choice == 3:
            pass
    if e.key == "Escape":
        def handle_close(e):
            page.window.close()
        def handle_keep(e):
            global flag
            page.close(dlg_modal)
            flag-=1
        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.Text("Do you really want to log out the game?"),
            actions=[
                ft.TextButton("Yes", on_click=handle_close),
                ft.TextButton("No", on_click=handle_keep),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.open(dlg_modal)
        page.update()

def character_choosing(e: ft.KeyboardEvent, page: ft.Page, td: ft.Stack):
    global currant_page
    global character_choice
    global story_choice
    if currant_page!="CHARACTER_CHOOSING":
        return
    if e.key == "1":
        td.controls[-1].controls[1].content.controls[1].controls[0].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\人物1.png",width=340,height=470)
        td.controls[-1].controls[1].content.controls[1].controls[1].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\人物2.png",width=315,height=450)
        td.controls[-1].controls[1].content.controls[1].controls[2].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\人物3.png",width=315,height=450)
        page.update()
        character_choice = 1
        print(character_choice)
        return
    if e.key == "2":
        td.controls[-1].controls[1].content.controls[1].controls[0].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\人物1.png",width=315,height=450)
        td.controls[-1].controls[1].content.controls[1].controls[1].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\人物2.png",width=340,height=470)
        td.controls[-1].controls[1].content.controls[1].controls[2].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\人物3.png",width=315,height=450)
        page.update()
        character_choice = 2
        print(character_choice)
        return
    if e.key == "3":
        td.controls[-1].controls[1].content.controls[1].controls[0].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\人物1.png",width=315,height=450)
        td.controls[-1].controls[1].content.controls[1].controls[1].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\人物2.png",width=315,height=450)
        td.controls[-1].controls[1].content.controls[1].controls[2].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\人物3.png",width=370,height=470)
        page.update()
        character_choice = 3
        print(character_choice)
        return
    if  e.key == "Enter":
        currant_page = "STARTING_GAME"
        response = requests.post("http://127.0.0.1:5000/character_choosing", json={"setting": "character", "choice": str(character_choice)})
        data = response.json()
        async def fade_out_container():
            for i in range(10):
                td.controls[-1].controls[1].opacity =1 - i / 10
                await page.update_async()
                await asyncio.sleep(0.05)  # 控制渐变速度
            td.controls[-1].controls[1].opacity = 0.0  # 确保完全透明
            await page.update_async()
            await asyncio.sleep(0.5)  # 每张图片延迟0.5秒消失
        def fade_out(audio_control, duration=3):
            steps = 50  # 分成多少步
            step_duration = duration / steps  # 每步的时间
            volume_decrement = 1.0 / steps  # 每步减少的音量
            for i in range(steps):
                if i == 10:
                    asyncio.run(fade_out_container())
                    page.update()
                if i == 25:
                    td.controls.pop()
                    video_story.jump_to(7)
                    page.update()
                new_volume = max(0, audio_control.volume - volume_decrement)
                audio_control.volume = new_volume
                audio_control.update()
                time.sleep(step_duration)
        fade_out(page.controls[0])
        page.bgcolor = ft.colors.BLACK
        page.clean()
        #page.update()
        td = ft.Stack(
        [ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\black.png")],
        width=1920,
        height=1080,alignment=ft.Alignment(-1,-1))
        page.add(td)
        page.update()
        async def fade_in_images():
            for i in range(10):
                td.controls[1].opacity = i / 10
                await page.update_async()
                await asyncio.sleep(0.1)  # 控制渐变速度
            await asyncio.sleep(0.5)  # 每张图片延迟0.5秒出现
        text_control = ft.Text("",color=ft.colors.WHITE ,size=20)
        async def stream_text(text_control, content, delay=0.1):#修改
            for char in content:
                td.controls[-1].content.value += char
                td.controls[-1].content.update()
                await asyncio.sleep(delay)
        if story_choice == 1:
            text_container = ft.Container(text_control,
                        padding=ft.Padding(70,90,500,0),
                        alignment=ft.alignment.top_left)
            #td.controls.append(ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\开始1black.png"))
            td.controls.append(story_start1)
        elif story_choice == 2:
            text_container = ft.Container(text_control,
                        padding=ft.Padding(70,90,500,0),#文字位置设置
                        alignment=ft.alignment.top_left)
            #td.controls.append(ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\开始2black.png"))
            td.controls.append(story_start2)
        elif story_choice == 3:
            text_container = ft.Container(text_control,
                        padding=ft.Padding(500,90,70,0),
                        alignment=ft.alignment.top_left)
            #td.controls.append(ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\开始3black.png"))
            td.controls.append(story_start3)
        asyncio.run(fade_in_images())
        page.update()
        time.sleep(1)
        td.controls.append(text_container)
        page.update()
        if story_choice == 1:
            content = "   烈日当空，炙热的阳光铺洒在一片荒芜的土地上。唐僧师徒四人一路西行，眼见前方山脉连绵，尽是红岩似火，仿佛天地间弥漫着无尽的热浪。四周没有一丝风，空气中仿佛燃烧着，看不到任何生机，连一株草木也未曾生长。远处的山岭似在燃烧，烈焰吞吐，热浪滚滚，热得人心生畏惧。\n\n   他们虽一路克服了无数艰险，但此刻却不由得驻足不前。汗水从唐僧的额头流下，湿透了僧衣，悟空眼中闪烁着警觉，耳畔微微一动，似乎听到了某种预兆。八戒擦拭着脸上的汗珠，低声自语着什么，沙僧则稳稳地立在师傅身侧，紧握着手中的行李。\n\n   眼前的景象似乎在昭示着一场难以避免的考验，师徒四人虽不言语，但都明白，这条取经之路，注定要面对更多未知的险阻。而此刻，他们站在这炙热的山脚下，望着那连绵不断的火红山岭，心中隐隐感到，此行之路，或许比他们预想的更加艰难。"
            page.add(background_audio2)
            page.update()
        elif story_choice == 2:
            content = "   群山巍峨，阴云低垂，狮驼岭的轮廓在远处隐约可见，如同一头沉睡的巨兽横卧于天地之间。唐僧师徒四人一路披荆斩棘，行至此地，眼前的景象却让他们不禁驻足凝神。山岭两侧怪石嶙峋，苍松枯藤相互交缠，仿佛在这寂静的天地间低语，传递着某种难以言喻的凶险。\n\n   狮驼岭的山风带着一股寒意，仿佛预示着这片土地上潜藏着不安的气息。孙悟空手中的金箍棒微微晃动，眼中透出警惕，似乎察觉到前方有什么东西在等待着他们。唐僧双手合十，心中默念着佛号，试图平息那莫名的心悸。八戒环顾四周，鼻尖嗅到一丝腥味，低声嘀咕着此地的不祥，沙僧则一言不发，紧握手中的行李。\n\n   四周的空气沉重而压抑，仿佛连呼吸都变得艰难。眼前的狮驼岭像是一个巨大的屏障，拦在他们的取经之路上。尽管四人一路风雨兼程，但此刻，每个人的心中都隐隐感到，这片诡异的山岭中，或许正潜伏着一场他们无法预料的挑战。一阵低沉的兽吼从山林深处传来，仿佛在暗示着他们，即将面临的考验远比以往更加艰险。"
            page.add(background_audio3)
            page.update()
        elif story_choice == 3:
            content = "   晨光熹微，天地间笼罩在一片薄雾之中。唐僧师徒四人继续西行，沿途山川秀丽，景色本应令人心旷神怡。然而，此时的队伍却笼罩着一层无形的阴影。孙悟空神色凝重，目光时而闪烁着困惑与不安，八戒也不再像往常那般随意打趣，而是满脸狐疑地打量着身旁的猴兄弟。沙僧始终沉默，似乎在心中酝酿着某种念头。唐僧虽然表面平静，但双眉微皱，显然察觉到气氛的异常。\n\n   一路上，师徒之间的默契似乎正悄然瓦解，彼此间的信任不再如昔。那只熟悉的孙悟空，似乎在不经意间变得陌生，连他自己也无法解释，为什么有种似曾相识又模糊不清的感觉始终缠绕在心头。\n\n   他们都明白，前方的路依然漫长，而此刻他们正处在一场无形的风暴中心。究竟是误会，还是另有玄机？是谁在暗中操控这场诡异的局面？在这个扑朔迷离的时刻，真假难辨的谜团正逐渐浮出水面，而师徒四人的命运，也将因此迎来新的波折与考验。"
            page.add(background_audio3)
            page.update()
        asyncio.run(stream_text(text_control, content))
        page.on_keyboard_event = lambda e:starting_game(e,page,td)
def story_choosing(e: ft.KeyboardEvent, page: ft.Page, td: ft.Stack):
    global currant_page
    global story_choice
    if currant_page!="STORY_CHOOSING":
        return
    if e.key == "1":
        td.controls[-1].controls[0].content.controls[1].controls[0].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\故事图标1.png",width=340,height=470)
        td.controls[-1].controls[0].content.controls[1].controls[1].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\故事图标2.png",width=315,height=450)
        td.controls[-1].controls[0].content.controls[1].controls[2].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\故事图标3.png",width=315,height=450)
        page.update()
        story_choice = 1
        print(story_choice)
        return
    if e.key == "2":
        td.controls[-1].controls[0].content.controls[1].controls[0].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\故事图标1.png",width=315,height=450)
        td.controls[-1].controls[0].content.controls[1].controls[1].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\故事图标2.png",width=340,height=470)
        td.controls[-1].controls[0].content.controls[1].controls[2].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\故事图标3.png",width=315,height=450)
        page.update()
        story_choice = 2
        print(story_choice)
        return
    if e.key == "3":
        td.controls[-1].controls[0].content.controls[1].controls[0].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\故事图标1.png",width=315,height=450)
        td.controls[-1].controls[0].content.controls[1].controls[1].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\故事图标2.png",width=315,height=450)
        td.controls[-1].controls[0].content.controls[1].controls[2].content = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\故事图标3.png",width=370,height=470)
        page.update()
        story_choice = 3
        print(story_choice)
        return
    if  e.key == "Enter":
        currant_page = "CHARACTER_CHOOSING"
        response = requests.post("http://127.0.0.1:5000/story_choosing", json={"setting": "character", "choice": str(story_choice)})
        data = response.json()
        async def fade_out_image():
            for i in range(10):
                td.controls[-1].controls[0].opacity =1 - i / 10
                await page.update_async()
                await asyncio.sleep(0.05)  # 控制渐变速度
            td.controls[-1].controls[0].opacity = 0.0  # 确保完全透明
            await page.update_async()
            await asyncio.sleep(0.5)  # 每张图片延迟0.5秒消失
        #td.controls.append(td.controls[-1].controls[0].content.controls[1])
        asyncio.run(fade_out_image())
        page.update()
        time.sleep(0.5)
        #page.bgcolor = ft.colors.BLACK
        async def fade_in_images():
            for i in range(10):
                character_container.opacity = i / 10
                await page.update_async()
                await asyncio.sleep(0.05)  # 控制渐变速度
            await asyncio.sleep(0.5)  # 每张图片延迟0.5秒出现
        td.controls[-1].controls.append(character_container)
        asyncio.run(fade_in_images())
        page.update()
        page.on_keyboard_event = lambda e:character_choosing(e,page,td)
        page.update()
        
def choose_story(e: ft.KeyboardEvent, page: ft.Page, td: ft.Stack):
    global currant_page
    global type_choice
    if currant_page!="TYPE_CHOOSING":
        return
    global choice
    if e.key == "1":
        td.controls[-1].controls[0].content.controls[1].content.controls[0].controls[1] =ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\白框.png", width=430,height=200)
        td.controls[-1].controls[0].content.controls[1].content.controls[1].controls[1] =ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\非白框.png", width=430,height=200)
        page.update()
        choice = 1
        type_choice = 0
        print(choice)
        return
    if e.key == "2":
        td.controls[-1].controls[0].content.controls[1].content.controls[1].controls[1] =ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\白框.png", width=430,height=200)
        td.controls[-1].controls[0].content.controls[1].content.controls[0].controls[1] =ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\非白框.png", width=430,height=200)
        page.update()
        choice = 2
        type_choice = 1
        print(choice)
        return
    if e.key == "Enter":
        response = requests.post("http://127.0.0.1:5000/setting_choosing", json={"setting": "character", "choice": str(type_choice)})
        data = response.json()
        async def fade_out_image():
            for i in range(10):
                td.controls[-1].controls[0].opacity =1 - i / 10
                await page.update_async()
                await asyncio.sleep(0.05)  # 控制渐变速度
            td.controls[-1].controls[0].opacity = 0.0  # 确保完全透明
            await page.update_async()
            await asyncio.sleep(0.5)  # 每张图片延迟0.5秒消失
        #td.controls.append(td.controls[-1].controls[0].content.controls[1])
        asyncio.run(fade_out_image())
        page.update()
        video_main.jump_to(8)
        page.update()
        time.sleep(1.5)
        page.controls.pop()
        page.update()
        story_stack = ft.Stack(
                        [story_container],
                        width=1920,
                        height=1080,alignment=ft.Alignment(0,-0.81),opacity=1)
        td = ft.Stack(
            controls=[video_story]
            )
        page.add(td)
        page.update()
        time.sleep(1.6)
        #page.bgcolor = ft.colors.BLACK
        async def fade_in_images():
            for i in range(10):
                story_container.opacity = i / 10
                await page.update_async()
                await asyncio.sleep(0.05)  # 控制渐变速度
            await asyncio.sleep(0.5)  # 每张图片延迟0.5秒出现
        td.controls.append(story_stack)
        asyncio.run(fade_in_images())
        page.update()
        currant_page = "STORY_CHOOSING"
        page.on_keyboard_event = lambda e:story_choosing(e,page,td)
        return

def choice_on_key_press(e: ft.KeyboardEvent, page: ft.Page, td: ft.Stack):
    global flag
    global choice
    global currant_page
    global stack_a
    global setting_round
    global setting_container
    if currant_page == "SETTING" and e.key == "Enter":
        async def fade_out_stack_a():
            
            for i in range(10):
                stack_a.controls[0].opacity =1 - i / 10
                await page.update_async()
                await asyncio.sleep(0.05)  # 控制渐变速度
            stack_a.controls[0].opacity = 0.0  # 确保完全透明
            await page.update_async()
            await asyncio.sleep(0.5)  # 每张图片延迟0.5秒消失
        if flag== 2 and currant_page == "SETTING":
            print(f"td:{td.controls}")
            asyncio.run(fade_out_stack_a())
            page.update()
            print(f"td:{td.controls}")
            
            print(f"td:{td.controls}")
            flag-=1
            currant_page = "MAIN"
            async def fade_in_images():
                for i in range(10):
                    choice_container.opacity = i / 10
                    #title_container.opacity = i/10
                    await page.update_async()
                    await asyncio.sleep(0.1)  # 控制渐变速度
                await asyncio.sleep(0.5)  # 每张图片延迟0.5秒出现
            #td.controls.append(choice_container)
            #td.controls.append(title_container)
            asyncio.run(fade_in_images())
            page.update()
        #page.on_keyboard_event = lambda e:choice_on_key_press(e,page,td)
            print(f"now:flag:{flag}")
            return
    if e.key == "1":
        td.controls[1].content.controls[0] = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\\开始游戏1.png",width=300, height=66)
        td.controls[1].content.controls[1] = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\\系统设置.png",width=300, height=66)
        td.controls[1].content.controls[2] = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\\退出.png",width=300, height=66)
        page.update()
        choice = 1
    if e.key == "2":
        td.controls[1].content.controls[0] = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\\开始游戏.png",width=300, height=66)
        td.controls[1].content.controls[1] = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\\系统设置1.png",width=300, height=66)
        td.controls[1].content.controls[2] = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\\退出.png",width=300, height=66)
        page.update()
        choice = 2
    if e.key == "3":
        td.controls[1].content.controls[0] = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\\开始游戏.png",width=300, height=66)
        td.controls[1].content.controls[1] = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\\系统设置.png",width=300, height=66)
        td.controls[1].content.controls[2] = ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\\退出1.png",width=300, height=66)
        page.update()
        choice = 3
    #page.on_keyboard_event = lambda e:Enter_setting(e,page,td)
    if e.key == "Enter" and currant_page == "MAIN":
        async def fade_out_images():
            for i in range(10):
                choice_container.opacity =1 - i / 10
                await page.update_async()
                await asyncio.sleep(0.05)  # 控制渐变速度
            choice_container.opacity = 0.0  # 确保完全透明
            await page.update_async()
            await asyncio.sleep(0.5)  # 每张图片延迟0.5秒消失
        
        
        #global flag
        if choice < 3:
            if flag == 1:
                print(f"choice:{choice}")
                #td.controls.append(choice_container)
                asyncio.run(fade_out_images())
                page.update()
                flag+=1
                print(f"flag:{flag}")
                #根据不同choice值进入游戏or系统设置
                if choice == 1:
                    type_image1 = ft.Image(
                        src=r"E:\pythoncode\项目Google\assets\素材\classicword.png",
                        width=193,
                        height=100
                    )
    
                    type_image2 = ft.Image(
                        src=r"E:\pythoncode\项目Google\assets\素材\经典模式.png",
        
                    )
                    type_container1 = ft.Container(

                        content=ft.Column(
                            controls=[
                                type_image1,
                                type_image2
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        bgcolor=ft.colors.with_opacity(0, ft.colors.BLACK),
                        width=193,  # 40% of 800px (Row container width)
                        height=200,
                        alignment=ft.alignment.center
                    )

                    image = ft.Image(
                        src=r"E:\pythoncode\项目Google\assets\素材\classic.png", 
                        width=237,  # 60% of 800px (Row container width)
                        height=200
                    )

                    row_container1 = ft.Container(
                        content=ft.Row(
                            controls=[
                                type_container1,
                                image
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        width=430,
                        height=200,
                        bgcolor=ft.colors.with_opacity(0, ft.colors.BLACK),
                        alignment=ft.alignment.center
                    )
                    image_in_stack1 = ft.Image(
                        src=r"E:\pythoncode\项目Google\assets\素材\非白框.png", 
                        width=430,  # 60% of 800px (Row container width)
                        height=200
                    )
                    type_stack1 = ft.Stack(
                        controls=[
                            row_container1, 
                            image_in_stack1
                        ],
                        width=800,
                        height=200,
                        alignment=ft.alignment.center
                    )
    
                    type_image3 = ft.Image(
                        src=r"E:\pythoncode\项目Google\assets\素材\DLCword.png",
                        width=193,
                        height=100
                    )
    
                    type_image4 = ft.Image(
                        src=r"E:\pythoncode\项目Google\assets\素材\创意工坊.png",
        
                    )
                    type_container2 = ft.Container(

                        content=ft.Column(
                            controls=[
                                type_image3,
                                type_image4
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        bgcolor=ft.colors.with_opacity(0, ft.colors.BLACK),
                        width=193,  # 40% of 800px (Row container width)
                        height=200,
                        alignment=ft.alignment.center
                    )

                    image1 = ft.Image(
                        src=r"E:\pythoncode\项目Google\assets\素材\DLC.png", 
                        width=237,  # 60% of 800px (Row container width)
                        height=200
                    )

                    row_container2 = ft.Container(
                        content=ft.Row(
                            controls=[
                                type_container2,
                                image1
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        width=430,
                        height=200,
                        bgcolor=ft.colors.with_opacity(0, ft.colors.BLACK),
                        alignment=ft.alignment.center
                    )
                    image_in_stack2 = ft.Image(
                        src=r"E:\pythoncode\项目Google\assets\素材\非白框.png", 
                        width=430,  # 60% of 800px (Row container width)
                        height=200
                    )
                    type_stack2 = ft.Stack(
                        controls=[
                            row_container2, 
                            image_in_stack2
                        ],
                        width=800,
                        height=200,
                        alignment=ft.alignment.center
                    )
                    type_choice_container = ft.Container(
                        content=ft.Column(
                            controls=[
                                type_stack1,
                                type_stack2
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing = 40
                        ),
                        bgcolor=ft.colors.with_opacity(0, ft.colors.BLACK),
                        width=430,  # 40% of 800px (Row container width)
                        height=400,
                        alignment=ft.alignment.center
                    )
                    #page.controls.append(type_choice_container)
                    #page.update()
                    type_container = ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\选择模式.png",fit=ft.ImageFit.CONTAIN),
                                type_choice_container
                                #ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\音量.png",width=200, height=44,fit=ft.ImageFit.CONTAIN),
                                
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        width=430,
                        height=800,
                        #padding=ft.Padding(800,0,50,0),
                        padding=ft.Padding(0, 15, 0, 50),
                        bgcolor=ft.colors.with_opacity(0.3,ft.colors.BLACK),
                        #border_radius=ft.border_radius.all(20),
                        alignment=ft.alignment.top_left
                    )
                    stack_type= ft.Stack(
                        [type_container],
                        width=1920,
                        height=1080,alignment=ft.Alignment(0.9,-1),opacity=1)
                    async def fade_in_images():
                        for i in range(10):
                            type_container.opacity = i / 10
                            await page.update_async()
                            await asyncio.sleep(0.05)  # 控制渐变速度
                        await asyncio.sleep(0.5)  # 每张图片延迟0.5秒出现
                    td.controls.append(stack_type)
                    asyncio.run(fade_in_images())
                    page.update()
                    currant_page = "TYPE_CHOOSING"
                    page.on_keyboard_event = lambda e:choose_story(e,page,td)
                    print("nb")
                    print(page.controls)
                    return
                    #pass#进入游戏接口
                if choice == 2:
                    if setting_round == True:
                        async def fade_in_images():
                            for i in range(10):
                                setting_container.opacity = i / 10
                                await page.update_async()
                                await asyncio.sleep(0.05)  # 控制渐变速度
                            await asyncio.sleep(0.5)  # 每张图片延迟0.5秒出现
                        asyncio.run(fade_in_images())
                        page.update()
                        currant_page = "SETTING"
                        return
                    def music_volumn_change(e):
                        page.controls[0].volume = int(e.control.value)/100
                        page.update()
                    gap_slider = ft.Slider(
                        min=0,
                        max=100,
                        divisions=20,
                        value=0,
                        label="{value}",
                        on_change=music_volumn_change,
                        width=500
                    )
                    setting_container = ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\\系统设置.png",width=300, height=66,fit=ft.ImageFit.CONTAIN),
                                ft.Image(src=r"E:\pythoncode\项目Google\assets\素材\音量.png",width=200, height=44,fit=ft.ImageFit.CONTAIN),
                                gap_slider,
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        width=1000,
                        height=600,
                        padding=ft.padding.all(20),
                        bgcolor=ft.colors.with_opacity(0.5,ft.colors.WHITE70),
                        border_radius=ft.border_radius.all(20),
                        alignment=ft.alignment.center
                    )
                    
                    stack_a= ft.Stack(
                        [setting_container],
                        width=1920,
                        height=1080,alignment=ft.Alignment(0,-0.74),opacity=1)
                    async def fade_in_images():
                        for i in range(10):
                            setting_container.opacity = i / 10
                            await page.update_async()
                            await asyncio.sleep(0.05)  # 控制渐变速度
                        await asyncio.sleep(0.5)  # 每张图片延迟0.5秒出现
                    td.controls.append(stack_a)
                    asyncio.run(fade_in_images())
                    print("ok")
                    page.update()
                    print(f"td:{td.controls}")
                    currant_page = "SETTING"
                    setting_round = True
                    #page.on_keyboard_event = lambda e:setting_back_to_main_page(e,page,td)
        else:
            if flag == 1:
                flag+=1
                def handle_close(e):
                    page.window.close()
                def handle_keep(e):
                    global flag
                    page.close(dlg_modal)
                    flag-=1
                dlg_modal = ft.AlertDialog(
                    modal=True,
                    title=ft.Text("Please confirm"),
                    content=ft.Text("Do you really want to log out the game?"),
                    actions=[
                        ft.TextButton("Yes", on_click=handle_close),
                        ft.TextButton("No", on_click=handle_keep),
                    ],
                    actions_alignment=ft.MainAxisAlignment.END,
                )
                page.open(dlg_modal)
                page.update()
def main_on_key_press(e: ft.KeyboardEvent, page: ft.Page, td: ft.Stack):
    global flag
    global currant_page
    if e.key == "Enter" and flag == 0:
        async def fade_in_images():
            for i in range(10):
                choice_container.opacity = i / 10
                await page.update_async()
                await asyncio.sleep(0.1)  # 控制渐变速度
            await asyncio.sleep(0.5)  # 每张图片延迟0.5秒出现
        flag +=1
        if td.controls[0].get_current_position() <=15060:
            td.controls[0].seek(15060)
            page.update()
            time.sleep(1.3)
            page.remove(td)
            td = ft.Stack(
            [video_main],
            width=1920,
            height=1080,alignment=ft.Alignment(-1,-1))
            page.add(td)
            page.update()
            time.sleep(3)
            td.controls.append(choice_container)
            asyncio.run(fade_in_images())
            page.update()
            
            currant_page = "MAIN"
            page.on_keyboard_event = lambda e:choice_on_key_press(e,page,td)
        else:
            td.controls[0].seek(31120)
            page.update()
            time.sleep(1)
            page.remove(td)
            td = ft.Stack(
            [video_main],
            width=1920,
            height=1080,alignment=ft.Alignment(-1,-1))
            page.add(td)
            page.update()
            time.sleep(3)
            td.controls.append(choice_container)
            asyncio.run(fade_in_images())
            page.update()
            currant_page = "MAIN"
            page.on_keyboard_event = lambda e:choice_on_key_press(e,page,td)
            
def change(page:ft.Page,td:ft.Stack):
        time.sleep(6.5)
        page.remove(td)
        # td = ft.Stack(
        # [video_start],
        #alignment=ft.Alignment(-1,-1))
        # page.add(td)
        video_start= ft.Video(
        alignment=ft.Alignment(-1,-1),
            # width=1920,
            # height=1080,
            playlist=START_VIDEO,
            playlist_mode=ft.PlaylistMode.LOOP,
            fill_color=ft.colors.WHITE70,
            aspect_ratio=page.window_width/page.window_height,
            volume=60,
            autoplay=True,
            filter_quality=ft.FilterQuality.HIGH,
            muted=False,
            show_controls=False,
            # on_loaded=lambda e: video_start_ended(),
            # on_enter_fullscreen=lambda e: print("Video entered fullscreen!"),
        )
        #page.add(video_start)
        td = ft.Stack(
        [video_start],
        width=1920,
        height=1080)#,alignment=ft.Alignment(-1,-1)
        page.add(td)
        page.add(
        background_audio1
        )
        page.update()
        page.on_keyboard_event = lambda e:main_on_key_press(e,page,td)
        page.update()
def main(page: ft.Page):
    global td
    page.fonts = {
        "Kanit": r"C:\Users\张智卿\Desktop\google\潮字社混元简繁.ttf",
        "Open Sans": "/fonts/OpenSans-Regular.ttf"
    }

    page.theme = ft.Theme(font_family="Kanit")

    step = 0
    #page.window.frameless = True###################################################################控制是否无边框"C:\Users\张智卿\Desktop\google\潮字社混元简繁.ttf"
    #page.window.maximized = True
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.window_height = 760
    window_width = page.window_width
    window_height = page.window_height
    print(page.window_width)
    print(page.window_height)
    video_brand= ft.Video(
        alignment=ft.Alignment(-1,-1),
            width=1920,
            height=1080,
            playlist=BRAND_VIDEO,
            playlist_mode=ft.PlaylistMode.NONE,
            fill_color=ft.colors.WHITE70,
            aspect_ratio=1920/1080,
            volume=60,
            autoplay=True,
            filter_quality=ft.FilterQuality.HIGH,
            muted=False,
            show_controls=False,
            on_loaded=lambda e: change(page,td),
            # on_enter_fullscreen=lambda e: print("Video entered fullscreen!"),
    )
    td = ft.Stack(
        [video_brand],
        width=1920,
        height=1080,alignment=ft.Alignment(-1,-1))
    page.add(td)
ft.app(target=main)
