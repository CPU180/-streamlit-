import streamlit as st # 导入Streamlit并用st代表它
import numpy as np #导入numpy库调用表格内容
import pandas as pd #导入pandas库调用表格内容

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

# 字体样式
#st.markdown('*斜体文本*')
#st.markdown(' 斜体文本 ')
#st.markdown('**斜体文本**')
#st.markdown('_*斜体文本 ')
#st.markdown('**斜体文本***')
#st.markdown('_* 斜体文本 ')

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





# 餐厅数据
restaurants = pd.DataFrame({
    "餐厅名称": ["舒记老友粉", "天福香老友粉", "三品王牛肉粉", "姜胖胖自助烤肉", "牛扒大亨西餐厅","素宴·蔬食(素食自助餐厅科德店)","隆江猪脚饭(衡阳店)",
    "尝回家猪脚饭·烧卤·白切(友爱店)","乐观面屋(东盟店)","重庆江湖拌面","苏氏小龙虾(东鸣路店)","三兄弟小龙虾馆","苏格里岛自助海鲜烤肉","吉布鲁牛排海鲜自助(南宁江南万达店)",
   "鹿客臻鲜·海鲜烤肉自助餐厅(蓝鲸世界店)","今邕烧烤(园湖店)","舌战烧烤酒馆(三街两巷店)","亿口香龙虾","炙爱烧烤(万秀店)","夏朗蛋糕(城市花园店)","卡卡米苏·生日蛋糕(西乡塘店)",
   "岁悦甜蜜蛋糕店","盛记顺德高佬猪杂粥店","南宁市雲菌瑶酒楼","啫啫村-生料啫啫煲(埌西店)"],
    "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐","自助","堂食","堂食","粉","粉","小吃","小吃","自助","自助","自助","烧烤","烧烤","小吃","烧烤","糕点","糕点","糕点","粥","自助","堂食"],
    "评分": [4.4, 4.1, 4.5, 4.9, 4.3,4.6,4.7,4.4,4.5,4.2,4.7,4.6,4.6,4.5,4.3,4.8,4.6,4.3,4.2,4.6,4.7,4.4,4.5,4.2,4.7],
    "人均消费(元)": [15, 15, 20, 60, 80,30,30,39,21,20,98,103,78,80,90,123,90,120,89,68,55,134,15,200,34],
    "营业时间": ["6:00-22:00","9:00-22:00","5:00-23:00","10:00-23:00","12:00-24:00","17:00-20:30","10:30-20:00","9:00-19:00","9:00-20:00","9:00-20:00","9:30-20:00","12:00-23:00","12:00-23:00","12:300-23:00","12:00-23:00","17:00-23:00","17:00-02:00","17:00-02:00","12:300-23:00“,”12:300-23:00“,”17:30-22:00“,”7:30-22:00“,”7:30-22:00“,”7:30-22:00“,"7:30-22:00"],
    "latitude": [22.809728,22.822481,22.838432,22.789523,22.808867,22.848224,22.831269,22.839999,22.689112,22.810435,23.160266,22.756756,22.813919,22.790188,22.769671,22.826847,22.813768,22.845349,22.789165,22.808243,22.846720,22.688017,22.819031,22.798990,22.805077],
    "longitude": [108.324614,108.387910,108.262110,108.313493,108.326838,108.257296,108.310691,108.309224,108.267817,108.403375,108.284216,108.332567,108.321484,108.312827,108.306724,108.339396,108.320656,108.315969,108.318908,108.370764,108.300288,109.460925,108.343062,108.378891,108.368414]
})





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



import streamlit.components.v1 as components



# 配置
TENCENT_API_KEY = "7QTBZ-NDMLM-GAQ6N-6YN54-XVWL2-5WFQS"
restaurants = pd.DataFrame({
    "name": ["舒记老友粉", "天福香老友粉", "三品王牛肉粉"],
    "lat": [22.809728, 22.822481, 22.838432],
    "lng": [108.324614, 108.387910, 108.262110],
    "price": [15, 15, 20]
})

# 生成地图
map_html = f"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://map.qq.com/api/gljs?v=1.exp&key={TENCENT_API_KEY}"></script>
    <style>#map {{ width:100%; height:500px; }}</style>
</head>
<body>
    <div id="map"></div>
    <script>
        var map = new TMap.Map("map", {{
            center: new TMap.LatLng(22.82, 108.35),
            zoom: 12,
            mapStyleId: "卫星图"
        }});

        // 动态加载Python数据
        var restaurants = {restaurants.to_json(orient="records")};
        
        restaurants.forEach(restaurant => {{
            var marker = new TMap.Marker({{
                position: new TMap.LatLng(restaurant.lat, restaurant.lng),
                map: map,
                content: '<div style="background:#FF6D00;color:white;padding:4px 8px;">' + restaurant.name + '</div>'
            }});

            marker.on("click", () => {{
                new TMap.InfoWindow({{
                    map: map,
                    position: new TMap.LatLng(restaurant.lat, restaurant.lng),
                    content: `
                        <h3>${{restaurant.name}}</h3>
                        <p>人均: ￥${{restaurant.price}}元</p>
                    `
                }}).open();
            }});
        }});
    </script>
</body>
</html>
"""

# 显示
st.title("🍜 南宁餐厅地图（腾讯卫星图）")
components.html(map_html, height=550)
