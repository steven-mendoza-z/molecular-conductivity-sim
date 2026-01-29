# libs/xtb_io.py
from pathlib import Path
import numpy as np

# 👇 adapta el import al nombre real de tu paquete
# ejemplos típicos:
#   from xtblite import XTB
#   from xtb.interface import Calculator
import xtblite  # placeholder: ajusta según la doc real


def _read_xyz(xyz_path: Path):
    """
    Lee un archivo .xyz y devuelve:
      - symbols: lista de strings ["C","H","N",...]
      - coords:  np.ndarray (N,3) en Angstrom
    """
    symbols = []
    coords = []
    with open(xyz_path, "r") as f:
        lines = f.readlines()

    for line in lines[2:]:
        parts = line.split()
        if len(parts) < 4:
            continue
        sym = parts[0]
        x, y, z = map(float, parts[1:4])
        symbols.append(sym)
        coords.append([x, y, z])

    return symbols, np.array(coords, dtype=float)


# ====== NUEVA API DE "CÁLCULOS" ======

def run_xtb_opt(xyz: Path, outdir: Path, nprocs: int = 4):
    """
    Interfaz de compatibilidad: antes lanzaba 'xtb --opt'.
    Ahora:
      - lee el .xyz
      - corre una optimización geométrica con xtblite
      - guarda la geometría optimizada como xtbopt.xyz en outdir
    """
    outdir.mkdir(exist_ok=True)

    symbols, coords = _read_xyz(xyz)

    # 👇 Ejemplo de uso, AJUSTA al API real de xtblite
    # --------- PSEUDOCÓDIGO --------------
    # calc = xtblite.Calculator(method="GFN2-xTB", charge=0, spin=0)
    # opt_result = calc.optimize(symbols=symbols, coords=coords)
    # opt_coords = opt_result.coords
    # -------------------------------------
    #
    # Para que el resto de tu código funcione, necesitamos coords optimizadas:
    #
    raise NotImplementedError(
        "Implementa aquí la llamada real a xtblite para optimizar la geometría."
    )

    # Ejemplo de escritura de xtbopt.xyz
    xtbopt_path = outdir / "xtbopt.xyz"
    with open(xtbopt_path, "w") as f:
        f.write(f"{len(symbols)}\n")
        f.write("xtblite optimized geometry\n")
        for sym, (x, y, z) in zip(symbols, opt_coords):
            f.write(f"{sym:2s}  {x:16.8f} {y:16.8f} {z:16.8f}\n")

    print(f"[xtblite] Geometría optimizada guardada en {xtbopt_path}")


def run_xtb_sp(xyzopt: Path, outdir: Path):
    """
    Interfaz de compatibilidad para el 'single point'.
    En la versión xtblite:
      - lee la geometría (xyzopt)
      - corre un cálculo de un solo punto
      - guarda energías orbitales en un .npz opcional
    """
    symbols, coords = _read_xyz(xyzopt)

    # 👇 PSEUDOCÓDIGO, AJUSTAR:
    # calc = xtblite.Calculator(method="GFN2-xTB", charge=0, spin=0)
    # sp_result = calc.single_point(symbols=symbols, coords=coords)
    #
    # # supongamos que sp_result tiene un atributo `orbital_energies_ev`
    # mo_energies_ev = np.array(sp_result.orbital_energies_ev)
    #
    raise NotImplementedError(
        "Implementa aquí la llamada real a xtblite para el single-point."
    )

    # Ejemplo: guardar energías en un fichero binario opcional
    out_npz = outdir / "xtb_sp_levels.npz"
    np.savez(out_npz, mo_energies_ev=mo_energies_ev)
    print(f"[xtblite] Energías de orbitales guardadas en {out_npz}")


def extract_levels_from_output(filepath: Path):
    """
    Compatibilidad con la firma antigua, pero ahora
    `filepath` será un .npz con energías de orbitales.
    Devuelve (HOMO_eV, LUMO_eV, GAP_eV).
    """
    data = np.load(filepath)
    mo_energies_ev = np.array(data["mo_energies_ev"])

    # Aquí asumimos ocupación de 2 electrones por orbital en orden,
    # tú puedes ajustar según nº de electrones reales.
    n_orbitals = len(mo_energies_ev)
    n_electrons = ...  # TODO: calcular a partir de symbols / carga
    n_occ = n_electrons // 2

    if n_occ == 0 or n_occ >= n_orbitals:
        return None, None, None

    homo = mo_energies_ev[n_occ - 1]
    lumo = mo_energies_ev[n_occ]
    gap = lumo - homo

    return float(homo), float(lumo), float(gap)


def extract_levels_from_dir(outdir: Path):
    """
    Versión para xtblite:
      - Busca xtb_sp_levels.npz en outdir
      - Calcula HOMO, LUMO y GAP desde ahí.
    """
    npz = outdir / "xtb_sp_levels.npz"
    if not npz.exists():
        print(f"⚠ No se encontraron niveles en {npz}")
        return None, None, None

    return extract_levels_from_output(npz)
