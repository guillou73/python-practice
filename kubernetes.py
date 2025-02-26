import boto3
from botocore.exceptions import NoCredentialsError
# aws credentials configurations
aws_region = "us-east-1"
instance_type = "t2-micro"
key_name = "my-aws-key "
security_group_id = "jenkins.sg"
ami_id = "ami-0db5e28c1b3823bb7"
instance_count = 3
# kubernertes setup
kube_version = "1.24.0"
docker_version = "5:20.10.12~30~ubuntu-focal"


def create_instances():
    """"
    create ec2 instances using Boto3
    """
    ec2_client = boto3.client("ec2", region__name = aws_region)

    try:
        # launch ec2 instance
        instances = ec2_client.run_instances(

            imageId=ami_id,
            instance_type=instance_type,
            key_name=key_name,
            security_group_id=[security_group_id],
            mincount=instance_count,
            maxcount=instance_count,
            tagspecifications=[{
                "resourcetype": "instance",
                "tags" :
                {"key": "name","value": "k8snode" }
            }]

        )
        instance_ids = [instance["instanceid"] for instance in instances["instances"]]
        print(f"instance created: {instance_ids}")
        return instance_ids
    except NoCredentialsError:
        print("credentials not available.")
        return None
def get_instance_ips(instance_ids):
    """"
    get the public ips of the ec2 instances.

    """""
    ec2_client = boto3.client("ec2", region_name=aws_region)
    reservation = ec2_client.describe_instances(instanceid=instance_ids)
    instance_ips = []
    for reservation in reservations["reservation"]:
        for instance in reservation["instances"]:
            instance_ips.append(instance["publicaddress"])
    return instance_ips
def ssh_connect(ip, user="ubuntu"):
    """""
    establish an ssh connection to the ec2 instance
    """""
    key = paramiko.rsakey.from_private_key_file(f'~/.ssh/jenkins.pem')
    client =paramiko.sshclient()
    client.set_missing_host_key_policy(paramiko.autoaddpolicy())
    try:
        client.connect(ip, username=user, pkey=key)
        return client
    except Exception as e:
        print(f"ssh connection failed {e}")
        return None
    

def setup_k8s_master(ip):
    """""
    setup the kubernetes master node using kubeadm.
    """""
    ssh_client = ssh_connect(ip)
    if not ssh_client:
        return
    commands = [
        "sudo apt-get update",
        "sudo apt-get install -y docker.io",
        "sudo systemctl enable docker",
        "sudo systemctl start docker",
        "sudo apt-get install -y apt-transport-https curl",
        "curl -s https:packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add"
        "echo 'deb https://apt.kubernetes.io/ kubernetes-xenial main' | sudo tee -a /etc/apt/sources.list",
        "sudo apt-get update",
        "sudo apt-get install -y kubelet={0}-00 kubectl={0}-00 kubeadm={0}-00". format(kube_version),
        "sudo apt-mark hold kubelet kubectl kubeadm",
        "sudo kubeadm init --pod-network-cidr=10.244.0.0/16",
        "mkdir -p $HOME/ .kube",
        "sudo cp -i /etc/kubernetes/admin.conf",
        

    ]