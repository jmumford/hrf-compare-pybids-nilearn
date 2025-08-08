import json
from pathlib import Path

from bids.layout import BIDSLayout
from bids.modeling import BIDSStatsModelsGraph

root = '/Users/jeanettemumford/Dropbox/Research/Projects/hrf_compare_pybids_nilearn/test_model_spec/ds000171'
db_path = '/Users/jeanettemumford/Dropbox/Research/Projects/hrf_compare_pybids_nilearn/test_model_spec/ds000171/dbcache'
reset_database = True
spec_path = '/Users/jeanettemumford/Dropbox/Research/Projects/hrf_compare_pybids_nilearn/test_model_spec/model_spec/fir_model_spec.json'


layout = BIDSLayout(root=root, database_path=db_path, reset_database=reset_database)

spec = json.loads(Path(spec_path).read_text())

graph = BIDSStatsModelsGraph(layout, spec)
graph.load_collections(scan_length=105 * 3)

root_node = graph.root_node
colls = root_node.get_collections()
first_sub = colls[0]

outputs = root_node.run(
    group_by=root_node.group_by, force_dense=False, transformation_history=True
)


first_output = outputs[0]

print('Finished running')
