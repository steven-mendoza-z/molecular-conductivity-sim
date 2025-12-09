# molecular-conductivity-sim

## Dev setup
```bash
conda create -n <nombredevenv> python=3.13

conda activate <nombredevenv>

conda install -c conda-forge tblite-python

pip install -r requirements.txt
```




# Dev push
conda env export --from-history > environment.yml

## Available parameters
{
"energy": library.get_energy,
"energies": library.get_energies,
"gradient": library.get_gradient,
"virial": library.get_virial,
"charges": library.get_charges,
"bond-orders": library.get_bond_orders,
"dipole": library.get_dipole,
"quadrupole": library.get_quadrupole,
"orbital-energies": library.get_orbital_energies,
"orbital-occupations": library.get_orbital_occupations,
"orbital-coefficients": library.get_orbital_coefficients,
"density-matrix": library.get_density_matrix,
"overlap-matrix": library.get_overlap_matrix,
"hamiltonian-matrix": library.get_hamiltonian_matrix,
"post-processing-dict": library.get_post_processing_dict,
"natoms": library.get_number_of_atoms,
"norbitals": library.get_number_of_orbitals,
}