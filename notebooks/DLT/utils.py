# import os, sys
# sys.path.append('/Workspace/Users/sarvesh.maheshwari@databricks.com/Test/notebooks')

import notebooks.Common.my_module as my_module

def test_my_module():
    return my_module.hello_world(1, 2)