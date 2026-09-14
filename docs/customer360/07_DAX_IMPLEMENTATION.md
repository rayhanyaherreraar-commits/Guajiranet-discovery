# Customer 360 — DAX V1 implementado

## Estado

Implementado el 2026-09-14 mediante el endpoint XMLA local de `Guajiranet_COMPAT_V2_TEST.pbix.pbix`, abierto en Power BI Desktop.

- Tabla desconectada creada: `KPI Customer360`.
- Medidas creadas: 15.
- Escenarios de prueba ejecutados: 16.
- Resultado final: 16 aprobados, 0 fallos.
- Tabla home de las medidas: `_medidas clientes 360`.
- Carpeta de visualización: `Customer 360 V1`.
- El PBIX quedó abierto en Power BI Desktop con el modelo modificado correctamente.
- No se modificaron visuales, relaciones, Power Query, Silver, Gold, Hop ni SQL.
- No se crearon calculation groups.

## Validación previa

Antes de escribir se confirmó:

- tablas: `fact facturacion`, `dim tiempo dax`, `dim cliente`, `_medidas clientes 360`;
- columnas: `fact facturacion[fecha_factura]`, `[Fecha Inicio Operacion]`, `[sk_cliente]`; `dim tiempo dax[Fecha]`; `dim cliente[nit]`, `[idsuc]`, `[razon social]`, `[sk_cliente]`;
- medidas base: `[Ingresos]` y `[Clientes Atendidos]`;
- ninguna de las 15 medidas nuevas existía;
- `dim cliente` tiene grano sucursal: 15.447 filas/SK, 14.993 NIT y 280 NIT multisucursal;
- `[Fecha Inicio Operacion]` está calculada por `sk_cliente`, por lo que Clientes Nuevos Observados no la usa para contar personas.

## Tabla desconectada implementada

### `KPI Customer360`

```DAX
KPI Customer360 =
DATATABLE (
    "KPI", STRING,
    "Dirección", INTEGER,
    "Orden KPI", INTEGER,
    "Comparación", STRING,
    "Orden Comparación", INTEGER,
    {
        { "Ingresos",                   1, 1, "PM",  1 },
        { "Ingresos",                   1, 1, "PY",  2 },
        { "Ingresos",                   1, 1, "YTD", 3 },
        { "Clientes Atendidos",         1, 2, "PM",  1 },
        { "Clientes Atendidos",         1, 2, "PY",  2 },
        { "Clientes Atendidos",         1, 2, "YTD", 3 },
        { "Clientes Nuevos Observados", 1, 3, "PM",  1 },
        { "Clientes Nuevos Observados", 1, 3, "PY",  2 },
        { "Clientes Nuevos Observados", 1, 3, "YTD", 3 }
    }
)
```

Configuración:

- 9 filas, 3 KPI y 3 comparaciones.
- Sin relaciones.
- `KPI` ordenada por `Orden KPI`.
- `Comparación` ordenada por `Orden Comparación`.
- Dirección y columnas de orden ocultas.
- Dirección `1` significa que subir es favorable; `-1` invierte el semáforo para un KPI de riesgo futuro.

## Medidas implementadas

### 1. `Clientes Nuevos Observados`

- Dependencias: facturación, `dim cliente[nit]` y `dim tiempo dax[Fecha]`.
- Uso: KPI, series y capa genérica.
- Filtros: el contexto visible define candidatos; la primera factura se calcula globalmente por NIT.
- Casos límite: excluye NIT vacío, conserva BLANK sin fechas y cuenta una vez un NIT multisucursal.

```DAX
Clientes Nuevos Observados =
VAR FechaInicial = MIN ( 'dim tiempo dax'[Fecha] )
VAR FechaFinal = MAX ( 'dim tiempo dax'[Fecha] )
VAR PersonasEnContexto =
    FILTER (
        SUMMARIZE ( 'fact facturacion', 'dim cliente'[nit] ),
        NOT ISBLANK ( 'dim cliente'[nit] )
    )
RETURN
    IF (
        ISBLANK ( FechaInicial ) || ISBLANK ( FechaFinal ),
        BLANK (),
        COUNTROWS (
            FILTER (
                PersonasEnContexto,
                VAR NitActual = 'dim cliente'[nit]
                VAR PrimeraFacturacionPersona =
                    CALCULATE (
                        MIN ( 'fact facturacion'[fecha_factura] ),
                        REMOVEFILTERS (),
                        TREATAS ( { NitActual }, 'dim cliente'[nit] )
                    )
                RETURN
                    NOT ISBLANK ( PrimeraFacturacionPersona )
                        && PrimeraFacturacionPersona >= FechaInicial
                        && PrimeraFacturacionPersona <= FechaFinal
            )
        )
    )
```

### 2. `Ingreso Promedio por Sucursal Atendida`

- Dependencias: `[Ingresos]`, `[Clientes Atendidos]`.
- Uso: KPI Resumen.
- Filtros: hereda el contexto de las medidas base.
- Caso límite: DIVIDE devuelve BLANK con denominador cero.

```DAX
Ingreso Promedio por Sucursal Atendida =
DIVIDE ( [Ingresos], [Clientes Atendidos] )
```

### 3. `Es Selección Única Persona`

- Dependencia: `dim cliente[nit]`.
- Uso: estado del Perfil.
- Caso límite: un NIT multisucursal sigue siendo una persona seleccionada.

```DAX
Es Selección Única Persona =
VAR NitSeleccionado = SELECTEDVALUE ( 'dim cliente'[nit] )
RETURN
    HASONEVALUE ( 'dim cliente'[nit] )
        && NOT ISBLANK ( NitSeleccionado )
```

### 4. `Mensaje Estado Perfil`

- Dependencia: `[Es Selección Única Persona]`.
- Uso: estado vacío/overlay del Perfil.
- Caso límite: con persona única devuelve BLANK.

```DAX
Mensaje Estado Perfil =
IF (
    [Es Selección Única Persona],
    BLANK (),
    "Selecciona un cliente para ver su perfil"
)
```

### 5. `KPI Periodo Actual`

- Dependencias: selector KPI y tres medidas base.
- Uso: valor genérico actual y dependencia temporal.
- Caso límite: sin un KPI único devuelve BLANK.

```DAX
KPI Periodo Actual =
SWITCH (
    SELECTEDVALUE ( 'KPI Customer360'[KPI] ),
    "Ingresos", [Ingresos],
    "Clientes Atendidos", [Clientes Atendidos],
    "Clientes Nuevos Observados", [Clientes Nuevos Observados],
    BLANK ()
)
```

### 6. `KPI PM`

- Dependencias: `[KPI Periodo Actual]`, calendario.
- Uso: tarjeta y tooltip.
- Caso límite: sin mes comparable devuelve BLANK.

```DAX
KPI PM =
CALCULATE (
    [KPI Periodo Actual],
    DATEADD ( 'dim tiempo dax'[Fecha], -1, MONTH )
)
```

### 7. `KPI PY`

- Dependencias: `[KPI Periodo Actual]`, calendario.
- Uso: tarjeta y tooltip.
- Caso límite: sin periodo comparable devuelve BLANK.

```DAX
KPI PY =
CALCULATE (
    [KPI Periodo Actual],
    DATEADD ( 'dim tiempo dax'[Fecha], -1, YEAR )
)
```

### 8. `KPI YTD`

- Dependencias: `[KPI Periodo Actual]`, calendario.
- Uso: valor acumulado y tooltip.
- Comportamiento: año calendario hasta el corte visible.

```DAX
KPI YTD =
CALCULATE (
    [KPI Periodo Actual],
    DATESYTD ( 'dim tiempo dax'[Fecha] )
)
```

### 9. `KPI PYTD`

- Dependencias: `[KPI Periodo Actual]`, calendario.
- Uso: base acumulada comparable.
- Comportamiento: misma ventana YTD desplazada un año.

```DAX
KPI PYTD =
CALCULATE (
    [KPI Periodo Actual],
    DATEADD (
        DATESYTD ( 'dim tiempo dax'[Fecha] ),
        -1,
        YEAR
    )
)
```

### 10. `KPI Var % vs PM`

- Dependencias: actual y PM.
- Uso: tooltip y selector.
- Casos límite: actual/base BLANK o base cero producen BLANK.

```DAX
KPI Var % vs PM =
VAR Actual = [KPI Periodo Actual]
VAR Base = [KPI PM]
RETURN
    IF (
        ISBLANK ( Actual ) || ISBLANK ( Base ) || Base = 0,
        BLANK (),
        DIVIDE ( Actual - Base, Base )
    )
```

### 11. `KPI Var % vs PY`

- Dependencias: actual y PY.
- Uso: tooltip y selector.
- Casos límite: actual/base BLANK o base cero producen BLANK.

```DAX
KPI Var % vs PY =
VAR Actual = [KPI Periodo Actual]
VAR Base = [KPI PY]
RETURN
    IF (
        ISBLANK ( Actual ) || ISBLANK ( Base ) || Base = 0,
        BLANK (),
        DIVIDE ( Actual - Base, Base )
    )
```

### 12. `KPI Var % YTD vs PYTD`

- Dependencias: YTD y PYTD.
- Uso: tooltip y selector.
- Casos límite: actual/base BLANK o base cero producen BLANK.

```DAX
KPI Var % YTD vs PYTD =
VAR Actual = [KPI YTD]
VAR Base = [KPI PYTD]
RETURN
    IF (
        ISBLANK ( Actual ) || ISBLANK ( Base ) || Base = 0,
        BLANK (),
        DIVIDE ( Actual - Base, Base )
    )
```

### 13. `KPI Valor Seleccionado`

- Dependencias: selector y valores genéricos.
- Uso: valor principal de tarjeta.
- Comportamiento: PM/PY muestran periodo actual; YTD muestra acumulado.

```DAX
KPI Valor Seleccionado =
SWITCH (
    SELECTEDVALUE ( 'KPI Customer360'[Comparación], "PM" ),
    "YTD", [KPI YTD],
    [KPI Periodo Actual]
)
```

### 14. `KPI Comparación Texto`

- Dependencias: selector y tres variaciones.
- Uso: porcentaje y texto bajo el valor principal.
- Casos límite: sin base válida muestra `Sin comparación`.

```DAX
KPI Comparación Texto =
VAR Comparacion =
    SELECTEDVALUE ( 'KPI Customer360'[Comparación], "PM" )
VAR Variacion =
    SWITCH (
        Comparacion,
        "PM", [KPI Var % vs PM],
        "PY", [KPI Var % vs PY],
        "YTD", [KPI Var % YTD vs PYTD],
        BLANK ()
    )
VAR Etiqueta =
    SWITCH (
        Comparacion,
        "PM", "vs. PM",
        "PY", "vs. PY",
        "YTD", "vs. YTD anterior",
        BLANK ()
    )
RETURN
    IF (
        ISBLANK ( Variacion ),
        "Sin comparación",
        FORMAT ( Variacion, "+0.0%;-0.0%;0.0%" ) & " " & Etiqueta
    )
```

### 15. `KPI Color Semáforo`

- Dependencias: selector, variaciones y dirección del KPI.
- Uso: formato condicional.
- Casos límite: sin base gris; exactamente ±10% amarillo.
- Riesgo: una fila futura con dirección `-1` invierte verde/rojo sin cambiar la medida.

```DAX
KPI Color Semáforo =
VAR Comparacion =
    SELECTEDVALUE ( 'KPI Customer360'[Comparación], "PM" )
VAR Variacion =
    SWITCH (
        Comparacion,
        "PM", [KPI Var % vs PM],
        "PY", [KPI Var % vs PY],
        "YTD", [KPI Var % YTD vs PYTD],
        BLANK ()
    )
VAR Direccion =
    SELECTEDVALUE ( 'KPI Customer360'[Dirección], 1 )
VAR Mejora =
    Variacion * Direccion
RETURN
    SWITCH (
        TRUE (),
        ISBLANK ( Variacion ), "#98A6B5",
        Mejora > 0.10, "#1FA463",
        Mejora >= -0.10, "#F4B740",
        "#D94A4A"
    )
```

## Resultados de validación

| Prueba | Resultado |
|---|---|
| Periodo con datos | Aprobada para los tres KPI |
| Periodo sin PM comparable | PM/variación BLANK, texto `Sin comparación`, color gris |
| Periodo con PY | Aprobada para los tres KPI |
| YTD/PYTD | Aprobada para los tres KPI |
| NIT de una sucursal | Selección única verdadera; Clientes Nuevos = 1 en su primera ventana |
| NIT multisucursal | Dos sucursales en dimensión; Clientes Nuevos = 1 en su primera ventana |
| Sin cliente seleccionado | Selección única falsa y mensaje visible |
| División por cero/sin datos | Ingreso promedio BLANK, sin error |
| Filtro directo sobre `dim tiempo dax[Fecha]` | Sin errores |
| KPI seleccionado PM/PY/YTD | Valor, texto y comparación correctos |
| Semáforo favorable | Verde >10%, amarillo dentro de ±10%, rojo <-10% |
| Límites exactos | +10% y -10% amarillos |
| Dirección de riesgo | +11% rojo y -11% verde con dirección -1 |
| Jerarquía automática | Ninguna expresión la referencia |
| Tabla desconectada | 9 filas, 3 KPI, 3 comparaciones, 0 relaciones |
| Alcance de medidas | 15 creadas; ninguna medida eliminada/diferida creada |
| Exclusiones | Sin comparaciones de cartera y sin Total Pagos |

## Corrección aplicada durante validación

La tabla calculada se creó inicialmente sin materializar filas. Se solicitó `Calculate` únicamente sobre `KPI Customer360`; no se refrescaron fuentes ni otras tablas. Después de la corrección pasaron las pruebas genéricas.

## Exclusiones conservadas

- `[Saldo Cartera]`, `[Cartera Vencida]` y `[Cartera No Vencida]` permanecen `Corte actual`.
- `[Pago Aplicado]` y `[Pago Pasarela]` permanecen separados.
- No se creó Total Pagos, churn, NPS, Health Score ni métrica predictiva.
- No se modificaron `[Clientes Atendidos Mes Anterior]`, `[Venta Mes Actual]` ni `[MoM% de Suma de venta]`.
