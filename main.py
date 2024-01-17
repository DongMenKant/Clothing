import streamlit as st
import pandas as pd
import numpy as np
from readmongodb import readmongodb, readmongodb_time
from streamlit_echarts import st_echarts
import numpy

global blouses_list
global polos_list
global t_shirts_list
global tanks_list
global tunics_list
global vests_list

def Layouts_plotly():

    # print(blouses_list)
    # print(polos_list)
    #*********************************
    st.title('亚马逊女装排行榜数据分析')
    st.title('\n')
    # st.sidebar.write('')

    add_selectbox = st.sidebar.radio(
        "服装样式",
        ("面料", "开合方式", "衣领", "适合场所")
    )
    if add_selectbox=="面料":
    # 面料pie***********************************
        # blouses
        option = {
            "title": {"text": "Blouses面料", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"],
                    ["Polyester", blouses_list[0][0][0], blouses_list[1][0][0], blouses_list[2][0][0], blouses_list[3][0][0], blouses_list[4][0][0], blouses_list[5][0][0], blouses_list[6][0][0], blouses_list[7][0][0]],
                    ["Spandex", blouses_list[0][0][1], blouses_list[1][0][1], blouses_list[2][0][1], blouses_list[3][0][1], blouses_list[4][0][1], blouses_list[5][0][1], blouses_list[6][0][1], blouses_list[7][0][1]],
                    ["Cotton", blouses_list[0][0][2], blouses_list[1][0][2], blouses_list[2][0][2], blouses_list[3][0][2], blouses_list[4][0][2], blouses_list[5][0][2], blouses_list[6][0][2], blouses_list[7][0][2]],
                    ["Rayon", blouses_list[0][0][3], blouses_list[1][0][3], blouses_list[2][0][3], blouses_list[3][0][3], blouses_list[4][0][3], blouses_list[5][0][3], blouses_list[6][0][3], blouses_list[7][0][3]],
                    ["Viscose", blouses_list[0][0][4], blouses_list[1][0][4], blouses_list[2][0][4], blouses_list[3][0][4], blouses_list[4][0][4], blouses_list[5][0][4], blouses_list[6][0][4], blouses_list[7][0][4]],
                    ["Lace", blouses_list[0][0][5], blouses_list[1][0][5], blouses_list[2][0][5], blouses_list[3][0][5], blouses_list[4][0][5], blouses_list[5][0][5], blouses_list[6][0][5], blouses_list[7][0][5]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                        {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px", key="echarts")
        # polos
        option = {
            "title": {"text": "Polos面料", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"],
                    ["Polyester", polos_list[0][0][0], polos_list[1][0][0], polos_list[2][0][0], polos_list[3][0][0], polos_list[4][0][0], polos_list[5][0][0], polos_list[6][0][0]],
                    ["Spandex", polos_list[0][0][1], polos_list[1][0][1], polos_list[2][0][1], polos_list[3][0][1], polos_list[4][0][1], polos_list[5][0][1], polos_list[6][0][1]],
                    ["Cotton", polos_list[0][0][2], polos_list[1][0][2], polos_list[2][0][2], polos_list[3][0][2], polos_list[4][0][2], polos_list[5][0][2], polos_list[6][0][2]],
                    ["Rayon", polos_list[0][0][3], polos_list[1][0][3], polos_list[2][0][3], polos_list[3][0][3], polos_list[4][0][3], polos_list[5][0][3], polos_list[6][0][3]],
                    ["Viscose", polos_list[0][0][4], polos_list[1][0][4], polos_list[2][0][4], polos_list[3][0][4], polos_list[4][0][4], polos_list[5][0][4], polos_list[6][0][4]],
                    ["Lace", polos_list[0][0][5], polos_list[1][0][5], polos_list[2][0][5], polos_list[3][0][5], polos_list[4][0][5], polos_list[5][0][5], polos_list[6][0][5]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                        {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # t-shirts
        option = {
            "title": {"text": "T-shirts面料", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"],
                    ["Polyester", t_shirts_list[0][0][0], t_shirts_list[1][0][0], t_shirts_list[2][0][0], t_shirts_list[3][0][0], t_shirts_list[4][0][0], t_shirts_list[5][0][0], t_shirts_list[6][0][0], t_shirts_list[7][0][0]],
                    ["Spandex", t_shirts_list[0][0][1], t_shirts_list[1][0][1], t_shirts_list[2][0][1], t_shirts_list[3][0][1], t_shirts_list[4][0][1], t_shirts_list[5][0][1], t_shirts_list[6][0][1], t_shirts_list[7][0][1]],
                    ["Cotton", t_shirts_list[0][0][2], t_shirts_list[1][0][2], t_shirts_list[2][0][2], t_shirts_list[3][0][2], t_shirts_list[4][0][2], t_shirts_list[5][0][2], t_shirts_list[6][0][2], t_shirts_list[7][0][2]],
                    ["Rayon", t_shirts_list[0][0][3], t_shirts_list[1][0][3], t_shirts_list[2][0][3], t_shirts_list[3][0][3], t_shirts_list[4][0][3], t_shirts_list[5][0][3], t_shirts_list[6][0][3], t_shirts_list[7][0][3]],
                    ["Viscose", t_shirts_list[0][0][4], t_shirts_list[1][0][4], t_shirts_list[2][0][4], t_shirts_list[3][0][4], t_shirts_list[4][0][4], t_shirts_list[5][0][4], t_shirts_list[6][0][4], t_shirts_list[7][0][4]],
                    ["Lace", t_shirts_list[0][0][5], t_shirts_list[1][0][5], t_shirts_list[2][0][5], t_shirts_list[3][0][5], t_shirts_list[4][0][5], t_shirts_list[5][0][5], t_shirts_list[6][0][5], t_shirts_list[7][0][5]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                        {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # tanks
        option = {
            "title": {"text": "Tanks面料", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],
                    ["Polyester", tanks_list[0][0][0], tanks_list[1][0][0], tanks_list[2][0][0], tanks_list[3][0][0], tanks_list[4][0][0], tanks_list[5][0][0], tanks_list[6][0][0]],
                    ["Spandex", tanks_list[0][0][1], tanks_list[1][0][1], tanks_list[2][0][1], tanks_list[3][0][1], tanks_list[4][0][1], tanks_list[5][0][1], tanks_list[6][0][1]],
                    ["Cotton", tanks_list[0][0][2], tanks_list[1][0][2], tanks_list[2][0][2], tanks_list[3][0][2], tanks_list[4][0][2], tanks_list[5][0][2], tanks_list[6][0][2]],
                    ["Rayon", tanks_list[0][0][3], tanks_list[1][0][3], tanks_list[2][0][3], tanks_list[3][0][3], tanks_list[4][0][3], tanks_list[5][0][3], tanks_list[6][0][3]],
                    ["Viscose", tanks_list[0][0][4], tanks_list[1][0][4], tanks_list[2][0][4], tanks_list[3][0][4], tanks_list[4][0][4], tanks_list[5][0][4], tanks_list[6][0][4]],
                    ["Lace", tanks_list[0][0][5], tanks_list[1][0][5], tanks_list[2][0][5], tanks_list[3][0][5], tanks_list[4][0][5], tanks_list[5][0][5], tanks_list[6][0][5]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                        {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # tunics
        option = {
            "title": {"text": "Tunics面料", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],
                    ["Polyester", tunics_list[0][0][0], tunics_list[1][0][0], tunics_list[2][0][0], tunics_list[3][0][0], tunics_list[4][0][0], tunics_list[5][0][0], tunics_list[6][0][0]],
                    ["Spandex", tunics_list[0][0][1], tunics_list[1][0][1], tunics_list[2][0][1], tunics_list[3][0][1], tunics_list[4][0][1], tunics_list[5][0][1], tunics_list[6][0][1]],
                    ["Cotton", tunics_list[0][0][2], tunics_list[1][0][2], tunics_list[2][0][2], tunics_list[3][0][2], tunics_list[4][0][2], tunics_list[5][0][2], tunics_list[6][0][2]],
                    ["Rayon", tunics_list[0][0][3], tunics_list[1][0][3], tunics_list[2][0][3], tunics_list[3][0][3], tunics_list[4][0][3], tunics_list[5][0][3], tunics_list[6][0][3]],
                    ["Viscose", tunics_list[0][0][4], tunics_list[1][0][4], tunics_list[2][0][4], tunics_list[3][0][4], tunics_list[4][0][4], tunics_list[5][0][4], tunics_list[6][0][4]],
                    ["Lace", tunics_list[0][0][5], tunics_list[1][0][5], tunics_list[2][0][5], tunics_list[3][0][5], tunics_list[4][0][5], tunics_list[5][0][5], tunics_list[6][0][5]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
                    {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
            {
                "type": "line",
                "smooth": True,
                "seriesLayoutBy": "row",
                "emphasis": {"focus": "series"},
            },
        ],
    }
        st_echarts(option, height="500px")
        # vests
        option = {
            "title": {"text": "Vests面料", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00"],
                    ["Polyester", vests_list[0][0][0], vests_list[1][0][0], vests_list[2][0][0], vests_list[3][0][0], vests_list[4][0][0], vests_list[5][0][0], vests_list[6][0][0]],
                    ["Spandex", vests_list[0][0][1], vests_list[1][0][1], vests_list[2][0][1], vests_list[3][0][1], vests_list[4][0][1], vests_list[5][0][1], vests_list[6][0][1]],
                    ["Cotton", vests_list[0][0][2], vests_list[1][0][2], vests_list[2][0][2], vests_list[3][0][2], vests_list[4][0][2], vests_list[5][0][2], vests_list[6][0][2]],
                    ["Rayon", vests_list[0][0][3], vests_list[1][0][3], vests_list[2][0][3], vests_list[3][0][3], vests_list[4][0][3], vests_list[5][0][3], vests_list[6][0][3]],
                    ["Viscose", vests_list[0][0][4], vests_list[1][0][4], vests_list[2][0][4], vests_list[3][0][4], vests_list[4][0][4], vests_list[5][0][4], vests_list[6][0][4]],
                    ["Lace", vests_list[0][0][5], vests_list[1][0][5], vests_list[2][0][5], vests_list[3][0][5], vests_list[4][0][5], vests_list[5][0][5], vests_list[6][0][5]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                        {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")

    elif add_selectbox=="开合方式": 
    # 开合方式bar***********************************
        # blouses
        option = {
            "title": {"text": "Blouses开合方式", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"],
                    ["Button", blouses_list[0][1][0], blouses_list[1][1][0], blouses_list[2][1][0], blouses_list[3][1][0], blouses_list[4][1][0], blouses_list[5][1][0], blouses_list[6][1][0], blouses_list[7][1][0]],
                    ["Pull", blouses_list[0][1][1], blouses_list[1][1][1], blouses_list[2][1][1], blouses_list[3][1][1], blouses_list[4][1][1], blouses_list[5][1][1], blouses_list[6][1][1], blouses_list[7][1][1]],
                    ["Zipper", blouses_list[0][1][2], blouses_list[1][1][2], blouses_list[2][1][2], blouses_list[3][1][2], blouses_list[4][1][2], blouses_list[5][1][2], blouses_list[6][1][2], blouses_list[7][1][2]],
                    ["Elastic", blouses_list[0][1][3], blouses_list[1][1][3], blouses_list[2][1][3], blouses_list[3][1][3], blouses_list[4][1][3], blouses_list[5][1][3], blouses_list[6][1][3], blouses_list[7][1][3]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # polos
        option = {
            "title": {"text": "Polos开合方式", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"],
                    ["Button", polos_list[0][1][0], polos_list[1][1][0], polos_list[2][1][0], polos_list[3][1][0], polos_list[4][1][0], polos_list[5][1][0], polos_list[6][1][0]],
                    ["Pull", polos_list[0][1][1], polos_list[1][1][1], polos_list[2][1][1], polos_list[3][1][1], polos_list[4][1][1], polos_list[5][1][1], polos_list[6][1][1]],
                    ["Zipper", polos_list[0][1][2], polos_list[1][1][2], polos_list[2][1][2], polos_list[3][1][2], polos_list[4][1][2], polos_list[5][1][2], polos_list[6][1][2]],
                    ["Elastic", polos_list[0][1][3], polos_list[1][1][3], polos_list[2][1][3], polos_list[3][1][3], polos_list[4][1][3], polos_list[5][1][3], polos_list[6][1][3]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # t-shirts
        option = {
            "title": {"text": "T-shirts开合方式", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"],
                    ["Button", t_shirts_list[0][1][0], t_shirts_list[1][1][0], t_shirts_list[2][1][0], t_shirts_list[3][1][0], t_shirts_list[4][1][0], t_shirts_list[5][1][0], t_shirts_list[6][1][0], t_shirts_list[7][1][0]],
                    ["Pull", t_shirts_list[0][1][1], t_shirts_list[1][1][1], t_shirts_list[2][1][1], t_shirts_list[3][1][1], t_shirts_list[4][1][1], t_shirts_list[5][1][1], t_shirts_list[6][1][1], t_shirts_list[7][1][1]],
                    ["Zipper", t_shirts_list[0][1][2], t_shirts_list[1][1][2], t_shirts_list[2][1][2], t_shirts_list[3][1][2], t_shirts_list[4][1][2], t_shirts_list[5][1][2], t_shirts_list[6][1][2], t_shirts_list[7][1][2]],
                    ["Elastic", t_shirts_list[0][1][3], t_shirts_list[1][1][3], t_shirts_list[2][1][3], t_shirts_list[3][1][3], t_shirts_list[4][1][3], t_shirts_list[5][1][3], t_shirts_list[6][1][3], t_shirts_list[7][1][3]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # tanks
        option = {
            "title": {"text": "Tanks开合方式", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],
                    ["Button", tanks_list[0][1][0], tanks_list[1][1][0], tanks_list[2][1][0], tanks_list[3][1][0], tanks_list[4][1][0], tanks_list[5][1][0], tanks_list[6][1][0]],
                    ["Pull", tanks_list[0][1][1], tanks_list[1][1][1], tanks_list[2][1][1], tanks_list[3][1][1], tanks_list[4][1][1], tanks_list[5][1][1], tanks_list[6][1][1]],
                    ["Zipper", tanks_list[0][1][2], tanks_list[1][1][2], tanks_list[2][1][2], tanks_list[3][1][2], tanks_list[4][1][2], tanks_list[5][1][2], tanks_list[6][1][2]],
                    ["Elastic", tanks_list[0][1][3], tanks_list[1][1][3], tanks_list[2][1][3], tanks_list[3][1][3], tanks_list[4][1][3], tanks_list[5][1][3], tanks_list[6][1][3]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # tunics
        option = {
            "title": {"text": "Tunics开合方式", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],
                    ["Button", tunics_list[0][1][0], tunics_list[1][1][0], tunics_list[2][1][0], tunics_list[3][1][0], tunics_list[4][1][0], tunics_list[5][1][0], tunics_list[6][1][0], tunics_list[7][1][0]],
                    ["Pull", tunics_list[0][1][1], tunics_list[1][1][1], tunics_list[2][1][1], tunics_list[3][1][1], tunics_list[4][1][1], tunics_list[5][1][1], tunics_list[6][1][1], tunics_list[7][1][1]],
                    ["Zipper", tunics_list[0][1][2], tunics_list[1][1][2], tunics_list[2][1][2], tunics_list[3][1][2], tunics_list[4][1][2], tunics_list[5][1][2], tunics_list[6][1][2], tunics_list[7][1][2]],
                    ["Elastic", tunics_list[0][1][3], tunics_list[1][1][3], tunics_list[2][1][3], tunics_list[3][1][3], tunics_list[4][1][3], tunics_list[5][1][3], tunics_list[6][1][3], tunics_list[7][1][3]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # vests
        option = {
            "title": {"text": "Vests开合方式", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00"],
                    ["Button", vests_list[0][1][0], vests_list[1][1][0], vests_list[2][1][0], vests_list[3][1][0], vests_list[4][1][0], vests_list[5][1][0], vests_list[6][1][0]],
                    ["Pull", vests_list[0][1][1], vests_list[1][1][1], vests_list[2][1][1], vests_list[3][1][1], vests_list[4][1][1], vests_list[5][1][1], vests_list[6][1][1]],
                    ["Zipper", vests_list[0][1][2], vests_list[1][1][2], vests_list[2][1][2], vests_list[3][1][2], vests_list[4][1][2], vests_list[5][1][2], vests_list[6][1][2]],
                    ["Elastic", vests_list[0][1][3], vests_list[1][1][3], vests_list[2][1][3], vests_list[3][1][3], vests_list[4][1][3], vests_list[5][1][3], vests_list[6][1][3]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
    elif add_selectbox=="衣领": 
    # 衣领pie*************************************
        # blouses
        option = {
            "title": {"text": "Blouses衣领", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"],
                    ["Scoop", blouses_list[0][3][0], blouses_list[1][3][0], blouses_list[2][3][0], blouses_list[3][3][0], blouses_list[4][3][0], blouses_list[5][3][0], blouses_list[6][3][0], blouses_list[7][3][0]],
                    ["Knit", blouses_list[0][3][1], blouses_list[1][3][1], blouses_list[2][3][1], blouses_list[3][3][1], blouses_list[4][3][1], blouses_list[5][3][1], blouses_list[6][3][1], blouses_list[7][3][1]],
                    ["Self-fabric", blouses_list[0][3][2], blouses_list[1][3][2], blouses_list[2][3][2], blouses_list[3][3][2], blouses_list[4][3][2], blouses_list[5][3][2], blouses_list[6][3][2], blouses_list[7][3][2]],
                    ["Ribbed", blouses_list[0][3][3], blouses_list[1][3][3], blouses_list[2][3][3], blouses_list[3][3][3], blouses_list[4][3][3], blouses_list[5][3][3], blouses_list[6][3][3], blouses_list[7][3][3]],
                    ["V-neck", blouses_list[0][3][4], blouses_list[1][3][4], blouses_list[2][3][4], blouses_list[3][3][4], blouses_list[4][3][4], blouses_list[5][3][4], blouses_list[6][3][4], blouses_list[7][3][4]],
                    ["others", blouses_list[0][3][5], blouses_list[1][3][5], blouses_list[2][3][5], blouses_list[3][3][5], blouses_list[4][3][5], blouses_list[5][3][5], blouses_list[6][3][5], blouses_list[7][3][5]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                        {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # polos
        option = {
            "title": {"text": "Polos衣领", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"],
                    ["Scoop", polos_list[0][3][0], polos_list[1][3][0], polos_list[2][3][0], polos_list[3][3][0], polos_list[4][3][0], polos_list[5][3][0], polos_list[6][3][0]],
                    ["Knit", polos_list[0][3][1], polos_list[1][3][1], polos_list[2][3][1], polos_list[3][3][1], polos_list[4][3][1], polos_list[5][3][1], polos_list[6][3][1]],
                    ["Self-fabric", polos_list[0][3][2], polos_list[1][3][2], polos_list[2][3][2], polos_list[3][3][2], polos_list[4][3][2], polos_list[5][3][2], polos_list[6][3][2]],
                    ["Ribbed", polos_list[0][3][3], polos_list[1][3][3], polos_list[2][3][3], polos_list[3][3][3], polos_list[4][3][3], polos_list[5][3][3], polos_list[6][3][3]],
                    ["V-neck", polos_list[0][3][4], polos_list[1][3][4], polos_list[2][3][4], polos_list[3][3][4], polos_list[4][3][4], polos_list[5][3][4], polos_list[6][3][4]],
                    ["others", polos_list[0][3][5], polos_list[1][3][5], polos_list[2][3][5], polos_list[3][3][5], polos_list[4][3][5], polos_list[5][3][5], polos_list[6][3][5]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                        {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # t-shirts
        option = {
            "title": {"text": "T-shirts衣领", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"],
                    ["Scoop", t_shirts_list[0][3][0], t_shirts_list[1][3][0], t_shirts_list[2][3][0], t_shirts_list[3][3][0], t_shirts_list[4][3][0], t_shirts_list[5][3][0], t_shirts_list[6][3][0], t_shirts_list[7][3][0]],
                    ["Knit", t_shirts_list[0][3][1], t_shirts_list[1][3][1], t_shirts_list[2][3][1], t_shirts_list[3][3][1], t_shirts_list[4][3][1], t_shirts_list[5][3][1], t_shirts_list[6][3][1], t_shirts_list[7][3][1]],
                    ["Self-fabric", t_shirts_list[0][3][2], t_shirts_list[1][3][2], t_shirts_list[2][3][2], t_shirts_list[3][3][2], t_shirts_list[4][3][2], t_shirts_list[5][3][2], t_shirts_list[6][3][2], t_shirts_list[7][3][2]],
                    ["Ribbed", t_shirts_list[0][3][3], t_shirts_list[1][3][3], t_shirts_list[2][3][3], t_shirts_list[3][3][3], t_shirts_list[4][3][3], t_shirts_list[5][3][3], t_shirts_list[6][3][3], t_shirts_list[7][3][3]],
                    ["V-neck", t_shirts_list[0][3][4], t_shirts_list[1][3][4], t_shirts_list[2][3][4], t_shirts_list[3][3][4], t_shirts_list[4][3][4], t_shirts_list[5][3][4], t_shirts_list[6][3][4], t_shirts_list[7][3][4]],
                    ["others", t_shirts_list[0][3][5], t_shirts_list[1][3][5], t_shirts_list[2][3][5], t_shirts_list[3][3][5], t_shirts_list[4][3][5], t_shirts_list[5][3][5], t_shirts_list[6][3][5], t_shirts_list[7][3][5]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                        {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # tanks
        option = {
            "title": {"text": "Tanks衣领", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],
                    ["Scoop", tanks_list[0][3][0], tanks_list[1][3][0], tanks_list[2][3][0], tanks_list[3][3][0], tanks_list[4][3][0], tanks_list[5][3][0], tanks_list[6][3][0]],
                    ["Knit", tanks_list[0][3][1], tanks_list[1][3][1], tanks_list[2][3][1], tanks_list[3][3][1], tanks_list[4][3][1], tanks_list[5][3][1], tanks_list[6][3][1]],
                    ["Self-fabric", tanks_list[0][3][2], tanks_list[1][3][2], tanks_list[2][3][2], tanks_list[3][3][2], tanks_list[4][3][2], tanks_list[5][3][2], tanks_list[6][3][2]],
                    ["Ribbed", tanks_list[0][3][3], tanks_list[1][3][3], tanks_list[2][3][3], tanks_list[3][3][3], tanks_list[4][3][3], tanks_list[5][3][3], tanks_list[6][3][3]],
                    ["V-neck", tanks_list[0][3][4], tanks_list[1][3][4], tanks_list[2][3][4], tanks_list[3][3][4], tanks_list[4][3][4], tanks_list[5][3][4], tanks_list[6][3][4]],
                    ["others", tanks_list[0][3][5], tanks_list[1][3][5], tanks_list[2][3][5], tanks_list[3][3][5], tanks_list[4][3][5], tanks_list[5][3][5], tanks_list[6][3][5]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                        {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # tunics
        option = {
            "title": {"text": "Tunics衣领", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],
                    ["Scoop", tunics_list[0][3][0], tunics_list[1][3][0], tunics_list[2][3][0], tunics_list[3][3][0], tunics_list[4][3][0], tunics_list[5][3][0], tunics_list[6][3][0], tunics_list[7][3][0]],
                    ["Knit", tunics_list[0][3][1], tunics_list[1][3][1], tunics_list[2][3][1], tunics_list[3][3][1], tunics_list[4][3][1], tunics_list[5][3][1], tunics_list[6][3][1], tunics_list[7][3][1]],
                    ["Self-fabric", tunics_list[0][3][2], tunics_list[1][3][2], tunics_list[2][3][2], tunics_list[3][3][2], tunics_list[4][3][2], tunics_list[5][3][2], tunics_list[6][3][2], tunics_list[7][3][2]],
                    ["Ribbed", tunics_list[0][3][3], tunics_list[1][3][3], tunics_list[2][3][3], tunics_list[3][3][3], tunics_list[4][3][3], tunics_list[5][3][3], tunics_list[6][3][3], tunics_list[7][3][3]],
                    ["V-neck", tunics_list[0][3][4], tunics_list[1][3][4], tunics_list[2][3][4], tunics_list[3][3][4], tunics_list[4][3][4], tunics_list[5][3][4], tunics_list[6][3][4], tunics_list[7][3][4]],
                    ["others", tunics_list[0][3][5], tunics_list[1][3][5], tunics_list[2][3][5], tunics_list[3][3][5], tunics_list[4][3][5], tunics_list[5][3][5], tunics_list[6][3][5], tunics_list[7][3][5]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                        {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # vests
        option = {
            "title": {"text": "Vests衣领", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00"],
                    ["Scoop", vests_list[0][3][0], vests_list[1][3][0], vests_list[2][3][0], vests_list[3][3][0], vests_list[4][3][0], vests_list[5][3][0], vests_list[6][3][0]],
                    ["Knit", vests_list[0][3][1], vests_list[1][3][1], vests_list[2][3][1], vests_list[3][3][1], vests_list[4][3][1], vests_list[5][3][1], vests_list[6][3][1]],
                    ["Self-fabric", vests_list[0][3][2], vests_list[1][3][2], vests_list[2][3][2], vests_list[3][3][2], vests_list[4][3][2], vests_list[5][3][2], vests_list[6][3][2]],
                    ["Ribbed", vests_list[0][3][3], vests_list[1][3][3], vests_list[2][3][3], vests_list[3][3][3], vests_list[4][3][3], vests_list[5][3][3], vests_list[6][3][3]],
                    ["V-neck", vests_list[0][3][4], vests_list[1][3][4], vests_list[2][3][4], vests_list[3][3][4], vests_list[4][3][4], vests_list[5][3][4], vests_list[6][3][4]],
                    ["others", vests_list[0][3][5], vests_list[1][3][5], vests_list[2][3][5], vests_list[3][3][5], vests_list[4][3][5], vests_list[5][3][5], vests_list[6][3][5]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                        {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
    elif add_selectbox=="适合场所": 
    # 适合场所bar***********************************
        # blouses
        option = {
            "title": {"text": "Blouses适合场所", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"],
                    ["Sport", blouses_list[0][4][0], blouses_list[1][4][0], blouses_list[2][4][0], blouses_list[3][4][0], blouses_list[4][4][0], blouses_list[5][4][0], blouses_list[6][4][0], blouses_list[7][4][0]],
                    ["Work", blouses_list[0][4][1], blouses_list[1][4][1], blouses_list[2][4][1], blouses_list[3][4][1], blouses_list[4][4][1], blouses_list[5][4][1], blouses_list[6][4][1], blouses_list[7][4][1]],
                    ["Daily", blouses_list[0][4][2], blouses_list[1][4][2], blouses_list[2][4][2], blouses_list[3][4][2], blouses_list[4][4][2], blouses_list[5][4][2], blouses_list[6][4][2], blouses_list[7][4][2]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # polos
        option = {
            "title": {"text": "Polos适合场所", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"],
                    ["Sport", polos_list[0][4][0], polos_list[1][4][0], polos_list[2][4][0], polos_list[3][4][0], polos_list[4][4][0], polos_list[5][4][0], polos_list[6][4][0]],
                    ["Work", polos_list[0][4][1], polos_list[1][4][1], polos_list[2][4][1], polos_list[3][4][1], polos_list[4][4][1], polos_list[5][4][1], polos_list[6][4][1]],
                    ["Daily", polos_list[0][4][2], polos_list[1][4][2], polos_list[2][4][2], polos_list[3][4][2], polos_list[4][4][2], polos_list[5][4][2], polos_list[6][4][2]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # t-shirts
        option = {
            "title": {"text": "T-shirts适合场所", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"],
                    ["Sport", t_shirts_list[0][4][0], t_shirts_list[1][4][0], t_shirts_list[2][4][0], t_shirts_list[3][4][0], t_shirts_list[4][4][0], t_shirts_list[5][4][0], t_shirts_list[6][4][0], t_shirts_list[7][4][0]],
                    ["Work", t_shirts_list[0][4][1], t_shirts_list[1][4][1], t_shirts_list[2][4][1], t_shirts_list[3][4][1], t_shirts_list[4][4][1], t_shirts_list[5][4][1], t_shirts_list[6][4][1], t_shirts_list[7][4][1]],
                    ["Daily", t_shirts_list[0][4][2], t_shirts_list[1][4][2], t_shirts_list[2][4][2], t_shirts_list[3][4][2], t_shirts_list[4][4][2], t_shirts_list[5][4][2], t_shirts_list[6][4][2], t_shirts_list[7][4][2]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # tanks
        option = {
            "title": {"text": "Tanks适合场所", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],
                    ["Sport", tanks_list[0][4][0], tanks_list[1][4][0], tanks_list[2][4][0], tanks_list[3][4][0], tanks_list[4][4][0], tanks_list[5][4][0], tanks_list[6][4][0]],
                    ["Work", tanks_list[0][4][1], tanks_list[1][4][1], tanks_list[2][4][1], tanks_list[3][4][1], tanks_list[4][4][1], tanks_list[5][4][1], tanks_list[6][4][1]],
                    ["Daily", tanks_list[0][4][2], tanks_list[1][4][2], tanks_list[2][4][2], tanks_list[3][4][2], tanks_list[4][4][2], tanks_list[5][4][2], tanks_list[6][4][2]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # tunics
        option = {
            "title": {"text": "Tunics适合场所", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],
                    ["Sport", tunics_list[0][4][0], tunics_list[1][4][0], tunics_list[2][4][0], tunics_list[3][4][0], tunics_list[4][4][0], tunics_list[5][4][0], tunics_list[6][4][0], tunics_list[7][4][0]],
                    ["Work", tunics_list[0][4][1], tunics_list[1][4][1], tunics_list[2][4][1], tunics_list[3][4][1], tunics_list[4][4][1], tunics_list[5][4][1], tunics_list[6][4][1], tunics_list[7][4][1]],
                    ["Daily", tunics_list[0][4][2], tunics_list[1][4][2], tunics_list[2][4][2], tunics_list[3][4][2], tunics_list[4][4][2], tunics_list[5][4][2], tunics_list[6][4][2], tunics_list[7][4][2]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")
        # vests
        option = {
            "title": {"text": "Vests适合场所", "left": "center", "textStyle": { "fontSize": 24}, "subtextStyle": { "fontSize": 20}},
            "legend": {"orient": "vertical", "left": "left", "textStyle": { "fontSize": 14}},
            "tooltip": {"trigger": "axis", "showContent": True},
            "dataset": {
                "source": [
                    ["Time", "10:00", "11:00", "12:00", "13:00", "14:00"],
                    ["Sport", vests_list[0][4][0], vests_list[1][4][0], vests_list[2][4][0], vests_list[3][4][0], vests_list[4][4][0], vests_list[5][4][0], vests_list[6][4][0]],
                    ["Work", vests_list[0][4][1], vests_list[1][4][1], vests_list[2][4][1], vests_list[3][4][1], vests_list[4][4][1], vests_list[5][4][1], vests_list[6][4][1]],
                    ["Daily", vests_list[0][4][2], vests_list[1][4][2], vests_list[2][4][2], vests_list[3][4][2], vests_list[4][4][2], vests_list[5][4][2], vests_list[6][4][2]],
                ]
            },
            "xAxis": {"type": "category"},
            "yAxis": {"gridIndex": 0},
            "grid": {"top": "55%"},
            "series": [
                {
                    "type": "pie",
                    "id": "pie",
                    "radius": "30%",
                    "center": ["50%", "30%"],
                    "emphasis": {"focus": "data"},
                    "label": {"formatter": "{b}: {@10:00} ({d}%)"},
                    "encode": {"itemName": "Time", "value": "10:00", "tooltip": "10:00"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
                {
                    "type": "line",
                    "smooth": True,
                    "seriesLayoutBy": "row",
                    "emphasis": {"focus": "series"},
                },
            ],
        }
        st_echarts(option, height="500px")


def main():
    Layouts_plotly()
    
if __name__ == "__main__":
    st.set_page_config(
    page_title="Clothing",
    layout="wide",
    initial_sidebar_state="expanded",
    )

    # 数据库表
    table = ("blouses", "polos", "t_shirts", "tanks", "tunics", "vests")


    blouses_data_list = readmongodb(table[0])
    polos_data_list = readmongodb(table[1])
    t_shirts_data_list = readmongodb(table[2])
    tanks_data_list = readmongodb(table[3])
    tunics_data_list = readmongodb(table[4])
    vests_data_list = readmongodb(table[5])
    total_data_list = numpy.zeros((5,6))
    for i in range(5):
        for j in range(6):
            total_data_list[i][j] = blouses_data_list[i][j] + polos_data_list[i][j] +  t_shirts_data_list[i][j] + tanks_data_list[i][j] + tunics_data_list[i][j] + vests_data_list[i][j]

    blouses_list = readmongodb_time(table[0]) #blouses_list中第一维是时刻、第二维是服装属性、第三维是属性值
    polos_list = readmongodb_time(table[1])
    t_shirts_list = readmongodb_time(table[2])
    tanks_list = readmongodb_time(table[3])
    tunics_list = readmongodb_time(table[4])
    vests_list = readmongodb_time(table[5])
    
    main()
