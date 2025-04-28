import sys, site, pprint, pkg_resources
print("VENV:", sys.prefix)
print("Packages:", [d.project_name for d in pkg_resources.working_set])