import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

tips=sns.load_dataset("tips")

st.set_page_config(page_title="Seaborn Visualizer - Tips Dataset", layout="centered", page_icon="📊")


st.title("📊 Manish Kumar - Seaborn Plot Explorer")
st.markdown("This interactive Streamlit app showcases various **Seaborn plots** using the famous `tips` dataset.")  



#Create and Display the plots
def display_plot(title,plot_func):
    st.subheader(title)
    fig,ax=plt.subplots(figsize=(8,6))
    plot_func(ax=ax)
    st.pyplot(fig)
    plt.close(fig)

def display_figure_plot(title,plot_func):
    st.subheader(title)
    fig=plot_func()
    st.pyplot(fig)
    plt.close(fig)    

def scatter_plot(ax):
    sns.scatterplot(data=tips,x="total_bill",y="tip",hue="day",ax=ax)   
    ax.set_title("Scatter plot of total bill vs tip")

def line_plot(ax):
    sns.lineplot(data=tips,x="size",y="total_bill",hue='sex',errorbar=None,marker='o',ax=ax)
    ax.set_title("Line plot of total bill vs size")

def bar_plot(ax):
    sns.barplot(data=tips,x='day',y='total_bill',hue='sex',palette='muted',ax=ax)
    ax.set_title("Bar Plot of day vs total bill")

def box_plot(ax):
    sns.boxplot(data=tips,x='day',y='tip',hue='smoker',palette='Set2',ax=ax)
    ax.set_title("Boxplot of Tips by Day")        

def violin_plot(ax):
    sns.violinplot(data=tips,x='day',y='total_bill',hue='time',split=True,palette='bright',ax=ax)
    ax.set_title("Violinplot of Total bill by Day")    

def count_plot(ax):
    sns.countplot(data=tips,x='day',hue='smoker',palette='dark',ax=ax)
    ax.set_title("Countplot of Days by Smoker Status")

def reg_plot(ax):
    sns.regplot(data=tips,x='total_bill',y='tip',scatter_kws={'s':50},line_kws={'color':'red'},ax=ax)
    ax.set_title("Regression Plot of Total Bill vs Tip")    

def hist_plot(ax):
    sns.histplot(data=tips,x='total_bill',bins=15,kde=True,color='blue',ax=ax)
    ax.set_title("Histogram of Total Bill")


def pair_plot():
    g=sns.pairplot(tips,hue='sex',vars=['total_bill','tip','size'],palette='husl')
    g.fig.suptitle("Pair Plot: numeric Variables by Gender",y=1.02)
    return g.fig   

def cat_plot(ax):
    sns.pointplot(data=tips,x='day',y='tip',hue='sex',palette='bright')
    ax.set_title("Catplot(Points): Tips by Day and Gender")    

def joint_plot():
    g=sns.jointplot(data=tips,x="total_bill",y='tip',kind='scatter',color='purple',hue='sex',palette='pastel')
    g.fig.suptitle("Joint Plot: Total Bill vs Tip",y=1.02)
    return g.fig


def facet_grid():
    g=sns.FacetGrid(tips,col='time',row='smoker',margin_titles=True).map(sns.histplot,'total_bill',bins=10,kde=True).add_legend()
    g.fig.suptitle("Facet Grid: Total Bill by Time and Smoker Status",y=1.02)
    return g.fig
    
def strip_plot(ax):
    sns.stripplot(data=tips,x='day',y='tip',hue='sex',jitter=True,palette='Set1',ax=ax)
    ax.set_title("Strip Plot: Tips by data and gender")


def kde_plot(ax):
    sns.kdeplot(data=tips,x='total_bill',y='tip',fill=True,hue='sex',palette='tab10',ax=ax)
    ax.set_title("KDE Plot: Total Bill vs Tip")


display_plot("Scatter Plot",scatter_plot)
display_plot("Line Plot",line_plot)
display_plot("Bar Plot",bar_plot)
display_plot("Box Plot",box_plot)
display_plot("Violin Plot",violin_plot)
display_plot("Count Plot",count_plot)
display_plot("Regression Plot",reg_plot)
display_plot("Histogram",hist_plot)
display_figure_plot("Pair Plot",pair_plot)
display_plot("Cat Plot",cat_plot)
display_figure_plot("Joint Plot",joint_plot)
display_figure_plot("Facet Grid",facet_grid)
display_plot("Strip Plot",strip_plot)
display_plot("KDE Plot",kde_plot)

st.markdown("---")
st.caption("This app is created by Manish Kumar | Powered by Streamlit")