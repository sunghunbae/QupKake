import tempfile
import pathlib
import rdworks
import subprocess
import os

def run_workflow(smiles: str, name: str):
    with tempfile.TemporaryDirectory() as tmp_dir:
        workdir = pathlib.Path(tmp_dir)
        proc = subprocess.run(['qupkake', 
                               'smiles', smiles,
                               '--name', name,
                               '--output', 'qupkake_output.sdf',
                               '-r', tmp_dir, 
                               '--tautomerize',
                               ], cwd=tmp_dir)
        
        if proc.returncode == 0:
            expected_output = workdir / 'output/qupkake_output.sdf'
            if expected_output.exists():
                libr = rdworks.read_sdf(expected_output, confs=True)
                assert libr.count() == 1, "Expected exactly one molecule in the output"
                print(libr[0].serialize())
                for conf in libr[0].confs:
                    print("idx=", conf.props.get('idx', 'N/A'), end=' ')
                    print("pka_type=", conf.props.get('pka_type', 'N/A'), end=' ')
                    print("pka=", conf.props.get('pka', 'N/A'))
                print("success")
            else:
                print("no pKa output")

def test_api():
    os.environ["device"] = "cuda:0"
    for (smiles, name) in [
            ("N[C@@H](CCCCN)C(=O)O", "L-Lysine"),
            ("CC(=O)OC1=CC=CC=C1C(=O)O", "Aspirin"),
            ("CCN(CC)CCOC(=O)C1=CC=CC=C1", "Lidocaine"),
            ("CN1C=NC2=C1C(=O)N(C(=O)N2C)C", "Theobromine"),
            ("COC1=CC2=NC=CC(=C2C=C1C(=O)N)OC3=CC(=C(C=C3)NC(=O)NC4CC4)Cl", "Lenvatinib")]:
        print(f"Processing {name} ({smiles})")
        run_workflow(smiles, name)
        break
