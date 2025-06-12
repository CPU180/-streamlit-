import streamlit as st # 导入Streamlit并用st代表它
import numpy as np #导入numpy库调用表格内容
import pandas as pd #导入pandas库调用表格内容

### 当前版本号0.6.12.4 
### （编辑后请保证与页脚版本号一致，以头部版本号为第一版本号）
###---------------------------------------------------------

# 网站上方页面标题设置
# 必须作为第一个Streamlit命令！
st.set_page_config(
    page_title="这是一个整合多功能的小网站！",
    page_icon="💡",
    layout="wide"
)



###----------------------------------------------------------------------------------
###  模块①
###  基本信息，streamlit课程进度，代码展示
###----------------------------------------------------------------------------------


# 标题格式
st.markdown('# 学生小陆-数学档案😇')

st.markdown('# 😃基本信息')

st.markdown('''# 姓名: *陆小陆😁*
#### 班级: *23级练习生一班😉*
#### 学号: *007😇*''')


# 创建一个为基本信息的标题，并指定锚点为基本信息
st.header('兴趣:smiley:', anchor='text!')
st.markdown('### :red[游戏] 🎮, :blue[游泳]🏊︎ ,:orange[唱跳]🎤 , :green[篮球]🏀')

#调用指标类展示元素metric
st.subheader('')
st.metric(label="当前学期", value="大二 上学期")
st.subheader('学习情况')

c1, c2, c3 = st.columns(3)
c1.metric(label="当前周数", value="15/20", delta="剩余5周")
c2.metric(label="四年级进度", value="1/2", delta="已过四级")
c3.metric(label="人生进度", value="20/100", delta="未来可期")

#对于箭头的表示通过在内容前使用+或-进行展示
st.metric(label="-心情状态",value="心情状态",delta="愉悦",label_visibility='visible')

# Streamlit课程进度部分
st.header('Streamlit课程进度')
st.progress(0.2, text="Streamlit课程进度") # 此处设置参数为20%



data = {
   '课程': ['高等数学', '大学英语', 'C语言程序设计'],
   '期末达标分数': [90,101,97],
   '状态': ['***通过***','***通过***','***补考***'], 
   '难度': ['***中等***','***简单***','***困难***']
}

###-------------------------------------------
# 字体样式提示
#st.markdown('*斜体文本*')
#st.markdown(' 斜体文本 ')
#st.markdown('**斜体文本**')
#st.markdown('_*斜体文本 ')
#st.markdown('**斜体文本***')
#st.markdown('_* 斜体文本 ')
###-------------------------------------------

index = pd.Series(['1','2','3'], name='') 
# 根据上面创建的data和index，创建数据框 
df = pd.DataFrame(data, index=index) 

st.subheader('课程日志')
st.table(df)
#使用datatrame可以增加用户对数据的处理，此处使用table表示仅进行展示

# 创建一个代码块，用于展示python_code的内容
# line_numbers=True 表示显示代码行数
# language为None，即该代码块无法满足高亮
st.subheader('Python代码展示')
python_code = '''def hello():
    print('你好，Streamlit！')'''

st.code(python_code, line_numbers=True)

st.subheader('java代码展示')
java_code = '''public class Hello {
    public static void main(String[] args) {
        System.out.println('你好！ Streamlit！');
    }
}'''

st.code(java_code, language='java',line_numbers=True)

st.subheader('JavaScript代码展示')
javascript_code = '''<p id="demo"></p>
<script>
    document.getElementById('demo').innerHTML ='你好！ Streamlit！';
</script>'''

st.code(javascript_code, language='javascript',line_numbers=True)


###----------------------------------------------------------------------------------
###  模块②
###  餐厅内容展示，包含数据，条形图，面积图，折线图（正在制作），基础兴趣点地图，进阶地图（未完）
###----------------------------------------------------------------------------------


###-------------------------------------------
### 餐厅数据 切勿随意改动

restaurants = pd.DataFrame({
    "餐厅名称": ["舒记老友粉", "天福香老友粉", "三品王牛肉粉", "姜胖胖自助烤肉", "牛扒大亨西餐厅","素宴·蔬食(素食自助餐厅科德店)","隆江猪脚饭(衡阳店)","尝回家猪脚饭·烧卤·白切(友爱店)","乐观面屋(东盟店)","重庆江湖拌面","三兄弟小龙虾馆","苏格里岛自助海鲜烤肉","吉布鲁牛排海鲜自助(南宁江南万达店)","鹿客臻鲜·海鲜烤肉自助餐厅(蓝鲸世界店)","今邕烧烤(园湖店)","舌战烧烤酒馆(三街两巷店)","亿口香龙虾","炙爱烧烤(万秀店)","夏朗蛋糕(城市花园店)","卡卡米苏·生日蛋糕(西乡塘店)","盛记顺德高佬猪杂粥店","南宁市雲菌瑶酒楼","啫啫村-生料啫啫煲(埌西店)"],
    "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐","自助","堂食","堂食","粉","粉","小吃","自助","自助","自助","烧烤","烧烤","小吃","烧烤","糕点","糕点","粥","自助","堂食"],
    "评分": [4.4, 4.1,  4.9, 4.3,4.6,4.7,4.4,4.5,4.2,4.7,4.6,4.6,4.5,4.3,4.8,4.6,4.3,4.2,4.6,4.7,4.4,4.2,4.7],
    "人均消费(元)": [15, 15, 20, 60, 80,30,30,39,21,20,103,78,80,90,123,90,120,89,68,134,15,200,34],
    "营业时间": ["6:00-22:00","5:00-23:00","10:00-23:00","12:00-24:00","17:00-20:30","10:30-20:00","9:00-19:00","9:00-20:00","9:00-20:00","12:00-23:00","12:00-23:00","12:300-23:00","12:00-23:00","17:00-23:00","17:00-02:00","17:00-02:00","12:300-23:00","12:300-23:00","17:30-22:00","7:30-22:00","7:30-22:00","7:30-22:00","7:30-22:00"],
    "latitude": [22.809728,22.822481,22.838432,22.789523,22.808867,22.848224,22.831269,22.839999,22.689112,22.810435,22.756756,22.813919,22.790188,22.769671,22.826847,22.813768,22.845349,22.789165,22.808243,22.688017,22.819031,22.798990,22.805077],
    "longitude": [108.324614,108.387910,108.262110,108.313493,108.326838,108.257296,108.310691,108.309224,108.267817,108.284216,108.332567,108.321484,108.312827,108.306724,108.339396,108.320656,108.315969,108.318908,108.370764,108.300288,108.343062,108.378891,108.368414]
})

###-------------------------------------------




st.markdown('### 门店详细数据（仅展示评分大于4.5的店铺）')

#仅展示评分大于4.5的店
high_rating = restaurants[restaurants["评分"] >= 4.5]
# 显示表格（可排序、搜索）
st.dataframe(high_rating[["餐厅名称", "类型", "评分", "人均消费(元)","营业时间"]])




st.markdown("### 人均消费数据")

st.bar_chart(restaurants.set_index("餐厅名称")["人均消费(元)"])


st.markdown('### 门店评分数据（仅展示评分大于4.5的店铺）')

# 设置餐厅名称为索引（X轴）
data_for_chart = restaurants.set_index("餐厅名称")["评分"]

# 绘制面积图
st.area_chart(data_for_chart)



import pydeck as pdk

# 方法1：修复 st.map() 的悬停
st.header("基础地图（自动悬停）")
st.map(restaurants[["latitude", "longitude", "餐厅名称"]])  # 只传需要的列



###-------------------------------------------------------------------------------
###腾讯地图模块



import streamlit.components.v1 as components


# 配置
TENCENT_API_KEY = "7QTBZ-NDMLM-GAQ6N-6YN54-XVWL2-5WFQS"




# 生成地图
# 1. 首先打印列名确认
print("当前数据列名:", restaurants.columns.tolist())

# 2. 根据实际列名进行处理（以下是示例，请根据你的实际列名调整）
# 如果列名是中文的'latitude'和'longitude':
if 'latitude' in restaurants.columns and 'longitude' in restaurants.columns:
    pass  # 列名已经正确
# 如果列名是其他中文名（如'纬度'/'经度'）:
elif '纬度' in restaurants.columns and '经度' in restaurants.columns:
    restaurants = restaurants.rename(columns={
        '纬度': 'latitude',
        '经度': 'longitude'
    })
else:
    st.error(f"无法找到经纬度列，现有列名: {restaurants.columns.tolist()}")
    st.stop()

# 3. 确保数据类型正确
restaurants['latitude'] = pd.to_numeric(restaurants['latitude'], errors='coerce')
restaurants['longitude'] = pd.to_numeric(restaurants['longitude'], errors='coerce')

# 4. 移除无效坐标的行
restaurants = restaurants.dropna(subset=['latitude', 'longitude'])


#地图参数设置（调用腾讯定位服务API）
map_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://map.qq.com/api/gljs?v=2.exp&key={TENCENT_API_KEY}"></script>
    <style>
        #map {{
            width: 100%;
            height: 500px;
            margin: 0;
            padding: 0;
        }}
        .info-window {{
            min-width: 200px;
            padding: 10px;
            font-family: Arial, sans-serif;
        }}
        .info-window h3 {{
            margin: 0 0 8px 0;
            font-size: 16px;
            color: #333;
        }}
        .info-window p {{
            margin: 4px 0;
            font-size: 14px;
            color: #666;
        }}
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        // 1. 确保数据正确转换
        var restaurantData = {restaurants.to_json(orient='records', force_ascii=False, default_handler=str)};
        
        // 2. 数据预处理
        var validRestaurants = restaurantData.filter(function(restaurant) {{
            var lat = Number(restaurant.latitude);
            var lng = Number(restaurant.longitude);
            return !isNaN(lat) && !isNaN(lng) && 
                   lat >= -90 && lat <= 90 && 
                   lng >= -180 && lng <= 180;
        }});
        
        console.log('有效餐厅数据:', validRestaurants);
        
        // 3. 初始化地图函数
        function initMap() {{
            try {{
                // 创建地图实例
                var map = new TMap.Map("map", {{
                    center: new TMap.LatLng(22.82, 108.35),
                    zoom: 12,
                    mapStyleId: "卫星图",
                    pitch: 30  // 添加倾斜角度增强视觉效果
                }});
                
                console.log('地图初始化完成');
                
                // 4. 准备标记点数据
                var geometries = validRestaurants.map(function(restaurant) {{
                    return {{
                        id: restaurant['餐厅名称'].toString(),
                        styleId: "default",
                        position: new TMap.LatLng(
                            Number(restaurant.latitude), 
                            Number(restaurant.longitude)
                        ),
                        properties: {{
                            name: restaurant['餐厅名称'],
                            category: restaurant['类型'],
                            rating: restaurant['评分'],
                            price: restaurant['人均消费(元)'],
                            hours: restaurant['营业时间']
                        }}
                    }};
                }});
                
                console.log('标记点数据:', geometries);
                
                // 5. 创建标记
                var markerLayer = new TMap.MultiMarker({{
                    map: map,
                    styles: {{
                        "default": new TMap.MarkerStyle({{
                            width: 25,
                            height: 35,
                            anchor: {{ x: 12, y: 35 }},
                            src: "https://mapapi.qq.com/web/lbs/javascriptGL/demo/img/markerDefault.png"
                        }})
                    }},
                    geometries: geometries
                }});
                
                console.log('标记点创建完成');
                
                // 6. 信息窗口设置
                var infoWindow = new TMap.InfoWindow({{
                    map: map,
                    enableCustom: true,
                    offset: {{ x: 0, y: -35 }}
                }});
                
                // 7. 点击事件处理
                markerLayer.on("click", function(evt) {{
                    console.log('标记点击:', evt);
                    var props = evt.geometry.properties;
                    infoWindow.setPosition(evt.geometry.position);
                    infoWindow.setContent(
                        '<div class="info-window">' +
                        '<h3>' + props.name + '</h3>' +
                        '<p><b>类型:</b> ' + props.category + '</p>' +
                        '<p><b>评分:</b> ' + props.rating + '/5.0</p>' +
                        '<p><b>人均:</b> ￥' + props.price + '元</p>' +
                        '<p><b>营业时间:</b> ' + props.hours + '</p>' +
                        '</div>'
                    );
                    infoWindow.open();
                }});
                
            }} catch (error) {{
                console.error('地图初始化错误:', error);
                document.getElementById('map').innerHTML = 
                    '<div style="color:red;padding:20px;text-align:center">' +
                    '<h3>地图加载失败</h3>' +
                    '<p>' + error.message + '</p>' +
                    '</div>';
            }}
        }}
        
        // 8. 地图API加载检测
        function checkTMapLoaded() {{
            if (typeof TMap !== 'undefined') {{
                initMap();
            }} else {{
                setTimeout(checkTMapLoaded, 100);
            }}
        }}
        
        // 9. 页面加载完成后执行
        window.onload = function() {{
            checkTMapLoaded();
        }};
    </script>
</body>
</html>
"""



#若想测试，删除下处的注释即可显示地图



# 显示地图
#st.title("🍜 南宁餐厅地图（腾讯卫星图）")
#components.html(map_html, height=600)




###-------------------------------------------------------------------------------







###----------------------------------------------------------------------------------
###  模块③
###  多媒体内容展示，包含图片展示，音频展示，视频播放器
###----------------------------------------------------------------------------------


###-------------------------------------------
# 图片网址
images = ["https://eskipaper.com/images/mountains-1.jpg",
          "https://wallpaperaccess.com/full/1167990.jpg",
          "https://wallpapercave.com/wp/D3r6gVH.jpg"]


###-------------------------------------------
st.subheader("一些风景图片")
st.image(images)



import streamlit as st


###-------------------------------------------

# 读取音频URL
audio_file = 'https://music.163.com/song/media/outer/url?id=28263184.mp3'

###-------------------------------------------

st.subheader('播放音频')
st.audio(audio_file)








import streamlit as st
from streamlit.components.v1 import html



# 自定义CSS样式
st.markdown("""
<style>
    /* 主标题样式 */
    .main-title {
        font-size: 2.5rem;
        text-align: center;
        color: #00a1d6;
        margin-bottom: 1.5rem;
        font-weight: bold;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
    }
    
    /* 自定义按钮样式 */
    .custom-btn {
        background-color: white !important;
        color: black !important;
        border: 2px solid #ff4b4b !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        font-weight: bold !important;
        transition: all 0.3s !important;
        width: 100% !important;
    }
    .custom-btn:hover {
        background-color: #fff0f0 !important;
        transform: scale(1.05) !important;
    }
    
    /* 视频容器样式 */
    .video-container {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
    }
    
    /* 当前播放信息样式 */
    .current-playing {
        font-size: 1.1rem;
        text-align: center;
        padding: 0.5rem;
        background-color: #f8f9fa;
        border-radius: 8px;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# 美化后的主标题
st.markdown('<p class="main-title">🎬 B站视频播放器</p>', unsafe_allow_html=True)

# B站视频数据
video_data = {
    "视频1 - 高山风景视频": "BV1ST411E7wb",  
    "视频2 - 这大概就是美到窒息的感觉吧": "BV13A4y1Z7m2",
    "视频3 - 仿佛来到了童话里的世界~": "BV1co7Bz6Ehp",
    "视频4 - 日落后的二十分钟，被称为蓝调时刻": "BV1gLB4YwEXH",  
    "视频5 - 久在樊笼里，复得返自然": "BV1exrdYZEfM",
    "视频6 - 这是地理课本里的峡湾地貌 也是我国唯一没有的地貌": "BV1d9f4YoEwV"
}

# 获取视频列表和当前索引
video_list = list(video_data.values())
current_index = st.session_state.get("current_index", 0)

# 处理导航按钮点击
def navigate(direction):
    if direction == "prev":
        st.session_state.current_index = (current_index - 1) % len(video_list)
    elif direction == "next":
        st.session_state.current_index = (current_index + 1) % len(video_list)
    st.session_state.current_video = video_list[st.session_state.current_index]
    st.rerun()

# 获取当前BV号
current_bv = st.session_state.get("current_video", video_list[current_index])

# 创建容器放置视频和按钮
with st.container():
    # 视频选择下拉菜单
    selected_title = st.selectbox(
        "选择视频",
        options=list(video_data.keys()),
        index=current_index,
        key="video_selector"
    )
    
    # 如果下拉菜单选择变化，更新当前视频
    if selected_title != list(video_data.keys())[current_index]:
        st.session_state.current_index = list(video_data.keys()).index(selected_title)
        st.session_state.current_video = video_data[selected_title]
        st.rerun()
    
    # B站播放器HTML模板
    st.markdown('<div class="video-container">', unsafe_allow_html=True)
    bili_player = f"""
    <div style="margin:10px 0">
        <iframe 
            width="100%" 
            height="500" 
            src="//player.bilibili.com/player.html?bvid={current_bv}&page=1&high_quality=1&volume=0.3" 
            scrolling="no" 
            frameborder="no" 
            allowfullscreen="true">
        </iframe>
    </div>
    """
    html(bili_player, height=520)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 创建导航按钮（优化后的样式和布局）
    col1, col2, col3 = st.columns([1, 1, 4])  # 调整比例
    with col1:
        if st.button("◀ 上一个", key="prev_btn", help="播放上一个视频"):
            navigate("prev")
    with col2:
        if st.button("下一个 ▶", key="next_btn", help="播放下一个视频"):
            navigate("next")
    
    # 显示当前视频标题
    current_title = list(video_data.keys())[current_index]
    st.markdown(f'<div class="current-playing">🎥 当前播放: <strong>{current_title}</strong></div>', unsafe_allow_html=True)




# 添加页脚
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem;">
    <p>© 2025 个人网页制作演示 | CPU180 版本号：0.6.12.4</p>
</div>
""", unsafe_allow_html=True)
