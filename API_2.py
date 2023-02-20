import subprocess
import json
from tabulate import tabulate

def get_deployments(namespace):
    cmd = f"kubectl get deployments --namespace={namespace} -o json"
    output = subprocess.check_output(cmd, shell=True)
    deployments = json.loads(output)["items"]
    return deployments

def get_diff(deployments1, deployments2):
    diff = []
    deployments1_dict = {deployment["metadata"]["name"]: deployment for deployment in deployments1}
    for deployment2 in deployments2:
        name = deployment2["metadata"]["name"]
        if name not in deployments1_dict:
            diff.append([name, "", deployment2["spec"]["template"]["spec"]["containers"][0]["image"], deployment2["metadata"]["creationTimestamp"]])
        else:
            deployment1 = deployments1_dict[name]
            if deployment2["spec"]["template"]["spec"]["containers"][0]["image"] != deployment1["spec"]["template"]["spec"]["containers"][0]["image"]:
                diff.append([name, deployment1["spec"]["template"]["spec"]["containers"][0]["image"], deployment2["spec"]["template"]["spec"]["containers"][0]["image"], deployment2["metadata"]["creationTimestamp"]])
    return diff

namespace1 = "sock-shop"
namespace2 = "sock-shop2"

deployments1 = get_deployments(namespace1)
deployments2 = get_deployments(namespace2)

diff = get_diff(deployments1, deployments2)

headers = ["DEPLOYMENT NAME", f"IMAGE ({namespace1})", f"IMAGE ({namespace2})", "UPDATED AT"]
print(tabulate(diff, headers=headers))
