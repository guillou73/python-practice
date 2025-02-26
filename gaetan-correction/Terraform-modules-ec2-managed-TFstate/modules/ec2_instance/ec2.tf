resource "aws_instance" "ec2-server" {
  ami           = var.ami_id  # Use variable for AMI ID
  instance_type = var.instance_type
  tags = {
    Name = var.instance_name  # Use variable for instance name
  }
}

