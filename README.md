# GuajiraNet Data Discovery Scanner

Escáner de solo lectura para descubrir automáticamente qué información existe en Aurora.

## Qué hace
- Inventaría tablas y columnas.
- Cuenta registros.
- Mide nulos y valores distintos.
- Detecta fechas mínima y máxima.
- Obtiene muestras limitadas.
- Busca relaciones candidatas.
- Clasifica datos relacionados con clientes, vinculación, planes, pagos, cartera, estados, retiros y geografía.

## Seguridad
El proyecto usa transacciones de solo lectura. Se recomienda además un usuario exclusivo con permisos `SELECT`.

## Instalación
```bash
python -m venv .venv
```

Windows:
```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
```

Completa `.env` con Aurora.

## Ejecución
Inventario rápido:
```bash
python main.py --mode inventory
```

Perfil completo:
```bash
python main.py --mode profile
```

Los resultados quedan en `output/`.
