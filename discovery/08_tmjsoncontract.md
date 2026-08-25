# `bronze_guajiranet.tmjsoncontract`

- Read-only. Sin interpretación de negocio.
- `datajson`: objeto plano, 60 claves, presentes en las 10998 filas. 0 objetos anidados, 0 arrays.
- No se muestrean `pppoe_password` ni `wifi_password`.

## Tabla

| columna | hallazgo |
|---|---|
| filas | 10998 |
| `id` (integer) | único, 0 nulos; no igual a `datajson.id` |
| `idcontrato` | único, 0 nulos; **igual a `datajson.id` en 10998/10998** |
| `idcliente` | 10740 distinct, 0 nulos; UUID 36; **igual a `datajson.client_id` en 10998/10998** |
| `datajson` | jsonb object, 0 nulos |

1–30 contratos por `idcliente` (avg 1.024).

## Claves de `datajson` (60/60 en todas las filas)

Cliente: `client_id` (string). Plan: `plan_id` (string, 109 distinct). Fechas string: `start_date` 2019-02-14 … 2026-06-12; `created_at` / `updated_at` ISO con offset -05:00. Estado: `state` = `enabled` 8637, `disabled` 2361.

Dirección: `address_street`, `address_number` (8904 null), `address_additional_data`, `address_city`, `address_state`, `address_country`. Geo: `latitude`/`longitude` string numérica en 10998.

Equipos (nombres de clave): `ont_id` / `ont_serial_number` 8187 no null; `ont_number` 8195; `olt_id` 8911; `interface_gpon` 8187; `mac_address` 10769; `cable_modem_*` 1757 no null. `olt_enabled` true 8911 / false 2087. `pppoe_enabled` false 10998.

`details`: string (no JSON), 10935 no null, max len 999. Prefijo más frecuente (5143): `CLIENTE SE LE ENTREGA ONUS EN COMODATO CON UN PLAN DE 25 MEG`.

Sin claves cuyo nombre coincida con instalación, activación, retiro, cancelación, precio, valor o costo. `ceil_dfl_percent` es number; no se etiqueta como precio.

## vs `matercerosuc`

`matercerosuc` no tiene `idcliente`. Columnas vistas: `nit`, `codcliente`, `id`, `idcontrato`.

| cruce | suc | json | ambas | solo suc | solo json |
|---|---:|---:|---:|---:|---:|
| `idcontrato` | 10935 | 10998 | **10466** | 469 | 532 |

Cobertura de claves suc: **95.711%**.

`idcliente` vs `nit` / `id` / `codcliente`: **0** coincidencias. En el join por `idcontrato` (10466 filas): `idcliente` ≠ `nit` en todas.

## Temas pedidos (solo match de nombre de clave)

| tema | claves observadas | no encontrado por nombre |
|---|---|---|
| cliente | `client_id` | — |
| plan/servicio | `plan_id`; `details` texto | objeto plan |
| fechas | `start_date`, `created_at`, `updated_at` | — |
| instalación | — | sí |
| activación | — | sí (`state` no se interpreta) |
| retiro/cancelación | — | sí |
| dirección/geografía | `address_*`, `latitude`, `longitude` | — |
| equipos/ONU | `ont_*`, `olt_*`, `interface_gpon`, `mac_address`, `cable_modem_*` | clave `onu` |
| valores/precios | — | sí |

JSON: `output/analisis_tmjsoncontract.json`
