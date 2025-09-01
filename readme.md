# Conociendo al Cliente 360°

## Descripción del Proyecto

**"Conociendo al Cliente 360°"** es un proyecto integrador del primer módulo del bootcamp de Data Science de Henry. Desarrollado para InsightReach, empresa ficticia de marketing digital especializada en campañas personalizadas. El objetivo es analizar el ecosistema gastronómico de Chicago combinando datos de usuarios y restaurantes para generar insights estratégicos.

## Objetivos del Proyecto

- **Análisis de usuarios**: Limpieza y segmentación de base de datos de clientes
- **Integración de datos externos**: Obtención de información de restaurantes via API de Yelp
- **Sistema de recomendaciones**: Desarrollo de modelos predictivos para matching usuario-restaurante
- **Insights estratégicos**: Generación de recomendaciones para campañas de marketing digital

## 🏗️ Estructura del Proyecto

### Notebooks Principales
- `Avance_EDA.ipynb` - Análisis Exploratorio y limpieza de datos
- `Avance_API_YELP.ipynb` - Consumo de API de Yelp y procesamiento
- `Avance_Analisis_Final.ipynb` - Análisis final y recomendaciones

### Scripts Auxiliares
- `mega_funcion.py` - Funciones de apoyo (usado en Avance_EDA)

### Datasets

**Input:**
- `base_datos_restaurantes_USA_v2.csv` - Dataset inicial proporcionado

**Output (Auto-generados):**
- `usuarios_limpios.csv` - Dataset limpio (Avance_EDA)
- `Datos_usuarios_Chicago_limpios.csv` - Datos por ciudad (Avance_EDA)
- `chicago_restaurants.csv` - Datos crudos de API (Avance_API_YELP)
- `Datos_YELP_limpios.csv` - Datos limpios de API (Avance_API_YELP)

### Configuración y Documentación
- `README.md` - Documentación del proyecto
- `requirements.txt` - Dependencias Python
- `Recomendaciones.pdf` - Insights y recomendaciones estratégicas finales

## Instalación y Configuración

### Requisitos Previos
Para ejecutar este proyecto necesitas tener instalado:
- Python 3.7+
- Jupyter Notebook (para ejecutar los archivos .ipynb)

### 🔑 Configuración de API Key de Yelp

**⚠️ IMPORTANTE:** Para ejecutar el `Avance_API_YELP.ipynb` necesitas una API Key de Yelp.

#### Opción 1: Con API Key Propia (RECOMENDADO)
1. Obtén tu API Key gratuita en: [Yelp for Developers](https://www.yelp.com/developers/v3/manage_app)
2. En el notebook `Avance_API_YELP.ipynb`, reemplaza la variable `API_KEY` con tu clave personal
3. **ELIMINA** el archivo `chicago_restaurants.csv` (datos de prueba) para forzar la obtención de datos frescos

#### Opción 2: Sin API Key (Datos de Prueba)
Si no cuentas con una API Key, se incluye el archivo `chicago_restaurants.csv` con datos pre-obtenidos para que puedas continuar con el flujo del proyecto. Sin embargo, estos datos podrían estar desactualizados.

**⚠️ IMPORTANTE:** Si usas los datos de prueba, debes **OMITIR la sección de conexión a la API** en el notebook `Avance_API_YELP.ipynb` para evitar errores. Ve directamente a la sección de procesamiento de datos.

### Instalación de Dependencias
```bash
pip install -r requirements.txt
```

### Librerías Principales Utilizadas
- **pandas**: Manipulación y análisis de datos
- **numpy**: Operaciones numéricas
- **matplotlib/seaborn**: Visualización de datos
- **fuzzywuzzy**: Análisis de similitud de strings
- **requests**: Consumo de API de Yelp
- **jupyter**: Ejecución de notebooks
- Otras dependencias específicas listadas en `requirements.txt`

## ⚙️ Cómo Ejecutar el Proyecto

### Paso Previo: Instalación de Dependencias
```bash
pip install -r requirements.txt
```

### Ejecución Secuencial (Recomendada)

**Paso 1: Avance EDA**
```bash
jupyter notebook Avance_EDA.ipynb
```
- **Entrada:** `base_datos_restaurantes_USA_v2.csv`
- **Salida:** `usuarios_limpios.csv`, `Datos_usuarios_Chicago_limpios.csv`

**Paso 2: Avance API YELP**
```bash
jupyter notebook Avance_API_YELP.ipynb
```
- **Configuración requerida:** API Key de Yelp (ver sección de configuración)
- **Entrada:** API de Yelp
- **Salida:** `chicago_restaurants.csv`, `Datos_YELP_limpios.csv`

> 🔑 **Nota sobre API Key:** Si tienes tu propia API Key de Yelp, asegúrate de eliminar el archivo `chicago_restaurants.csv` antes de ejecutar este notebook para obtener datos actualizados directamente de la API.

> ⚠️ **Sin API Key:** Si no tienes API Key, omite las celdas de conexión a la API y usa directamente el archivo `chicago_restaurants.csv` incluido.

**Paso 3: Avance Análisis Final**
```bash
jupyter notebook Avance_Analisis_Final.ipynb
```
- **Entrada:** Datasets procesados de Avance EDA y API YELP
- **Salida:** Análisis, visualizaciones y `Recomendaciones.pdf`

### Ejecución Individual
Cada notebook puede ejecutarse independientemente si ya tienes los archivos de entrada correspondientes.

> ⚠️ **Importante:** Asegúrate de instalar las dependencias antes de ejecutar cualquier notebook para evitar errores de importación.

## Resultados por Avance

### Avance EDA: Análisis Exploratorio de Usuarios
**Dataset procesado:** 30,000 → +28,000 registros limpios

✅ Valores nulos imputados inteligentemente por ciudad y estrato  
✅ Rangos de edad normalizados (18-90 años)  
✅ Tipos de datos estandarizados  
✅ Ciudad foco seleccionada: Chicago  

**Archivos generados:**
- `usuarios_limpios.csv` - Dataset completo limpio
- `Datos_usuarios_Chicago_limpios.csv` - Solo usuarios de Chicago

### Avance API YELP: Datos de Restaurantes
**Dataset obtenido:** 199 restaurantes de Chicago

✅ Conexión exitosa a API de Yelp  
✅ Análisis de similitud con FuzzyWuzzy (>70%)  
✅ Imputación contextual de precios por categoría  
✅ Estructuras JSON normalizadas  

**Archivos generados:**
- `chicago_restaurants.csv` - Datos crudos de la API
- `Datos_YELP_limpios.csv` - Dataset procesado y limpio

### Avance Análisis Final: Sistema de Recomendaciones

Integración de datasets de usuarios y restaurantes  
Sistema de recomendaciones personalizado  
Desarrollo de visualizaciones para análisis  

### Documento Final: Recomendaciones Estratégicas
**Archivo generado:** `Recomendaciones.pdf`

✅ Insights más valiosos identificados  
✅ Recomendaciones estratégicas para InsightReach  
✅ Conclusiones basadas en análisis integral  
✅ Propuestas para campañas de marketing dirigidas  

## Características Técnicas Destacadas

### Metodologías Innovadoras
- **Imputación Contextual**: Valores faltantes por ciudad + estrato socioeconómico
- **Análisis de Similitud**: FuzzyWuzzy para consolidación de datos redundantes
- **Pipeline ETL Robusto**: Procesamiento escalable y reproducible
- **Validación Cruzada**: Múltiples métricas de calidad de datos

### Calidad de Datos Lograda
- **Completitud**: 100% en variables críticas
- **Consistencia**: Tipos de datos estandarizados
- **Precisión**: >95% en matching de entidades
- **Validez**: Rangos realistas en todas las variables

## Próximos Desarrollos

- **Modelos de ML**: Random Forest, Clustering, Sistemas de recomendación
- **Dashboard Interactivo**: Visualización de insights en tiempo real
- **API de Recomendaciones**: Servicio REST para recomendaciones
- **A/B Testing Framework**: Validación de recomendaciones

## Soporte y Contacto

**Desarrollador Principal:** María Fernanda Yañez Zavala  
**Email:** feryaza1707@gmail.com  
**LinkedIn:** [María Fernanda Yañez Zavala](https://www.linkedin.com/in/maria-fernanda-ya%C3%B1ez-zavala-410484280/)

## Licencia

Este proyecto se desarrolla con fines académicos para InsightReach.

---
**Última actualización:** Agosto 2025