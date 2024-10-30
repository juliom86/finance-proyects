import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px

# Título de la aplicación
st.title('Stock Dashboard')

# CEDEARs clasificados por países
cedears_usa = [
    "AAPL", "AMZN", "GOOGL", "MSFT", "META", "TSLA", "NFLX", "BA", "GE", "C", "KO",
    "JPM", "MRNA", "PFE", "MCD", "IBM"
]

cedears_brazil = [
    "ABEV", "AMX", "ARCO", "BAK", "BBD", "BBAS3.SA", "BSBR", "BRFS", "ERJ", "GGB",
    "LND", "PRIO3.SA", "SID", "SBS", "SUZ", "VALE"
]

cedears_china = [
    "BABA", "JD", "TCEHY", "BIDU", "PDD", "NIO", "XPEV", "LI"
]

cedears_uk = ["HSBC", "UL", "BP", "AZN", "RIO"]

cedears_germany = ["BAYRY", "DDAIF", "SAP"]

cedears_japan = ["SONY", "HMC", "TM", "NTDOY"]

cedears_other = ["DEO", "TOT", "VEON", "TEF"]

# ADR Argentinos (Anteriormente Acciones Argentinas)
adr_argentinos_tickers = [
    "YPF", "GGAL", "BMA", "BBAR", "CEPU", "CRESY", "EDN", "IRS", "LOMA", "PAM",
    "SUPV", "TEO", "TS", "TGS"
]

# Acciones Argentinas correctas (BA tickers)
acciones_argentinas_tickers = [
    "AGRO.BA", "ALUA.BA", "AUSO.BA", "BBAR.BA", "BHIP.BA", "BMA.BA", "BOLT.BA", "BPAT.BA", "BYMA.BA", 
    "CADO.BA", "CAPX.BA", "CECO2.BA", "CELU.BA", "CEPU.BA", "CGPA2.BA", "COME.BA", "CRES.BA", "CTIO.BA", 
    "CVH.BA", "DGCU2.BA", "DYCA.BA", "EDN.BA", "FERR.BA", "FIPL.BA", "GAMI.BA", "GARO.BA", "GBAN.BA", 
    "GCDI.BA", "GGAL.BA", "GCLA.BA", "HARG.BA", "HAVA.BA", "INTR.BA", "INVJ.BA", "IRSA.BA", "LEDE.BA", 
    "LOMA.BA", "METR.BA", "MIRG.BA", "MOLI.BA", "MORI.BA", "MTR.BA", "OEST.BA", "PAMP.BA", "PATA.BA", 
    "SAMI.BA", "SEMI.BA", "SUPV.BA", "TECO2.BA", "TGNO4.BA", "TGSU2.BA", "TRAN.BA", "TXAR.BA", "VALO.BA", 
    "YPFD.BA"
]

# Agregar Bonos Argentinos
bonos_argentinos_tickers = [
    "GD29", "GD30", "GD38", "GD46", "GD35", "GD41"
]

# Commodities y Forex
commodities_tickers = [
    "GC=F",  # Oro
    "CL=F",  # Petróleo Crudo WTI
    "SI=F",  # Plata
    "NG=F",  # Gas Natural
    "HG=F",  # Cobre
    "ZC=F",  # Maíz
    "ZS=F",  # Soja
    "KE=F"   # Trigo
]

forex_tickers = [
    "EURUSD=X", "JPY=X", "GBPUSD=X", "AUDUSD=X", "USDCAD=X",
    "USDARS=X", "USDCHF=X", "USDCNY=X", "USDMXN=X", "USDCLP=X"
]

# LECAPS Tickers
lecaps_tickers = ['S31O4', 'S11NA', 'S29N4']  # Puedes agregar más LECAPS aquí

# Inputs interactivos en la barra lateral con pestañas para tickers predefinidos y manual
tabs = st.sidebar.tabs([
    "Commodities", "Forex", "STOCKS", "Bonos Argentinos", "LECAPS"
])

# Inicializar variable para almacenar tickers seleccionados
selected_tickers = []
selected_lecaps = []

# Pestaña Commodities
with tabs[0]:
    selected_commodities = st.multiselect('Selecciona Commodities', commodities_tickers)
    selected_tickers.extend(selected_commodities)

# Pestaña Forex
with tabs[1]:
    selected_forex = st.multiselect('Selecciona Forex', forex_tickers)
    selected_tickers.extend(selected_forex)

# Pestaña STOCKS con subpestañas anidadas
with tabs[2]:
    sub_tabs = st.tabs([
        "CEDEARs (USA)", "CEDEARs (Brasil)", "CEDEARs (China)", "CEDEARs (Reino Unido)",
        "CEDEARs (Alemania)", "CEDEARs (Japón)", "CEDEARs (Otros)", "ADR Argentinos", "Acciones Argentinas"
    ])
    
    # Pestaña CEDEARs USA
    with sub_tabs[0]:
        selected_cedears_usa = st.multiselect('Selecciona CEDEARs (USA)', cedears_usa)
        selected_tickers.extend(selected_cedears_usa)

    # Pestaña CEDEARs Brasil
    with sub_tabs[1]:
        selected_cedears_brazil = st.multiselect('Selecciona CEDEARs (Brasil)', cedears_brazil)
        selected_tickers.extend(selected_cedears_brazil)

    # Pestaña CEDEARs China
    with sub_tabs[2]:
        selected_cedears_china = st.multiselect('Selecciona CEDEARs (China)', cedears_china)
        selected_tickers.extend(selected_cedears_china)

    # Pestaña CEDEARs Reino Unido
    with sub_tabs[3]:
        selected_cedears_uk = st.multiselect('Selecciona CEDEARs (Reino Unido)', cedears_uk)
        selected_tickers.extend(selected_cedears_uk)

    # Pestaña CEDEARs Alemania
    with sub_tabs[4]:
        selected_cedears_germany = st.multiselect('Selecciona CEDEARs (Alemania)', cedears_germany)
        selected_tickers.extend(selected_cedears_germany)

    # Pestaña CEDEARs Japón
    with sub_tabs[5]:
        selected_cedears_japan = st.multiselect('Selecciona CEDEARs (Japón)', cedears_japan)
        selected_tickers.extend(selected_cedears_japan)

    # Pestaña CEDEARs Otros
    with sub_tabs[6]:
        selected_cedears_other = st.multiselect('Selecciona CEDEARs (Otros países)', cedears_other)
        selected_tickers.extend(selected_cedears_other)

    # Pestaña ADR Argentinos
    with sub_tabs[7]:
        selected_adr_argentinos = st.multiselect('Selecciona ADR Argentinos', adr_argentinos_tickers)
        selected_tickers.extend(selected_adr_argentinos)

    # Pestaña Acciones Argentinas
    with sub_tabs[8]:
        selected_acciones_argentinas = st.multiselect('Selecciona Acciones Argentinas', acciones_argentinas_tickers)
        selected_tickers.extend(selected_acciones_argentinas)

# Pestaña Bonos Argentinos
with tabs[3]:
    selected_bonos_argentinos = st.multiselect('Selecciona Bonos Argentinos', bonos_argentinos_tickers)
    selected_tickers.extend(selected_bonos_argentinos)

# Pestaña LECAPS
with tabs[4]:
    selected_lecaps = st.multiselect('Selecciona LECAPS', lecaps_tickers)

# Mostrar los tickers seleccionados
st.write(f"Tickers seleccionados: {', '.join(selected_tickers + selected_lecaps)}")

# Datos de Bonos Hardcodeados (extraídos de la imagen)
bonos_data = {
    "Ticker": ["GD29", "GD30", "GD38", "GD46", "GD35", "GD41"],
    "Price": [69.21, 64.63, 57.21, 55.18, 53.21, 49.31],
    "%1D": ["+0.37%", "+0.41%", "+0.43%", "+0.47%", "+0.49%", "+0.36%"],
    "%MTD": ["+6.01%", "+6.42%", "+8.68%", "+8.94%", "+10.52%", "+7.90%"],
    "%YTD": ["+73.15%", "+60.60%", "+44.15%", "+58.97%", "+55.68%", "+44.07%"],
    "Yield": [17.99, 18.01, 14.81, 13.65, 14.38, 14.17],
    "OAS": [1406, 1410, 1081, 953, 1037, 1011],
    "Dur": [1.91, 2.23, 4.93, 5.20, 5.83, 5.98]
}

# Crear DataFrame de los bonos seleccionados
if selected_bonos_argentinos:
    bonos_df = pd.DataFrame(bonos_data)
    bonos_df = bonos_df[bonos_df['Ticker'].isin(selected_bonos_argentinos)]
    
    if not bonos_df.empty:
        st.subheader('Datos de Bonos Seleccionados')
        st.dataframe(bonos_df)

        # Gráfico de Precios vs Yield
        st.subheader('Gráfico de Precios vs Yield')
        fig = px.scatter(bonos_df, x="Price", y="Yield", text="Ticker", title="Precios vs Rendimiento (Yield)")
        st.plotly_chart(fig)

        # Gráfico de Yield vs Duración
        st.subheader('Gráfico de Yield vs Duración')
        fig2 = px.scatter(bonos_df, x="Dur", y="Yield", text="Ticker", title="Rendimiento (Yield) vs Duración")
        st.plotly_chart(fig2)

# Función para descargar datos históricos
@st.cache_data
def download_data(tickers, start, end):
    return yf.download(tickers, start=start, end=end)

# Función para obtener datos fundamentales
@st.cache_data
def get_fundamentals(ticker):
    ticker_obj = yf.Ticker(ticker)
    return ticker_obj.info

# Inputs de fecha
start_date = st.sidebar.date_input('Fecha de inicio', value=pd.to_datetime("2019-01-01"))
end_date = st.sidebar.date_input('Fecha de fin', value=pd.to_datetime("2023-12-31"))

if selected_tickers or selected_lecaps:
    # Descargar datos históricos para todos los tickers seleccionados (excluyendo LECAPS)
    if selected_tickers:
        data = download_data(selected_tickers, start_date, end_date)
    else:
        data = pd.DataFrame()

    # Procesar datos de LECAPS
    if selected_lecaps:
        # Datos de ejemplo de LECAPS
        lecaps_data = {
            'LECAPS': ['S31O4', 'S11NA', 'S29N4'],
            'Precio': [102.81, 106.76, 129.32],
            'Fecha de VTO': ['2024-10-31', '2024-11-20', '2024-11-29'],
            'Pago Final': [100, 100, 100]
        }

        # Crear DataFrame
        lecaps_df = pd.DataFrame(lecaps_data)

        # Filtrar solo las LECAPS seleccionadas
        lecaps_df = lecaps_df[lecaps_df['LECAPS'].isin(selected_lecaps)].reset_index(drop=True)

        # Convertir 'Fecha de VTO' a tipo datetime
        lecaps_df['Fecha de VTO'] = pd.to_datetime(lecaps_df['Fecha de VTO'])

        # Calcular 'Días restantes' desde la fecha actual
        lecaps_df['Días restantes'] = (lecaps_df['Fecha de VTO'] - pd.Timestamp.today()).dt.days

        # Calcular 'Rendimiento al Vencimiento (%)' usando la fórmula de TIR
        lecaps_df['Rendimiento al Vencimiento (%)'] = ((lecaps_df['Pago Final'] / lecaps_df['Precio']) ** (365 / lecaps_df['Días restantes']) - 1) * 100

        # Formatear los porcentajes
        lecaps_df['Rendimiento al Vencimiento (%)'] = lecaps_df['Rendimiento al Vencimiento (%)'].map('{:.3f}%'.format)
    else:
        lecaps_df = pd.DataFrame()

    # Verificar si se obtuvieron datos
    if not data.empty or not lecaps_df.empty:
        # Procesar datos de los tickers (excluyendo LECAPS)
        if not data.empty:
            # Si data tiene columnas multinivel, ajustar
            if isinstance(data.columns, pd.MultiIndex):
                # Usar 'Adj Close' para el análisis
                adj_close = data['Adj Close']
            else:
                adj_close = data['Adj Close'].to_frame()

            # Crear tabla comparativa de precios
            latest_prices = adj_close.iloc[-1]

            # Definir períodos para calcular cambios porcentuales
            periods = {
                '1 Día': 1,
                '4 Días': 4,
                '1 Semana': 5,
                '1 Mes': 21,
                '1 Año': 252,
                '4 Años': 1008
            }

            price_changes = {}
            for period_name, period_days in periods.items():
                if len(adj_close) > period_days:
                    pct_change = adj_close.pct_change(periods=period_days).iloc[-1] * 100
                    price_changes[period_name] = pct_change
                else:
                    price_changes[period_name] = pd.Series([0]*len(adj_close.columns), index=adj_close.columns)

            # Crear DataFrame de cambios porcentuales
            price_comparison_df = pd.DataFrame({
                'Ticker': latest_prices.index,
                'Último Precio': latest_prices.values
            })

            for period_name, changes in price_changes.items():
                price_comparison_df[f'Cambio % {period_name}'] = changes.values

            # Mostrar tabla comparativa de precios
            st.subheader('Tabla Comparativa de Precios')
            st.dataframe(
                price_comparison_df.style.format({
                    'Último Precio': '{:.2f}',
                    **{f'Cambio % {period_name}': '{:.2f}%' for period_name in periods.keys()}
                })
            )

            # Obtener datos fundamentales para todos los tickers
            fundamental_list = []
            for ticker in selected_tickers:
                try:
                    fundamentals = get_fundamentals(ticker)
                    data_fund = {
                        'Ticker': ticker,
                        'Nombre Corto': fundamentals.get('shortName', 'N/A'),
                        'Sector': fundamentals.get('sector', 'N/A'),
                        'Industria': fundamentals.get('industry', 'N/A'),
                        'Capitalización de Mercado': fundamentals.get('marketCap', 0),
                        'Beta': fundamentals.get('beta', 0),
                        'PE Trailing': fundamentals.get('trailingPE', 0),
                        'PE Forward': fundamentals.get('forwardPE', 0),
                        'EPS Trailing': fundamentals.get('trailingEps', 0),
                        'EPS Forward': fundamentals.get('forwardEps', 0),
                        'Rendimiento de Dividendo': fundamentals.get('dividendYield', 0),
                        'Precio a Valor en Libros': fundamentals.get('priceToBook', 0),
                        'EBITDA': fundamentals.get('ebitda', 0),
                        'Margen de Beneficio': fundamentals.get('profitMargins', 0),
                        'ROE': fundamentals.get('returnOnEquity', 0),
                        'Cash Disponible': fundamentals.get('totalCash', 0),
                        'Deuda Total': fundamentals.get('totalDebt', 0),
                        'Current Ratio': fundamentals.get('currentRatio', 0),
                        'Quick Ratio': fundamentals.get('quickRatio', 0),
                    }
                    fundamental_list.append(data_fund)
                except Exception as e:
                    st.write(f"Error al obtener datos fundamentales para {ticker}: {e}")
                    # Agregar datos vacíos si hay error
                    data_fund = {'Ticker': ticker}
                    for key in ['Nombre Corto', 'Sector', 'Industria', 'Capitalización de Mercado', 'Beta', 'PE Trailing',
                                'PE Forward', 'EPS Trailing', 'EPS Forward', 'Rendimiento de Dividendo',
                                'Precio a Valor en Libros', 'EBITDA', 'Margen de Beneficio', 'ROE', 'Cash Disponible',
                                'Deuda Total', 'Current Ratio', 'Quick Ratio']:
                        data_fund[key] = 0
                    fundamental_list.append(data_fund)

            # Crear DataFrame de datos fundamentales
            fundamentals_df = pd.DataFrame(fundamental_list)

            # Mostrar tabla comparativa de datos fundamentales
            st.subheader('Tabla Comparativa de Datos Fundamentales')
            st.dataframe(fundamentals_df)

            # Gráficos comparativos
            st.subheader('Gráficos Comparativos de Precios')

            # **Gráfico de precios ajustados con línea de promedio**
            fig = px.line(adj_close, x=adj_close.index, y=adj_close.columns,
                          labels={'value': 'Precio Ajustado', 'variable': 'Ticker'},
                          title='Comparación de Precios Ajustados')

            # Calcular promedios de precios para cada ticker
            averages = adj_close.mean()

            # Agregar líneas horizontales de promedio para cada ticker
            for ticker in adj_close.columns:
                mean_price = averages[ticker]
                fig.add_hline(y=mean_price, line_dash="dash", line_color='gray',
                              annotation_text=f"Promedio {ticker}: {mean_price:.2f}",
                              annotation_position="top left")

            st.plotly_chart(fig)

            # Gráfico de retornos acumulados
            returns = adj_close.pct_change().dropna()
            cumulative_returns = (1 + returns).cumprod()
            fig2 = px.line(cumulative_returns, x=cumulative_returns.index, y=cumulative_returns.columns,
                           labels={'value': 'Retorno Acumulado', 'variable': 'Ticker'},
                           title='Comparación de Retornos Acumulados')
            st.plotly_chart(fig2)

            # Correlaciones entre los retornos de los tickers
            st.subheader('Mapa de Calor de Correlación de Retornos')
            corr = returns.corr()
            fig4 = px.imshow(corr, text_auto=True, aspect="auto", title='Correlación entre Retornos de Tickers')
            st.plotly_chart(fig4)
        else:
            st.write("No se encontraron datos para los tickers seleccionados en el rango de fechas proporcionado.")

        # Mostrar datos de LECAPS si hay
        if not lecaps_df.empty:
            st.subheader('Información sobre LECAPS')

            # Mostrar la tabla de LECAPS
            st.dataframe(lecaps_df)

            # Gráfico de Rendimiento al Vencimiento vs Días Restantes
            st.subheader('Rendimiento al Vencimiento de LECAPS')
            fig_lecaps = px.scatter(
                lecaps_df,
                x='Días restantes',
                y=lecaps_df['Rendimiento al Vencimiento (%)'].str.rstrip('%').astype(float),
                hover_name='LECAPS',  # Esto añade el nombre de la LECAP al pasar el cursor
                text='LECAPS',        # Esto añade las etiquetas de las LECAPS en el gráfico
                hover_data=['Precio', 'Fecha de VTO'],  # Información adicional en el hover
                title='Rendimiento al Vencimiento vs Días Restantes',
                labels={'Días restantes': 'Días Restantes', 'y': 'Rendimiento al Vencimiento (%)'}
            )
            
            # Asegurarse de que las etiquetas no se superpongan
            fig_lecaps.update_traces(textposition='top center')
            
            st.plotly_chart(fig_lecaps)

    else:
        st.write("No se encontraron datos para los instrumentos seleccionados.")
else:
    st.write("No se seleccionaron tickers ni LECAPS.")
