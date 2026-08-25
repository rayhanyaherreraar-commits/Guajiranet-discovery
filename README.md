# GuajiraNet Data Discovery

Escáner de solo lectura sobre Aurora PostgreSQL y archivo de discovery para ampliar el modelo dimensional de GuajiraNet.

**Leer primero:** [`ESTADO.md`](ESTADO.md) y [`discovery/INDEX.md`](discovery/INDEX.md).

## Qué hace el código

- Inventario de tablas y columnas (`--mode inventory`).
- Perfil de nulos, cardinalidad, fechas y muestras (`--mode profile`).
- Análisis de **una** tabla (`--mode table`).
- Auditorías dirigidas ya usadas en el discovery (`--mode audit`).

Los JSON grandes de corridas nuevas van a `output/` (no se versionan). Los informes cerrados viven en `discovery/`.

## Seguridad

Transacciones de solo lectura (`default_transaction_read_only=on`). Usar un usuario con `SELECT` únicamente.

## Instalación

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
```

Completar `.env` con Aurora. No commitear `.env`.

## Ejecución

```powershell
python main.py --mode inventory
python main.py --mode profile
python main.py --mode table --table matercerosuc
python main.py --mode audit --audit all
python main.py --mode audit --audit lookup_idcontrato
```

SQL equivalente en `sql/auditoria/`.

## Hallazgo rector (2026-08-24)

El Silver actual no es Cliente 360 ISP: es un estrella de facturación ERP más un recorte de cartera. El plan ISP está en `tmjsonplan_server` (`tipo='P'`), no en `tbl_dim_servicio`. Detalle en `discovery/11_model_audit.md`.

## Principio

Primero el dato, después el significado, luego el modelo, al final el dashboard. No inventar indicadores si el campo no existe o no es confiable.
