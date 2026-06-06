# Análisis de Ventas de una Pequeña Empresa

## Integrantes y roles

- P1 - Hugo: líder y organizador del repositorio.
- P2 - Paco: desarrollador técnico del análisis de datos.
- P3 - Luis: revisor de calidad, documentación y Pull Request.

## Escenario elegido

Se seleccionó el escenario B: Análisis de Ventas de una Pequeña Empresa.

## Descripción del proyecto

El objetivo del proyecto es analizar un dataset de ventas comerciales para obtener indicadores simples que ayuden a interpretar el desempeño de la empresa.

El análisis permite calcular:

- Ventas totales.
- Venta promedio.
- Día con mayor venta.
- Ventas agrupadas por mes.
- Gráfico de ventas mensuales.

## Dataset utilizado

Se utilizó el dataset `sales_sample_2024.csv`, sugerido en la consigna del trabajo práctico.  
El archivo fue guardado dentro de la carpeta `/datos` con el nombre `dataset.csv`.

## Estructura del repositorio

```text
tp-gestion-ventas-git-jira/
│
├── datos/
│   └── dataset.csv
│
├── scripts/
│   └── analisis_datos.py
│
├── resultados/
│   ├── resumen_ventas.txt
│   └── grafico_resultados.png
│
├── README.md
└── .gitignore
