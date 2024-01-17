from select import select
import streamlit as st
from st_on_hover_tabs import on_hover_tabs
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
from readmongodb import readmongodb, readmongodb_time, readmongodb_style, connectmongodb, computer_max
from streamlit_echarts import st_echarts
from selected import getValue
import numpy
import json
from PIL import Image
import time


def clear(value):
    # 写入新的文件内容
    with open("select_item.txt", "w") as f:
        f.write(value)
    time.sleep(2)
    st.experimental_rerun()



def Layouts_plotly(selected):


    #*********************************
    # st.header("Custom tab component for on-hover navigation bar")
    st.markdown('<style>' + open('./css/style1.css').read() + '</style>', unsafe_allow_html=True)


    with st.sidebar:
        add_selectbox = on_hover_tabs(tabName=['商品指数', '流行指数', '销售指数', '评价指数'], 
                         iconName=['dashboard', 'money', 'economy', 'store'], default_choice = selected,
                         styles = {'navtab': {'background-color':'rgb(240,242,246)',
                                                  'color': '#818181',
                                                  'font-size': '23px',
                                                  'transition': '.3s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'},
                                       'tabOptionsStyle': {':hover :hover': {'color': '#000000',
                                                                      'cursor': 'pointer'}},
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'},
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'}},
                             key='1')


    if add_selectbox=="商品指数":
        st.title("亚马逊羽绒服Top5商品指数词云图")
        st.header('澳大利亚地区')
        image1 = Image.open("image/productListau.png").resize((1700, 1200))
        st.image(image1, caption='')
        st.header('中国地区')
        image2 = Image.open("image/productListca.png").resize((1700, 1200))
        st.image(image2, caption='')
        st.header('德国地区')
        image3 = Image.open("image/productListde.png").resize((1700, 1200))
        st.image(image3, caption='')
        st.header('新加坡地区')        
        image4 = Image.open("image/productListsg.png").resize((1700, 1200))
        st.image(image4, caption='')
        st.header('英国地区')
        image5 = Image.open("image/productListuk.png").resize((1700, 1200))
        st.image(image5, caption='')
        st.header('美国地区')
        image6 = Image.open("image/productListusa.png").resize((1700, 1200))
        st.image(image6, caption='')
    elif add_selectbox=="流行指数": 

        # 创建一个 Markdown 文本，用于嵌入 CSS 样式
        css = """
        <style>
        .hide {
            display: none;
        }
        .row-widget stButton {
            display: none;
        }

        .show {
            display: block;
        }
        </style>
        """
        st.write(css, unsafe_allow_html=True)
        selected2 = option_menu(None, ["面料", "款式", '风格'], 
            icons=['house', 'cloud-upload', "list-task", 'gear'], 
            menu_icon="cast", default_index=0, orientation="horizontal")
        if selected2 == "面料":
            st.title("亚马逊羽绒服Top5面料曲线图")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                image = Image.open("image/纯棉.png").resize((300, 300))
                st.image(image, caption='纯棉')
            with col2:
                image = Image.open("image/尼龙.png").resize((300, 300))
                st.image(image, caption='尼龙')
            with col3:
                image = Image.open("image/聚酯纤维.png").resize((300, 300))
                st.image(image, caption='聚酯纤维')
            with col4:
                image = Image.open("image/弹性纤维.png").resize((300, 300))
                st.image(image, caption='弹性纤维')
            # 面料pie***********************************
            # blouses
            option = {
                "title": {"text": "澳大利亚地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "legend": {"left": "center", "textStyle": { "fontSize": 14}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "toolbox": {
                    "feature": {
                        "dataZoom": {"yAxisIndex": 'none'},
                        "restore": {},
                        "saveAsImage": {},
                    }
                },
                "dataset": {"source": fabric_blouses_data[0]},
                "xAxis": {"type": 'category', "boundaryGap": False},
                "yAxis": {"type": 'value', "max":100, "gridIndex": 0,"boundaryGap": [0, '100%']},
                "grid": {"top": "55%"},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "type": "pie",
                        "id": "pie",
                        "radius": "30%",
                        "center": ["50%", "25%"],
                        "emphasis": {"focus": "data"},
                        "label": {"formatter": "{b}: {@2023-02-01} ({d}%)"},
                        "encode": {"itemName": "Time", "value": now, "tooltip": now},
                    },
                    {
                        "name": 'Polyester',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                        # "areaStyle": {}, #显示覆盖区域
                        # "data": data
                    },
                    {
                        "name": 'Spandex',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Cotton',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Rayon',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Viscose',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    }
                ]
            }
            st_echarts(option, height="500px", key="echarts")
            # polos
            option = {
                "title": {"text": "中国地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "legend": {"left": "center", "textStyle": { "fontSize": 14}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "toolbox": {
                    "feature": {
                        "dataZoom": {"yAxisIndex": 'none'},
                        "restore": {},
                        "saveAsImage": {},
                    }
                },
                "dataset": {"source": fabric_polos_data[0]},
                "xAxis": {"type": 'category', "boundaryGap": False},
                "yAxis": {"type": 'value', "max":100, "gridIndex": 0,"boundaryGap": [0, '100%']},
                "grid": {"top": "55%"},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "type": "pie",
                        "id": "pie",
                        "radius": "30%",
                        "center": ["50%", "25%"],
                        "emphasis": {"focus": "data"},
                        "label": {"formatter": "{b}: {@2023-02-01} ({d}%)"},
                        "encode": {"itemName": "Time", "value": now, "tooltip": now},
                    },
                    {
                        "name": 'Polyester',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                        # "areaStyle": {}, #显示覆盖区域
                        # "data": data
                    },
                    {
                        "name": 'Spandex',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Cotton',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Rayon',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                ]
            }
            st_echarts(option, height="500px")
            # t-shirts
            option = {
                "title": {"text": "德国地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "legend": {"left": "center", "textStyle": { "fontSize": 14}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "toolbox": {
                    "feature": {
                        "dataZoom": {"yAxisIndex": 'none'},
                        "restore": {},
                        "saveAsImage": {},
                    }
                },
                "dataset": {"source": fabric_t_shirts_data[0]},
                "xAxis": {"type": 'category', "boundaryGap": False},
                "yAxis": {"type": 'value', "max":100, "gridIndex": 0,"boundaryGap": [0, '100%']},
                "grid": {"top": "55%"},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "type": "pie",
                        "id": "pie",
                        "radius": "30%",
                        "center": ["50%", "25%"],
                        "emphasis": {"focus": "data"},
                        "label": {"formatter": "{b}: {@2023-02-01} ({d}%)"},
                        "encode": {"itemName": "Time", "value": now, "tooltip": now},
                    },
                    {
                        "name": 'Polyester',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                        # "areaStyle": {}, #显示覆盖区域
                        # "data": data
                    },
                    {
                        "name": 'Spandex',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Cotton',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Rayon',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    }
                ]
            }
            st_echarts(option, height="500px")
            # tanks
            option = {
                "title": {"text": "新加坡地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "legend": {"left": "center", "textStyle": { "fontSize": 14}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "toolbox": {
                    "feature": {
                        "dataZoom": {"yAxisIndex": 'none'},
                        "restore": {},
                        "saveAsImage": {},
                    }
                },
                "dataset": {"source": fabric_tanks_data[0]},
                "xAxis": {"type": 'category', "boundaryGap": False},
                "yAxis": {"type": 'value', "max":100, "gridIndex": 0,"boundaryGap": [0, '100%']},
                "grid": {"top": "55%"},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "type": "pie",
                        "id": "pie",
                        "radius": "30%",
                        "center": ["50%", "25%"],
                        "emphasis": {"focus": "data"},
                        "label": {"formatter": "{b}: {@2023-02-01} ({d}%)"},
                        "encode": {"itemName": "Time", "value": now, "tooltip": now},
                    },
                    {
                        "name": 'Polyester',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                        # "areaStyle": {}, #显示覆盖区域
                        # "data": data
                    },
                    {
                        "name": 'Spandex',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Cotton',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Rayon',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    }
                ]
            }
            st_echarts(option, height="500px")
            # tunics
            option = {
                "title": {"text": "英国地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "legend": {"left": "center", "textStyle": { "fontSize": 14}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "toolbox": {
                    "feature": {
                        "dataZoom": {"yAxisIndex": 'none'},
                        "restore": {},
                        "saveAsImage": {},
                    }
                },
                "dataset": {"source": fabric_tunics_data[0]},
                "xAxis": {"type": 'category', "boundaryGap": False},
                "yAxis": {"type": 'value', "max":100, "gridIndex": 0,"boundaryGap": [0, '100%']},
                "grid": {"top": "55%"},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "type": "pie",
                        "id": "pie",
                        "radius": "30%",
                        "center": ["50%", "25%"],
                        "emphasis": {"focus": "data"},
                        "label": {"formatter": "{b}: {@2023-02-01} ({d}%)"},
                        "encode": {"itemName": "Time", "value": now, "tooltip": now},
                    },
                    {
                        "name": 'Polyester',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                        # "areaStyle": {}, #显示覆盖区域
                        # "data": data
                    },
                    {
                        "name": 'Spandex',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Cotton',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Rayon',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    }
                ]
            }
            st_echarts(option, height="500px")
            # vests
            option = {
                "title": {"text": "美国地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "legend": {"left": "center", "textStyle": { "fontSize": 14}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "toolbox": {
                    "feature": {
                        "dataZoom": {"yAxisIndex": 'none'},
                        "restore": {},
                        "saveAsImage": {},
                    }
                },
                "dataset": {"source": fabric_vests_data[0]},
                "xAxis": {"type": 'category', "boundaryGap": False},
                "yAxis": {"type": 'value', "max":100, "gridIndex": 0,"boundaryGap": [0, '100%']},
                "grid": {"top": "55%"},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "type": "pie",
                        "id": "pie",
                        "radius": "30%",
                        "center": ["50%", "25%"],
                        "emphasis": {"focus": "data"},
                        "label": {"formatter": "{b}: {@2023-02-01} ({d}%)"},
                        "encode": {"itemName": "Time", "value": now, "tooltip": now},
                    },
                    {
                        "name": 'Polyester',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                        # "areaStyle": {}, #显示覆盖区域
                        # "data": data
                    },
                    {
                        "name": 'Spandex',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Cotton',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Rayon',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    }
                ]
            }
            st_echarts(option, height="500px")
        elif selected2 == "色系":
            selected2
        elif selected2 == "款式":
            st.title("亚马逊女装开合方式数据分析")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                image = Image.open("image/downjacket1.jpg").resize((224, 450))
                st.image(image, caption='downjacket1')
            with col2:
                image = Image.open("image/downjacket2.jpg").resize((224, 450))
                st.image(image, caption='downjacket2')
            with col3:
                image = Image.open("image/downjacket3.jpg").resize((224, 450))
                st.image(image, caption='downjacket3')
            with col4:
                image = Image.open("image/downjacket4.jpg").resize((224, 450))
                st.image(image, caption='downjacket4')
            # 开合方式bar***********************************
            # blouses
            option = {
                "title": {"text": "Blouses开合方式", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "toolbox": {
                    "feature": {
                        "dataZoom": {"yAxisIndex": 'none'},
                        "restore": {},
                        "saveAsImage": {},
                    }
                },
                "dataset": {"source": fabric_blouses_data[1]},
                "xAxis": {"type": 'category', "boundaryGap": False},
                "yAxis": {"type": 'value', "max":100, "gridIndex": 0,"boundaryGap": [0, '100%']},
                "grid": {"top": "55%"},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "type": "pie",
                        "id": "pie",
                        "radius": "30%",
                        "center": ["50%", "25%"],
                        "emphasis": {"focus": "data"},
                        "label": {"formatter": "{b}: {@2023-02-01} ({d}%)"},
                        "encode": {"itemName": "Time", "value": now, "tooltip": now},
                    },
                    {
                        "name": 'Button',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                        # "areaStyle": {}, #显示覆盖区域
                        # "data": data
                    },
                    {
                        "name": 'Pull',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Zipper',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Elastic',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Others',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    }
                ]
            }
            st_echarts(option, height="500px")
            # polos
            option = {
                "title": {"text": "Polos开合方式", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "toolbox": {
                    "feature": {
                        "dataZoom": {"yAxisIndex": 'none'},
                        "restore": {},
                        "saveAsImage": {},
                    }
                },
                "dataset": {"source": fabric_polos_data[1]},
                "xAxis": {"type": 'category', "boundaryGap": False},
                "yAxis": {"type": 'value', "max":100, "gridIndex": 0,"boundaryGap": [0, '100%']},
                "grid": {"top": "55%"},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "type": "pie",
                        "id": "pie",
                        "radius": "30%",
                        "center": ["50%", "25%"],
                        "emphasis": {"focus": "data"},
                        "label": {"formatter": "{b}: {@2023-02-01} ({d}%)"},
                        "encode": {"itemName": "Time", "value": now, "tooltip": now},
                    },
                    {
                        "name": 'Button',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                        # "areaStyle": {}, #显示覆盖区域
                        # "data": data
                    },
                    {
                        "name": 'Pull',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Zipper',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Elastic',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Others',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    }
                ]
            }
            st_echarts(option, height="500px")
            # t-shirts
            option = {
                "title": {"text": "T-shirts开合方式", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "toolbox": {
                    "feature": {
                        "dataZoom": {"yAxisIndex": 'none'},
                        "restore": {},
                        "saveAsImage": {},
                    }
                },
                "dataset": {"source": fabric_t_shirts_data[1]},
                "xAxis": {"type": 'category', "boundaryGap": False},
                "yAxis": {"type": 'value', "max":100, "gridIndex": 0,"boundaryGap": [0, '100%']},
                "grid": {"top": "55%"},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "type": "pie",
                        "id": "pie",
                        "radius": "30%",
                        "center": ["50%", "25%"],
                        "emphasis": {"focus": "data"},
                        "label": {"formatter": "{b}: {@2023-02-01} ({d}%)"},
                        "encode": {"itemName": "Time", "value": now, "tooltip": now},
                    },
                    {
                        "name": 'Button',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                        # "areaStyle": {}, #显示覆盖区域
                        # "data": data
                    },
                    {
                        "name": 'Pull',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Zipper',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Elastic',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Others',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    }
                ]
            }
            st_echarts(option, height="500px")
            # tanks
            option = {
                "title": {"text": "Tanks开合方式", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "toolbox": {
                    "feature": {
                        "dataZoom": {"yAxisIndex": 'none'},
                        "restore": {},
                        "saveAsImage": {},
                    }
                },
                "dataset": {"source": fabric_tanks_data[1]},
                "xAxis": {"type": 'category', "boundaryGap": False},
                "yAxis": {"type": 'value', "max":100, "gridIndex": 0,"boundaryGap": [0, '100%']},
                "grid": {"top": "55%"},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "type": "pie",
                        "id": "pie",
                        "radius": "30%",
                        "center": ["50%", "25%"],
                        "emphasis": {"focus": "data"},
                        "label": {"formatter": "{b}: {@2023-02-01} ({d}%)"},
                        "encode": {"itemName": "Time", "value": now, "tooltip": now},
                    },
                    {
                        "name": 'Button',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                        # "areaStyle": {}, #显示覆盖区域
                        # "data": data
                    },
                    {
                        "name": 'Pull',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Zipper',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Elastic',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Others',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    }
                ]
            }
            st_echarts(option, height="500px")
            # tunics
            option = {
                "title": {"text": "Tunics开合方式", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "toolbox": {
                    "feature": {
                        "dataZoom": {"yAxisIndex": 'none'},
                        "restore": {},
                        "saveAsImage": {},
                    }
                },
                "dataset": {"source": fabric_tunics_data[1]},
                "xAxis": {"type": 'category', "boundaryGap": False},
                "yAxis": {"type": 'value', "max":100, "gridIndex": 0,"boundaryGap": [0, '100%']},
                "grid": {"top": "55%"},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "type": "pie",
                        "id": "pie",
                        "radius": "30%",
                        "center": ["50%", "25%"],
                        "emphasis": {"focus": "data"},
                        "label": {"formatter": "{b}: {@2023-02-01} ({d}%)"},
                        "encode": {"itemName": "Time", "value": now, "tooltip": now},
                    },
                    {
                        "name": 'Button',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                        # "areaStyle": {}, #显示覆盖区域
                        # "data": data
                    },
                    {
                        "name": 'Pull',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Zipper',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Elastic',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Others',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    }
                ]
            }
            st_echarts(option, height="500px")
            # vests
            option = {
                "title": {"text": "Vests开合方式", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "toolbox": {
                    "feature": {
                        "dataZoom": {"yAxisIndex": 'none'},
                        "restore": {},
                        "saveAsImage": {},
                    }
                },
                "dataset": {"source": fabric_vests_data[1]},
                "xAxis": {"type": 'category', "boundaryGap": False},
                "yAxis": {"type": 'value', "max":100, "gridIndex": 0,"boundaryGap": [0, '100%']},
                "grid": {"top": "55%"},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "type": "pie",
                        "id": "pie",
                        "radius": "30%",
                        "center": ["50%", "25%"],
                        "emphasis": {"focus": "data"},
                        "label": {"formatter": "{b}: {@2023-02-01} ({d}%)"},
                        "encode": {"itemName": "Time", "value": now, "tooltip": now},
                    },
                    {
                        "name": 'Button',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                        # "areaStyle": {}, #显示覆盖区域
                        # "data": data
                    },
                    {
                        "name": 'Pull',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Zipper',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Elastic',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    },
                    {
                        "name": 'Others',
                        "type": 'line',
                        "smooth": True,
                        "seriesLayoutBy": "row",
                        "emphasis": {"focus": "series"},
                    }
                ]
            }
            st_echarts(option, height="500px")
        elif selected2 == "风格":
            st.title("亚马逊女装(裙子)风格占比")
            options = {
                "title": {"text": "中国地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "legend": {"data": ["波西米亚风", "迷彩风", "中国风", "学院风", "嘻哈风", "宫廷风", "职场风", "香奈儿风格", "运动风"], "textStyle": { "fontSize": 16}, },
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "data": np.array(style_cn_list['data']).tolist(),
                },
                "yAxis": {"type": "value", "max":style_cnlist_max, "gridIndex": 0, "boundaryGap": [0, '100%']},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50,
                    "bottom": 30
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "name": "波西米亚风",
                        "type": "line",
                        "data": np.array(style_cn_list['boho']).tolist(),
                    },
                    {
                        "name": "迷彩风",
                        "type": "line",
                        "data": np.array(style_cn_list['camo']).tolist(),
                    },
                    {
                        "name": "中国风",
                        "type": "line",
                        "data": np.array(style_cn_list['chinese_national']).tolist(),
                    },
                    {
                        "name": "学院风",
                        "type": "line",
                        "data": np.array(style_cn_list['college'],).tolist()
                    },
                    {
                        "name": "嘻哈风",
                        "type": "line",
                        "data": np.array(style_cn_list['hip_hop']).tolist(),
                    },
                    {
                        "name": "宫廷风",
                        "type": "line",
                        "data": np.array(style_cn_list['palace']).tolist(),
                    },
                    {
                        "name": "职场风",
                        "type": "line",
                        "data": np.array(style_cn_list['professional']).tolist(),
                    },
                    {
                        "name": "香奈儿风格",
                        "type": "line",
                        "data": np.array(style_cn_list['small_fragrance']).tolist(),
                    },
                    {
                        "name": "运动风",
                        "type": "line",
                        "data": np.array(style_cn_list['sports']).tolist(),
                    },
                ],
            }
            st_echarts(options=options, height="500px")
            options = {
                "title": {"text": "日本地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "legend": {"data": ["波西米亚风", "迷彩风", "中国风", "学院风", "嘻哈风", "宫廷风", "职场风", "香奈儿风格", "运动风"], "textStyle": { "fontSize": 16}, },
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "data": np.array(style_jp_list['data']).tolist(),
                },
                "yAxis": {"type": "value", "max":style_jplist_max, "gridIndex": 0, "boundaryGap": [0, '100%']},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "name": "波西米亚风",
                        "type": "line",
                        "data": np.array(style_jp_list['boho']).tolist(),
                    },
                    {
                        "name": "迷彩风",
                        "type": "line",
                        "data": np.array(style_jp_list['camo']).tolist(),
                    },
                    {
                        "name": "中国风",
                        "type": "line",
                        "data": np.array(style_jp_list['chinese_national']).tolist(),
                    },
                    {
                        "name": "学院风",
                        "type": "line",
                        "data": np.array(style_jp_list['college'],).tolist()
                    },
                    {
                        "name": "嘻哈风",
                        "type": "line",
                        "data": np.array(style_jp_list['hip_hop']).tolist(),
                    },
                    {
                        "name": "宫廷风",
                        "type": "line",
                        "data": np.array(style_jp_list['palace']).tolist(),
                    },
                    {
                        "name": "职场风",
                        "type": "line",
                        "data": np.array(style_jp_list['professional']).tolist(),
                    },
                    {
                        "name": "香奈儿风格",
                        "type": "line",
                        "data": np.array(style_jp_list['small_fragrance']).tolist(),
                    },
                    {
                        "name": "运动风",
                        "type": "line",
                        "data": np.array(style_jp_list['sports']).tolist(),
                    },
                ],
            }
            st_echarts(options=options, height="500px")
            options = {
                "title": {"text": "美国地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "legend": {"data": ["波西米亚风", "迷彩风", "中国风", "学院风", "嘻哈风", "宫廷风", "职场风", "香奈儿风格", "运动风"], "textStyle": { "fontSize": 16}, },
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "data": np.array(style_usa_list['data']).tolist(),
                },
                "yAxis": {"type": "value", "max":style_usalist_max, "gridIndex": 0, "boundaryGap": [0, '100%']},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "name": "波西米亚风",
                        "type": "line",
                        "data": np.array(style_usa_list['boho']).tolist(),
                    },
                    {
                        "name": "迷彩风",
                        "type": "line",
                        "data": np.array(style_usa_list['camo']).tolist(),
                    },
                    {
                        "name": "中国风",
                        "type": "line",
                        "data": np.array(style_usa_list['chinese_national']).tolist(),
                    },
                    {
                        "name": "学院风",
                        "type": "line",
                        "data": np.array(style_usa_list['college'],).tolist()
                    },
                    {
                        "name": "嘻哈风",
                        "type": "line",
                        "data": np.array(style_usa_list['hip_hop']).tolist(),
                    },
                    {
                        "name": "宫廷风",
                        "type": "line",
                        "data": np.array(style_usa_list['palace']).tolist(),
                    },
                    {
                        "name": "职场风",
                        "type": "line",
                        "data": np.array(style_usa_list['professional']).tolist(),
                    },
                    {
                        "name": "香奈儿风格",
                        "type": "line",
                        "data": np.array(style_usa_list['small_fragrance']).tolist(),
                    },
                    {
                        "name": "运动风",
                        "type": "line",
                        "data": np.array(style_usa_list['sports']).tolist(),
                    },
                ],
            }
            st_echarts(options=options, height="500px")
            options = {
                "title": {"text": "英国地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "legend": {"data": ["波西米亚风", "迷彩风", "中国风", "学院风", "嘻哈风", "宫廷风", "职场风", "香奈儿风格", "运动风"], "textStyle": { "fontSize": 16}, },
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "data": np.array(style_uk_list['data']).tolist(),
                },
                "yAxis": {"type": "value", "max":style_uklist_max, "gridIndex": 0, "boundaryGap": [0, '100%']},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "name": "波西米亚风",
                        "type": "line",
                        "data": np.array(style_uk_list['boho']).tolist(),
                    },
                    {
                        "name": "迷彩风",
                        "type": "line",
                        "data": np.array(style_uk_list['camo']).tolist(),
                    },
                    {
                        "name": "中国风",
                        "type": "line",
                        "data": np.array(style_uk_list['chinese_national']).tolist(),
                    },
                    {
                        "name": "学院风",
                        "type": "line",
                        "data": np.array(style_uk_list['college'],).tolist()
                    },
                    {
                        "name": "嘻哈风",
                        "type": "line",
                        "data": np.array(style_uk_list['hip_hop']).tolist(),
                    },
                    {
                        "name": "宫廷风",
                        "type": "line",
                        "data": np.array(style_uk_list['palace']).tolist(),
                    },
                    {
                        "name": "职场风",
                        "type": "line",
                        "data": np.array(style_uk_list['professional']).tolist(),
                    },
                    {
                        "name": "香奈儿风格",
                        "type": "line",
                        "data": np.array(style_uk_list['small_fragrance']).tolist(),
                    },
                    {
                        "name": "运动风",
                        "type": "line",
                        "data": np.array(style_uk_list['sports']).tolist(),
                    },
                ],
            }
            st_echarts(options=options, height="500px")
            options = {
                "title": {"text": "新加坡地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "legend": {"data": ["波西米亚风", "迷彩风", "中国风", "学院风", "嘻哈风", "宫廷风", "职场风", "香奈儿风格", "运动风"], "textStyle": { "fontSize": 16}, },
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "data": np.array(style_sg_list['data']).tolist(),
                },
                "yAxis": {"type": "value", "max":style_sglist_max, "gridIndex": 0, "boundaryGap": [0, '100%']},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "name": "波西米亚风",
                        "type": "line",
                        "data": np.array(style_sg_list['boho']).tolist(),
                    },
                    {
                        "name": "迷彩风",
                        "type": "line",
                        "data": np.array(style_sg_list['camo']).tolist(),
                    },
                    {
                        "name": "中国风",
                        "type": "line",
                        "data": np.array(style_sg_list['chinese_national']).tolist(),
                    },
                    {
                        "name": "学院风",
                        "type": "line",
                        "data": np.array(style_sg_list['college'],).tolist()
                    },
                    {
                        "name": "嘻哈风",
                        "type": "line",
                        "data": np.array(style_sg_list['hip_hop']).tolist(),
                    },
                    {
                        "name": "宫廷风",
                        "type": "line",
                        "data": np.array(style_sg_list['palace']).tolist(),
                    },
                    {
                        "name": "职场风",
                        "type": "line",
                        "data": np.array(style_sg_list['professional']).tolist(),
                    },
                    {
                        "name": "香奈儿风格",
                        "type": "line",
                        "data": np.array(style_sg_list['small_fragrance']).tolist(),
                    },
                    {
                        "name": "运动风",
                        "type": "line",
                        "data": np.array(style_sg_list['sports']).tolist(),
                    },
                ],
            }
            st_echarts(options=options, height="500px",)    
    elif add_selectbox=="销售指数": 
        selected3 = option_menu(None, ["厂商"], 
            icons=['house', 'cloud-upload', "list-task", 'gear'], 
            menu_icon="cast", default_index=0, orientation="horizontal")
        if selected3 == "销量":
            selected3
        elif selected3 == "厂商":
            st.title("亚马逊羽绒服Top5厂商词云图")
            col1, col2, col3, col4, col5 = st.columns(5)
            col6, col7, col8, col9, col10 = st.columns(5)
            with col1:
                image = Image.open("image/manufacture/cole.png").resize((280, 100))
                st.image(image, caption='cole haan')
            with col2:
                image = Image.open("image/manufacture/bestseller.png").resize((280, 100))
                st.image(image, caption='bestseller')
            with col3:
                image = Image.open("image/manufacture/essentials.png").resize((280, 100))
                st.image(image, caption='essentials')
            with col4:
                image = Image.open("image/manufacture/fuinloth.png").resize((280, 100))
                st.image(image, caption='fuinloth')
            with col5:
                image = Image.open("image/manufacture/goldwin.png").resize((280, 100))
                st.image(image, caption='goldwin')
            with col6:
                image = Image.open("image/manufacture/adidas.png").resize((280, 100))
                st.image(image, caption='adidas')
            with col7:
                image = Image.open("image/manufacture/laundry.png").resize((280, 100))
                st.image(image, caption='laundry')
            with col8:
                image = Image.open("image/manufacture/longking.png").resize((280, 100))
                st.image(image, caption='longking')
            with col9:
                image = Image.open("image/manufacture/regatta.png").resize((280, 100))
                st.image(image, caption='regatta')
            with col10:
                image = Image.open("image/manufacture/TK.png").resize((280, 100))
                st.image(image, caption='TK')
            st.header('澳大利亚地区')
            image1 = Image.open("image/manufacturerau.png").resize((1700, 1200))
            st.image(image1, caption='')
            st.header('中国地区')
            image2 = Image.open("image/manufacturerca.png").resize((1700, 1200))
            st.image(image2, caption='')
            st.header('德国地区')
            image3 = Image.open("image/manufacturerde.png").resize((1700, 1200))
            st.image(image3, caption='')
            st.header('新加坡地区')        
            image4 = Image.open("image/manufacturersg.png").resize((1700, 1200))
            st.image(image4, caption='')
            st.header('英国地区')
            image5 = Image.open("image/manufactureruk.png").resize((1700, 1200))
            st.image(image5, caption='')
            st.header('美国地区')
            image6 = Image.open("image/manufacturerusa.png").resize((1700, 1200))
            st.image(image6, caption='')
    elif add_selectbox=="评价指数": 
        selected4 = option_menu(None, ["曝光度", "点赞量"], 
            icons=['house', 'cloud-upload', "list-task", 'gear'], 
            menu_icon="cast", default_index=0, orientation="horizontal")
        if selected4 == "曝光度": # productRatings
            st.title("亚马逊羽绒服Top5曝光度曲线图")
            options = {
                "title": {"text": "澳大利亚地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "legend": {"data": ["曝光度"], "textStyle": { "fontSize": 16}, },
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "data": np.array(date).tolist(),
                },
                "yAxis": {"type": "value", "max":productRatings_max_au, "gridIndex": 0, "boundaryGap": [0, '100%']},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50,
                    "bottom": 30
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "name": "曝光度",
                        "type": "line",
                        "data": np.array(productRatings_data[0]).tolist(),
                    }
                ],
            }
            st_echarts(options=options, height="500px")
            options = {
                "title": {"text": "中国地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "legend": {"data": ["曝光度"], "textStyle": { "fontSize": 16}, },
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "data": np.array(date).tolist(),
                },
                "yAxis": {"type": "value", "max":productRatings_max_ca, "gridIndex": 0, "boundaryGap": [0, '100%']},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "name": "",
                        "type": "line",
                        "data": np.array(productRatings_data[1]).tolist(),
                    },
                ],
            }
            st_echarts(options=options, height="500px")
            options = {
                "title": {"text": "德国地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "legend": {"data": ["曝光度"], "textStyle": { "fontSize": 16}, },
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "data": np.array(date).tolist(),
                },
                "yAxis": {"type": "value", "max":productRatings_max_de, "gridIndex": 0, "boundaryGap": [0, '100%']},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "name": "",
                        "type": "line",
                        "data": np.array(productRatings_data[2]).tolist(),
                    }
                ],
            }
            st_echarts(options=options, height="500px")
            options = {
                "title": {"text": "新加坡地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "legend": {"data": ["曝光度"], "textStyle": { "fontSize": 16}, },
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "data": np.array(date).tolist(),
                },
                "yAxis": {"type": "value", "max":productRatings_max_sg, "gridIndex": 0, "boundaryGap": [0, '100%']},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "name": "",
                        "type": "line",
                        "data": np.array(productRatings_data[3]).tolist(),
                    }
                ],
            }
            st_echarts(options=options, height="500px",)    
            options = {
                "title": {"text": "英国地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "legend": {"data": ["曝光度"], "textStyle": { "fontSize": 16}, },
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "data": np.array(date).tolist(),
                },
                "yAxis": {"type": "value", "max":productRatings_max_uk, "gridIndex": 0, "boundaryGap": [0, '100%']},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "name": "",
                        "type": "line",
                        "data": np.array(productRatings_data[4]).tolist(),
                    }
                ],
            }
            st_echarts(options=options, height="500px")
            options = {
                "title": {"text": "美国地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "legend": {"data": ["曝光度"], "textStyle": { "fontSize": 16}, },
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "data": np.array(date).tolist(),
                },
                "yAxis": {"type": "value", "max":productRatings_max_usa, "gridIndex": 0, "boundaryGap": [0, '100%']},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "name": "",
                        "type": "line",
                        "data": np.array(productRatings_data[5]).tolist(),
                    }
                ],
            }
            st_echarts(options=options, height="500px")
        elif selected4 == "点赞量":
            st.title("亚马逊羽绒服Top5点赞量曲线图")
            options = {
                "title": {"text": "澳大利亚地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "legend": {"data": ["点赞量"], "textStyle": { "fontSize": 16}, },
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "data": np.array(date).tolist(),
                },
                "yAxis": {"type": "value", "max":productStarts_max_au, "min":4.2, "gridIndex": 0, "boundaryGap": [0, '100%']},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50,
                    "bottom": 30
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "name": "点赞量",
                        "type": "line",
                        "data": np.array(productStarts_data[0]).tolist(),
                    }
                ],
            }
            st_echarts(options=options, height="500px")
            options = {
                "title": {"text": "中国地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "legend": {"data": ["点赞量"], "textStyle": { "fontSize": 16}, },
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "data": np.array(date).tolist(),
                },
                "yAxis": {"type": "value", "max":productStarts_max_ca, "min":4.2, "gridIndex": 0, "boundaryGap": [0, '100%']},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "name": "",
                        "type": "line",
                        "data": np.array(productStarts_data[1]).tolist(),
                    },
                ],
            }
            st_echarts(options=options, height="500px")
            options = {
                "title": {"text": "德国地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "legend": {"data": ["点赞量"], "textStyle": { "fontSize": 16}, },
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "data": np.array(date).tolist(),
                },
                "yAxis": {"type": "value", "max":productStarts_max_de, "min":4.2, "gridIndex": 0, "boundaryGap": [0, '100%']},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "name": "",
                        "type": "line",
                        "data": np.array(productStarts_data[2]).tolist(),
                    }
                ],
            }
            st_echarts(options=options, height="500px")
            options = {
                "title": {"text": "新加坡地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "legend": {"data": ["点赞量"], "textStyle": { "fontSize": 16}, },
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "data": np.array(date).tolist(),
                },
                "yAxis": {"type": "value", "max":productStarts_max_sg, "min":4.2, "gridIndex": 0, "boundaryGap": [0, '100%']},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "name": "",
                        "type": "line",
                        "data": np.array(productStarts_data[3]).tolist(),
                    }
                ],
            }
            st_echarts(options=options, height="500px",)    
            options = {
                "title": {"text": "英国地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "legend": {"data": ["点赞量"], "textStyle": { "fontSize": 16}, },
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "data": np.array(date).tolist(),
                },
                "yAxis": {"type": "value", "max":productStarts_max_uk, "min":4.2, "gridIndex": 0, "boundaryGap": [0, '100%']},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "name": "",
                        "type": "line",
                        "data": np.array(productStarts_data[4]).tolist(),
                    }
                ],
            }
            st_echarts(options=options, height="500px")
            options = {
                "title": {"text": "美国地区", "left": "left", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
                "tooltip": {"trigger": "axis", "showContent": True},
                "legend": {"data": ["点赞量"], "textStyle": { "fontSize": 16}, },
                "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
                "toolbox": {"feature": {"saveAsImage": {}}},
                "xAxis": {
                    "type": "category",
                    "boundaryGap": False,
                    "data": np.array(date).tolist(),
                },
                "yAxis": {"type": "value", "max":productStarts_max_usa, "min":4.2, "gridIndex": 0, "boundaryGap": [0, '100%']},
                "dataZoom": [
                    {
                    "type": 'inside',
                    "start": 0,
                    "end": 50
                    },
                    {
                    "start": 0,
                    "end": 20
                    }
                ],
                "series": [
                    {
                        "name": "",
                        "type": "line",
                        "data": np.array(productStarts_data[5]).tolist(),
                    }
                ],
            }
            st_echarts(options=options, height="500px")
    

    
if __name__ == "__main__":
    print("start")
    st.set_page_config(
        page_title="Clothing",
        page_icon=":clothes:",  
        layout="wide",
        initial_sidebar_state="auto",
    )
    
    with open("json/blouses.json", 'r') as load_f:
        fabric_blouses_data = json.load(load_f)
    with open("json/polos.json", 'r') as load_f:
        fabric_polos_data = json.load(load_f)
    with open("json/t_shirts.json", 'r') as load_f:
        fabric_t_shirts_data = json.load(load_f)
    with open("json/tanks.json", 'r') as load_f:
        fabric_tanks_data = json.load(load_f)
    with open("json/tunics.json", 'r') as load_f:
        fabric_tunics_data = json.load(load_f)
    with open("json/vests.json", 'r') as load_f:
        fabric_vests_data = json.load(load_f)
    with open("json/data.json", 'r') as load_f:
        now = json.load(load_f)
    with open("json/productRatings.json", 'r') as load_f:
        productRatings_data = json.load(load_f)
    with open("json/productStarts.json", 'r') as load_f:
        productStarts_data = json.load(load_f)
    with open("json/date.json", 'r') as load_f:
        date = json.load(load_f)

    connectmongodb()
    style_jp_list, style_jplist_max = readmongodb_style("clothing_style_jp")
    style_cn_list, style_cnlist_max = readmongodb_style("clothing_style_cn")
    style_usa_list, style_usalist_max = readmongodb_style("clothing_style_usa")
    style_uk_list, style_uklist_max = readmongodb_style("clothing_style_uk")
    style_sg_list, style_sglist_max = readmongodb_style("clothing_style_sg")
    productRatings_max_au = computer_max("productRatings", 0)
    productRatings_max_ca = computer_max("productRatings", 1)
    productRatings_max_de = computer_max("productRatings", 2)
    productRatings_max_sg = computer_max("productRatings", 3)
    productRatings_max_uk = computer_max("productRatings", 4)
    productRatings_max_usa = computer_max("productRatings", 5)
    productStarts_max_au = computer_max("productStarts", 0)
    productStarts_max_ca = computer_max("productStarts", 1)
    productStarts_max_de = computer_max("productStarts", 2)
    productStarts_max_sg = computer_max("productStarts", 3)
    productStarts_max_uk = computer_max("productStarts", 4)
    productStarts_max_usa = computer_max("productStarts", 5)
    selected = getValue()
    print(str(selected) + '************************************')
    Layouts_plotly(selected)
