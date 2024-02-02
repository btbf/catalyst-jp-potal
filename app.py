import streamlit as st
import numpy as np
import const
#import pandas as pd
#from st_aggrid import AgGrid
#from st_aggrid.grid_options_builder import GridOptionsBuilder
#from st_aggrid.shared import JsCode

st.set_page_config(**const.SET_PAGE_CONFIG)
st.markdown(const.HIDE_ST_STYLE, unsafe_allow_html=True)

#st.set_page_config(
#    layout="wide"
#)

st.title("カタリスト提案日本語ポータルサイト v0.1-α")
with st.expander("はじめにお読みください"):
    st.write("""
        カタリスト提案の日本語ポータルサイト構築に向けて取り急ぎ無料で出来る範囲で構築しました。
        これから本格的なポータルサイト開発に向けてFund12へ提案を提出予定です。
    """)

# Initialize connection.
conn = st.connection("snowflake")
#sql = "SELECT * from proposals WHERE CHALLENGE_ID = 130 FETCH FIRST 10 ROWS ONLY;"
#sql = "SELECT * from proposals FETCH FIRST 10 ROWS ONLY;"

@st.cache_resource
def load_data(sql):
    df = conn.query(sql, ttl=600)
    return df

#df = load_data(sql)

with st.container():
    col5, col6 = st.columns([1, 1]) 
    options = col5.selectbox(
        '表示カテゴリを選択してください',
        ['オープン開発者 - 技術系', 'オープンエコシステム - 非技術系', 'ユースケース: コンセプト', 'ユースケース: ソリューション', 'ユースケース: 製品', 'カタリスト改善: 発見'],
        index=0,
        #key='select_category', 
        #on_change=re_query,
        #placeholder="カテゴリを選択してください",
    )
    serch_text = col5.text_input(label='検索',placeholder='aaa')
    # '表示件数',
    # ['10', '20', '30', '40', '50', '100'],
    # index=0,
    #key='select_category', 
    #on_change=page_nation
    #placeholder="カテゴリを選択してください",
    #)


#st.write(st.session_state.select_category)
match options:
    case "オープン開発者 - 技術系":
        cat_id = 130
        subheader="Cardano 開発者エクスペリエンスの実現と向上を中心としたオープンソース テクノロジーへの貢献または開発を行う開発者とエンジニアをサポートすることを目的としています。目標は、統合開発環境を合理化し、より効率的にコードを作成し、開発者に使いやすさを提供する、開発者にとって使いやすいツールとアプローチを作成することです。  "
    case "オープンエコシステム - 非技術系":
        cat_id = 131
        subheader="エコシステムの成長を促進し、教育とコミュニティの取り組みを促進し、Cardano の世界的な拠点を拡大し、より多くの Cardano ユーザーを参加させることです。カルダノがコミュニティに存在する既存の地域と他の新しいコミュニティの両方で、マーケティング、教育、コミュニティ構築、その他の手段を通じてそのような目標を推進するのに役立つ幅広い取り組みをカバーし、意識を高め、影響力のあるコミュニティを実現します。"
    case "ユースケース: コンセプト":
        cat_id = 132
        subheader="革新的な Cardano ベースの製品、サービス、ビジネス モデルの概念実証、設計調査、および基本的なプロトタイピングを提供する初期段階のアイデアの開発を目指すプロジェクトを対象としています。特に Catalyst の新規参入者がアイデアを軌道に乗せ、製品設計プロセスに取り組む経験を得るのをサポートするのに役立ちます。プロジェクトでは、Cardano に実用性をもたらす新しいアイデアを生成し、テストする必要があります。 "
    case "ユースケース: ソリューション":
        cat_id = 133
        subheader="ソリューションの技術的実現可能性を開発およびテストし、イノベーションを最小実行可能製品 (MVP) の準備段階に準備しようとしているプロジェクトを対象としています。このカテゴリの提案者は、製品、サービス、または革新的なビジネス モデルにおけるイノベーションが機能することを実証する必要があります。 "
    case "ユースケース: 製品":
        cat_id = 134
        subheader="すでに市場で入手可能な既存の製品の機能を大幅に拡張することで、既存の製品、サービス、または革新的なビジネス提案を強化しようとしているプロジェクトやチームを対象としています。既存のベンチャーや企業に新しい機能を追加するためにこのカテゴリに提出するプロジェクトは、提案するソリューションがカルダノ ブロックチェーンをどのように活用しているかを示す必要があります。  "
    case "カタリスト改善: 発見":
        cat_id = 135
        subheader="Catalyst 投票システムの最先端技術を進歩させるには、どのような研究開発が必要ですか?新しい戦略的要件を探索したり、高度な検証がすでに達成されていることをまだ実証していない Catalyst の技術的または手順的な実験をテストすることです。"
    case "カタリスト改善: 開発":
        cat_id = 136
        subheader=""

st.info(subheader)
#st.write(f"{cat_id}")

sql = f"""SELECT * FROM proposals
WHERE CHALLENGE_ID = {cat_id}
;"""


df = load_data(sql)
st.text(f"提案数:{len(df)} 件")
for row in df.itertuples():

    with st.container():
        
        with st.container():
            # st.info(f"{row.TITLE}",icon="ℹ️")
            st.subheader(f"{row.TITLE})",divider="rainbow")
            col1, col2 = st.columns([3, 2]) 
            with col1.container():
                st.caption(f"課題：{row.PROBLEM}")
                #st.write(f"{row.PROBLEM}")
                st.caption(f"解決策：{row.SOLUTION}")
                #st.write(f"{row.SOLUTION}")
                st.link_button("提案詳細ページを見る",f"{row.LINK}",type="primary")
            
            with col2.container():
                st.warning("レビュアー評価")
                col3, col4 = st.columns([1, 2])
                col3.write("総合評価")
                #col3.write(f"{row.AVG_SCORE}/5",unsafe_allow_html=True)
                new_title = f"<p style=\"font-family:sans-serif; color:Green; font-size: 42px;\">{row.AVG_SCORE}/5</p>"
                col3.markdown(new_title, unsafe_allow_html=True)
                col4.write(f"エコシステム影響度：<span style=\"color:red;\">{row.ALIGNMENT_SCORE}/5</span>",unsafe_allow_html=True)
                col4.write(f"実現可能性：<span style=\"color:red;\">{row.FEASIBILITY_SCORE}/5</span>",unsafe_allow_html=True)
                col4.write(f"コストパフォーマンス：<span style=\"color:red;\">{row.AUDITABILITY_SCORE}/5</span>",unsafe_allow_html=True)




    #st.session_state.select_category
    #return df

#st.write('You selected:', options)


