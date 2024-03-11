import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw

# Function to generate molecular structure image
def generate_mol_image(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        drawer = rdMolDraw2D.MolDraw2DCairo(300, 300)  # You can change the size as per your requirement
        drawer.DrawMolecule(mol)
        drawer.FinishDrawing()
        return drawer.GetDrawingText()
    else:
        return None

# Read CSV file
csv_file_path = 'odorMolecules.csv'
data = pd.read_csv(csv_file_path)

# Add a new column for molecular structure images
data['Mol_Image'] = data['SMILES'].apply(generate_mol_image)

# Save the updated CSV file
updated_csv_file_path = 'updated_odorMolecules.csv'
data.to_csv(updated_csv_file_path, index=False)
