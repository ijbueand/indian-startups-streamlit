import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv('startup_funding.csv', index_col = 'Sr No')

# Limpiamos los datos de las fechas y convertimos la columna en fecha

df.drop(df[[len(date) != 10 for date in df['Date dd/mm/yyyy']]].index, inplace = True)
df.drop(df[df['Date dd/mm/yyyy'] == '12/05.2015'].index, inplace = True)
df.drop(df[df['Date dd/mm/yyyy'] == '13/04.2015'].index, inplace = True)
df.drop(df[df['Date dd/mm/yyyy'] == '15/01.2015'].index, inplace = True)

df['Date dd/mm/yyyy'] = pd.to_datetime(df['Date dd/mm/yyyy'], format = "%d/%m/%Y")

# Renombramos las columnas

df.rename({'Date dd/mm/yyyy': 'Date', 
           'Industry Vertical': 'Industry',
           'SubVertical': 'Sub-Industry',
           'Investors Name': 'Investors',
           'InvestmentnType': 'Investment Type'}, axis = 1, inplace = True)

# Vemos si hay NAs

# df.isna().sum()/len(df)

# Eliminamos la columna con más NAs y las filas con NAs.

df.drop('Remarks', axis = 1, inplace = True)
df.dropna(axis = 0, inplace = True)

# df.isna().sum()/len(df)

# Corregimos imperfecciones en los nombres de los inversores
df['Investors'] = df['Investors'].apply(lambda x: str(x).title())
df = df.replace(['Undisclosed Investor', 'Undisclosed'], 'Undisclosed Investors')

# Corregimos imperfecciones en los nombres
df = df.replace(['Seed Funding', 'Seed', 'Seed Round', 'Seed / Angle Funding', 'Angel', 'Seed/ Angel Funding', 'Seed/Angel Funding', 'Angel / Seed Funding'], 'Seed / Angel Funding')
df = df.replace(['Private Equity Round', 'Equity'], 'Private Equity')
df = df.replace(['pre-series A', 'pre-Series A'], 'Pre-Series A')
df = df.replace(['ECommerce', 'E-Commerce', 'Ecommerce'], 'eCommerce')
df = df.replace(['Transportation'], 'Transport')
df = df.replace(['FinTech'], 'Fin-Tech')
df = df.replace(['EdTech', 'Edtech'], 'Ed-Tech')
df = df.replace(['Bengaluru'], 'Bangalore')
df = df.replace(['Ola'], 'Ola Cabs')
df = df.replace(['Oyo Rooms'], 'OYO Rooms')

# Convertimos 'Amount of USD' en numérico
df['Amount in USD'] = df['Amount in USD'].apply(lambda x: str(x).replace(",",""))
df.drop(df[[row.isnumeric() == False for row in df['Amount in USD']]].index, inplace = True)
df['Amount in USD'] = pd.to_numeric(df['Amount in USD'])

st.set_page_config(layout = 'wide')

row_spacer01, row01, row_spacer02, row02, row_spacer03 = st.columns((.1, 2.3, .1, 1.3, .1))
with row01:
    st.markdown('# La India en Startups')
with row02:
    st.text("")
    st.subheader('Streamlit App by [Isaías Bueno](https://www.linkedin.com/in/isaiasbue/)')

row_spacer11, row11, row_spacer12 = st.columns((.1, 3.2, .1))
with row11:
    st.image('https://cdn2.civitatis.com/singapur/singapur/guia/little-india.jpg')
    st.markdown('## Una breve historia de éxito')
    st.markdown("India se ha desarrollado económicamente en las últimas décadas debido a una serie de factores, entre ellos la **apertura de su economía al comercio internacional, la implementación de reformas económicas y la creciente demanda de bienes y servicios en el país**. Además, India cuenta con una **población joven y en crecimiento**, lo que proporciona una importante **fuerza laboral** y un **mercado interno en expansión**.")
    st.markdown("Otro factor que ha contribuido al desarrollo económico de India ha sido la **inversión en educación, ciencia y tecnología**, lo que ha permitido al país aumentar su competitividad y desempeño en sectores como la **tecnología de la información** y la **industria manufacturera**.")
    st.markdown("Gracias a estos factores, India ha logrado un **crecimiento económico sostenido** y ha mejorado su posición en el ranking mundial de economías. Si continúa en esta tendencia, es posible que India se convierta en una **potencia mundial en el futuro cercano**.")
    st.markdown('### Aviso a navegantes')
    st.markdown("_¡Atención! Si estás considerando invertir en startups en India, es importante que hagas tu propia investigación y evalúes cuidadosamente el riesgo y la potencial rentabilidad de cualquier inversión en particular. Además, es recomendable hablar con un asesor financiero o un profesional de inversiones para obtener más información y consejos sobre cómo invertir de manera inteligente y prudente._")

row_spacer21, row21, row_spacer22 = st.columns((.1, 3.2, .1))
with row21:
    st.markdown('## Indian Startup Fundings Dataset')
    st.markdown('Una **startup** es una empresa nueva y en crecimiento que busca resolver un problema o aprovechar una oportunidad en el mercado. A diferencia de las empresas establecidas, **las startups suelen tener un enfoque innovador y están orientadas a la escalabilidad y al crecimiento rápido**. Las startups suelen operar en entornos altamente competitivos y pueden enfrentar riesgos significativos, pero también pueden ofrecer un **potencial de rentabilidad elevado para los inversores**.')
    st.markdown("Este [conjunto de datos](https://www.kaggle.com/datasets/sudalairajkumar/indian-startup-funding) contiene información sobre la creación y financiación de las startups en India desde enero de 2015 hasta enero de 2020. Incluye columnas con la fecha de financiación, la ciudad en la que está radicada la startup, los nombres de los financiadores y la cantidad invertida (en USD).")
    df
    estado_del_checkbox = st.checkbox("Ver procedimiento de limpieza de datos", value = False)
    if estado_del_checkbox:
        code = ''' df = pd.read_csv('startup_funding.csv', index_col = 'Sr No')

    # Limpiamos los datos de las fechas y convertimos la columna en fecha

    df.drop(df[[len(date) != 10 for date in df['Date dd/mm/yyyy']]].index, inplace = True)
    df.drop(df[df['Date dd/mm/yyyy'] == '12/05.2015'].index, inplace = True)
    df.drop(df[df['Date dd/mm/yyyy'] == '13/04.2015'].index, inplace = True)
    df.drop(df[df['Date dd/mm/yyyy'] == '15/01.2015'].index, inplace = True)

    df['Date dd/mm/yyyy'] = pd.to_datetime(df['Date dd/mm/yyyy'], format = "%d/%m/%Y")

    # Renombramos las columnas

    df.rename({'Date dd/mm/yyyy': 'Date', 
            'Industry Vertical': 'Industry',
            'SubVertical': 'Sub-Industry',
            'Investors Name': 'Investors',
            'InvestmentnType': 'Investment Type'}, axis = 1, inplace = True)

    # Vemos si hay NAs

    df.isna().sum()/len(df)

    # Eliminamos la columna con más NAs y las filas con NAs.

    df.drop('Remarks', axis = 1, inplace = True)
    df.dropna(axis = 0, inplace = True)

    df.isna().sum()/len(df)

    # Corregimos imperfecciones en los nombres de los inversores
    df['Investors'] = df['Investors'].apply(lambda x: str(x).title())
    df = df.replace(['Undisclosed Investor', 'Undisclosed'], 'Undisclosed Investors')

    # Corregimos imperfecciones en los nombres de las etapas de inversión
    df = df.replace(['Seed Funding', 'Seed', 'Seed Round', 'Seed / Angle Funding', 'Angel', 'Seed/ Angel Funding', 'Seed/Angel Funding', 'Angel / Seed Funding'], 'Seed / Angel Funding')
    df = df.replace(['Private Equity Round', 'Equity'], 'Private Equity')
    df = df.replace(['pre-series A', 'pre-Series A'], 'Pre-Series A')

    # Convertimos 'Amount of USD' en numérico
    df['Amount in USD'] = df['Amount in USD'].apply(lambda x: str(x).replace(",",""))
    df.drop(df[[row.isnumeric() == False for row in df['Amount in USD']]].index, inplace = True)
    df['Amount in USD'] = pd.to_numeric(df['Amount in USD'])
    '''
        st.code(code, language='python')
    st.markdown('## Evolución del ecosistema de inversión en India')

row_spacer31, row31, row_spacer32  = st.columns((.1, 3.2, .1))
with row31:
    st.markdown('Los inversores a menudo buscan **invertir en economías en crecimiento**, y la economía de India ha experimentado un crecimiento sostenido en los últimos años. Esto ha atraído a muchos inversores que buscan aprovechar las **oportunidades de inversión en el mercado indio**. Además, la creciente población y la clase media emergente en India han creado un **mercado atractivo para muchas empresas y startups**, lo que ha aumentado el interés de los inversores en el país.')
    st.markdown('En relación a la inversión por meses, puede parecer que se relizan más inversiones a primeros de año que a finales de año, pudiéndose percibir una ligera tendencia bajista. No obstante, esto es sólo resultado del hecho de que los datos recojan sólo hasta enero de 2020, faltando aún aquellos relativos a mediados y finales de año. De hecho, la frecuencia con la que se realizan inversiones puede depender de muchos factores, como el perfil de riesgo del inversor, su situación financiera, sus objetivos de inversión y otros factores. Por lo tanto, **no hay una tendencia generalizada en cuanto a cuándo se realizan la mayoría de las inversiones**.')

row_spacer41, row41, row_spacer42, row42, row_spacer43  = st.columns((.1, 3.2, .1, 3.2, .1))
with row41:
    df['Date'] = pd.to_datetime(df['Date'].astype('string').str[:7])

    fig = plt.figure(figsize=(8,3), dpi=150)
    plt.style.use('seaborn-v0_8-darkgrid')
    sns.lineplot(data = df, x = 'Date', y = 'Amount in USD', color = '#FF9933')
    plt.xticks(['2016-01', '2017-01', '2018-01', '2019-01', '2020-01'], labels=['2016', '2017', '2018', '2019', '2020'])
    plt.yscale('log')
    plt.title("Inversión ($M) destinada a Startups Indias")
    plt.ylabel('')
    plt.xlabel('')
    fig 
with row42:
    investment_by_month_count = df["Date"].dt.month.value_counts().sort_index()

    fig = plt.figure(figsize=(8,3), dpi=150)
    plt.title("Número de Inversiones por Mes")
    plt.bar(['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'], investment_by_month_count, color = '#FF9933')
    fig 
    

row_spacer51, row51, row_spacer52 = st.columns((.1, 3.2, .1))
with row51:
    st.markdown('## Startups indias más importantes')
    st.markdown("A continuación, verá las startups indias más importantes en relación al capital que se ha invertido en ellas. Puede seleccionar cuántas empresas ver desplazando la siguiente barra.")
    
    n = st.select_slider('Número de empresas', range(1,14), value=10)

    fig = plt.figure(figsize=(8,3), dpi=200)
    df.groupby('Startup Name').sum()['Amount in USD'].sort_values(ascending = False).head(n).plot(kind = 'barh', linewidth=3, color = '#FF9933').invert_yaxis()
    plt.title("Inversión Total ($M) por Startup")
    plt.ylabel('')
    plt.show()
    fig

    st.markdown("### Más sobre el Top 3...")
    with st.expander("Flipkart (el Aliexpress indio)"):
        st.write("""
            Flipkart es una empresa de **comercio electrónico** india fundada en 2007. La empresa se dedica a ofrecer una amplia gama de productos a sus clientes, incluyendo **libros, electrónica, ropa y accesorios**, entre otros. Flipkart ha tenido un gran éxito en el mercado indio y se ha convertido en **uno de los principales minoristas en línea del país**. Además, la empresa ha adquirido varias otras empresas en un esfuerzo por expandirse y ampliar su oferta de productos y servicios.
        """)
    with st.expander("Rapido Bike Taxi (el Uber indio)"):
        st.write("""
            Rapido Bike Taxi es una empresa de **transporte de pasajeros en motocicleta** en India. La empresa ofrece una plataforma de viajes en motocicleta a través de su **aplicación móvil**, que permite a los usuarios solicitar un viaje en cualquier momento y lugar. Rapido Bike Taxi se enfoca en ofrecer una **opción de transporte rápida y conveniente en entornos urbanos** y tiene una amplia presencia en varias ciudades de India. La empresa ha tenido un gran éxito en el mercado indio y ha expandido su negocio a otros países de la región.        """)
    with st.expander("Paytm (el Bizum indio)"):
        st.write("""
            Paytm es una empresa india de **tecnología financiera y pagos en línea**. La empresa ofrece una plataforma de pagos digitales que permite a los usuarios **realizar transacciones en línea de manera segura y conveniente**. Paytm tiene una amplia presencia en India y ofrece una variedad de servicios, como **pagos de facturas, transferencias de dinero, compras en línea y pagos en tiendas físicas**. La empresa ha tenido un gran éxito en el mercado indio y ha expandido su negocio a otros países de la región.
        """)

row_spacer61, row61, row_spacer62 = st.columns((.1, 3.2, .1))
with row61:
    st.markdown('## Inversiones por sector')
    st.markdown("A continuación, verá las industrias o sectores con más empresas fundadas y con más financiación. Puede seleccionar cuántas ver desplazando la siguiente barra.")
    
    m = st.select_slider('Número de sectores', range(1,11), value=5)

row_spacer71, row71, row_spacer72, row72, row_spacer73, row73, row_spacer74 = st.columns((.1, 3.2, .1, 3.2, .1, 3.2, .1))
with row71:
    fig = plt.figure(figsize=(4, 5), dpi=200)
    df['Industry'].value_counts().sort_values(ascending = False).head(m).plot(kind = 'barh', linewidth=3, color = '#FF9933').invert_yaxis()
    plt.title("Industrias con más Startups registradas")
    plt.ylabel('')
    fig
with row72:
    fig = plt.figure(figsize=(4, 5), dpi=200)
    df.groupby('Industry').sum()['Amount in USD'].sort_values(ascending = False).head(m).plot(kind = 'barh', linewidth=3, color = '#FF9933').invert_yaxis()
    plt.title("Inversión Total ($M) por Industria")
    plt.ylabel('')
    fig
with row73:
    st.markdown('Como se puede observar, las **industrias más relevantes son Customer Internet y eCommerce**. La diferencia entre consumer internet y ecommerce radica en el tipo de servicios o productos que ofrecen. **Consumer internet** se refiere a la industria de internet que ofrece servicios directamente a los consumidores, como **aplicaciones de mensajería, redes sociales, juegos en línea y otros servicios en línea**. Por otro lado, **eCommerce** se refiere a la industria de comercio electrónico, que se enfoca en la **venta de productos a través de internet**. Las empresas de eCommerce suelen ofrecer una amplia gama de productos a través de sus sitios web o aplicaciones móviles, y permiten a los consumidores comprar y recibir productos en línea.')

st.markdown('### Empresas más relevantes de cada sector')

row_spacer81, row81, row_spacer82 = st.columns((.5, 3.5, .5))
with row81:
    industry = st.selectbox(
    'Industrias:',
    ('Consumer Internet', 'Technology', 'eCommerce', 'Finance', 'Healthcare',
        'Logistics', 'Education', 'Food & Beverage', 'Ed-Tech', 'IT',
        'Transport', 'Health and Wellness', 'Social Media', 'Others'))
    fig = plt.figure(figsize=(10, 3), dpi=200)
    df.loc[df['Industry'] == industry].groupby('Startup Name').sum()['Amount in USD'].sort_values(ascending = False).head(8).plot(kind = 'bar', color = '#FF9933')
    plt.title('Empresas con mayor inversión ($M) en el sector %s' % industry)
    plt.xticks(rotation = 30)
    plt.ylabel('')
    plt.xlabel('')
    fig

row_spacer91, row91, row_spacer92 = st.columns((.1, 3.2, .1))
with row91:
    st.markdown('## Análisis geográfico de las inversiones')

row101, row102, row103 = st.columns(3)
with row101:
    fig = plt.figure(figsize=(4, 5), dpi=200)
    df['City  Location'].value_counts().sort_values(ascending = False).head(5).plot(kind = 'barh', linewidth=3, color = '#FF9933').invert_yaxis()
    plt.title("Ciudades con más Startups fundadas")
    plt.ylabel('')
    fig
with row102:
    st.image('https://i.pinimg.com/originals/15/5f/2a/155f2aab9cf295fa4ed5e96f20f1431e.jpg')
with row103:
    st.markdown('**Bangalore** es una ciudad importante en India debido a su papel como **centro tecnológico** y de la industria de la **tecnología de la información**. La ciudad es conocida como la "capital de la tecnología de la información" de India y cuenta con una **amplia presencia de empresas de tecnología y startups**. Además, Bangalore es un importante **centro de investigación y desarrollo** y cuenta con una gran cantidad de **universidades y centros de investigación de renombre**. Estas características han atraído a un gran número de trabajadores calificados y empresas de tecnología, lo que ha contribuido al crecimiento y desarrollo de la ciudad.')
    st.markdown('Por otra parte, **Mumbai** es la **ciudad más grande y poblada de India** y es un importante **centro financiero y comercial** y **Nueva Delhi** es la **capital de India**, así como un importante **centro de negocios y comercio**.')

row_spacer101, row104, row_spacer102 = st.columns((.5, 3.5, .5))
with row104:
    st.video('https://www.youtube.com/watch?v=3S5-GaldDpk&ab_channel=MostAmazingKlips')

row_spacer111, row111, row_spacer112 = st.columns((.1, 3.2, .1))
with row111:
    st.markdown('## ¿Quiénes son los inversores más importantes?')
    st.markdown('Como se puede observar, lo más común es que la financiación provenga de **undisclosed investors**, es decir, **inversores que no se identifican públicamente**. En el contexto de las inversiones en startups, los undisclosed investors suelen ser inversores individuales o fondos de inversión que invierten en una empresa en sus etapas tempranas, pero no desean hacer pública su inversión. Estos inversores pueden preferir mantener su identidad en privado por diferentes razones, como la protección de su privacidad, la evitación de competencia o la no exposición a la presión de los mercados financieros. Aunque los undisclosed investors no se identifican públicamente, su inversión puede ser importante para la empresa en la que invierten y puede contribuir al crecimiento y desarrollo de la misma.')
    st.markdown('Por otra parte, en relación a los inversores con más capital invertido destaca **WestBridge Capital**, la **mayor empresa de capital de riesgo de India**. La empresa se dedica a invertir en empresas en sus etapas tempranas y ayudarlas a crecer y desarrollarse. WestBridge Capital ha invertido en una amplia gama de empresas en diferentes sectores, como tecnología, consumo, salud y finanzas. La empresa ha tenido un gran éxito en el mercado indio y ha ayudado a muchas empresas a crecer y desarrollarse, participando en muchas de las principales rondas de financiamiento en el país.')

row_spacer121, row121, row_spacer122, row122, row_spacer123 = st.columns((.1, 2.7, .1, 3.2, .1))
with row121:    
    fig = plt.figure(figsize=(4, 5), dpi=200)
    df['Investors'].value_counts().sort_values(ascending = False).head(10).plot(kind = 'barh', linewidth=3, color = '#FF9933').invert_yaxis()
    plt.title("Fuentes de inversión más comunes")
    plt.ylabel('')
    fig
with row122:
    fig = plt.figure(figsize=(4, 5), dpi=200)
    df.groupby('Investors').sum()['Amount in USD'].sort_values(ascending = False).head(10).plot(kind = 'barh', linewidth=3, color = '#FF9933').invert_yaxis()
    plt.title("Inversores con más capital invertido ($M)")
    plt.ylabel('')
    fig

row_spacer131, row131, row_spacer132 = st.columns((.1, 3.2, .1))
with row131:
    st.markdown('## Estado de financiación y desarrollo')
    st.markdown('El **estado de financiación** de una startup es una medida del financiamiento que ha recibido la empresa a través de diferentes rondas de inversión. Puede ser una **indicación del éxito y la viabilidad de la empresa**, ya que refleja el interés de los inversores en su idea o producto, así como un **indicador de su crecimiento y desarrollo**, ya que el capital recibido puede ser utilizado para expandirse y desarrollarse. Por lo tanto, el estado de financiación de una startup puede ser una medida importante para los inversores y otros interesados en la empresa.')
    
    fig = plt.figure(figsize=(10, 3), dpi=200)
    df['Investment Type'].value_counts().sort_values(ascending = False).head(9).plot(kind = 'barh', linewidth=3, color = '#FF9933').invert_yaxis()
    plt.title('Tipos de inversión más comunes')
    plt.ylabel('')
    fig

    st.markdown("### ¿Qué significa...?")
    with st.expander("Seed / Angel Funding"):
        st.write("""
            Seed funding y angel funding son dos tipos de financiación que reciben las startups en sus **etapas tempranas de desarrollo**, con el objetivo de desarrollar su idea o producto.\n
            El **seed funding** suele provenir de **incubadoras o aceleradoras**, y suele ser una cantidad relativamente pequeña de financiamiento.\n
            El **angel funding** suele provenir de **inversores individuales**, que suelen ser **empresarios o profesionales experimentados** que invierten su propio dinero en empresas en las que creen.\n
            Aunque seed funding y angel funding son diferentes tipos de financiamiento, ambos pueden ser importantes para las startups en sus etapas tempranas de desarrollo y pueden ayudarlas a crecer y desarrollarse.
        """)
    with st.expander("Private Equity"):
        st.write("""
            El **private equity** es un tipo de inversión en el que un inversor adquiere una participación en una empresa no cotizada en bolsa. Las inversiones en private equity suelen realizarse en empresas en sus etapas tempranas o en crecimiento, con el objetivo de ayudar a la empresa a crecer y desarrollarse. En el contexto de las inversiones en startups, el private equity suele referirse a la adquisición de una participación en una empresa en sus etapas tempranas de desarrollo con el fin de ayudarla a crecer y desarrollarse. Las inversiones en private equity pueden ser una forma atractiva para los inversores ya que pueden ofrecer un potencial de rentabilidad elevado, pero también pueden conllevar riesgos significativos debido a la naturaleza incierta de las empresas en sus etapas tempranas.        
        """)
    with st.expander("Debt Funding"):
        st.write("""
            El **debt funding** es un tipo de financiamiento en el que una empresa recibe un **préstamo de un inversor** y se compromete a devolver el préstamo **con intereses en un plazo determinado**. En el contexto de las startups, el debt funding puede ser una forma atractiva de obtener financiamiento ya que **no requiere la dilución del accionariado y permite a la empresa mantener el control sobre su negocio**. Sin embargo, el debt funding también **puede conllevar riesgos**, ya que la empresa está obligada a devolver el préstamo y puede enfrentar dificultades si no es capaz de generar suficientes ingresos para hacer frente a sus obligaciones de pago. Por lo tanto, el debt funding puede ser una opción viable para algunas startups, pero es importante evaluar cuidadosamente los riesgos y beneficios antes de tomar una decisión.
        """)
    with st.expander("Pre-Series A / Series A"):
        st.write("""
            La etapa **pre-series A** suele ser la **primera ronda de financiamiento significativa después del seed funding** y suele ser utilizada por las empresas para **desarrollar su idea o producto y demostrar su viabilidad**. La etapa pre-series A suele involucrar a inversores individuales o pequeños fondos de inversión que invierten en la empresa en sus primeras etapas de crecimiento.\n 
            La etapa **series A**, por otro lado, suele ser la siguiente ronda de financiamiento después de la pre-series A y suele ser utilizada por las empresas para **expandirse y desarrollarse**. La etapa series A suele involucrar a **inversores más grandes**, como **fondos de capital de riesgo o inversores institucionales**, que invierten una cantidad significativa de financiamiento en la empresa.
        """)
    with st.expander("Series B"):
        st.write("""
            La etapa **series B** suele ser la siguiente ronda de financiamiento después de la etapa series A y suele ser utilizada por las empresas que **ya han demostrado su viabilidad** y necesitan **financiamiento adicional para seguir creciendo y desarrollándose**. Al igual que series A, la etapa series B suele involucrar a **inversores más grandes**, como **fondos de capital de riesgo o inversores institucionales**, que invierten una cantidad significativa de financiamiento en la empresa. La etapa series B suele ser una **etapa crucial en el ciclo de vida de una startup** ya que el financiamiento recibido en esta etapa puede ser decisivo para el crecimiento y desarrollo de la empresa. Sin embargo, la etapa series B también **puede conllevar riesgos, ya que los inversores suelen esperar un retorno significativo en su inversión** y la empresa puede enfrentarse a presiones para generar ingresos y crecer rápidamente. Por lo tanto, la etapa series B puede ser un desafío para las startups, pero también puede ser una oportunidad para acelerar su crecimiento y desarrollo.
        """)
    with st.expander("Series C"):
        st.write("""
            La etapa **series C** suele ser la siguiente ronda de financiamiento después de la etapa series B y suele ser utilizada por las empresas que **han demostrado un crecimiento significativo** y necesitan **financiamiento adicional para seguir expandiéndose y desarrollándose**. La etapa series C suele involucrar a **inversores más grandes que las etapas anteriores**, ya que ya **se ha alcanzado un mayor nivel de crecimiento**. Por lo tanto, la principal diferencia entre series B y C en financiación de startups es el momento en el ciclo de vida de la empresa en el que se realizan y el tamaño y tipo de inversores que participan en cada etapa.
        """)
    with st.expander("Series D / E"):
        st.write("""
            La etapa **series D** suele ser utilizada por las empresas que ya **han demostrado un crecimiento sostenido** y **necesitan financiamiento adicional para seguir expandiéndose y desarrollándose**.\n 
            Finalmente, la etapa **series E** suele ser la **última ronda de financiamiento en el ciclo de vida de una startup** y suele ser utilizada por las empresas que **han demostrado un éxito significativo**.\n
            Estas etapas suelen involucrar a **inversores mucho más grandes, como fondos de capital de riesgo o inversores institucionales**, que invierten una cantidad significativa de financiamiento en la empresa. 
        """)

row_spacer141, row141, row_spacer142 = st.columns((.1, 3.2, .1))
with row141:
    st.markdown('## Conclusiones finales')
    st.markdown('En conclusión, **la inversión en startups indias ha experimentado un crecimiento significativo en los últimos años**. La creciente cantidad de financiamiento recibido por las startups indias ha permitido a muchas de estas empresas desarrollarse y crecer, lo que ha contribuido al **dinamismo de la economía india**. Los inversores han mostrado un interés creciente en las startups indias debido a su **potencial de crecimiento** y al **interés en la innovación y la tecnología en el país**. Además, las políticas **gubernamentales favorables** a las startups y el creciente apoyo del sector privado han contribuido a impulsar el crecimiento de estas empresas. En pocas palabras, la inversión en startups indias sigue siendo una opción atractiva para los inversores y se espera que continúe creciendo en el futuro.')